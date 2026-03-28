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
