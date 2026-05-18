# Public Research Notes

Checked on 2026-04-26.

## Competition Pages

- Checked on `2026-05-18`: no new high-signal public code beyond existing high-level baselines was observed. `wangleboro/churn-prediction-gbdt` remains the only notable notebook update, but its code is unchanged conceptually from earlier and still dominated by simple tree-ensemble baselines.
- Evaluation: ROC AUC on predicted `Exited` probability.
- Data: competition train/test were generated from a deep learning model trained on an original Bank Customer Churn Prediction dataset; original public data is explicitly allowed.
- Rules: public external data is allowed when available to all competitors at no cost.

## Current Competition Public Notebooks

- Himanshu Dhiman and Payal Dhokane notebooks: simple 5-fold XGBoost, drop `id`, `CustomerId`, `Surname`, label encode `Geography/Gender`, add `Balance_Per_Product`.
- Le Wang notebook: sklearn `GradientBoostingClassifier`, drops `id/CustomerId`, keeps `Surname` dropped through label processing, adds `SingleProduct`, `CardButInactive`, `ZeroBalance`; notes public submission around `0.8855`.
- Nada Arfaoui notebook: broader EDA plus RF/XGB/LGB ensemble; mostly holdout validation rather than competition-grade CV.

## Related S4E1 High-Score Signal

The earlier Kaggle Playground S4E1 bank churn competition used the same source family. A public README summarizing the first-place discussion says the important point was to treat `CustomerId` and `Surname` as high-cardinality categorical variables and encode them correctly; it also says a single tuned CatBoost averaged over 20 folds was enough to win.

Actionable experiment: add `cat_native` mode that leaves `CustomerId` and `Surname` raw for CatBoost ordered CTRs, while removing hand-made target/frequency encodings for those columns.

## 2026-04-26 Experiments

- `run03_cat_native_20f`: 20-fold CatBoost with native `CustomerId/Surname`; OOF `0.889285`. Useful diversity, but lower than `run02` alone.
- `run04_blend_run02_run03`: best two-way OOF blend was `0.68*run02 + 0.32*run03`, OOF `0.890206`, public `0.88634`.
- `run05_cat_native_ext_5f`: added public original Churn_Modelling data only to training folds; validation stayed on competition train rows. OOF `0.889288`, so original data did not help as a standalone model.
- `run06_blend_235`: best coarse three-way blend was `0.62*run02 + 0.18*run03 + 0.20*run05`, OOF `0.890246`, public `0.88635`.

Next likely directions:

- Hyperparameter sweep around robust CatBoost/LightGBM rather than more high-cardinality leakage.
- Try rank averaging instead of probability averaging for `run02/run03/run05`.
- Train multiple seeds for the robust blend; current gains are mostly variance reduction.

## 2026-04-28 Public Code Follow-Up

Current-competition public notebooks still mostly use simple XGBoost/GBDT baselines and do not expose the top two teams' full code. The more useful public signal came from the related Playground S4E1 high-score notebooks and solution writeups:

- CatBoost-native treatment of high-cardinality `CustomerId`/`Surname` remains useful, but only when combined conservatively; direct target/frequency leakage-like statistics overfit badly in run01.
- S4E1 notebooks repeatedly use interaction categories such as `Sur_Geo_Gend_Sal` and `AllCat`, plus derived features like `Products_Per_Tenure`, `IsSenior`, and coarse age categories.
- Text/vector features over `Surname` and combined categorical strings were a plausible way to extract signal without hand-made target encodings, so `s4e1_text` adds char TF-IDF plus 4-component SVD for `Surname` and `AllCat`.

Experiments:

- `run07_rank_blend_235`: rank blend over run02/run03/run05, OOF `0.890280`, public `0.88637`.
- `run08_s4e1_text_cat_5f`: CatBoost with native categories, S4E1 combo categories, and text SVD features. OOF `0.890760`. It was not submitted standalone because blending offered higher OOF.
- `run09_prob_blend_2358`: best coarse 4-run blend collapsed to `0.35*run02 + 0.65*run08`, OOF `0.891021`, public `0.88725`. This improved the public score by `+0.00088` over run07 and moved the team to rank 4 of 10.

Next likely directions:

- Train `s4e1_text` with additional seeds/folds and blend them; run08 is now the strongest single local signal.
- Try a small Optuna/manual sweep around the run08 CatBoost parameters, especially `depth`, `l2_leaf_reg`, `random_strength`, `bagging_temperature`, and `ctr_leaf_count_limit`.
- Revisit original-data use only after comparing distribution shift feature-by-feature; adding original rows directly did not help run05.

## 2026-04-28 GPU CatBoost Follow-Up

Public research takeaway:

- Current competition notebooks remain weaker than the existing local best.
- Related S4E1/S5E8/S6E3 solution archives reinforce the value of many OOF sources and blending/stacking rather than a single baseline model.

Experiment:

- CatBoost GPU cannot use the non-default `ctr_leaf_count_limit`; GPU mode now removes it.
- `run10` seed 202 OOF `0.897375`.
- `run11` seed 777 OOF `0.897412`.
- `run12` seed average OOF `0.897786`.

Risk:

- The OOF jump is large and stable, but test predictions are more extreme and correlate strongly with the known-overfit run01. This is a high-risk/high-reward submission candidate rather than a guaranteed safe improvement.
- Submission attempt returned Kaggle `400 Client Error` after upload, with no new entry in the submissions list, likely because the daily quota was already used.

## 2026-04-29 Two-Submission Cycle

- `run12_gpu_cat_seed_blend_10_11` was submitted successfully after quota reset. Public score `0.89293`, moving the team to rank 1.
- After `run12` validated the GPU CatBoost CTR path, two more remote GPU seeds were trained:
  - `run13_s4e1_text_cat_gpu_s314`: OOF `0.897482`.
  - `run14_s4e1_text_cat_gpu_s1001`: OOF `0.897616`.
- `run15_gpu_cat_4seed_weighted`: weighted blend of `run10/run11/run13/run14`, OOF `0.898070`, public `0.89291`.

Takeaway:

- Public score confirmed that the high-capacity GPU CatBoost family is the main scoring path.
- More seed averaging improved OOF but did not beat the simpler `run12` public score. Further submissions should be more careful than simply adding same-family seeds.

## 2026-04-30 Two-Submission Cycle

- Public update check: `wangleboro/churn-prediction-gbdt` was rerun on Kaggle, but the pulled notebook was byte-identical to the prior version; no new modeling signal.
- `run16_run12_70_seed1314_30`: OOF `0.897998`, public `0.89293`, tied the current best.
- `run17_rank_run12_50_rank1314_50`: OOF `0.898053`, public `0.89291`, below best by `0.00002`.

Takeaway:

- Public results favor staying extremely close to `run12`; rank transforms and broader seed averaging have not beaten it.
- The next real improvement likely needs a changed modeling axis, not another near-duplicate blend.

## 2026-05-01 Two-Submission Cycle

- Kaggle submissions list confirmed a fresh `2/2` quota at `2026-05-01 00:07:48 UTC`.
- Public notebook list still contained the same five notebooks; `wangleboro/churn-prediction-gbdt` reran at `2026-04-30 16:57:26.153000`, but notebook pull and leaderboard refresh failed due intermittent Kaggle DNS.
- `run18_run12_99_run02_01`: OOF `0.897777`, public `0.89293`, tied current best. A tiny `run02` robust-model hedge did not hurt public score.
- `run19_rank_run12_90_run09_10`: OOF `0.897605`, public `0.89280`, below best by `0.00013`.

Takeaway:

- Very small probability-space hedges around `run12` can preserve public score, but rank-space perturbations with weaker pre-GPU models are currently harmful.
- Avoid spending more submissions on `run09` rank blending. The next useful work should be a new remote-trained model axis or a better validation scheme for choosing borderline ordering changes.

## 2026-05-01 Follow-Up Request

- A later quota check at `2026-05-01 02:16 UTC` showed the two same-day submissions `run18` and `run19`, so remaining quota was `0/2`.
- Leaderboard refresh succeeded and confirmed current rank `1 / 11`, best public `0.89293`.
- The latest pulled `wangleboro/churn-prediction-gbdt` notebook remains a simple sklearn GBDT baseline; it does not change the scoring direction.
- Next queued experiment is `run20_s4e1_text_cat_gpu_reg_d5_ctr1_2seed`: same seeds as `run10/run11`, but stronger regularization and lower CTR complexity.
- Remote server was not reachable during the prep check (`Host is down`), so GPU training waits for remote recovery.
