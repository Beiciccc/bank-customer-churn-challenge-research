# Bank Customer Churn Challenge

Kaggle competition: `binary-battle-ml-bank-customer-churn-challenge`

Key facts checked on 2026-04-25:

- Task: predict bank customer churn probability (`Exited`).
- Metric: ROC AUC.
- Submission format: `id,Exited`.
- Max daily submissions: 2.
- Team size: 1.
- Deadline: 2027-01-26 06:30 UTC.

Remote project path:

`C:/Users/Kun/Bank Customer Churn Challenge`

Local sync path:

`/Volumes/Z/Bank Customer Churn Challenge`

## Repository Scope (Public View)

- `src/train.py`: single training/evaluation script used for local experiment orchestration.
- `requirements.txt`: dependency list.
- `data/raw`: official competition train/test/sample-submission files.
- `research/notes.md`: notes from public code scan and feature-direction analysis.
- `research/iteration_log_public.md`: public-facing checkpoint log with each submission outcome.
- `submissions/public`: curated submission outputs used during iteration.

## Notes

- Use this repository for experiment records and reproducibility; raw model arrays and large intermediate artifacts are kept out to keep the public repo concise.
- GPU experiments are run on the remote machine and synced to this path.

## Runs

| run | file | CV | public score | notes |
| --- | --- | ---: | ---: | --- |
| run01 | `submissions/public/run01_cat_lgb_lgb.csv` | 0.898116 | 0.87387 | Overfit from high-cardinality `CustomerId`/`Surname` statistics. |
| run02 | `submissions/public/run02_robust.csv` | 0.890000 | 0.88633 | Robust CatBoost/LightGBM/XGBoost blend. |
| run03 | `submissions/public/run03_cat_native_20f.csv` | 0.889285 | not submitted | 20-fold CatBoost with native high-cardinality `CustomerId/Surname`. |
| run04 | `submissions/public/run04_blend_run02_run03.csv` | 0.890206 | 0.88634 | `0.68*run02 + 0.32*run03`. |
| run05 | `submissions/public/run05_cat_native_ext_5f.csv` | 0.889288 | not submitted | External original data added only to training folds, not validation folds. |
| run06 | `submissions/public/run06_blend_235.csv` | 0.890246 | 0.88635 | `0.62*run02 + 0.18*run03 + 0.20*run05`. |
| run07 | `submissions/public/run07_rank_blend_235.csv` | 0.890280 | 0.88637 | Rank blend of run02/run03/run05. |
| run08 | `submissions/public/run08_s4e1_text_cat_5f.csv` | 0.890760 | not submitted | CatBoost native categorical with S4E1-style combo categories plus Surname/AllCat TF-IDF SVD. |
| run09 | `submissions/public/run09_prob_blend_2358.csv` | 0.891021 | 0.88725 | `0.35*run02 + 0.65*run08`; best pre-GPU submission. |
| run10 | `submissions/public/run10_s4e1_text_cat_gpu_s202.csv` | 0.897375 | not submitted | GPU CatBoost seed 202 with expanded cardinality handling. |
| run11 | `submissions/public/run11_s4e1_text_cat_gpu_s777.csv` | 0.897412 | not submitted | GPU CatBoost seed 777 with expanded cardinality handling. |
| run12 | `submissions/public/run12_gpu_cat_seed_blend_10_11.csv` | 0.897786 | 0.89293 | `0.5*run10 + 0.5*run11`; public best on 2026-04-29. |
| run13 | `submissions/public/run13_s4e1_text_cat_gpu_s314.csv` | 0.897482 | not submitted | GPU CatBoost seed 314 for seed diversity. |
| run14 | `submissions/public/run14_s4e1_text_cat_gpu_s1001.csv` | 0.897616 | not submitted | GPU CatBoost seed 1001 for seed diversity. |
| run15 | `submissions/public/run15_gpu_cat_4seed_weighted.csv` | 0.898070 | 0.89291 | Weighted blend of run10/run11/run13/run14; slightly below run12 on public. |
| run16 | `submissions/public/run16_run12_70_seed1314_30.csv` | 0.897998 | 0.89293 | `0.70*run12 + 0.30*avg(run13,run14)`; tied public best. |
| run17 | `submissions/public/run17_rank_run12_50_rank1314_50.csv` | 0.898053 | 0.89291 | Rank blend of run12 and avg(run13,run14); below run12/run16 on public. |
| run18 | `submissions/public/run18_run12_99_run02_01.csv` | 0.897777 | 0.89293 | `0.99*run12 + 0.01*run02`; tied public best. |
| run19 | `submissions/public/run19_rank_run12_90_run09_10.csv` | 0.897605 | 0.89280 | Rank blend of run12/run09; below current best. |

Latest checkpoint in `research/iteration_log_public.md` shows best public score `0.89293` (runs `run12`, `run16`, `run18` tied). Subsequent cycles (`run20`-`run31`) were recorded for process continuity but did not surpass this score.
