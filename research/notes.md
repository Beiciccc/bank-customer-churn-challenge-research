# Public Research Notes

Checked on 2026-04-26.

## 2026-05-29 追加提分循环

- 公开扫描与讨论更新：
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun -v` 仍显示 `wangleboro/churn-prediction-gbdt` 最近运行于 `2026-05-23 20:37:50`，未发现可迁移的新 notebook 版本。
  - 对 `discussion`、`rules` 与高分入口的直接抓取在当前执行环境仍不稳定/不可读；本次改为基于可访问 kernel 元信息与本地 OOF 先验循环。
  - 关键公开代码检查结论：高分公开 notebook 仍以 `GBDT + 交叉特征 + 简单 CV` 为主，未出现可直接落地的新模型族。
- 提交流程（本轮两次）：
  - `run45_rank_40_20_20_20_v1.csv`（`0.89327`） ✅
  - `run45_rank_60_25_15_v1.csv`（`0.89321`） ✅
- 误差分析与策略更新：
  - 两次都高于旧基线 (`0.89306`)，其中 `run45_rank_40_20_20_20_v1.csv` 为新基线（`+0.00021`）。
  - 第二条较第二高，提示 rank-space权重继续下压至更稳健区域。
- 下一步方向（本次提交结束后）：
  - 锁定新的全局最佳为 `run45_rank_40_20_20_20_v1.csv`；
  - 缓慢推进 `run45_isotonic_90_10_on12_v1.csv` 与 `run45_w97_3_isotonic_on12_v1.csv` 做可控校准对照；
  - 若再次回落，则回退到远端重新训练的轻量特征轴（如高基数名称/交互）再回到 rank 空间融合。

## 2026-05-27 Research Note

- 公开更新扫描结果：`wangleboro/churn-prediction-gbdt` 仍是最新公开 notebook（`2026-05-23`），讨论区仍不可稳定抓取。
- 本轮候选生成来源于可用 OOF/test 预测：
  - `run43_prob14_40_33_60.csv`
  - `run43_rank14_50_33_50.csv`
- 两者均通过本地文件与提交预检（`id` 对齐、`110,023` 行、`[0,1]` 且有限）。
- 公开分数结果：
  - `0.89123`（`run43_prob14_40_33_60.csv`）
  - `0.89247`（`run43_rank14_50_33_50.csv`）
- 结论：
  - run14/run33_xgb 的概率与 rank 空间方向本轮均未超越基线；
  - rank 空间路径虽然把相关性显著压低，但短期未带来增益。
- 下一步：
  - 转向 run41 家族（`run41_xgb_robust` / `run41_lgb_robust`）与 run33 的低相关 mix，保留单轮只两步提交节奏，并严格记录预期与失效原因。

## 2026-05-27 追加提分循环（提交受限）

- 当前提交通知：`2026-05-27` 仍有 `2/2` 次提交（`run43_prob14_40_33_60.csv`, `run43_rank14_50_33_50.csv`）已完成，配额到达上限，API 直接返回 `23 hours from now` 的重置提示。
- 公网更新扫描保持不变：
  - `wangleboro/churn-prediction-gbdt` 仍是最新 notebook（`2026-05-23`）。
  - 讨论区抓取仍无效（反爬/反验证码导致不可稳定提取）。
- 本轮新增候选（本地 OOF 先验 + 本地格式验证）：
  - `run44_rank33_14_41xgb_60_20_20.csv`
  - `run44_prob33_14_41lgb_60_20_20.csv`
- 预检结果：
  - 两者均是 `id,Exited`、`110,023` 行、`[0,1]` 且无 NaN/inf；
  - test id 完全对齐；
  - OOF 指标：
    - `rank` 版：`0.89714`（`corr(run33_xgb)=0.8480`）
    - `prob` 版：`0.89727`（`corr(run33_xgb)=0.9966`）
- 结果与规则：
  - `run44_rank33_14_41xgb_60_20_20.csv` 提交前 1 次尝试被 `daily Submission allowance (2)` 拒绝；
  - 暂停第二次提交；
  - 计划 UTC 归位后按既定顺序提交；若两者都失败，继续回溯到更低相关方向（新 feature 轴或 rank-only 混合）而非增大高相关 prob 方向。

## 2026-05-28 Research Note

- 今日更新：`2026-05-28` 额度已恢复为可用（当日未检测到历史提交）。
- 公开更新扫描保持不变：
  - `wangleboro/churn-prediction-gbdt`（`2026-05-23`）仍是可见最新 notebook；
  - 讨论区仍无法稳定抓取（反爬/验证码拦截）。
- 按既定队列提交两份候选：
  - `run44_rank33_14_41xgb_60_20_20.csv`
  - `run44_prob33_14_41lgb_60_20_20.csv`
- 公榜结果：
  - `0.89103`（rank 混合）
  - `0.89101`（prob 混合）
- 错误分析与规则更新：
  - 两份均未超越当前基线 `0.89306`；
  - 低相关 rank 路径未兑现预期提升；
  - 高相关 prob 路径回撤更明显；
  - 下一步转向不同建模轴（校准/分组-校准策略，或远端新增特征轴重训）再重新进入提交。

## 2026-05-28 追加提分循环（配额阻塞，候选重排）

- 公开扫描维持不变：`wangleboro/churn-prediction-gbdt` 截止仍是 `2026-05-23` 的版本，讨论抓取仍不可稳定读取。
- 当前配额：`2026-05-28` 已使用 `2/2`，未到 UTC 重置。
- 本地 OOF 重扫（run45 系列 + run33/run12）后，新增可用候选：
  - `run45_rank_40_20_20_20_v1.csv`（OOF `0.8985637`）
  - `run45_rank_60_25_15_v1.csv`（OOF `0.8985034`）
  - `run45_isotonic_90_10_on12_v1.csv`（OOF `0.8983295`）
  - `run45_w97_3_isotonic_on12_v1.csv`（OOF `0.8982906`）
- 通过本地验证：`id,Exited`、`110,023` 行、`[0,1]`、无 NaN/Inf、id 对齐。
- 同步状态：候选文件已本地生成并同步到远端路径。
- 下一步：解封后按以下顺序提交并逐条记录分数：
  1) `run45_rank_40_20_20_20_v1.csv`
  2) `run45_rank_60_25_15_v1.csv`

如果两条都失败，再评估是否引入保守的校准备选。

## 2026-05-26 Research Note

- `kaggle competitions submissions` showed `0` entries for this date at loop start (remaining quota 5/5), so 2 submits were executed.
- Kernel/discussion refresh:
  - `wangleboro/churn-prediction-gbdt` remained the latest public notebook snapshot (`2026-05-23 20:37:50.307000`).
  - Discussion pages were not extractable in this environment.
- Submission probes:
  - `run39_rank_hybrid_87_05_00_08.csv` → `0.88904`.
  - `run39_mix_72_12_08_08.csv` → `0.89014`.
- Both submissions used valid files (`id,Exited`, row alignment, finite predictions), but still regressed versus best public baseline.
- Next direction:
  - pause run33-heavy probability mixtures.
  - prioritize lower-correlation rank/prob hedges and new engineered-feature model candidates (surname-derived interaction/click-frequency variants) on remote GPU, one experiment per cycle.

## Competition Pages

- Checked on `2026-05-18`: no new high-signal public code beyond existing high-level baselines was observed. `wangleboro/churn-prediction-gbdt` remains the only notable notebook update, but its code is unchanged conceptually from earlier and still dominated by simple tree-ensemble baselines.
- Evaluation: ROC AUC on predicted `Exited` probability.
- Data: competition train/test were generated from a deep learning model trained on an original Bank Customer Churn Prediction dataset; original public data is explicitly allowed.
- Rules: public external data is allowed when available to all competitors at no cost.

## 2026-05-24 Research Note

- Public kernel refresh:
  - `kaggle kernels list --competition ... --sort-by dateRun -v` now shows latest `wangleboro/churn-prediction-gbdt` run time `2026-05-23 20:37:50`.
  - `scoreDescending` ordering remains unchanged.
  - Discussion endpoints still inaccessible in this environment (forum scrape failure), so no new external discussion signal available.
- Extracted feature signals from latest notebook pull:
  - `SingleProduct`, `CardButInactive`, `ZeroBalance`, `Balance_Per_Product`.
  - surname features such as `Surname_prefix`, `Surname_len`, `Surname_freq`.
- Cycle 2026-05-24 execution:
  - `run40_rank14_33_70_30_r.csv` scored `0.89304` (regression).
  - `run42_prob_25_35_40.csv` scored `0.89278` (further regression).
  - Best remains `run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Next research direction:
  - Rebuild feature extraction on a fresh GPU training pass using surname-derived engineered signals before any further large blend sweeps.
  - Keep blend experiments conservative and risk-gated (rank-space / low-corr direction first).

## 2026-05-25 Research Note

- Pre-loop status:
  - `kaggle competitions submissions --csv` showed one existing 2026-05-25 entry, so remaining daily allowance remained `4/5`.
  - `kaggle kernels list --competition ... --sort-by dateRun -v` still shows latest public notebook `wangleboro/churn-prediction-gbdt` at `2026-05-23 20:37:50`.
  - Discussion/forum endpoints are still not accessible in this environment.
- Cycle execution signal:
  - `run40_pair14_33_w067_033_prob.csv`: `0.89248` (`-0.00058` from best).
  - `run42_trip_25_30_45.csv`: `0.89279` (`-0.00027` from best).
- Error/risk analysis:
  - Both results suggest the high-correlation probability blend family still over-corrects on public folds.
  - The leaderboard top is still not moving upward with these families, so direct probability-space perturbations from the same OOF manifold are high-risk.
- Next research direction:
  - Shift to lower-correlation rank-space hedges and/or remote GPU re-training that adds explicit `Surname`/ID interaction features from `wangleboro` feature patterns, with strict score-guard rule:
    - any candidate used as next step must be locally validated for monotonicity and prediction spread before submission.

## 2026-05-23 Execution Note (Quota 0/2, Queue Hold)

- `kaggle competitions submissions` is blocked at **2/2** for this date (`2026-05-23 07:47 UTC` check), so no new Kaggle upload is currently possible.
- Rechecked `kaggle kernels` and `kaggle competitions pages`:
  - No new high-signal notebook or public code change since the prior loop.
  - No discoverable new discussion thread content in this environment (anti-forgery errors / inaccessible forum endpoints).
- Experiment path retained for next retry:
  - `run40_rank14_33_70_30_r.csv` as safer rank-space hedge.
  - `run42_prob_25_35_40.csv` as controlled follow-up (higher OOF, higher corr risk).
- ETA to reset: `~17.11h` from `2026-05-23 07:47 UTC` check.
- Both files remain validated in both local and remote workdirs.

## 2026-05-23 Execution Note

- 2 new stack candidates were generated and validated locally:
  - `run38_stack_lr_5f_div_c0p1.csv` (5-feature logistic stack, C=0.1) with local OOF `0.8984406`.
  - `run38_stack_lr_4f_div_c05.csv` (4-feature logistic stack, C=0.05) with local OOF `0.8984239`.
- Both files passed format checks (`id` alignment, `[0,1]`, no NaNs).
- Submission attempts were blocked by Kaggle API permission (`Permission 'competitions.participate' was denied`) before a new public score could be obtained.

## Current Competition Public Notebooks

- Himanshu Dhiman and Payal Dhokane notebooks: simple 5-fold XGBoost, drop `id`, `CustomerId`, `Surname`, label encode `Geography/Gender`, add `Balance_Per_Product`.
- Le Wang notebook: sklearn `GradientBoostingClassifier`, drops `id/CustomerId`, keeps `Surname` dropped through label processing, adds `SingleProduct`, `CardButInactive`, `ZeroBalance`; notes public submission around `0.8855`.
- Nada Arfaoui notebook: broader EDA plus RF/XGB/LGB ensemble; mostly holdout validation rather than competition-grade CV.

## Related S4E1 High-Score Signal

The earlier Kaggle Playground S4E1 bank churn competition used the same source family. A public README summarizing the first-place discussion says the important point was to treat `CustomerId` and `Surname` as high-cardinality categorical variables and encode them correctly; it also says a single tuned CatBoost averaged over 20 folds was enough to win.

Actionable experiment: add `cat_native` mode that leaves `CustomerId` and `Surname` raw for CatBoost ordered CTRs, while removing hand-made target/frequency encodings for those columns.

## 2026-05-23 Quota Blocked Submission Queue

- `kaggle competitions submissions` shows 2 entries for 2026-05-23 (this date quota usage reached `2/2`).
- Current best remains `run33run14_on12_w10_10_v3.csv` (`0.89306`).
- New local experiment queue prepared for next reset:
  - `run39_rank_hybrid_87_05_00_08.csv` (rank-space hedge, lower correlation to current baseline, safer).
  - `run39_mix_72_12_08_08.csv` (higher OOF `0.90499` but high correlation, higher overfit risk).
- Kaggle API create-submission block now explicitly confirms: allowance used up for the day; `Submission not allowed: your team has used its daily Submission allowance (2) today`.
- Re-check at 2026-05-23 06:43 UTC:
  - Public-kernel refresh still unchanged (`wangleboro/churn-prediction-gbdt` still top with no visible model-family jump).
  - New candidate generation after local/OOF probing:
    - `run40_pair14_33_w067_033_prob.csv` (OOF `0.8982258`, corr vs current best `0.99760`).
    - `run40_rank14_33_70_30_r.csv` (OOF `0.898210`, corr vs current best `0.85074`, rank-space hedge).
    - `run40_trip125_075_10_prob.csv` (OOF `0.8983447`, corr `0.99915`, high-risk/low-diversity).
  - One fresh remote run (`run40_cat_native_202_regA`) was synced locally, but it produced CPU-only CatBoost with weak OOF (`0.888953`) and will not be submitted first.

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
