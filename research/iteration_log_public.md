# Public Record

# Submission Iteration Log

This file is the required checkpoint after each Kaggle submission. Each cycle records the score first, then the research and experiment plan for the next attempt.

## Current Best

- Submission: `submissions/public/run45_rank_40_20_20_20_v1.csv`
- Latest submission: `2026-05-29 00:28:39.500000`
- OOF/CV (local blend): `0.8985637`
- Public score: `0.89327`
- Rank after submission: `1 / 11` as refreshed on `2026-05-29 UTC`.
- Delta vs previous best: `+0.00021`
- Notes: 3-model-style rank-space hedge with improved public transfer (`+0.00021`).

## 2026-05-29 Two-Submission Cycle

- Pre-loop:
  - `kaggle competitions submissions --csv` showed `0` entries for `2026-05-29`; quota started at `2/2`.
  - Public kernel baseline unchanged: `wangleboro/churn-prediction-gbdt` (`2026-05-23`).
  - Discussion feed remains inaccessible in this environment.
  - Queue validated:
    - `run45_rank_40_20_20_20_v1.csv`
    - `run45_rank_60_25_15_v1.csv`

Cycle 1:

- File: `run45_rank_40_20_20_20_v1.csv`
- Public score: `0.89327` (improved)

Cycle 2:

- File: `run45_rank_60_25_15_v1.csv`
- Public score: `0.89321` (small drop from cycle best, still above old baseline)

Current status:

- Best remains `submissions/public/run45_rank_40_20_20_20_v1.csv` at `0.89327`.
- Quota used on 2026-05-29: `2/2`.
- Next plan: keep `run45_rank_40_20_20_20_v1.csv` as anchor; next validation batch should explore calibration/orthogonality-preserving variants (`run45_isotonic_90_10_on12_v1.csv`, `run45_w97_3_isotonic_on12_v1.csv`) after the next reset.

## 2026-05-26 Two-Submission Cycle

- Pre-loop:
  - Two-submission cycle started with full daily quota (`5/5`).
  - Top recent public kernel is still `wangleboro/churn-prediction-gbdt` (`2026-05-23`), and discussion feed is not accessible in this environment.

Cycle 1:

- File: `run39_rank_hybrid_87_05_00_08.csv`
- Public score: `0.88904` (regressed)

Cycle 2:

- File: `run39_mix_72_12_08_08.csv`
- Public score: `0.89014` (regressed)

Current status:

- Best remains `run33run14_on12_w10_10_v3.csv` (`0.89306`).
- Daily remaining submissions: `3/5`.
- Next plan: test lower-correlation rank-style hedges and feature-variant models first, then evaluate only one high-risk mix as follow-up.

## 2026-05-27 Two-Submission Cycle

- Pre-loop:
  - Two-submission cycle started with full daily quota (`5/5`).
  - `kaggle kernels list` still latest `wangleboro/churn-prediction-gbdt` (`2026-05-23`), no accessible discussion feed.
  - Queue prepared:
    - `run43_prob14_40_33_60.csv`
    - `run43_rank14_50_33_50.csv`

Cycle 1:

- File: `run43_prob14_40_33_60.csv`
- Public score: `0.89123` (regressed)

Cycle 2:

- File: `run43_rank14_50_33_50.csv`
- Public score: `0.89247` (regressed)

Current status:

- Best remains `run33run14_on12_w10_10_v3.csv` (`0.89306`).
- Daily remaining submissions: `3/5`.
- Next plan: evaluate run41-family diversification with conservative run33/41 mixtures and a rank-space follow-up when stable.

## 2026-05-27 Two-Submission Cycle (Quota Block)

- Pre-loop:
  - UTC check at `2026-05-27 01:23`: today already has `2/2` completed submissions.
  - Public-kernel scan unchanged: `wangleboro/churn-prediction-gbdt` (`2026-05-23`).
  - Discussion still inaccessible.
  - Queue prepared and validated:
    - `run44_rank33_14_41xgb_60_20_20.csv`
    - `run44_prob33_14_41lgb_60_20_20.csv`

Cycle 1:

- Candidate: `run44_rank33_14_41xgb_60_20_20.csv`
- Status: BLOCKED by quota.
- Message: `Submission not allowed: Your team has used its daily Submission allowance (2) today`.

Cycle 2:

- Not started due quota.
- ETA to retry: `23.6` hours.
- Plan: wait for UTC reset then submit candidates in order (`rank` then `prob`).

## 2026-05-28 Two-Submission Cycle

- Pre-loop:
  - `2026-05-28` started with `0` completed submissions in list, so cycle had `2/2` quota.
  - Public-kernel scan unchanged: `wangleboro/churn-prediction-gbdt` (latest `2026-05-23`).
  - Discussion抓取仍不可稳定获取。
  - Queue confirmed:
    - `run44_rank33_14_41xgb_60_20_20.csv`
    - `run44_prob33_14_41lgb_60_20_20.csv`

Cycle 1:

- File: `run44_rank33_14_41xgb_60_20_20.csv`
- Public score: `0.89103` (failed)

Cycle 2:

- File: `run44_prob33_14_41lgb_60_20_20.csv`
- Public score: `0.89101` (failed)

Current status:

- Best remains `run33run14_on12_w10_10_v3.csv` (`0.89306`) by public record.
- 2026-05-28 submissions used: `2/2`.
- Next direction:
  - pause direct convex run33/run41 variants.
  - reroute to orthogonal feature/model-axis experiments before next public submission.

## 2026-05-28 Two-Submission Cycle (Refresh Before Reset)

- Pre-loop check at `2026-05-28 12:08 UTC`:
  - `kaggle competitions submissions ... --csv` shows `2/2` used for this date, so submissions are blocked until UTC reset.
  - `kaggle kernels list --competition ... --sort-by dateRun -v` remains unchanged: `wangleboro/churn-prediction-gbdt` (`2026-05-23 20:37:50`).
  - Discussion pages still unavailable via current scraping path.

- Candidate refresh from local OOF scan (run45 family) for post-reset queue:
  - `run45_rank_40_20_20_20_v1.csv` (OOF `0.8985637`)
  - `run45_rank_60_25_15_v1.csv` (OOF `0.8985034`)
  - `run45_isotonic_90_10_on12_v1.csv` (OOF `0.8983295`)
  - `run45_w97_3_isotonic_on12_v1.csv` (OOF `0.8982906`)
  - All candidates are format-valid and synced to remote project path.

- Cycle status:
  - No submission yet (quota block).
  - Reset-queue order for next cycle:
    1) `run45_rank_40_20_20_20_v1.csv`
    2) `run45_rank_60_25_15_v1.csv`
  - Calibrated backups remain for controlled follow-up if first two candidates both fail the next rule test.

## 2026-05-25 Two-Submission Cycle

- Pre-loop checks at `2026-05-25 06:58 UTC`:
  - `kaggle competitions submissions ... --csv` showed `1` entry for `2026-05-25`, so quota at start was `4/5`.
  - `kaggle kernels list --competition ... --sort-by dateRun -v` unchanged from prior check (`wangleboro/churn-prediction-gbdt`, `2026-05-23 20:37:50.307000`).
  - Discussion pages remain inaccessible in this environment; no new forum signal was available.
  - Queue validated locally:
    - `run40_pair14_33_w067_033_prob.csv`
    - `run42_trip_25_30_45.csv`

Cycle 1:

- File: `submissions/public/run40_pair14_33_w067_033_prob.csv`
- Submitted: `2026-05-25 06:58:37.757000`.
- Public score: `0.89248`.
- Status: COMPLETE.
- Result: FAILED (below best by `-0.00058`).

Cycle 2:

- File: `submissions/public/run42_trip_25_30_45.csv`
- Submitted: `2026-05-25 07:02:59.587000`.
- Public score: `0.89279`.
- Status: COMPLETE.
- Result: FAILED (below best by `-0.00027`).

Cycle result:

- Best remains unchanged:
  - `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Remaining quota for `2026-05-25`: `3/5` (if limit is still 5/day).
- Next step:
  - Continue with lower-correlation ranking/feature-axis experiments before more high-correlated probability blends.

## 2026-05-24 Two-Submission Cycle

- Pre-loop checks at `2026-05-24 03:19 UTC`:
  - `kaggle competitions submissions ... --csv` showed `0/5` used for `2026-05-24`.
  - `kaggle kernels list --competition ... --sort-by dateRun -v`: latest active notebook remains `wangleboro/churn-prediction-gbdt` with run time `2026-05-23 20:37:50.307000`.
  - `kaggle kernels list --competition ... --sort-by scoreDescending -v` ranking order unchanged.
  - Discussion channels remained inaccessible (no forum scrape available in this environment).
- Public-signal direction before submit:
  - Pull and inspect of `wangleboro/churn-prediction-gbdt` confirmed continued use of interaction features:
    - `SingleProduct`, `CardButInactive`, `ZeroBalance`, `Balance_Per_Product`,
    - basic surname processing (`Surname_prefix`, `Surname_len`, `Surname_freq`).
  - Queue unchanged and format-valid:
    - `run40_rank14_33_70_30_r.csv`
    - `run42_prob_25_35_40.csv`

Cycle 1:

- File: `run40_rank14_33_70_30_r.csv`
- Submitted: `2026-05-24 03:20:26.063000`.
- Public score: `0.89304`.
- Status: COMPLETE.
- Result: FAILED (below best, no public improvement).

Cycle 2:

- File: `run42_prob_25_35_40.csv`
- Submitted: `2026-05-24 03:21:01.500000`.
- Public score: `0.89278`.
- Status: COMPLETE.
- Result: FAILED (further below best).

Cycle result:

- Best remains unchanged at `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`.
- Remaining quota for 2026-05-24 after two attempts: `3/5`.
- Rule rewrite:
  - Decrease blend-confidence on high-correlated probability combinations in this phase.
  - Next experiments should prioritize additional low-overfit feature-axis changes (surname-derived handling and interaction flags), then re-test with conservative blends.

## 2026-05-23 Submission Attempt Blocked (Quota 0/2, Refresh + Queue Freeze)

- Pre-loop checks at `2026-05-23 07:47 UTC`:
  - `kaggle competitions submissions ... --csv` confirms `2` entries for this date; remaining is `0/2`.
  - Latest submissions for today: `run36_nonleak_55_25_10_10` and `run37_rank21_595_255_05_10` (both COMPLETE).
- Public-signal refresh:
  - `kaggle kernels list` in both `dateRun` and `scoreDescending` remains unchanged; latest active notebook remains `wangleboro/churn-prediction-gbdt` (`2026-05-07`).
  - Discussion endpoints are still inaccessible from this environment (anti-forgery failure), so no reliable thread signal to pivot on.
- Candidate queue/validation hold:
  - `run40_rank14_33_70_30_r.csv` and `run42_prob_25_35_40.csv` remain the next two submissions, each format-validated (`id,Exited`, `110,023` rows, aligned ids, finite predictions in `[0,1]`).
- Submission status:
  - No legal upload possible (`Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`).
- Error analysis and next action:
  - Limitation is quota-level, not content-level.
  - ETA to reset: `~17h11m` (`2026-05-24 00:00:00 UTC`).
  - Next retry should preserve candidate order and log public-score deltas immediately after each successful upload.

## 2026-05-23 Submission Attempt Blocked (Quota 0/2, Research Re-scan + Queue Locked)

- Pre-loop checks at `2026-05-23 07:42 UTC`:
  - `kaggle competitions submissions` confirms **2** entries for today, so quota is `0/2`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun -v` remains unchanged; latest active benchmark is `wangleboro/churn-prediction-gbdt` (`2026-05-07`), with no new candidate pattern.
  - `kaggle competitions pages` returns the same core pages only (no changed public constraints surfaced).
  - Discussion pages remain blocked in this environment by anti-forgery / 403-style access behavior (cannot extract fresh high-signal thread content).
- Experiment direction and queue:
  - Keep queue unchanged to preserve a controlled probe:
    - Cycle-2 step 1: `run40_rank14_33_70_30_r.csv`.
    - Cycle-2 step 2: `run42_prob_25_35_40.csv` if first step is not clearly regressive in score delta.
  - These were selected from local OOF/correlation screens and are already mirrored to `submissions/public` and synced to remote.
- Verification before submission:
  - `id/Exited` format + test id alignment, no NaN/infinite values, all values in `[0,1]`, `110,023` rows.
- Submission status:
  - No submission request was accepted due daily allowance block (`Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`).
- Error analysis:
  - Submission is currently blocked by API allowance.
  - Immediate next action: retry exactly at UTC reset window in the same two-candidate order and log post-submit deltas.

## 2026-05-23 Submission Attempt (Quota Block)

- Pre-loop checks at `2026-05-23 06:03 UTC`:
  - `kaggle competitions submissions` still shows **2** entries for today (`run35_stack_lr_5f`, `run36`, `run37` already complete this date).
  - Public baseline remained `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged since last loop; no visible high-signal notebook updates.
  - Discussion API/pages were again blocked in this environment; no new high-signal thread content available.
- Experiment direction before submission:
  - I generated two new candidates from local OOF/test assets and validated format (`id/Exited`, `110,023` rows, no NaN, `[0, 1]`):
    - `run39_rank_hybrid_87_05_00_08.csv` (rank blend: `0.87*run33 + 0.05*run34 + 0.08*run21`)
    - `run39_mix_72_12_08_08.csv` (prob blend: `0.72*run33 + 0.12*run34 + 0.08*run12 + 0.08*run21`)
  - Local OOF checks:
    - `run39_rank_hybrid...`: `0.9020047308`
    - `run39_mix...`: `0.9049923967`
  - Correlation risk note:
    - `run39_rank_hybrid...` corr vs run33 test: `0.855` (lower risk blend)
    - `run39_mix...` corr vs run33 test: `0.9975` (high collinearity / higher overfit risk)
- Submission attempt 1:
  - File: `run39_rank_hybrid_87_05_00_08.csv`
  - Result: **BLOCKED before scoring**.
  - API message: `Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`.
- Submission attempt 2:
  - File: `run39_mix_72_12_08_08.csv`
  - Result: **BLOCKED before scoring**.
  - API message: same allowance block.
  - Result:
  - No leaderboard update; public best remains `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - Daily allowance remaining now inferred as `0/2`.
- Error rewrite:
  - This cycle ended on **submission-day-limit** gating, not a content issue.
  - Next step: wait for UTC reset (`~18h` from now when this limit hit), then resubmit the queue starting with the lower-risk rank blend first.

## 2026-05-23 Submission Attempt (Quota Block, Experiment Queue Finalized)

- Pre-loop checks at `2026-05-23 06:42 UTC`:
  - `kaggle competitions submissions` confirms **2** entries for today (`run39_rank_hybrid...`, `run39_mix...`), so quota is still `0/2` and direct submit is blocked.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` still returns only the existing top kernels (`wangleboro/churn-prediction-gbdt` remains latest public update).
  - Discussion feed/API pages remain unusable in this environment (403/parse failures).
- Experiment direction before reset:
  - Added a deterministic local sweep on `(run33, run14, run12, run34)` OOFs to pick one low-risk and one higher-omega candidate for the next two submissions:
    - `run40_rank14_33_70_30_r.csv` (`rank` blend equivalent to approx `0.70*run14 + 0.30*run33`): local OOF proxy `0.898210`, corr with run33 `0.84552` (low drift-risk).
    - `run42_prob_25_35_40.csv` (`0.25*run33 + 0.35*run14 + 0.40*run12`): local OOF proxy `0.898358`, corr with run33 `0.99087` (higher-risk, expected to be less stable).
  - Both files pass hard validation on test set format (`id,Exited`, 110,023 rows, no NaN, in `[0,1]`, ID alignment).
  - Current queue was mirrored to `submissions/public/` and synced to remote path `/C:/Users/Kun/Bank Customer Churn Challenge/submissions/public`.
- Submission status:
  - Still blocked: no submit executed in this cycle.
- Rule update:
  - First submission after reset should be `run40_rank14_33_70_30_r.csv`.
  - Second submission should be `run42_prob_25_35_40.csv` only if first-step behavior appears acceptable; otherwise continue rank-style hedges and skip high-corr pair family.

## 2026-05-23 Submission Attempt (Quota Block, Candidate Refresh)

- Pre-loop checks at `2026-05-23 06:43 UTC`:
  - `kaggle competitions submissions` remains capped at **2** for this date (`run36_nonleak_55_25_10_10`, `run37_rank21_595_255_05_10`).
  - Public baseline is still `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged since last loop.
- Research:
  - Highest-signal public kernels still point to high-cardinality handling (`SingleProduct`, `CardButInactive`, `ZeroBalance`) but no new novel method since last cycle.
  - Discussion/Forum endpoint still not parseable in this environment.
- Experiment/refresh:
  - Remote CatBoost fallback run `run40_cat_native_202_regA` finished successfully and was synced to local (`models/run40_cat_native_202_regA_{oof,test}.npy`, `submissions/run40_cat_native_202_regA*.csv`, report). Local CV score was weak for this variant (`0.888953`), so not queued as a public submission target.
  - Candidate set updated after local validity checks:
    - `run40_pair14_33_w067_033_prob.csv`: OOF `0.8982258`, corr vs best `0.99760`.
    - `run40_pair14_33_w060_040_prob.csv`: OOF `0.8981989`, corr vs best `0.99728`.
    - `run40_rank14_33_70_30_r.csv`: OOF `0.898210`, corr vs best `0.85074` (low order-rank correlation candidate).
    - `run40_trip125_075_10_prob.csv`: OOF `0.8983447`, corr vs best `0.99915` (higher local but higher transfer-risk).
- Submission status:
  - No upload possible in this cycle (quota still blocks; same error message as above).
  - Candidate queue retained for next UTC day.

## 2026-05-23 Submission Attempt Blocked (2 candidates)

- Pre-loop checks at 2026-05-23 05:50 UTC / 04:50 BST:
  - `kaggle competitions submissions` shows 2 entries for today (`run35_stack_lr_6f` and `run36`/`run37` from this date).
  - Public baseline remained `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` and `voteCount` unchanged; no new high-score public code since 2026-05-07.
  - Discussion endpoint still not extractable in this environment.
- Experiment direction before submission:
  - I generated constrained stacker candidates directly from local OOF/test sources to avoid run21 heavy leakage, using only current high-performing GPU-family sources:
    - `run38_stack_lr_5f_div_c0p1.csv` (5-model logistic stack on run12/run13/run14/run33/run34, C=0.1).
    - `run38_stack_lr_4f_div_c05.csv` (4-model logistic stack on run12/run13/run14/run33/run34, C=0.05).
  - Both files were locally validated (`id,Exited`, `110,023` rows, no NaNs, values in `[0,1]`) and OOF checks passed before submission:
    - `run38_stack_lr_5f_div_c0p1.csv` local OOF: `0.8984406136`.
    - `run38_stack_lr_4f_div_c05.csv` local OOF: `0.8984238507`.
- Cycle 1 (attempt):
  - File: `submissions/public/run38_stack_lr_5f_div_c0p1.csv`
  - Submission attempt result: **FAILED before scoring**.
  - API response: `403 Client Error ... Permission 'competitions.participate' was denied` (StartSubmissionUpload).
- Cycle 2 (attempt):
  - File: `submissions/public/run38_stack_lr_4f_div_c05.csv`
  - Submission attempt result: **FAILED before scoring**.
  - API response: same `403 Permission 'competitions.participate' was denied`.
- Result:
  - No public score updates due upload gate; best remains `0.89306` on `run33run14_on12_w10_10_v3.csv`.
- Error analysis and rule rewrite:
  - This is not a submission-content validation error (format checks already passed), so the current blocker is API participation permission.
  - Next-step rule: pause further API submissions until participation token/session is restored; once unblocked, first retry should be one conservative stack hedge (`run38_stack_lr_5f_div_c0p1`) followed by one orthogonal fallback.

## 2026-05-22 Two-Submission Cycle

- Pre-loop checks at 2026-05-22 01:10 UTC / 00:10 UTC:
  - `kaggle competitions submissions` initially showed `2` submissions for `2026-05-22` at loop start? check: `0` before submission, hence inferred allowance `5/5`.
  - Public baseline remained `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`, rank `1 / 11`.
  - `research/pages/rules.txt` states general daily limit is `5` entries/day for this competition.
- Public-code and discussion refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by voteCount -v` unchanged from earlier; no new high-score notebook with novel training logic since last loops.
  - `kaggle kernels pull` of recent/top public notebooks confirms no materially new feature or stacking trick beyond standard GBDT/CatBoost/XGBoost blending.
  - Discussion endpoints remain inaccessible / non-parseable in this environment.
- Experiment direction before submission:
  - OOF trend indicates this direction is still overfit-prone (`run13/14/33/run12` family), so I tried a second-level meta learner on single-model OOFs for possible non-linear correction while keeping submissions gated.
  - Candidate validation candidates (CV-stacked logistic on first-level OOFs):
    - `run35_stack_lr_5f` using `[run12, run13, run14, run33, run34]`
    - `run35_stack_lr_6f` using `[run12, run13, run14, run33, run34, run09]`
  - Both candidates passed local CSV format checks (`id,Exited`, 110,023 rows, no NaNs, values in `[0,1]`).
  - Local OOF proxy:
    - `run35_stack_lr_5f`: `0.898422`
    - `run35_stack_lr_6f`: `0.898516` (top local among tested stackers)
- Cycle 1:
  - File: `submissions/public/run35_stack_lr_5f.csv`
  - Submitted: `2026-05-22 01:10:02.383000`.
  - Public score: `0.89270`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
- Cycle 2:
  - File: `submissions/public/run35_stack_lr_6f.csv`
  - Submitted: `2026-05-22 01:10:08.770000`.
  - Public score: `0.89271`.
  - Status: COMPLETE.
  - Result: FAILED (slightly better than cycle1 but still below best).
- Cycle result:
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - Remaining quota after cycle: `3/5` (based on today's limit = 5 and 2 used).
- Error analysis and rule update:
  - Stacked models showed very high correlation with `run33` meta-OOF (`corr≈0.98`), indicating the stacker is mostly reweighting existing ranking rather than learning new ordering.
  - Local OOF gains did not transfer to public (classic local-global drift), so risk gate tightened:
    - Next-stack experiments should include at least one less-correlated base source (`run21`, `run22`, `run32`) by default,
    - and any future stacker should prefer constrained regularized weights or pre-transformed/calibrated features to prevent overfitting signal collapse.
- Planned next direction:
  - Create targeted ranking-space/odds-space stack candidates with diversified feature sets (incl. `run21_all_cat_s202`, `run22_xgb_all_777`, `run32_s4e1_d5c1_s202`) and strong overfit checks before submit.
  - Continue deep check of public kernels for calibration and feature cross-combination updates before next two-submit cycle.

## 2026-05-20 Two-Submission Cycle

- Pre-loop checks at 2026-05-20 00:51 BST / 23:51 UTC:
  - `kaggle competitions submissions` showed no `2026-05-20` entries at loop start; inferred remaining quota `2/2`.
  - Public baseline before loop remained `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`, rank `1 / 11`.
- Public-code and discussion refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged; no new high-score notebooks.
  - Discussion scrape remains unavailable in this environment due anti-forgery/anti-bot checks.
- Experiment direction before submission:
  - After two consecutive 2026-05-19 regressions, we removed direct 40/30/30 raw/strongly monotonic variants from first tier.
  - Cycle plan: conservative 65/35 run14+run33 blend first, then CV-calibrated 40/30/30 variant (run13/calibration) only.
- Candidate validation:
  - `run34_run14_run33_65_35.csv`: `id,Exited`, `110,023` rows, no NaN, predictions in `[0,1]`, IDs aligned.
  - `run34_run14_run33_run13_40_30_30_v1_isotonic_cv.csv`: `id,Exited`, `110,023` rows, no NaN, predictions in `[0,1]`, IDs aligned.
- Cycle 1:
  - File: `submissions/public/run34_run14_run33_65_35.csv`
  - Submitted: `2026-05-20 00:51:11.363000`.
  - Public score: `0.89241`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error/analysis note: Even the conservative 65/35 blend failed to recover the best score.
- Cycle 2:
  - File: `submissions/public/run34_run14_run33_run13_40_30_30_v1_isotonic_cv.csv`
  - Submitted: `2026-05-20 00:51:32.603000`.
  - Public score: `0.89258`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error/analysis note: CV-calibrated monotonic transformation lowered variance but remained publicly overfit-prone in this family.
- Cycle result:
  - Remaining quota after cycle: `0/2`.
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - Next direction:
    - stop additional `run13/run14/run33` linear/blended variants unless backed by new OOF-generation;
    - prioritize orthogonal GPU generation (different model architecture / meta model) before any further weighting shifts around this family.


## 2026-05-21 Two-Submission Cycle

- Pre-loop checks at 2026-05-21 02:38 BST / 01:38 UTC:
  - `kaggle competitions submissions` showed no `2026-05-21` entries; inferred remaining quota `2/2`.
  - Public leaderboard baseline before cycle remained `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Public-code and discussion refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` still unchanged (`wangleboro/churn-prediction-gbdt` latest from 2026-05-07).
  - Discussion endpoints remained non-actionable in this environment (anti-forgery/blocked responses), so no reliable new forum signal.
- Research/experiment direction before submission:
  - Since previous run13/14/33-heavy families remained unstable, I shifted to a rank-diverse 4-model family using the local orthogonal `run34_cat_s2718_d6_lr003` OOF:
    - Sweep over `run34_cat + run13 + run14 + run33` showed top OOF region around:
      - `25% cat + 20% run13 + 30% run14 + 25% run33` (`0.8984434`)
      - `30% cat + 20% run13 + 25% run14 + 25% run33` (`0.8984369`)
  - Local sanity checks confirmed `id`/format integrity and `[0,1]` probability bounds for both candidates.
- Cycle 1:
  - File: `submissions/public/run34_cat13_14_33_25_20_30_25_v1.csv`
  - Submitted: `2026-05-21 02:38:44.630000`.
  - Public score: `0.89276`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error note: this 4-model linear OOF-updated direction still overfit on this leaderboard split.
- Cycle 2:
  - File: `submissions/public/run34_cat13_14_33_30_20_25_25_v1.csv`
  - Submitted: `2026-05-21 02:39:05.790000`.
  - Public score: `0.89276`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error note: near-tie to cycle1, confirming limited public gain from simple weight perturbation in this family.
- Cycle result:
  - Remaining quota after cycle: `0/2`.
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - Next direction:
    - convert this 4-model blend into a second-level meta/stacking route (out-of-fold meta learner) to break the observed overfit mode,
    - prioritize generation of a new non-tree signal on GPU before further linear blend experiments,
    - keep these 4-model candidates as high-level priors for calibration/rank variants.


## 2026-05-19 Two-Submission Cycle

- Pre-loop checks at 2026-05-19 02:32 BST / 01:32 UTC:
  - `kaggle competitions submissions` showed no `2026-05-19` entries; inferred start-of-day remaining quota `2/2`.
  - Public leaderboard baseline before cycle remained `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`, rank `1 / 11`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged from prior checks; no new public notebooks with visible new strategies.
- Public/discussion research:
  - Web-facing discussion pages returned anti-forgery/blocked responses in this environment, so no extractable new forum signal.
  - No new high-score public notebook refresh since the last checkpoint.
- Candidate validation before submit:
  - `run34_mix34_14_33_30_40_30_v1.csv`: format checked (`id,Exited`), 110,023 rows, no NaN, predictions in `[0, 1]`, aligned IDs.
  - `run34_run14_run33_run13_40_30_30_v1.csv`: format checked (`id,Exited`), 110,023 rows, no NaN, predictions in `[0, 1]`, aligned IDs.
- Cycle 1:
  - File: `submissions/public/run34_mix34_14_33_30_40_30_v1.csv`
  - Submitted: `2026-05-19 02:32:57.747000`.
  - Public score: `0.89261`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error/analysis note: score dropped after adding the GPU run14/33-heavy hedge despite the higher OOF proxy, indicating remaining public overfitting in this direction.
- Cycle 2:
  - File: `submissions/public/run34_run14_run33_run13_40_30_30_v1.csv`
  - Submitted: `2026-05-19 02:33:26.097000`.
  - Public score: `0.89257`.
  - Status: COMPLETE.
  - Result: FAILED (regression).
  - Error/analysis note: 3-way `run14/run33/run13` also moved opposite on public and failed to recover the benchmark.
- Cycle result:
  - Remaining quota after cycle: `0/2`.
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - Next direction:
    - continue with lower-correlation hedge routes only (stronger rank-based ensembling/temperature control),
    - test calibrated blends around `run13/run14` while keeping run33 contribution below a new cap,
    - prioritize remote GPU experiments on orthogonal model families before mixing additional run33-heavy weights.


## 2026-05-18 Follow-up: quota block & queued candidates

- Pre-loop checks at 2026-05-18 18:10 BST / 17:10 UTC:
  - Kaggle API `kaggle competitions submissions` shows latest two entries are `run33run14_on12_w30_30_v6*.csv`; remaining quota now `0/2`.
  - Public best remains `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`, rank 1).
- Public/noise refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged (only the same 5 notebooks); no new solution code signal found.
  - Pulled `wangleboro/churn-prediction-gbdt` for comparison; still baseline 3-model GBDT/ensemble, no new high-score stack trick.
- Next candidate experiment (local OOF validation only, no submission yet):
  - `run14 40% + run33_xgb_all 30% + run13 30%` (`run34_run14_run33_run13_40_30_30_v1.csv`)
    - OOF AUC proxy: `0.8983648366` (higher than prior blend family).
    - test mean/std/p99: `0.212875/0.270618/0.966316`.
  - `run14 65% + run33_xgb_all 35%` (`run34_run14_run33_65_35.csv`)
    - OOF AUC proxy: `0.8982237095`, mean/std/p99: `0.213334/0.270863/0.966293`.
  - New remote GPU sweep (`run34_cat_s2718_d6_lr003`) produced model OOF `0.8973838765` and a higher-scoring 3-way hedge:
    - `30% run34_cat_s2718_d6_lr003 + 40% run14 + 30% run33_xgb_all` (`run34_mix34_14_33_30_40_30_v1.csv`)
    - OOF AUC proxy: `0.8983911746`
    - test mean/std/p99: `0.213183/0.270791/0.966272`.
    - currently best local OOF proxy among checked hedge candidates in this pause window.
  - Isotonic calibration on full OOF (`run34_run14_run33_run13_40_30_30_v1_isotonic.csv`) raised internal OOF AUC to `0.8986291654` but is high-variance by design;
    5-fold OOF-calibrated variant (`..._isotonic_cv`) dropped to `0.8979918482`.
- Queue for first resume cycle:
  1) `run34_mix34_14_33_30_40_30_v1.csv`
  2) `run34_run14_run33_run13_40_30_30_v1.csv`
  3) `run34_run14_run33_65_35.csv`
  (calibration variants kept as backups)
- All above files are synced to `C:/Users/Kun/Bank Customer Churn Challenge/submissions/public` and ready for submission once quota resets.

## 2026-05-18 Two-Submission Cycle

- Pre-cycle checks:
  - UTC check time at cycle start: `2026-05-18 04:53 UTC`.
  - Remaining quota at start: `2/2` (`kaggle competitions submissions` had no `2026-05-18` records).
  - Public leaderboard before cycle: `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Public-code and discussion refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged; `wangleboro/churn-prediction-gbdt` still last runs 2026-05-07.
  - No newly readable Kaggle discussion content from available API endpoints.
- Experiment hypothesis:
  - 3-way `run33/run14/run12` OOF peaks still look brittle publicly.
  - Run calibrated hedge candidate instead of another raw 3-way peak:
    - Candidate A: `run33run14_on12_w30_30_v6.csv` (`0.3*run33_xgb_all_s202 + 0.3*run14 + 0.4*run12`).
    - Candidate B: `run33run14_on12_w30_30_v6_platt.csv` (Platt calibration fit on Candidate A OOF to reduce score-space extremity).
- Validation before submit:
  - `id,Exited` format, `110,023` rows, aligned sample IDs, finite predictions in `[0,1]` for both candidates.
  - Candidate A test envelope: mean `0.21323`, std `0.27098`, p99 `0.96659`.
  - Candidate B test envelope: mean `0.21355`, std `0.27324`, p99 `0.94424`.
  - Candidate A local OOF proxy computed from source OOF arrays: `0.898352873`.
  - Candidate B OOF proxy `0.898352873` (monotonic transform preserved OOF).
- Cycle 1:
  - File: `run33run14_on12_w30_30_v6.csv`
  - Submitted: `2026-05-18 04:53:54.827000`.
  - Public score: `0.89262`.
  - Status: FAILED (public regression).
  - Error note: still overfit-sensitive under this 3-way raw probability pattern.
- Cycle 2:
  - File: `run33run14_on12_w30_30_v6_platt.csv`
  - Submitted: `2026-05-18 04:54:46.043000`.
  - Public score: `0.89262`.
  - Status: FAILED (public regression).
- Conclusion:
  - Remaining quota after cycle: `0/2`.
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`, rank `1 / 11`.
  - Next direction:
    - pause raw `run33/run14/run12` perturbations until a remote GPU experiment with a distinct feature axis or stack/meta layer is available;
    - keep Platt/rank calibration in the pre-check list for future hedge candidates.

## 2026-05-17 Two-Submission Cycle

- Pre-cycle checks:
  - UTC check time: `2026-05-17 00:36 UTC`.
  - Remaining quota at cycle start: `2/2`.
  - Public leaderboard top before cycle: `0.89306` (team `Kun Zhang`), rank `1 / 11`.
- Public-code discussion check:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun|scoreDescending` returned no new notebooks/updates since prior checkpoints.
  - Discussion endpoint remains not directly readable in this environment.
- Research direction:
  - Previous OOF sweeps pointed to `run33/run14/run12` optima (`27/38/35` and `28/30/42` blends).
  - Since OOF peaks did not convert publicly in earlier blocked-cycle prep, we proceeded with a strict two-step rule: first try peak, then hedge-close alternative.
- Candidate checks:
  - `run33run14_on12_w27_38_v5.csv`: format/alignment/range checks passed; OOF `0.898360867`.
  - `run33run14_on12_w28_30_v5.csv`: format/alignment/range checks passed; OOF `0.898355608`.

Cycle 1:

- File: `submissions/public/run33run14_on12_w27_38_v5.csv`
- Submitted: `2026-05-17 00:36:21.600000`.
- Public score: `0.89272`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: no best improvement.

Cycle 2:

- File: `submissions/public/run33run14_on12_w28_30_v5.csv`
- Submitted: `2026-05-17 00:43:50.893000`.
- Public score: `0.89269`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: no best improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Next direction:
  - reduce candidate concentration on the `run33/run14` component and prioritize calibration/hedge candidates with conservative distributions.
  - continue watch on public notebooks/discussion and retry remote experiments when GPU server becomes reachable.

## 2026-05-16 Quota Block + Prepared 2-Submission Queue

- Pre-loop checks:
  - Current day submission count: `2/2`; no remaining daily allowance.
  - Submit probe returned API error:
    - `Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC (4.2 hours from now).`
  - ETA to retry: `~4h12m` (UTC midnight reset).
  - Public best still `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Discussion/code checks before queue build:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by scoreDescending` shows only existing public kernels; no fresh high-signal pattern changed strategy.
  - Local notebook refresh confirms similar trajectory: boosting/feature-engineering + blending families already covered.
- Local OOF-driven direction:
  - Scan over `run12 + run14 + run33` convex weights found OOF improvements around:
    - `run33=0.27, run14=0.38, run12=0.35` (`0.89836`)
    - `run33=0.28, run14=0.30, run12=0.42` (`0.89836`)
  - Both candidates kept distribution/risk checks near baseline (`corr_to_best >= 0.9988`, std/p99 not expanded).
- Prepared files (validated):
  - `submissions/public/run33run14_on12_w27_38_v5.csv`
  - `submissions/public/run33run14_on12_w28_30_v5.csv`

Cycle 1 / Cycle 2 (planned, blocked by quota):

- Submit status: blocked by daily allowance; no public upload this cycle.
- Retry plan:
  - submit `run33run14_on12_w27_38_v5.csv` then `run33run14_on12_w28_30_v5.csv` immediately after reset.
- Error analysis outcome:
  - block is quota-side; no file-format/API payload issue detected.

Conclusion:

- Remaining quota at this checkpoint: `0/2`.
- Current best unchanged: `0.89306` (`run33run14_on12_w10_10_v3.csv`).

## 2026-05-14 Two-Submission Cycle

- Pre-cycle quota check:
  - UTC check time: `2026-05-14` (before submission round).
  - Remaining quota at start: `2/2`.
  - Current best before cycle: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`, rank `1 / 11`.
- Research watch before each experiment:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge` had no new notebook updates since previous cycle.
  - Discussion/discourse access remained unavailable in this environment; no new high-confidence guidance from discussions.
  - Candidate direction remained dual-channel diversity path around `run31` family.
- Pre-submit validation (format + sanity for both files):
  - `run31_exp_a_080_010_010_dual30p70.csv`: `id,Exited`, `110,023` rows, no NaN, aligned IDs, values in `[0,1]`.
  - `run31_exp_a_080_010_010_dual50p50.csv`: `id,Exited`, `110,023` rows, no NaN, aligned IDs, values in `[0,1]`.
  - Correlation/risk check: both remain less coupled to strong overfit patterns than run33-heavy baseline and kept local stability checks.

Cycle 1:

- File: `submissions/public/run31_exp_a_080_010_010_dual30p70.csv`
- Submitted: `2026-05-14 02:08:19.357000`.
- Public score: `0.89281`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: no improvement.

Cycle 2:

- File: `submissions/public/run31_exp_a_080_010_010_dual50p50.csv`
- Submitted: `2026-05-14 02:16:12.650000`.
- Public score: `0.89281`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: no improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best remains `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv` (`1 / 11`).
- Planned next hypotheses: `run31_exp_b_097_001_002_dual30p70.csv`, `run31_exp_b_097_001_002_dual50p50.csv`, and `run32_tempT*` calibrations if next reset opens.

## 2026-05-15 Two-Submission Cycle (pre-collected from submission engine)

- Pre-cycle quota check at UTC reset:
  - Remaining quota at cycle start: `2/2` (confirmed by two completed entries now present in Kaggle submission list for 2026-05-15).
- Public-code scan before submission:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge` unchanged from previous cycles.
  - Discussion endpoint in this environment remained unusable for direct harvest.
- Candidate validation prior to submission:
  - `run31_exp_b_097_001_002_dual50p50.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, in-range.
  - `run31_exp_b_097_001_002_dual30p70.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, in-range.

Cycle 1:

- File: `submissions/public/run31_exp_b_097_001_002_dual50p50.csv`
- Submitted: `2026-05-15 02:31:46.697000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: accepted, no best improvement.

Cycle 2:

- File: `submissions/public/run31_exp_b_097_001_002_dual30p70.csv`
- Submitted: `2026-05-15 02:32:10.123000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: accepted, no best improvement.

Conclusion:

- Daily quota after cycle: `0/2`.
- Current best remains `0.89306` from `run33run14_on12_w10_10_v3.csv` (best unchanged).
- Next planned direction: evaluate calibrated `run32_tempT*` blends and any stable `run31_exp_b` perturbation that materially alters correlation structure.

## 2026-05-16 Two-Submission Cycle

- Pre-cycle quota check:
  - Remaining quota at UTC reset: `2/2` (no `2026-05-16` submissions before this cycle).
- Public-code/Discussion scan:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge` remained unchanged versus prior cycles.
  - Discussion endpoint remained inaccessible in this environment for direct harvest.
- Research hypothesis:
  - execute calibrated `run32_tempT*` candidates as the next risk-controlled axis after dual-channel candidates and retain the “run31 exp b” plateau behavior.
- Pre-submit validation:
  - `run32_tempT1_0.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.
  - `run32_tempT1_2.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.

Cycle 1:

- File: `submissions/public/run32_tempT1_0.csv`
- Submitted: `2026-05-16 19:42:00.767000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: no improvement.

Cycle 2:

- File: `submissions/public/run32_tempT1_2.csv`
- Submitted: `2026-05-16 19:42:28.567000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: no improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best remains `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Next planned direction: `run32_tempT0_8.csv` as calibration hedge and any new candidate generated by remote experiment queue; if no new signals, keep to risk-managed blend perturbations around existing anchors.

## 2026-05-14 Quota Blocked + Next 2-Submission Cycle (historical pre-reset)

- UTC check time: `2026-05-13` (late)
- Remaining quota today at that point: `0/2`.
- Planned queue from that state:
  - `run31_exp_a_080_010_010_dual30p70.csv`
  - `run31_exp_a_080_010_010_dual50p50.csv`

## Loop Checklist

- Record score and rank before starting new work.
- Review public notebooks, discussion threads, related S4E1 high-score code, and any newly visible leaderboard patterns.
- Pick one or two concrete hypotheses, not a broad search.
- Run GPU training on the remote server only.
- Sync outputs and reports back to `/Volumes/Z/Bank Customer Churn Challenge`.
- Validate OOF/fold stability/blend behavior and submission CSV format locally.
- Submit only when the candidate beats or usefully diversifies the current best.

## 2026-05-13 Two-Submission Cycle

0.89306 -> 0.89269 -> 0.89262 (no best improvement)

Pre-cycle checks:

- UTC date/time at quota check: `2026-05-13`.
- Remaining quota before cycle: `2/2`.
- Remaining today’s submissions from new cycle:
  - `run33run14_on12_w30_20_50_v4.csv` (2026-05-13 00:32:08.413000) `0.89262`.
  - `run33run14_on12_w28_34_38_v4.csv` (2026-05-13 00:33:43.450000) `0.89269`.
- Candidate verification:
  - `A_main_run33run14_run12.csv` passes format checks and is exact duplicate of `run33run14_on12_w28_34_38_v4.csv`.
  - `D_mix_run33run14_run12.csv` passes format checks and is exact duplicate of `run33run14_on12_w30_20_50_v4.csv`.
  - `B_safe_run33run14_run12.csv`, `C_lean_run33run14_run12.csv`, `E_light_run33run14_run12.csv` pass format checks (not sent due zero remaining quota).

Cycle 1:

- File: `submissions/public/run33run14_on12_w30_20_50_v4.csv` (alias `D_mix_run33run14_run12.csv`)
- Submitted: `2026-05-13 00:32:08.413000`.
- Public score: `0.89262`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: accepted, no improvement.

Cycle 2:

- File: `submissions/public/run33run14_on12_w28_34_38_v4.csv` (alias `A_main_run33run14_run12.csv`)
- Submitted: `2026-05-13 00:33:43.450000`.
- Public score: `0.89269`.
- Status: COMPLETE.
- Rank: `1 / 11`.
- Result: accepted, no improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best stays `0.89306` from `run33run14_on12_w10_10_v3.csv` (`1 / 11`).

## 2026-05-09 Quota Blocked Cycle + Next Step

Pre-submit checks:

- UTC date and time at check: `2026-05-09`.
- Remaining quota today: `0/2`.
- Today's Kaggle submissions:
  - `run33_on12_w01_v2.csv` at `2026-05-09 02:22:40.103000` (public `0.89296`).
  - `run33_on12_w02_v2.csv` at `2026-05-09 02:22:33.593000` (public `0.89299`).
- Public benchmark remains:
  - `run33_on12_w05_v2.csv` at `0.89304` (1 / 11).
- Research update:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` unchanged (still dominated by baseline methods).
  - No direct forum endpoint is yielding a stronger immediate public-code signal in current tooling.

Local candidate scan before reset (no new GPU run in this blocked phase):

- `run33_on12_w10_v3.csv` (10% run33): OOF `0.898027165`; test std/99th-pctl `0.27164 / 0.96761`.
- `run33_on12_w15_v3.csv` (15% run33): OOF `0.898110121`; test std/99th-pctl `0.27143 / 0.96719`.
- `run33_on12_w20_v3.csv` (20% run33): OOF `0.898167081`; test std/99th-pctl `0.27126 / 0.96683`.
- `run33run14_on12_w10_10_v3.csv` (10% run33 + 10% run14): OOF `0.898108728`; test std/99th-pctl `0.27160 / 0.96752`.

Submit plan after UTC reset:

1) `run33_on12_w20_v3.csv` (primary).
2) `run33run14_on12_w10_10_v3.csv` (risk hedge).

Risk rule before each submission:

- `id` / `Exited` format valid, 110,023 rows, no duplicates, no NaN, all predictions in `[0,1]`.
- If first step fails to improve or is unstable, apply error analysis immediately and continue with step 2 in the same loop.

## 2026-05-12 Two-Submission Cycle

Pre-cycle checks:

- UTC date and time at check: `2026-05-12`.
- Remaining quota at start: `2/2` (no local `2026-05-12` entries before submission).
- Leaderboard before submit: `run33_on12_w05_v2` at `0.89304` rank `1 / 11`.
- Public notebook scan via `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` continued to show no new actionable strategy.
- Discussion/discourse endpoint remained inaccessible/low-signal through API tooling; no high-value public merge strategy found.

Experiment and local validation:

- Candidate 1: `run33_on12_w20_v3.csv` (20% run33)
  - Local OOF: `0.898167`
  - Pred stats: std `0.27126`, `p99 0.96683`
- Candidate 2: `run33run14_on12_w10_10_v3.csv` (10% run33 + 10% run14)
  - Local OOF: `0.898109`
  - Pred stats: std `0.27160`, `p99 0.96752`
- Both files passed local checks:
  - `id,Exited` format
  - `110,023` rows
  - monotonic unique IDs matching `sample_submission.csv`
  - finite and in-range `[0,1]` predictions, no NaN

Cycle 1:

- File: `submissions/public/run33_on12_w20_v3.csv`
- Submitted: `2026-05-12 07:58:07.923000`
- Public score: `0.89291`
- Status: COMPLETE
- Result: no improvement vs current best.

Cycle 2:

- File: `submissions/public/run33run14_on12_w10_10_v3.csv`
- Submitted: `2026-05-12 07:58:27.390000`
- Public score: `0.89306`
- Status: COMPLETE
- Result: success; team best became `Kun Zhang — 0.89306`.
- Remaining quota after cycle: `0/2`.

Conclusion:

- This cycle is completed with one successful uplift.
- Next experiment direction: refine 3-way blends around `(run33_xgb_all_s202, run12, run14)` and test conservative calibration/monotonic constraints to keep public-safe transfer without score erosion.

## 2026-04-28 Cycle After run09

Recorded score:

- `run09_prob_blend_2358.csv`: OOF `0.891021`, public `0.88725`, rank `4 / 10`.

Research status:

- Current competition public notebooks remain mostly baseline XGBoost/GBDT-style solutions.
- Related S4E1 high-score public code suggests CatBoost-native high-cardinality categoricals, interaction categories, and text/vector encodings over `Surname`/combined categorical strings.
- Direct original-data injection did not improve standalone CV in `run05`; revisit only with distribution-aware use.

Next plan:

- Primary path: train additional `s4e1_text` CatBoost seeds/folds on the remote GPU and blend with `run02`/`run08`.
- Secondary path: small manual/Optuna sweep around run08 CatBoost parameters: `depth`, `l2_leaf_reg`, `random_strength`, `bagging_temperature`, `ctr_leaf_count_limit`.
- Submit rule: only submit if OOF beats `0.891021` or correlation analysis shows useful diversity with stable fold scores.

## 2026-04-28 Next Experiment: GPU CatBoost CTR Capacity

Research inputs:

- Current competition notebooks still expose only baseline XGBoost/GBDT approaches.
- S4E1 public solution archive and discussion mirrors point to AutoGluon/stacking, many OOFs, and CatBoost/high-cardinality handling as the most useful related ideas.
- S5E8/S6E3 solution archives emphasize many OOFs, ridge/meta blending, and diversity selection; this supports adding more OOF sources before a richer blender.

Experiment:

- First remote GPU attempt failed because CatBoost GPU does not support the current non-default `ctr_leaf_count_limit`.
- Patched GPU mode to remove `ctr_leaf_count_limit` while keeping the rest of the `s4e1_text` CatBoost setup.
- Trained on remote RTX 4080:
  - `run10_s4e1_text_cat_gpu_s202`: OOF `0.897375`.
  - `run11_s4e1_text_cat_gpu_s777`: OOF `0.897412`.
- Local validation:
  - `run12_gpu_cat_seed_blend_10_11`: `0.5*run10 + 0.5*run11`, OOF `0.897786`.
  - `run10/run11` test correlation `0.999466`, so the seed average is stable.
  - Test predictions are more extreme than `run09` and correlate strongly with the known-overfit `run01`, so public score risk is high despite excellent OOF.

Submission decision:

- `run12` beats the current best OOF by `+0.006765`, so it satisfies the local submit rule.
- Remote submission attempt on 2026-04-28 uploaded the file but Kaggle returned `400 Client Error` during `CreateSubmission`; the submission list did not add `run12`.
- Since `run07` and `run09` already used the two allowed submissions on 2026-04-28, treat `run12` as queued for the next available submission slot.

## 2026-04-29 Cycle 1 Submission

Pre-submit checks:

- Remaining daily quota inferred as `2/2` because there were no 2026-04-29 submissions before this cycle.
- Current competition notebook list unchanged from prior research.
- Public leaderboard before submit: `run09` rank `4 / 11`, score `0.88725`.
- CSV/id/range validation passed for `run12`.
- OOF `0.897786`; test correlation vs `run09` `0.985426`; test correlation vs overfit `run01` `0.948965`.

Submission:

- File: `submissions/public/run12_gpu_cat_seed_blend_10_11.csv`.
- Submitted: `2026-04-29 13:38:26.160000`.
- Public score: `0.89293`.
- Rank after submission: `1 / 11`.
- Result: success; proceed to cycle 2.

Cycle 2 plan:

- Since `run12` validated publicly, continue the same family with more remote GPU CatBoost seeds and average them with `run10/run11`.
- Target: train two additional seeds, then submit the best local multi-seed average if OOF and distribution checks pass.

## 2026-04-29 Cycle 2 Submission

Pre-cycle status:

- Remaining daily quota after `run12`: `1/2`.
- Public leaderboard after `run12`: rank `1 / 11`, score `0.89293`.
- Current competition notebook list unchanged; no new public code signal.

Experiment:

- Remote GPU training on RTX 4080:
  - `run13_s4e1_text_cat_gpu_s314`: OOF `0.897482`.
  - `run14_s4e1_text_cat_gpu_s1001`: OOF `0.897616`.
- Local seed-blend search over `run10/run11/run13/run14`:
  - Equal 4-seed average OOF `0.898061`.
  - Best coarse weighted blend `run15`: `0.20*run10 + 0.20*run11 + 0.25*run13 + 0.35*run14`, OOF `0.898070`.
  - Validation: CSV/id/range passed, test std `0.271797`, p99 `0.968020`, corr vs `run12` `0.999896`, corr vs overfit `run01` `0.949224`.

Submission:

- File: `submissions/public/run15_gpu_cat_4seed_weighted.csv`.
- Submitted: `2026-04-29 14:02:34.337000`.
- Public score: `0.89291`.
- Result: successful submission, but slightly below `run12` by `-0.00002`.
- Current selected best remains `run12_gpu_cat_seed_blend_10_11.csv`, public `0.89293`, rank `1 / 11`.

Next notes:

- Additional same-family seed averaging improved OOF but did not improve public score over the 2-seed average.
- Next loop should not blindly add more same-family seeds; investigate public-aware weighting, rank/probability transforms, or a small holdout/blend selection strategy around `run12` before spending another submission.

## 2026-04-30 Two-Submission Cycle

Pre-cycle checks:

- UTC time at start: `2026-04-30 01:42:17`.
- No 2026-04-30 submissions existed at the start, so remaining quota was treated as `2/2`.
- Public leaderboard before submit: rank `1 / 11`, best public `0.89293`.
- Public notebook update check found `wangleboro/churn-prediction-gbdt` rerun at `2026-04-30 00:15:49.953000`, but the notebook MD5 matched the previous pulled version. No new useful public-code signal.

Cycle 1:

- Candidate selected after research update: `run16_run12_70_seed1314_30`.
- Rationale: stay anchored to public-best `run12`, add 30% of `avg(run13,run14)` because this improved OOF while slightly reducing prediction extremity.
- OOF `0.897998`; validation passed: row/id/range/NaN checks OK, test std `0.271974`, p99 `0.968122`, corr vs `run12` `0.999974`.
- Submitted: `2026-04-30 01:51:29.800000`.
- Public score: `0.89293`.
- Result: successful submission, tied current best.

Cycle 2:

- Candidate selected: `run17_rank_run12_50_rank1314_50`.
- Rationale: probability-space local blend tied public; rank-space blend tests whether a different ordering can break the plateau.
- OOF `0.898053`; validation passed: row/id/range/NaN checks OK. Rank predictions had mean `0.500000`, std `0.288641`, p99 `0.989941`.
- Submitted: `2026-04-30 01:54:01.277000`.
- Public score: `0.89291`.
- Result: successful submission but below best by `-0.00002`.

Conclusion:

- `run12`/`run16` remain the public-best family at `0.89293`.
- `run15` and `run17` both had higher OOF than `run12` but public `0.89291`, showing the public plateau is sensitive and OOF-only optimization is now unreliable.
- Next cycle should avoid more same-family OOF chasing. Prefer a changed real axis: regularization/CTR constraints/fold design, or private-risk hedge only if explicitly desired.

## 2026-05-01 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-01 00:07:48`.
- Kaggle submissions list showed no 2026-05-01 submissions before this cycle, so remaining quota was `2/2`.
- Public notebook list via Kaggle CLI still showed the same five public notebooks. `wangleboro/churn-prediction-gbdt` had a newer `lastRunTime` of `2026-04-30 16:57:26.153000`, but pulling the notebook failed twice due Kaggle DNS resolution errors.
- Kaggle leaderboard query also failed with DNS resolution errors, so rank was not refreshed. The submissions list still showed the current best public score as `0.89293`.

Cycle 1:

- Candidate selected: `run18_run12_99_run02_01`.
- Rationale: stay almost entirely anchored to public-best `run12`, while injecting 1% of the more conservative `run02` robust blend as a small private-risk hedge.
- OOF `0.897777`; validation passed: row/id/range/NaN checks OK, test mean `0.212154`, std `0.272053`, p99 `0.968016`, corr vs `run12` `0.999998`, corr vs `run09` `0.985718`, corr vs overfit `run01` `0.948894`.
- Submitted: `2026-05-01 00:11:27.720000`.
- Public score: `0.89293`.
- Result: successful submission, tied current public best.

Cycle 2:

- Candidate selected: `run19_rank_run12_90_run09_10`.
- Rationale: test whether a run12-anchored rank blend with the strongest pre-GPU public model can improve borderline ordering without relying on the weaker same-family seed averages.
- OOF `0.897605`; validation passed: row/id/range/NaN checks OK, rank predictions had mean `0.500000`, std `0.288200`, p99 `0.989630`.
- Submitted: `2026-05-01 00:12:05.580000`.
- Public score: `0.89280`.
- Result: successful submission but below best by `-0.00013`.

Conclusion:

- `run18` confirms the public plateau tolerates a tiny robust-model hedge, but it did not improve beyond `run12`/`run16`.
- `run19` shows rank-space blending with the weaker pre-GPU model hurts public ordering; avoid further rank blends with `run09` unless there is a new validation reason.
- Current selected best remains the `0.89293` tie family: `run12`, `run16`, and `run18`.
- Next cycle should spend effort on a genuinely new modeling axis before using quota: remote GPU regularization/CTR/fold design, or a more principled holdout/meta-blend selection strategy.

## 2026-05-01 One-Submission Request: Quota Blocked and run20 Prep

Pre-cycle checks:

- UTC time at quota check: `2026-05-01 02:16:56`.
- Today's two allowed submissions were already used:
  - `run18_run12_99_run02_01.csv`, submitted `2026-05-01 00:11:27.720000`, public `0.89293`.
  - `run19_rank_run12_90_run09_10.csv`, submitted `2026-05-01 00:12:05.580000`, public `0.89280`.
- Remaining same-day quota: `0/2`; no legal submission attempt should be made before the next UTC reset.
- Leaderboard refreshed successfully: current team rank `1 / 11`, selected best public score `0.89293`.

Public research update:

- Kaggle CLI still lists the same five public notebooks.
- `wangleboro/churn-prediction-gbdt` was pulled to `research/current_notebooks/wangleboro_20260501`; it remains a sklearn `GradientBoostingClassifier` baseline with three simple cross-features and no CatBoost/OOF/blending signal.
- Discussion/web search did not reveal a new current-competition high-score path.

Preparation:

- Patched `src/train.py` to expose CatBoost parameter overrides while keeping default behavior unchanged.
- Next candidate queued for remote GPU training: `run20_s4e1_text_cat_gpu_reg_d5_ctr1_2seed`.
- Hypothesis: reduce high-cardinality CTR/tree capacity and increase regularization relative to `run10/run11`.
- Planned two seed commands use seeds `202` and `777`, `feature_mode=s4e1_text`, GPU CatBoost, `depth=5`, `l2_leaf_reg=12`, `random_strength=0.8`, `bagging_temperature=1.0`, `max_ctr_complexity=1`, `one_hot_max_size=3`.

Blocked state:

- Remote SSH to `100.66.71.25:12345` returned `Host is down`; ping and TCP checks failed.
- Because all GPU experiments must run on the remote server, training is queued until the server is reachable.

Submit gate after remote training:

- Build a two-seed average, then search probability-space blends with `run12` at new-model weights `0.02, 0.05, 0.10, 0.15, 0.20, 0.30`.
- Strong submit if blend OOF is at least `0.89784` and test distribution is no more extreme than `run12`.
- Risk-hedge submit if blend OOF is at least `0.89775`, test std/p99 stay at or below the `run12` envelope, and correlation to overfit `run01` drops below the `run12` reference.
- Do not submit rank blends or additional same-family seed averages without a new validation reason.

## 2026-05-05 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-05 01:19:39`.
- Kaggle submissions list showed one entry from this day (`run21_all_cat_s202.csv`), so today remaining quota was `1/2`.
- Public notebook scan (`kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge`) showed latest `lastRunTime` for `wangleboro/churn-prediction-gbdt` as `2026-05-04 14:36:04`; no new public scoring direction was visible.
- No direct discussion API endpoint returned high-value new code this cycle; continue within the existing Cat/XGB feature axis with remote GPU enforcement.

Cycle 1:

- Candidate selected: `submissions/public/run21_all_cat_s202.csv` (remote `run21_*` bundle synced to local).
- Reasoning: `run21` had very high local OOF (`0.939132` on first `110023` evaluation rows from earlier remote report), worth testing whether this overfit-like family could transfer to public LB.
- Validation passed for submission format and ranges (`id,Exited`, `110,023` rows, finite values, IDs unique/matching test IDs).
- Submitted: `2026-05-05 00:51:56.753000`.
- Public score: `0.88584`.
- Result: successful but below best; `run21` behaves as high-risk OOF-only signal and is not kept as new best.

Cycle 2:

- Candidate selected: `run22_xgb_all_777` from remote GPU XGBoost training.
- Remote artifact review:
  - `models/run22_xgb_all_777_oof.npy`, `models/run22_xgb_all_777_test.npy` synced.
  - Reported local OOF `0.89406` (5 folds), fold scores around `0.8935–0.8951`.
  - Submission candidates: `run22_xgb_all_777.csv` and `run22_xgb_all_777_xgb.csv` are identical; we kept `run22_xgb_all_777.csv`.
- Validation:
  - Row/id alignment, NaN/range checks, monotonic id checks passed.
  - OOF(mean/std/p99): `0.20798 / 0.25986 / 0.94546` (eval split).
  - Test(mean/std/p99): `0.21213 / 0.26343 / 0.94627`, min/max in `(0,1)`.
  - Corr vs `run12` in OOF: `0.9848`; corr vs `run01`: `0.8056` (less aligned to known overfit mode than many prior seed variants).
- Submitted: `2026-05-05 01:20:15.737000`.
- Public score: `0.88899`.
- Result: successful but below best (`0.89293`).

Conclusion:

- Current best remains `0.89293` from `run12`/`run16`/`run18`.
- Same-day quota after cycle: `0/2`; no further legal submissions before next UTC reset.
- Error-analysis direction: the `run22` family reduced overfit correlation vs `run01` but still regressed public; next should increase diversity with a different non-duplicate modeling axis (e.g., calibration/reliability treatment, outlier-robust blending, or post-fit isotonic/Platt calibration + constrained blending with `run12`), rather than more single-family XGBoost variants.

## 2026-05-04 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-04 19:35:00` (submission engine local wall time).
- The latest file in the public submission history was still `run19_rank_run12_90_run09_10` on 2026-05-01, so remaining same-day quota was treated as `2/2` and valid for submission.
- Public research/debate status remained low-signal:
  - `wangleboro/churn-prediction-gbdt` updates were visible but no new architecture was extracted.
  - No high-impact changes from Kaggle discussion scraping in accessible pages.
- Direction: continue the `s4e1_text` GPU CatBoost axis with lower CTR complexity + heavier regularization, then hedge against `run12` in probability space.

Experiment:

- Remote GPU trainings completed:
  - `run20_regA_s777`: OOF `0.896908562`.
  - `run20_regB_s777`: OOF `0.896906052`.
- Candidate predictions produced:
  - `run20_regA_2seed` = 0.5*(regA s202+s777), OOF `0.897215`.
  - `run20_regB_2seed` = 0.5*(regB s202+s777), OOF `0.897158`.
  - `run20_regA_w10_on12` = 0.90*run12 + 0.10*`run20_regA_2seed`, OOF `0.897796`.
  - `run20_regA_w05_on12` = 0.95*run12 + 0.05*`run20_regA_2seed`, OOF `0.897793`.
- Distribution and validation checks passed:
  - CSV format valid (`id,Exited`, 110,023 rows, monotonic and unique ids, finite in-range values).
  - Correlation to `run12` remained very high (`~0.99999`), and correlation to `run01` stayed low relative to risk threshold (`~0.9335`).

Cycle 1:

- Candidate: `submissions/public/run20_regA_w10_on12.csv`.
- Submitted: `2026-05-04 19:37:35.273000`.
- Public score: `0.89291`.
- Rank: `1 / 11` (unchanged, best remains `0.89293`).

Cycle 2:

- Candidate: `submissions/public/run20_regA_w05_on12.csv`.
- Submitted: `2026-05-04 19:38:19.733000`.
- Public score: `0.89292`.
- Rank: `1 / 11` (unchanged, best remains `0.89293`).

Conclusion:

- Both submissions had only marginal local OOF uplift over `run12` blends and did not improve public score.
- Selected best remains `0.89293` from `run12`, `run16`, and `run18`.
- Next axis should move away from near-duplicate GPU CatBoost seed perturbations (e.g., distinct feature family or calibrated stacking/holdout-meta blending), with strict fold/diversity checks before next submission block.

## 2026-05-06 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-06 02:18:58`.
- Today's submissions before cycle: `0`.
- Public leaderboard before submit: rank `1 / 10` with team best score `0.89293`.
- Public notebook scan (`kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun`) unchanged from previous cycle; latest run remains `wangleboro/churn-prediction-gbdt` at `2026-05-06 01:54:58`.
- No new discussion/API signals that indicate a higher-scoring public strategy beyond blending/regression control.
- Hypothesis from failure pattern: the run12-family overfits in probability extremity; test tiny cross-model hedges with lower-reg CatBoost regularized family (`run20`) and XGBoost (`run22`) using OOF-guided blend search.

Cycle 1:

- Candidate: `submissions/public/run23_blend_10_10_80.csv`.
- Form: `0.80*run12 + 0.10*run20_regA_2seed + 0.10*run22_xgb`.
- OOF (local): `0.897833`.
- Validation: file format/id alignment/NaN/range checks passed; test p99 `0.96549`, std `0.27074`; correlation to `run12` OOF `0.99981`.
- Submitted: `2026-05-06 02:18:58.637000`.
- Public score: `0.89290` (below best `0.89293`).
- Result: failure path; kept score for analysis, moved to safer perturbation search.

Cycle 2:

- Re-scan outcome: no new public notebooks or notable discussion evidence from this day.
- Candidate search: OOF-weight grid/random search over `run12`, `run20_regA_2seed`, `run20_regB_2seed`, `run22_xgb` found best local point at approximately
  - `0.85*run12 + 0.06*run20_regA_2seed + 0.09*run22_xgb`.
- Candidate: `submissions/public/run28_best_mix_085_06_09.csv`.
- OOF (local): `0.897834`, correlation to `run12` `0.99987`, test mean/std `0.21212 / 0.27096`, p99 `0.96581`.
- Submitted: `2026-05-06 02:25:22.730000`.
- Public score: `0.89291` (below best `0.89293`).
- Result: failure; required-score target not reached.

Post-cycle note:

- `run28` did not improve public score but remained close; this supports the current evidence that this public leaderboard has a tight overfit-sensitive plateau around `0.8929`.
- Next required direction: move to a materially different modeling axis (fresh GPU CatBoost target/CTR budget + external-validation-aware folds / stack of diverse non-Cat features), rather than further same-family blend perturbations.

## 2026-05-07 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-07 01:33:00` (estimated from local polling).
- Today's submissions before cycle: `0` (`run28` was on 2026-05-06), so remaining same-day quota treated as `2/2`.
- Leaderboard snapshot before submit: top score still `0.89293` (`run18` / `run16` / `run12` set).
- Public notebook scan remained unchanged:
  - Latest Kaggle notebook activity still `wangleboro/churn-prediction-gbdt` at `2026-05-06 23:57:48` (byte-identical local copy).
  - Discussion endpoint access remained unreliable (anti-forgery errors), so no extra high-signal strategy was extracted.
- Hypothesis after last-cycle failure: the aggressive probability-space `run21` mix improved OOF but regressed public; pivot to lower-identifiability blend and/or rank-space blending to reduce overfit sensitivity.

Experiment:

- Loaded OOF/test arrays from:
  - `run12_gpu_cat_seed_blend_10_11`
  - `run21_all_cat_s202`
  - `run22_xgb_all_777`
  - `run20_regA_2seed` (`run20_regA_s202` + `run20_regA_s777`)
- Candidate 1: `0.77*run12 + 0.10*run21 + 0.10*run22 + 0.03*run20_regA`
  - Local OOF AUC: `0.907188` (higher than prior blends)
  - Validation passed:
    - `id,Exited` format
    - `110,023` rows
    - all values finite in `[0,1]`
    - test std `0.271293`, p99 `0.966435`
- Candidate 2: rank-space blend `0.85*rank(run12) + 0.10*rank(run21) + 0.05*rank(run22)`
  - Local OOF AUC: `0.904908`
  - Validation passed:
    - `id,Exited` format
    - `110,023` rows
    - all values in `[~0,1]` (normalized rank scale)
    - test std `0.287914`, p99 `0.989429`

Cycle 1:

- Candidate file: `submissions/public/exp_d_077_010_010_003_prob.csv`.
- Submitted: `2026-05-07 00:33:21.613000`.
- Public score: `0.89280` (failure: below best `0.89293`).
- Result/analysis:
  - Despite high OOF, public dropped; confirms overfit risk from large raw-probability `run21` and mixed `run22` perturbation.
  - Rule triggered: move away from the same `run12 + raw OOF blend` path for next step.

Cycle 2:

- Candidate file: `submissions/public/rank_mix_85_10_05_rank.csv`.
- Submitted: `2026-05-07 00:33:57.013000`.
- Public score: `0.89280` (failure).
- Result/analysis:
-   No public improvement from rank-space hedge either.
- Next required direction:
  - keep `run12` as base but explore genuinely different model families/feature families on remote GPU.
  - avoid further large `run21` raw-probability coupling unless fold-level stability and public-safe validation can be demonstrated first.

Conclusion:

- Both submissions in this cycle failed to improve public score (`0.89280`, `0.89280`).
- Best remains `0.89293` from `run12` / `run16` / `run18`.
- Next cycle should prioritize distinct non-duplicate signal (e.g., fresh GPU model with different feature construction or calibrated blending constraints) before submitting.

## 2026-05-08 Two-Submission Cycle

Pre-cycle checks:

- UTC time at quota check: `2026-05-08 10:27:00`.
- Kaggle submissions list before cycle contained `run31_mix_run21_050.csv` as latest from 2026-05-07, so remaining quota was treated as `2/2`.
- Leaderboard refresh was available:
  - Current team score: `0.89293` (`run18` / `run16` / `run12` set).
- Public notebook scan (`kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun`) remained unchanged in useful signal.
- No high-impact discussion signal appeared in available endpoints.
- Research direction selected after analysis: evaluate a fresh GPU CatBoost variant on same feature path with tighter CTR settings (`run32`) and a fresh GPU XGBoost run (`run33`) as low-risk diversifiers, then blend small weight into `run12`.

Cycle 1:

- Candidate selected: `submissions/public/run32_on12_w05_v2.csv`.
- Candidate construction: `0.95*run12 + 0.05*run32_2seed`, where `run32_2seed` is average of seeds `202` and `777`.
- Pre-submit diagnostics:
  - `run32_s202` OOF `0.896725`, `run32_s777` OOF `0.896957`, mean two-seed OOF `0.897213`.
  - Candidate OOF: `0.897792`.
  - Validation: `id,Exited` format, `110,023` rows, finite `[0,1]` values.
  - Pred statistics: test mean `0.21213`, std `0.27207`, p99 `0.96824`.
  - Correlation checks:
    - vs `run12`: high but acceptable `0.99999`
    - vs overfit proxy `run01`: slightly lower than risk floor from earlier same-family seeds.
- Submitted: `2026-05-08 10:50:20.580000`.
- Public score: `0.89292`.
- Result: failed to improve best; no score break.

Cycle 2:

- Candidate selected: `submissions/public/run33_on12_w05_v2.csv`.
- Candidate construction: `0.95*run12 + 0.05*run33_xgb_all_s202`.
- Pre-submit diagnostics:
  - `run33_xgb_all_s202` OOF `0.895616`.
  - Candidate OOF: `0.897919`.
  - Validation: `id,Exited` format, `110,023` rows, monotonic/unique ids, finite predictions.
  - Pred statistics: mean `0.21235`, std `0.27190`, p99 `0.96800`.
  - Correlation checks:
    - vs `run12`: `0.99981` (small, stable perturbation).
    - vs `run01`: reduced alignment versus `run12` and `run32` regime, indicating lower overfit coupling.
- Submitted: `2026-05-08 10:54:24.343000`.
- Public score: `0.89304`.
- Result: successful + new public best; leaderboard returned `Kun Zhang` at rank `1`.

Conclusion:

- New global best became `0.89304` on `run33_on12_w05_v2.csv` and becomes the current anchor.
- Rule for next cycle: prioritize controlled public-safe candidates that remain close to `run33` and avoid larger probability perturbations unless fold-level public-risk diagnostics improve.
