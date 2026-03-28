# Research Log

## 2026-03-28

- Initialized `specs/in-context-rl/` from the approved agenda because no implementation spec existed.
- Locked scope to a controlled hidden-task Bernoulli bandit slice.
- Chose a vertical slice that can test three things end-to-end:
  - explicit candidate state
  - memory / history handling
  - calibration under task shift
- Remaining uncertainty before implementation:
  - whether the opaque baseline will be competitive enough to make the comparison meaningful
  - how stable the simple calibration metric will be at small scale

## 2026-03-28 (implementation update)

- Implemented `src/icrl_slice/` with:
  - `HiddenTaskBandit`
  - `OpaqueHistoryAgent`
  - `ExplicitStateAgent`
  - metrics helpers
  - CLI runner
- Added validation layer:
  - `tests/test_icrl_slice.py`
  - `scripts/validate_icrl_slice.py`
  - root `README.md` with run / validate / test commands
- Produced validation artifacts under `artifacts/in-context-rl/min_slice/`:
  - `summary.json`
  - `per_seed_metrics.json`
  - `transitions.jsonl`
  - `calibration.csv`
  - `smoke_check.txt`

## 2026-03-28 (validation update)

- `unittest` passed on the minimum slice.
- Default smoke run completed successfully.
- Tightened the default slice from `5` arms to `3` arms so the minimum configuration better exposes the intended controlled comparison rather than hiding it behind a broader task family.
- Current default validation summary:
  - `explicit_state` cumulative regret: `15.234375`
  - `opaque_history` cumulative regret: `18.046875`
  - `explicit_state_better_on_regret`: `true`
  - `explicit_state_better_on_reward`: `true`
  - `explicit_state` belief Brier score: `0.025831978173633568`

## Remaining uncertainty

- The slice is still toy and hand-structured; it only demonstrates the agenda claim in a controlled hidden-task bandit family.
- The `ExplicitStateAgent` knows the candidate task family in advance, so the result should be interpreted as a controlled proof-of-concept rather than a general ICRL result.
- The calibration metric is intentionally simple and should not be over-read beyond this slice.
- The current build instantiates Aim 1 and a thin Aim 3 proxy; it does not implement Aim 2 `experience compilation`.
- Uncertainty is currently observational only; it is logged for evaluation purposes, but the slice does not implement abstention or a safer uncertainty-gated action policy.
