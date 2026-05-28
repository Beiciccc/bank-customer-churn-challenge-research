# Kaggle Iteration Runbook

This runbook is binding for future "perform x submissions" requests.

## Required Cycle Order

For each requested successful submission:

1. Query remaining daily submissions.
2. Browse or query updates in public code, discussion, solution archives, and leaderboard.
3. Produce an experiment hypothesis and submit/no-submit rule.
4. Run the experiment, with GPU jobs only on the remote server.
5. If training is long, estimate ETA and keep this session alive with sleep/polling.
6. Sync outputs between the remote project and `/Volumes/Z/Bank Customer Churn Challenge`.
7. Validate OOF, fold scores, blend behavior, correlations, prediction distribution, and CSV format.
8. Submit only if validation passes.
9. Wait until Kaggle returns the public score.
10. Record score and rank immediately.
11. On success, continue to the next cycle.
12. On failure, analyze the error, update rules/code/docs, then continue.

## Long-Term Subagents

- Research Watcher: tracks public notebooks, discussions, related high-score writeups, solution archives, and leaderboard deltas.
- Experiment Planner/Verifier: checks hypotheses, validation design, OOF stability, correlations, distributions, CSV format, and submit/no-submit gates.

The main agent coordinates all work and owns all file edits, remote commands, synchronization, submissions, and final decisions.

## Subagent Summary Formats

Research Watcher returns:

```text
Research Watch Summary - Cycle N

External Updates:
- Current competition notebooks:
- Discussions:
- Leaderboard:
- Related S4E1/S5E8/S6E3/Solutions archive:

Signals Worth Acting On:
- ...

Risks / Warnings:
- ...

Recommendation For Next Experiment:
- Primary:
- Backup:
- Submit caution:
```

Experiment Planner/Verifier returns:

```text
Verifier Summary - runXX

Candidate:
- Submission:
- Report:
- Command checked:
- GPU remote requirement satisfied:

Scores:
- OOF AUC:
- Delta vs current best:
- Fold stability:

Diversity / Risk:
- Corr vs run09:
- Corr vs run01 overfit reference:
- Prediction distribution:
- Main risk:

CSV Check:
- Format id,Exited:
- Row/id alignment:
- NaN/range/duplicates:

Decision:
- submit / queue / do not submit
- Reason:
```

## Risk Gates

- Strong submit: OOF beats current best, folds are stable, CSV passes, and prediction behavior is not dominated by the known-overfit run01 pattern.
- Cautious submit: OOF is much stronger, but predictions are more extreme or highly correlated with run01. This is allowed only after explicitly recording the risk.
- Do not submit: no remaining daily quota, CSV failure, unreproducible outputs, unstable folds, or no OOF gain/diversity.

## Current Queued Candidate

- `run45_rank_40_20_20_20_v1.csv`
  - OOF `0.8985637`
  - Low/moderate-correlation rank-space candidate (corr to run33 OOF about `0.8443`).
- `run45_rank_60_25_15_v1.csv`
  - OOF `0.8985034`
  - Similar rank-space hedge with slightly lower run45_weight and OOF/corr balance.
- `run45_isotonic_90_10_on12_v1.csv`
  - OOF `0.8983295`
  - Calibrated probability path with high run12 similarity; low-variance backup.
- `run45_w97_3_isotonic_on12_v1.csv`
  - OOF `0.8982906`
  - Calibrated probability path, even lower perturbation.
- Queue status: ready; awaiting UTC quota reset before actual submissions.
