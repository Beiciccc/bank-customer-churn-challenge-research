from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold


TARGET = "Exited"
ID_COL = "id"
BASE_CATEGORICAL = ["Surname", "Geography", "Gender", "CustomerId"]
EXTERNAL_FLAG = "__is_external"


@dataclass
class PreparedData:
    train: pd.DataFrame
    test: pd.DataFrame
    features: list[str]
    categorical: list[str]
    target: pd.Series
    test_ids: pd.Series
    eval_mask: np.ndarray


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--external-path", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=Path("submissions"))
    parser.add_argument("--models-dir", type=Path, default=Path("models"))
    parser.add_argument("--report-dir", type=Path, default=Path("reports"))
    parser.add_argument("--models", default="cat,lgb")
    parser.add_argument("--feature-mode", choices=["all", "robust", "cat_native", "s4e1_text"], default="all")
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--cat-iterations", type=int, default=5000)
    parser.add_argument("--cat-learning-rate", type=float, default=None)
    parser.add_argument("--cat-depth", type=int, default=None)
    parser.add_argument("--cat-l2-leaf-reg", type=float, default=None)
    parser.add_argument("--cat-random-strength", type=float, default=None)
    parser.add_argument("--cat-bagging-temperature", type=float, default=None)
    parser.add_argument("--cat-border-count", type=int, default=None)
    parser.add_argument("--cat-one-hot-max-size", type=int, default=None)
    parser.add_argument("--cat-max-ctr-complexity", type=int, default=None)
    parser.add_argument("--lgb-rounds", type=int, default=5000)
    parser.add_argument("--xgb-rounds", type=int, default=3500)
    parser.add_argument("--use-gpu", action="store_true")
    parser.add_argument("--gpu-device", default="0")
    parser.add_argument("--tag", default="blend")
    return parser.parse_args()


def read_data(data_dir: Path, external_path: Path | None) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv(data_dir / "train.csv")
    test = pd.read_csv(data_dir / "test.csv")
    train[EXTERNAL_FLAG] = 0

    if external_path is not None and external_path.exists():
        ext = pd.read_csv(external_path)
        rename = {"RowNumber": ID_COL}
        ext = ext.rename(columns=rename)
        keep = [c for c in train.columns if c in ext.columns]
        ext = ext[keep].copy()
        ext[ID_COL] = -(np.arange(len(ext)) + 1)
        ext[EXTERNAL_FLAG] = 1
        ext = ext.drop_duplicates()
        train = pd.concat([train, ext], ignore_index=True)
        print(f"Loaded external rows: {len(ext)} from {external_path}")

    return train, test


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["CustomerId"] = out["CustomerId"].astype(str)
    out["Surname"] = out["Surname"].astype(str)
    out["Geography"] = out["Geography"].astype(str)
    out["Gender"] = out["Gender"].astype(str)

    out["AgeInt"] = out["Age"].round().astype(int)
    out["IsZeroBalance"] = (out["Balance"] == 0).astype(int)
    out["BalanceLog"] = np.log1p(out["Balance"])
    out["EstimatedSalaryLog"] = np.log1p(out["EstimatedSalary"])
    out["BalanceSalaryRatio"] = out["Balance"] / (out["EstimatedSalary"] + 1.0)
    out["BalancePerProduct"] = out["Balance"] / out["NumOfProducts"].clip(lower=1)
    out["SalaryPerProduct"] = out["EstimatedSalary"] / out["NumOfProducts"].clip(lower=1)
    out["CreditAgeRatio"] = out["CreditScore"] / (out["Age"] + 1.0)
    out["TenureAgeRatio"] = out["Tenure"] / (out["Age"] + 1.0)
    out["CreditSalaryRatio"] = out["CreditScore"] / (out["EstimatedSalary"] + 1.0)
    out["ActiveByCreditCard"] = out["IsActiveMember"] * out["HasCrCard"]
    out["ProductsByBalance"] = out["NumOfProducts"] * out["IsZeroBalance"]
    out["IsSenior"] = (out["Age"] >= 60).astype(int)
    out["Products_Per_Tenure"] = out["Tenure"] / out["NumOfProducts"].clip(lower=1)
    out["AgeCatS4"] = np.round(out["Age"] / 20).astype(int).astype(str)

    out["AgeBin"] = pd.cut(
        out["Age"],
        bins=[0, 30, 40, 50, 60, 120],
        labels=["age_le_30", "age_31_40", "age_41_50", "age_51_60", "age_gt_60"],
        include_lowest=True,
    ).astype(str)
    out["CreditBin"] = pd.cut(
        out["CreditScore"],
        bins=[0, 550, 650, 750, 900],
        labels=["credit_low", "credit_mid", "credit_good", "credit_high"],
        include_lowest=True,
    ).astype(str)
    out["BalanceBin"] = pd.cut(
        out["Balance"],
        bins=[-1, 0, 50000, 100000, 150000, 300000],
        labels=["balance_zero", "balance_low", "balance_mid", "balance_high", "balance_vhigh"],
    ).astype(str)

    combos = {
        "GeoGender": ["Geography", "Gender"],
        "GeoProduct": ["Geography", "NumOfProducts"],
        "GenderProduct": ["Gender", "NumOfProducts"],
        "AgeBinProduct": ["AgeBin", "NumOfProducts"],
        "GeoActive": ["Geography", "IsActiveMember"],
        "SurnameGeo": ["Surname", "Geography"],
        "CustomerProduct": ["CustomerId", "NumOfProducts"],
    }
    for name, cols in combos.items():
        out[name] = out[cols[0]].astype(str)
        for col in cols[1:]:
            out[name] = out[name] + "_" + out[col].astype(str)

    out["Sur_Geo_Gend_Sal"] = (
        out["Surname"].astype(str)
        + "_"
        + out["Geography"].astype(str)
        + "_"
        + out["Gender"].astype(str)
        + "_"
        + np.round(out["EstimatedSalary"]).astype(int).astype(str)
    )
    out["AllCat"] = (
        out["Surname"].astype(str)
        + "_"
        + out["Geography"].astype(str)
        + "_"
        + out["Gender"].astype(str)
        + "_"
        + np.round(out["EstimatedSalary"]).astype(int).astype(str)
        + "_"
        + out["CreditScore"].astype(str)
        + "_"
        + out["AgeInt"].astype(str)
        + "_"
        + out["NumOfProducts"].astype(str)
        + "_"
        + out["Tenure"].astype(str)
        + "_"
        + out["CustomerId"].astype(str)
    )

    return out


def add_tfidf_svd_features(
    train: pd.DataFrame,
    test: pd.DataFrame,
    cols: Iterable[str],
    max_features: int = 1000,
    n_components: int = 4,
    seed: int = 42,
) -> list[str]:
    from sklearn.decomposition import TruncatedSVD
    from sklearn.feature_extraction.text import TfidfVectorizer

    new_cols: list[str] = []
    for col in cols:
        combined = pd.concat([train[col], test[col]], axis=0).astype(str)
        vectorizer = TfidfVectorizer(max_features=max_features, analyzer="char_wb", ngram_range=(2, 4))
        mat = vectorizer.fit_transform(combined)
        n_comp = min(n_components, max(1, mat.shape[1] - 1))
        svd = TruncatedSVD(n_components=n_comp, random_state=seed)
        emb = svd.fit_transform(mat)
        for i in range(n_comp):
            name = f"{col}_svd{i}"
            train[name] = emb[: len(train), i]
            test[name] = emb[len(train) :, i]
            new_cols.append(name)
    return new_cols


def add_frequency_features(train: pd.DataFrame, test: pd.DataFrame, cols: Iterable[str]) -> None:
    combined = pd.concat([train[list(cols)], test[list(cols)]], axis=0, ignore_index=True)
    for col in cols:
        vc = combined[col].value_counts(dropna=False)
        train[f"{col}_freq"] = train[col].map(vc).astype(float)
        test[f"{col}_freq"] = test[col].map(vc).astype(float)


def smooth_target_mean(sum_: pd.Series, count: pd.Series, prior: float, smooth: float) -> pd.Series:
    return (sum_ + prior * smooth) / (count + smooth)


def add_target_encoding(
    train: pd.DataFrame,
    test: pd.DataFrame,
    y: pd.Series,
    cols: Iterable[str],
    folds: int,
    seed: int,
    smooth: float = 20.0,
) -> None:
    prior = float(y.mean())
    cv = StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed)

    for col in cols:
        train[f"{col}_te"] = prior
        for tr_idx, val_idx in cv.split(train, y):
            stats = train.iloc[tr_idx].groupby(col)[TARGET].agg(["sum", "count"])
            mapping = smooth_target_mean(stats["sum"], stats["count"], prior, smooth)
            train.loc[train.index[val_idx], f"{col}_te"] = (
                train.iloc[val_idx][col].map(mapping).fillna(prior).to_numpy()
            )

        stats_full = train.groupby(col)[TARGET].agg(["sum", "count"])
        mapping_full = smooth_target_mean(stats_full["sum"], stats_full["count"], prior, smooth)
        test[f"{col}_te"] = test[col].map(mapping_full).fillna(prior).astype(float)


def prepare(train_raw: pd.DataFrame, test_raw: pd.DataFrame, folds: int, seed: int, feature_mode: str) -> PreparedData:
    y = train_raw[TARGET].astype(int).copy()
    test_ids = test_raw[ID_COL].copy()
    eval_mask = train_raw.get(EXTERNAL_FLAG, pd.Series(0, index=train_raw.index)).to_numpy() == 0

    train = add_features(train_raw)
    test = add_features(test_raw)

    all_categorical = [
        "Surname",
        "Geography",
        "Gender",
        "CustomerId",
        "AgeBin",
        "CreditBin",
        "BalanceBin",
        "GeoGender",
        "GeoProduct",
        "GenderProduct",
        "AgeBinProduct",
        "GeoActive",
        "SurnameGeo",
        "CustomerProduct",
        "AgeCatS4",
        "Sur_Geo_Gend_Sal",
        "AllCat",
    ]
    robust_categorical = [
        "Geography",
        "Gender",
        "AgeBin",
        "CreditBin",
        "BalanceBin",
        "GeoGender",
        "GeoProduct",
        "GenderProduct",
        "AgeBinProduct",
        "GeoActive",
    ]

    if feature_mode == "robust":
        categorical = robust_categorical
        freq_cols = robust_categorical + ["AgeInt"]
        te_cols = ["Geography", "Gender", "GeoGender", "GeoProduct", "GenderProduct", "AgeBinProduct", "GeoActive"]
        manual_drop = {
            "Surname",
            "CustomerId",
            "SurnameGeo",
            "CustomerProduct",
            "AgeCatS4",
            "Sur_Geo_Gend_Sal",
            "AllCat",
        }
    elif feature_mode == "cat_native":
        categorical = all_categorical
        # Keep high-cardinality columns raw for CatBoost ordered CTRs. Hand-made
        # target/frequency encodings of CustomerId/Surname overfit this competition.
        freq_cols = robust_categorical + ["AgeInt"]
        te_cols = ["Geography", "Gender", "GeoGender", "GeoProduct", "GenderProduct", "AgeBinProduct", "GeoActive"]
        manual_drop = set()
    elif feature_mode == "s4e1_text":
        categorical = all_categorical
        add_tfidf_svd_features(train, test, ["Surname", "AllCat"], max_features=1000, n_components=4, seed=seed)
        freq_cols = robust_categorical + ["AgeInt"]
        te_cols = ["Geography", "Gender", "GeoGender", "GeoProduct", "GenderProduct", "AgeBinProduct", "GeoActive"]
        manual_drop = set()
    else:
        categorical = all_categorical
        freq_cols = categorical + ["AgeInt"]
        te_cols = [
            "Surname",
            "CustomerId",
            "Geography",
            "Gender",
            "GeoGender",
            "GeoProduct",
            "GenderProduct",
            "AgeBinProduct",
            "SurnameGeo",
            "CustomerProduct",
        ]
        manual_drop = set()

    add_frequency_features(train, test, freq_cols)
    add_target_encoding(train, test, y, te_cols, folds=folds, seed=seed)

    drop_cols = {ID_COL, TARGET, EXTERNAL_FLAG, *manual_drop}
    features = [c for c in train.columns if c not in drop_cols]
    categorical = [c for c in categorical if c in features]
    for col in categorical:
        categories = pd.Index(pd.concat([train[col], test[col]], axis=0).astype(str).unique())
        dtype = CategoricalDtype(categories=categories, ordered=False)
        train[col] = train[col].astype(str).astype(dtype)
        test[col] = test[col].astype(str).astype(dtype)

    return PreparedData(
        train=train,
        test=test,
        features=features,
        categorical=categorical,
        target=y,
        test_ids=test_ids,
        eval_mask=eval_mask,
    )


def make_fold_indices(data: PreparedData, folds: int, seed: int) -> list[tuple[np.ndarray, np.ndarray]]:
    comp_idx = np.flatnonzero(data.eval_mask)
    ext_idx = np.flatnonzero(~data.eval_mask)
    y_comp = data.target.iloc[comp_idx]
    cv = StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed)
    fold_indices = []
    for tr_pos, val_pos in cv.split(comp_idx, y_comp):
        tr_idx = comp_idx[tr_pos]
        if len(ext_idx):
            tr_idx = np.concatenate([tr_idx, ext_idx])
        val_idx = comp_idx[val_pos]
        fold_indices.append((tr_idx, val_idx))
    return fold_indices


def fit_catboost(
    data: PreparedData, args: argparse.Namespace, fold_indices: list[tuple[np.ndarray, np.ndarray]]
) -> tuple[np.ndarray, np.ndarray, list[float]]:
    from catboost import CatBoostClassifier, Pool

    params = {
        "loss_function": "Logloss",
        "eval_metric": "AUC",
        "iterations": args.cat_iterations,
        "learning_rate": 0.035,
        "depth": 5,
        "l2_leaf_reg": 6.0,
        "random_strength": 0.6,
        "border_count": 254,
        "verbose": 250,
        "allow_writing_files": False,
        "random_seed": args.seed,
        "thread_count": -1,
    }
    if args.feature_mode in {"cat_native", "s4e1_text"}:
        params.update(
            {
                "iterations": args.cat_iterations,
                "learning_rate": 0.025,
                "depth": 6,
                "l2_leaf_reg": 8.0,
                "random_strength": 0.35,
                "bootstrap_type": "Bayesian",
                "bagging_temperature": 0.5,
                "one_hot_max_size": 3,
                "max_ctr_complexity": 2,
                "ctr_leaf_count_limit": 64,
                "eval_metric": "AUC",
            }
        )
    if args.use_gpu:
        params.pop("ctr_leaf_count_limit", None)
        params.update({"task_type": "GPU", "devices": args.gpu_device})

    cat_overrides = {
        "learning_rate": args.cat_learning_rate,
        "depth": args.cat_depth,
        "l2_leaf_reg": args.cat_l2_leaf_reg,
        "random_strength": args.cat_random_strength,
        "bagging_temperature": args.cat_bagging_temperature,
        "border_count": args.cat_border_count,
        "one_hot_max_size": args.cat_one_hot_max_size,
        "max_ctr_complexity": args.cat_max_ctr_complexity,
    }
    params.update({key: value for key, value in cat_overrides.items() if value is not None})

    cat_idx = [data.features.index(c) for c in data.categorical]
    oof = np.zeros(len(data.train))
    test_pred = np.zeros(len(data.test))
    scores: list[float] = []

    for fold, (tr_idx, val_idx) in enumerate(fold_indices, 1):
        x_tr = data.train.iloc[tr_idx][data.features]
        x_val = data.train.iloc[val_idx][data.features]
        y_tr = data.target.iloc[tr_idx]
        y_val = data.target.iloc[val_idx]

        model = CatBoostClassifier(**params)
        model.fit(
            Pool(x_tr, y_tr, cat_features=cat_idx),
            eval_set=Pool(x_val, y_val, cat_features=cat_idx),
            use_best_model=True,
            early_stopping_rounds=350,
        )
        oof[val_idx] = model.predict_proba(x_val)[:, 1]
        test_pred += model.predict_proba(data.test[data.features])[:, 1] / len(fold_indices)
        score = roc_auc_score(y_val, oof[val_idx])
        scores.append(score)
        print(f"cat fold {fold}: {score:.6f}; best_iteration={model.get_best_iteration()}")

    return oof, test_pred, scores


def fit_lightgbm(
    data: PreparedData, args: argparse.Namespace, fold_indices: list[tuple[np.ndarray, np.ndarray]]
) -> tuple[np.ndarray, np.ndarray, list[float]]:
    import lightgbm as lgb

    params = {
        "objective": "binary",
        "metric": "auc",
        "learning_rate": 0.025,
        "num_leaves": 31,
        "max_depth": -1,
        "min_child_samples": 80,
        "subsample": 0.85,
        "subsample_freq": 1,
        "colsample_bytree": 0.85,
        "reg_alpha": 0.15,
        "reg_lambda": 3.0,
        "verbosity": -1,
        "seed": args.seed,
        "num_threads": -1,
        "force_col_wise": True,
    }
    if args.use_gpu:
        params.update(
            {
                "device_type": "gpu",
                "gpu_device_id": int(args.gpu_device),
                "force_col_wise": False,
            }
        )

    oof = np.zeros(len(data.train))
    test_pred = np.zeros(len(data.test))
    scores: list[float] = []

    for fold, (tr_idx, val_idx) in enumerate(fold_indices, 1):
        x_tr = data.train.iloc[tr_idx][data.features]
        x_val = data.train.iloc[val_idx][data.features]
        y_tr = data.target.iloc[tr_idx]
        y_val = data.target.iloc[val_idx]
        train_set = lgb.Dataset(x_tr, y_tr, categorical_feature=data.categorical, free_raw_data=False)
        valid_set = lgb.Dataset(x_val, y_val, categorical_feature=data.categorical, free_raw_data=False)
        model = lgb.train(
            params,
            train_set,
            num_boost_round=args.lgb_rounds,
            valid_sets=[valid_set],
            callbacks=[lgb.early_stopping(250), lgb.log_evaluation(250)],
        )
        oof[val_idx] = model.predict(x_val, num_iteration=model.best_iteration)
        test_pred += model.predict(data.test[data.features], num_iteration=model.best_iteration) / len(fold_indices)
        score = roc_auc_score(y_val, oof[val_idx])
        scores.append(score)
        print(f"lgb fold {fold}: {score:.6f}; best_iteration={model.best_iteration}")

    return oof, test_pred, scores


def fit_xgboost(
    data: PreparedData, args: argparse.Namespace, fold_indices: list[tuple[np.ndarray, np.ndarray]]
) -> tuple[np.ndarray, np.ndarray, list[float]]:
    import xgboost as xgb

    x_train = data.train[data.features].copy()
    x_test = data.test[data.features].copy()
    for col in data.categorical:
        x_train[col] = x_train[col].astype("category")
        x_test[col] = x_test[col].astype("category")

    params = {
        "objective": "binary:logistic",
        "eval_metric": "auc",
        "learning_rate": 0.025,
        "max_depth": 4,
        "min_child_weight": 8,
        "subsample": 0.85,
        "colsample_bytree": 0.85,
        "reg_alpha": 0.05,
        "reg_lambda": 4.0,
        "tree_method": "hist",
        "max_cat_to_onehot": 8,
        "seed": args.seed,
        "nthread": -1,
    }
    if args.use_gpu:
        params.update({"device": f"cuda:{args.gpu_device}"})

    oof = np.zeros(len(data.train))
    test_pred = np.zeros(len(data.test))
    scores: list[float] = []

    for fold, (tr_idx, val_idx) in enumerate(fold_indices, 1):
        dtrain = xgb.DMatrix(x_train.iloc[tr_idx], label=data.target.iloc[tr_idx], enable_categorical=True)
        dvalid = xgb.DMatrix(x_train.iloc[val_idx], label=data.target.iloc[val_idx], enable_categorical=True)
        dtest = xgb.DMatrix(x_test, enable_categorical=True)
        model = xgb.train(
            params,
            dtrain,
            num_boost_round=args.xgb_rounds,
            evals=[(dvalid, "valid")],
            early_stopping_rounds=250,
            verbose_eval=250,
        )
        oof[val_idx] = model.predict(dvalid, iteration_range=(0, model.best_iteration + 1))
        test_pred += model.predict(dtest, iteration_range=(0, model.best_iteration + 1)) / len(fold_indices)
        score = roc_auc_score(data.target.iloc[val_idx], oof[val_idx])
        scores.append(score)
        print(f"xgb fold {fold}: {score:.6f}; best_iteration={model.best_iteration}")

    return oof, test_pred, scores


def best_blend(oofs: dict[str, np.ndarray], y: pd.Series, eval_mask: np.ndarray) -> dict[str, float]:
    names = list(oofs)
    if len(names) == 1:
        return {names[0]: 1.0}

    best_score = -math.inf
    best_weights: dict[str, float] | None = None
    steps = np.linspace(0.0, 1.0, 21)

    if len(names) == 2:
        a, b = names
        for w in steps:
            pred = w * oofs[a] + (1.0 - w) * oofs[b]
            score = roc_auc_score(y[eval_mask], pred[eval_mask])
            if score > best_score:
                best_score = score
                best_weights = {a: float(w), b: float(1.0 - w)}
    else:
        for w0 in steps:
            for w1 in steps:
                if w0 + w1 > 1.0:
                    continue
                w2 = 1.0 - w0 - w1
                weights = {names[0]: float(w0), names[1]: float(w1), names[2]: float(w2)}
                pred = sum(weights[n] * oofs[n] for n in names)
                score = roc_auc_score(y[eval_mask], pred[eval_mask])
                if score > best_score:
                    best_score = score
                    best_weights = weights

    assert best_weights is not None
    print(f"best blend OOF: {best_score:.6f}; weights={best_weights}")
    return best_weights


def write_submission(path: Path, test_ids: pd.Series, pred: np.ndarray) -> None:
    sub = pd.DataFrame({ID_COL: test_ids, TARGET: np.clip(pred, 0.0, 1.0)})
    sub.to_csv(path, index=False)
    print(f"wrote {path}")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.models_dir.mkdir(parents=True, exist_ok=True)
    args.report_dir.mkdir(parents=True, exist_ok=True)

    train_raw, test_raw = read_data(args.data_dir, args.external_path)
    data = prepare(train_raw, test_raw, folds=args.folds, seed=args.seed, feature_mode=args.feature_mode)
    print(f"train={data.train.shape}; test={data.test.shape}; features={len(data.features)}")

    fold_indices = make_fold_indices(data, folds=args.folds, seed=args.seed)
    requested = [m.strip().lower() for m in args.models.split(",") if m.strip()]
    runners = {
        "cat": fit_catboost,
        "lgb": fit_lightgbm,
        "xgb": fit_xgboost,
    }

    oofs: dict[str, np.ndarray] = {}
    test_preds: dict[str, np.ndarray] = {}
    report: dict[str, object] = {
        "seed": args.seed,
        "folds": args.folds,
        "models": requested,
        "use_gpu": args.use_gpu,
        "gpu_device": args.gpu_device if args.use_gpu else None,
        "external_path": str(args.external_path) if args.external_path else None,
        "feature_mode": args.feature_mode,
        "feature_count": len(data.features),
        "categorical": data.categorical,
        "cat_overrides": {
            "learning_rate": args.cat_learning_rate,
            "depth": args.cat_depth,
            "l2_leaf_reg": args.cat_l2_leaf_reg,
            "random_strength": args.cat_random_strength,
            "bagging_temperature": args.cat_bagging_temperature,
            "border_count": args.cat_border_count,
            "one_hot_max_size": args.cat_one_hot_max_size,
            "max_ctr_complexity": args.cat_max_ctr_complexity,
        },
        "scores": {},
    }

    for model_name in requested:
        if model_name not in runners:
            raise ValueError(f"unknown model: {model_name}")
        print(f"===== training {model_name} =====")
        oof, test_pred, fold_scores = runners[model_name](data, args, fold_indices)
        model_auc = roc_auc_score(data.target[data.eval_mask], oof[data.eval_mask])
        print(f"{model_name} OOF AUC: {model_auc:.6f}")
        oofs[model_name] = oof
        test_preds[model_name] = test_pred
        report["scores"][model_name] = {
            "folds": [float(x) for x in fold_scores],
            "oof_auc": float(model_auc),
        }
        write_submission(args.output_dir / f"{args.tag}_{model_name}.csv", data.test_ids, test_pred)

    weights = best_blend(oofs, data.target, data.eval_mask)
    blend_oof = sum(weights[name] * oofs[name] for name in weights)
    blend_test = sum(weights[name] * test_preds[name] for name in weights)
    blend_auc = roc_auc_score(data.target[data.eval_mask], blend_oof[data.eval_mask])
    report["scores"]["blend"] = {"oof_auc": float(blend_auc), "weights": weights}

    out_path = args.output_dir / f"{args.tag}.csv"
    write_submission(out_path, data.test_ids, blend_test)
    np.save(args.models_dir / f"{args.tag}_oof.npy", blend_oof)
    np.save(args.models_dir / f"{args.tag}_test.npy", blend_test)
    with open(args.report_dir / f"{args.tag}_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report["scores"], indent=2))


if __name__ == "__main__":
    main()
