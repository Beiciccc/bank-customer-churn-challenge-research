# Public Record

# Submission Iteration Log

This file is the required checkpoint after each Kaggle submission. Each cycle records the score first, then the research and experiment plan for the next attempt.

## Current Best

- Submission: `submissions/public/run33_on12_w05_v2.csv`
- Latest submission: `2026-05-08 10:54:24.343000`
- OOF/CV: `run33=0.897919`
- Public score: `0.89304`
- Rank after submission: `1 / 11` as refreshed on `2026-05-08 UTC`.
- Delta vs previous best: `+0.00011`
- Notes: `run33` is a 95% `run12` + 5% `run33_xgb_all_s202` blend and is a public-safe bump while preserving `run12` backbone behavior.

## Loop Checklist

- Record score and rank before starting new work.
- Review public notebooks, discussion threads, related S4E1 high-score code, and any newly visible leaderboard patterns.
- Pick one or two concrete hypotheses, not a broad search.
- Run GPU training on the remote server only.
- Sync outputs and reports back to `/Volumes/Z/Bank Customer Churn Challenge`.
- Validate OOF/fold stability/blend behavior and submission CSV format locally.
- Submit only when the candidate beats or usefully diversifies the current best.

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
