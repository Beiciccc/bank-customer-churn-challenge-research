# Submission Iteration Log

This file is the required checkpoint after each Kaggle submission. Each cycle records the score first, then the research and experiment plan for the next attempt.

## Current Best

- Submission: `submissions/public/run33run14_on12_w10_10_v3.csv`
- Latest submission: `2026-05-12 07:58:27.390000`
- OOF/CV (local blend): `0.898109`
- Public score: `0.89306`
- Rank after submission: `1 / 11` as refreshed on `2026-05-17 UTC`.
- Delta vs previous best: `+0.00002`

## 2026-05-25 Two-Submission Cycle

- Pre-loop checks at `2026-05-25 06:58 UTC`:
  - `kaggle competitions submissions -c binary-battle-ml-bank-customer-churn-challenge --csv` now showed one entry for 2026-05-25 before this cycle started, so quota at start was `4/5` remaining.
  - `kaggle kernels list --competition ... --sort-by dateRun -v` still shows `wangleboro/churn-prediction-gbdt` as latest notebook (`2026-05-23 20:37:50.307000`).
  - Discussion endpoints are still inaccessible in this environment; no fresh forum signal.
  - Candidate queue pre-validated:
    - `run40_pair14_33_w067_033_prob.csv`
    - `run42_trip_25_30_45.csv`
    - both passed format (`id,Exited`), `110,023` rows, `[0,1]`, and test-id alignment checks.

Cycle 1:

- File: `submissions/public/run40_pair14_33_w067_033_prob.csv`
- Submitted: `2026-05-25 06:58:37.757000`.
- Public score: `0.89248`.
- Status: COMPLETE.
- Result: FAILED (regressed by `-0.00058` from best).
- Rule update: first hedge did not improve; move to fallback trip blend immediately.

Cycle 2:

- File: `submissions/public/run42_trip_25_30_45.csv`
- Submitted: `2026-05-25 07:02:59.587000`.
- Public score: `0.89279`.
- Status: COMPLETE.
- Result: FAILED (regressed by `-0.00027` from best).
- Error analysis: this keeps the same drift direction as other high-corr probability blends despite stronger OOF proxy.

Cycle result:

- Current best remains unchanged:
  - `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Next step:
  - Keep next probes on rank-space or feature-diverse candidates with lower correlation to run33/run12/14 family.
  - Prefer remote GPU re-training that adds surname-derived or interaction features with conservative calibration.

## 2026-05-24 Two-Submission Cycle

- Pre-loop checks at `2026-05-24 03:19 UTC`:
  - `kaggle competitions submissions -c binary-battle-ml-bank-customer-churn-challenge --csv` showed `0` entries for `2026-05-24`, so quota start-of-cycle was `5/5`.
  - `kaggle kernels list --competition ... --sort-by dateRun -v` showed latest run:
    - `wangleboro/churn-prediction-gbdt` updated at `2026-05-23 20:37:50.307000` (top activity).
  - Discussion/forum channels remained inaccessible in this environment; no extra thread-level signal was usable.
  - Candidate queue confirmed and validated:
    - `run40_rank14_33_70_30_r.csv`
    - `run42_prob_25_35_40.csv`
    - both with correct schema (`id,Exited`), `110,023` rows, finite values in `[0,1]`, and ID alignment.

Cycle 1:

- File: `submissions/public/run40_rank14_33_70_30_r.csv`
- Submitted: `2026-05-24 03:20:26.063000`.
- Public score: `0.89304`.
- Status: COMPLETE.
- Result: FAILED (slightly worse than best by `-0.00002`).
- Rule update: first hedge did not improve and exposed mild public drift; move to planned second hedge immediately.

Cycle 2:

- File: `submissions/public/run42_prob_25_35_40.csv`
- Submitted: `2026-05-24 03:21:01.500000`.
- Public score: `0.89278`.
- Status: COMPLETE.
- Result: FAILED (further regression).

Cycle result:

- Remaining quota at the end of day: `3/5` (today entries total `2`).
- Current best remains unchanged:
  - `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Next step:
  - Revisit feature-space updates from `wangleboro/churn-prediction-gbdt` (`CardButInactive`, `ZeroBalance`, `SingleProduct`, surname-derived flags/length/frequency).
  - Prioritize a new low-overfit candidate path with these features before additional probability/rank blends.

## 2026-05-23 Submission Attempt Blocked (Quota 0/2, Wait + Re-scan + Queue Hold)

- Pre-loop checks at `2026-05-23 07:47 UTC`:
  - `kaggle competitions submissions -c binary-battle-ml-bank-customer-churn-challenge --csv` shows exactly 2 entries today, so remaining allowance is `0/2`.
  - Latest submissions today: `run36_nonleak_55_25_10_10`, `run37_rank21_595_255_05_10` (both COMPLETE).
- Public code and discussion refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun -v` still returns top notebook `wangleboro/churn-prediction-gbdt`, last run `2026-05-07 20:38:58`.
  - `kaggle kernels list --competition ... --sort-by scoreDescending -v` still unchanged top vote ranks.
  - Forum/discussion endpoints still return anti-forgery/read failure in this environment; no actionable new thread signal.
- Candidate experiment direction before reset:
  - Queue remains unchanged:
    - `run40_rank14_33_70_30_r.csv` (low-rank-corr hedge, OOF `0.8982097`, corr vs `run33` `0.84552`).
    - `run42_prob_25_35_40.csv` (higher OOF `0.8983578`, higher corr vs `run33` `0.99087`).
  - Validation still green for both files:
    - `id,Exited` schema exact,
    - `110,023` rows and test-id exact alignment,
    - finite values in `[0,1]`, no NaN/inf.
- Submission status:
  - No submission action is legal today due quota block (`Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`).
- Error analysis + next step:
  - Blocking is quota-level only; not model/data related.
  - ETA to UTC reset: `1031.67` minutes (`~17h11m`) from the current check.
  - Next automatic cycle: retry in this exact order after reset, then log public score before deciding the third file (`run42_trip_25_30_45.csv`) if any risk rollback is needed.

## 2026-05-23 Submission Attempt Blocked (Quota 0/2, Research Re-scan + Queue Locked)

- Pre-loop checks at `2026-05-23 07:42 UTC`:
- `kaggle competitions submissions -c binary-battle-ml-bank-customer-churn-challenge --csv` still shows exactly `2` entries for today (`run36_nonleak_55_25_10_10`, `run37_rank21_595_255_05_10`), so remaining daily allowance is `0/2`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun -v` still returns only:
    - `wangleboro/churn-prediction-gbdt` as latest public notebook (`2026-05-07`),
    - no materially new high-score kernel content.
  - Discussion/Forum endpoints are still blocked in this environment (anti-forgery / parse failures), so no extra reliable thread signal can be pulled.
  - `kaggle competitions pages -c binary-battle-ml-bank-customer-churn-challenge` still lists only known rule/evaluation pages, no new operational constraints visible.
- Experiment direction before submit:
  - Keep the existing low-variance queue to preserve generalization while probing for a better public update:
    - Primary: `run40_rank14_33_70_30_r.csv` (low-rank-correlation hedge, OOF `0.8982097`, corr vs `run33` `0.84552`).
    - Secondary: `run42_prob_25_35_40.csv` (OOF `0.8983578`, corr vs `run33` `0.99087`).
  - This queue remains the best validated pair after local OOF/correlation checks on both current and prior iterations.
- Local verification done before submission:
  - `id,Exited` format and test-id alignment checked.
  - Row count checked (`110,023`).
  - `0 <= Exited <= 1`, no NaN/inf values.
  - `run40_rank14_33_70_30_r` and `run42_prob_25_35_40` file integrity verified in both `submissions/` and `submissions/public/`.
- Submission status:
  - Direct submit attempt was made on `run40_rank14_33_70_30_r.csv`; API response:
    - `400 Client Error: Bad Request for url: https://api.kaggle.com/v1/competitions.CompetitionApiService/CreateSubmission`.
  - No new entry appeared in `kaggle competitions submissions`, confirming blocked by day-limit.
  - Historical block text remains: `Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`.
- Error analysis / next action:
  - Gate is not data/model-related.
  - Next step is immediate auto-retry once UTC reset is reached (`~17.28h` estimated from `2026-05-23 06:42 UTC`), in queue order above.

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

## 2026-05-23 Submission Attempt (Quota Block, GPU re-check + Candidate Prep)

- Pre-loop check at `2026-05-23 06:43 UTC`:
  - `kaggle competitions submissions` still shows exactly **2** entries for today (`run36_nonleak_55_25_10_10`, `run37_rank21_595_255_05_10`); submission path remains blocked by daily quota.
  - Public baseline remains `0.89306` from `submissions/public/run33run14_on12_w10_10_v3.csv`.
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` still only exposes `wangleboro/churn-prediction-gbdt` as latest public notebook (2026-05-07), no new notebook-level ideas beyond previously captured.
- Research and discussion:
  - Remote Kaggle kernel pull still shows the same useful public pattern from `wangleboro/churn-prediction-gbdt` (e.g., `SingleProduct`, `CardButInactive`, `ZeroBalance`, `Balance_Per_Product`) with no new signal over last cycle.
  - Public discussion feed/API endpoint remains non-reliable from this environment; no extractable new forum thread details.
- Experiments run while blocked:
  - Ran remote training for `run40_cat_native_202_regA` with CatBoost cat_native mode and 5-fold CV. (Due remote command mismatch, this specific run was CPU-mode and produced weak OOF; file generated and validated but not queued for submission).
  - Synchronised new artifacts from remote to local (`models/run40_cat_native_202_regA_{oof,test}.npy`, `submissions/run40_cat_native_202_regA*.csv`, `reports/run40_cat_native_202_regA_report.json`).
- Candidate preparation for post-reset (all format-valid and alignment-checked):
  - `run40_pair14_33_w067_033_prob.csv` (`0.667*run14 + 0.333*run33`): local OOF `0.8982258`, corr vs best 0.99760.
  - `run40_pair14_33_w060_040_prob.csv` (`0.600*run14 + 0.400*run33`): local OOF `0.8981989`, corr vs best 0.99728.
  - `run40_rank14_33_70_30_r.csv` (`rank` blend 70/30): local OOF `0.898210`, corr vs best 0.85074.
  - `run40_trip125_075_10_prob.csv` (`0.45*run12 + 0.30*run34 + 0.25*run33`): local OOF `0.8983447`, corr vs best 0.99915 (higher local gain, higher risk).
- Submission result for this cycle:
  - No submissions sent; queue prepared only.
  - Block reason unchanged: `Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC`.
- Rule rewrite for next cycle:
  - Keep first attempt on lower-risk rank-family candidate to reduce drift (`run40_rank14_33_70_30_r.csv`) and use one probability-family candidate second only if first does not materially worsen global behavior.

## 2026-05-23 Submission Attempt Blocked (2 candidates)

- Pre-loop checks:
  - UTC time at cycle start: `2026-05-23 05:50 UTC`.
  - Existing entries for this date: 2 (`run36` / `run37` / `run35` already complete), baseline remained `0.89306`.
  - `wangleboro/churn-prediction-gbdt` remains latest public kernel (2026-05-07); discussion scrape still unavailable in this environment.
- Candidate generation:
  - `run38_stack_lr_5f_div_c0p1.csv` (5-model stack, C=0.1).
  - `run38_stack_lr_4f_div_c05.csv` (4-feature stack, C=0.05).
  - Local checks passed for all candidates (`id,Exited`, row/ID alignment, no NaN, values in `[0,1]`).
  - Local OOF/CV proxies:
    - `run38_stack_lr_5f_div_c0p1` = `0.8984406136`
    - `run38_stack_lr_4f_div_c05` = `0.8984238507`
- Submission attempt 1:
  - File: `run38_stack_lr_5f_div_c0p1.csv`
  - Result: **BLOCKED** (no public score).
  - Error: `Permission 'competitions.participate' was denied` (HTTP 403 on `StartSubmissionUpload`).
- Submission attempt 2:
  - File: `run38_stack_lr_4f_div_c05.csv`
  - Result: **BLOCKED** (no public score).
  - Error: same `Permission 'competitions.participate' was denied`.
- Conclusion:
  - Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - This cycle ends on API block rather than score update; next move is unblock participation token/session before continuing two-submission loop.

## 2026-05-18 Two-Submission Cycle

- Pre-loop checks:
  - UTC time at cycle start: `2026-05-18 04:53 UTC`.
  - Remaining quota at start: `2/2`.
  - Public leaderboard before cycle: `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Research refresh:
  - `kaggle kernels list ... --sort-by dateRun` unchanged since 2026-05-07.
  - No fresh Kaggle discussion text was extractable in current environment.
- Candidate prep:
  - `run33run14_on12_w30_30_v6.csv` generated from OOF/test blends:
    - composition: `0.3 run33_xgb_all_s202 + 0.3 run14 + 0.4 run12`
    - local OOF proxy: `0.898352873`
    - test mean/std/p99: `0.21323/0.27098/0.96659`.
  - `run33run14_on12_w30_30_v6_platt.csv` produced by Platt fit on candidate OOF:
    - OOF AUC unchanged.
    - test mean/std/p99: `0.21355/0.27324/0.94424`.
- Gate checks (both):
  - `id,Exited` format.
  - `110,023` rows.
  - IDs aligned to sample submission.
  - finite predictions in `[0,1]`.
- Cycle 1:
  - File: `run33run14_on12_w30_30_v6.csv`
  - Submitted: `2026-05-18 04:53:54.827000`.
  - Public score: `0.89262` (regressed).
- Cycle 2:
  - File: `run33run14_on12_w30_30_v6_platt.csv`
  - Submitted: `2026-05-18 04:54:46.043000`.
  - Public score: `0.89262` (regressed).
- Conclusion:
  - Remaining quota after cycle: `0/2`.
  - Current best unchanged at `submissions/public/run33run14_on12_w10_10_v3.csv` (`0.89306`).
  - next cycle should prioritize a new remote GPU axis (different feature construction / calibration-aware stacking) before more score-sensitive raw perturbations.

## 2026-05-17 Two-Submission Cycle

- Pre-loop checks:
  - UTC time at cycle start: `2026-05-17 00:36 UTC`.
  - Remaining quota at start: `2/2` (latest prior history entry was `2026-05-16 19:42:28`).
  - Public leaderboard before start: `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Research/discussion/code refresh:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` and `--sort-by scoreDescending` show no new competition notebooks or fresh public updates.
  - API discussion/discourse channel remains inaccessible in this environment.
  - Error path from previous cycle remained: 3-way `run33 + run14 + run12` OOF-optimal candidates did not convert on public after queue was blocked by quota, so we kept the same candidate family with tighter risk notes.
- Experiment hypothesis and rule rewrite:
  - Keep `run33/run14/run12` sweep candidates only if local OOF uplift is meaningful and risk checks are not more extreme than best.
  - Add a fail-fast rule: if first OOF-upshift candidate drops public score, second submission should be a close hedge (not another full-strength OOF peak) with explicit rationale logged and no additional family expansion.
- Candidate local validation:
  - `run33run14_on12_w27_38_v5.csv`: `id,Exited` format, `110,023` rows, no NaN, values `[0,1]`, OOF `0.8983608678126821`, p99 `0.96729`.
  - `run33run14_on12_w28_30_v5.csv`: `id,Exited` format, `110,023` rows, no NaN, values `[0,1]`, OOF `0.8983556084148695`, p99 `0.96719`.
  - Candidate risk check passed: no fold instability observed in quick local verification; both predictions were less extreme than the existing best-envelope baseline.

Cycle 1:

- File: `submissions/public/run33run14_on12_w27_38_v5.csv`
- Submitted: `2026-05-17 00:36:21.600000`.
- Public score: `0.89272`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: rejected (public regression); triggers rule rewrite for next submission in cycle.

Cycle 2:

- File: `submissions/public/run33run14_on12_w28_30_v5.csv`
- Submitted: `2026-05-17 00:43:50.893000`.
- Public score: `0.89269`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: rejected (public regression).

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.
- Error analysis: best two OOF peaks in this family likely overfit on this benchmark; next cycle should reduce run33/run14 concentration and prioritize a calibration hedge path around stable anchors (including `run32_tempT0_8`) once remote training artifacts are available.
- New queued/prepared file for future: `submissions/public/run33run14_on12_w30_30_v6.csv` (generated from local oof/test blend as a control hedge).

## 2026-05-16 Quota Block + Prepared 2-Submission Queue

- Pre-loop checks:
  - Query before this loop: `today submissions = 2`, quota status `0/2` (already used).
  - Kaggle API detail from submit probe:
    - Error: `Submission not allowed: Your team has used its daily Submission allowance (2) today, please try again tomorrow UTC (4.2 hours from now).`
  - Remaining ETA to retry: `~4h12m` (UTC midnight reset).
  - Public leaderboard best remained `0.89306` (`run33run14_on12_w10_10_v3.csv`), rank `1 / 11`.
- Discussion/code scan (before queue build):
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by scoreDescending` outputs only 5 kernels, no new high-score pattern beyond historical baselines.
  - Local notebook snapshot also shows no new public method materially beyond existing strong cross-family blends/stacking paths.
- Local OOF-driven re-exploration:
  - Used components `run12`, `run14`, `run33` to scan 3-way convex weights.
  - Found improved OOF region around `run33 0.27`, `run14 0.38`, `run12 0.35` (OOF `0.89836`) and `run33 0.28`, `run14 0.30`, `run12 0.42` (OOF `0.89836`) versus current blend `0.89811`.
  - Risk controls checked: std, p99, correlation to current best remained near-baseline (`corr >= 0.9988`).
- Candidate files prepared after local validation:
  - `submissions/public/run33run14_on12_w27_38_v5.csv`
  - `submissions/public/run33run14_on12_w28_30_v5.csv`
  - Validation: both `id,Exited`, `110,023` rows, no NaN, values in `[0,1]`.

Cycle 1 / Cycle 2 (planned, blocked by quota):

- Status:
  - Not submitted this loop due hard daily limit error.
  - Next allowed submission time: tomorrow UTC (4.2h later).
- Next action:
  - Submit the two prepared queue files in order once allowance resets.
  - If score regresses, fallback to run33run14 safe candidates and continue OOF-guided refinement.

Conclusion:

- Remaining quota at end of loop: `0/2`.
- Current best remains `run33run14_on12_w10_10_v3.csv` at `0.89306` (`1 / 11`).
- Error analysis: the current process is blocked by API quota, not by experiment validity.

## 2026-05-14 Two-Submission Cycle

- Pre-cycle checks:
  - UTC check time at cycle start: `2026-05-14 02:00 UTC` (estimated from submission list polling).
  - Remaining quota: `2/2`.
  - Previous best before start remained `0.89306` (`run33run14_on12_w10_10_v3.csv`, rank `1 / 11`).
- Public-code review:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` returned no materially new notebooks versus previous cycle.
  - Discussion endpoint was still not usable for direct high-value extraction in this run.
- Candidate validation:
  - `run31_exp_a_080_010_010_dual30p70.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, finite `[0,1]`.
  - `run31_exp_a_080_010_010_dual50p50.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, finite `[0,1]`.
  - Risk gate kept both files for submission due passing local checks.

Cycle 1:

- File: `submissions/public/run31_exp_a_080_010_010_dual30p70.csv`
- Submitted: `2026-05-14 02:08:19.357000`.
- Public score: `0.89281`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: accepted, no best improvement.

Cycle 2:

- File: `submissions/public/run31_exp_a_080_010_010_dual50p50.csv`
- Submitted: `2026-05-14 02:16:12.650000`.
- Public score: `0.89281`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: accepted, no best improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306` (`1 / 11`).
- Next candidate family retained for future loop: `run31_exp_b_097_001_002_*`, then `run32_tempT` calibrations if stable.

## 2026-05-15 Two-Submission Cycle

- Quota and starting state:
  - Starting remaining quota: `2/2` (two entries from this date now complete in Kaggle submission list).
- Public-code review:
  - No public notebook refresh since prior scan.
  - Discussion read path still unavailable from environment.
- Candidate checks before submit:
  - `run31_exp_b_097_001_002_dual50p50.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.
  - `run31_exp_b_097_001_002_dual30p70.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.

Cycle 1:

- File: `submissions/public/run31_exp_b_097_001_002_dual50p50.csv`
- Submitted: `2026-05-15 02:31:46.697000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: accepted, no best improvement.

Cycle 2:

- File: `submissions/public/run31_exp_b_097_001_002_dual30p70.csv`
- Submitted: `2026-05-15 02:32:10.123000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: accepted, no best improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`.

## 2026-05-16 Two-Submission Cycle

- Pre-cycle checks:
  - Remaining quota at start: `2/2` (no 2026-05-16 entries in submission log before this cycle).
  - Public leaderboard best remained `run33run14_on12_w10_10_v3.csv` at `0.89306`, rank `1 / 11`.
- Public review:
  - `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge` unchanged.
  - Discussion read path remained low-signal in this environment.
- Candidate sanity before submission:
  - `run32_tempT1_0.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.
  - `run32_tempT1_2.csv`: `id,Exited`, `110,023` rows, aligned IDs, no NaN, values in `[0,1]`.

Cycle 1:

- File: `submissions/public/run32_tempT1_0.csv`
- Submitted: `2026-05-16 19:42:00.767000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: no best improvement.

Cycle 2:

- File: `submissions/public/run32_tempT1_2.csv`
- Submitted: `2026-05-16 19:42:28.567000`.
- Public score: `0.89293`.
- Status: COMPLETE.
- Rank after submission: `1 / 11`.
- Result: no best improvement.

Conclusion:

- Remaining quota after cycle: `0/2`.
- Current best unchanged: `0.89306` (`run33run14_on12_w10_10_v3.csv`, rank `1 / 11`).
- Next direction retained: `run32_tempT0_8.csv` for a calibration hedge; continue to monitor whether remote generated models alter correlation structure versus run33/`run12`.

## 2026-05-14 Quota Blocked + Next 2-Submission Cycle (historical pre-reset)

- UTC check time: `2026-05-13` (late in day).
- Remaining quota then: `0/2`.
- Planned queue at that point:
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

0.89306 (current best) -> 0.89269 -> 0.89262 (no best improvement)

Pre-cycle checks:

- UTC date/time at quota check: `2026-05-13`.
- Remaining quota before cycle: `2/2`.
- Today's pre-logged submissions found in Kaggle history at cycle start:
  - `run33run14_on12_w30_20_50_v4.csv` at `2026-05-13 00:32:08.413000` (public `0.89262`).
  - `run33run14_on12_w28_34_38_v4.csv` at `2026-05-13 00:33:43.450000` (public `0.89269`).
- Candidate file verification (all IDs/columns/row counts/finite range checks):
  - `A_main_run33run14_run12.csv` → exact duplicate of `run33run14_on12_w28_34_38_v4.csv`.
  - `D_mix_run33run14_run12.csv` → exact duplicate of `run33run14_on12_w30_20_50_v4.csv`.
  - `B_safe_run33run14_run12.csv`, `C_lean_run33run14_run12.csv`, `E_light_run33run14_run12.csv` pass format checks but were not submitted because quota was exhausted.
- OOF proxies (derived from base OOF blends) showed:
  - `A_main`: `0.898360`
  - `D_mix`: `0.898328`
  - `E_light`: `0.898272`
  - `B_safe`: `0.898274`
  - `C_lean`: `0.898260`

Cycle 1:

- File: `submissions/public/run33run14_on12_w30_20_50_v4.csv` (alias `D_mix_run33run14_run12.csv`)
- Submitted: `2026-05-13 00:32:08.413000`.
- Public score: `0.89262`.
- Rank: `1 / 11`.
- Result: accepted, no public gain.

Cycle 2:

- File: `submissions/public/run33run14_on12_w28_34_38_v4.csv` (alias `A_main_run33run14_run12.csv`)
- Submitted: `2026-05-13 00:33:43.450000`.
- Public score: `0.89269`.
- Rank: `1 / 11`.
- Result: accepted, no public gain.

Conclusion:

- Daily quota is now `0/2` with both slots consumed.
- Current best remains unchanged: `submissions/public/run33run14_on12_w10_10_v3.csv` at `0.89306`, rank `1 / 11`.
- Remaining queued candidates require next UTC reset before submission.

## 2026-05-12 Two-Submission Cycle

Pre-cycle checks:

- UTC date/time at quota check: `2026-05-12`.
- Remaining quota before cycle: `2/2` (no local `2026-05-12` entries before cycle).
- Leaderboard before first submission: top was `0.89304` (`run33_on12_w05_v2`), rank `1 / 11`.
- Public notebooks scan via `kaggle kernels list --competition binary-battle-ml-bank-customer-churn-challenge --sort-by dateRun` did not reveal a new high-signal strategy.
- Discussion endpoint remained low-signal/unavailable through API, so no direct discussion update was actionable.
- Experiment focus: keep local-overfit-aware blend path with `run33`/`run12`/`run14` and validate distribution/correlation before submission.

Cycle 1:

- File: `submissions/public/run33_on12_w20_v3.csv`
- Local notes:
  - Candidate OOF: `0.898167`
  - std/p99: `0.27126` / `0.96683`
  - Format checks: `id,Exited` columns, `110,023` rows, IDs aligned to `data/raw/sample_submission.csv`, finite in-range predictions.
- Submitted: `2026-05-12 07:58:07.923000`.
- Public score: `0.89291`.
- Rank: unchanged (`1 / 11`).
- Result: did not improve best, proceeded to secondary candidate in same loop.

Cycle 2:

- File: `submissions/public/run33run14_on12_w10_10_v3.csv`
- Local notes:
  - Candidate OOF: `0.898109`
  - std/p99: `0.27160` / `0.96752`
  - Format checks passed.
- Submitted: `2026-05-12 07:58:27.390000`.
- Public score: `0.89306`.
- Rank: `1 / 11`.
- Result: success; this became current best.

Conclusion:

- Two submission cycle complete, with one improvement.
- Next planned hypothesis: 3-way blend around `(run33_xgb_all_s202, run12, run14)` with small weight perturbation and conservative calibration.

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

- File: `submissions/run12_gpu_cat_seed_blend_10_11.csv`.
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
- Research and verifier subagents both recommended exploiting the now-validated GPU CatBoost family via more seed averaging rather than submitting individual seeds or conservative blends.

Experiment:

- Remote GPU training on RTX 4080:
  - `run13_s4e1_text_cat_gpu_s314`: OOF `0.897482`.
  - `run14_s4e1_text_cat_gpu_s1001`: OOF `0.897616`.
- Local seed-blend search over `run10/run11/run13/run14`:
  - Equal 4-seed average OOF `0.898061`.
  - Best coarse weighted blend `run15`: `0.20*run10 + 0.20*run11 + 0.25*run13 + 0.35*run14`, OOF `0.898070`.
  - Validation: CSV/id/range passed, test std `0.271797`, p99 `0.968020`, corr vs `run12` `0.999896`, corr vs overfit `run01` `0.949224`.

Submission:

- File: `submissions/run15_gpu_cat_4seed_weighted.csv`.
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

- Candidate selected: `submissions/run21_all_cat_s202.csv` (remote `run21_*` bundle synced to local).
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

- Candidate: `submissions/run20_regA_w10_on12.csv`.
- Submitted: `2026-05-04 19:37:35.273000`.
- Public score: `0.89291`.
- Rank: `1 / 11` (unchanged, best remains `0.89293`).

Cycle 2:

- Candidate: `submissions/run20_regA_w05_on12.csv`.
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

- Candidate: `submissions/run23_blend_10_10_80.csv`.
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
- Candidate: `submissions/run28_best_mix_085_06_09.csv`.
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

- Candidate file: `submissions/exp_d_077_010_010_003_prob.csv`.
- Submitted: `2026-05-07 00:33:21.613000`.
- Public score: `0.89280` (failure: below best `0.89293`).
- Result/analysis:
  - Despite high OOF, public dropped; confirms overfit risk from large raw-probability `run21` and mixed `run22` perturbation.
  - Rule triggered: move away from the same `run12 + raw OOF blend` path for next step.

Cycle 2:

- Candidate file: `submissions/rank_mix_85_10_05_rank.csv`.
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
