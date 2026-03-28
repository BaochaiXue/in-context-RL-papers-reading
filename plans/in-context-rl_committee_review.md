# In-Context RL Committee Review

## Goal

Run a skeptical committee review over the current `in-context-rl` proposal, spec, and minimum implementation slice, then patch the weakest points conservatively.

## Review surface

- `proposal/in-context-rl/`
- `specs/in-context-rl/`
- `artifacts/in-context-rl/min_slice/`
- `src/icrl_slice/`
- `tests/test_icrl_slice.py`
- `notes/claims/in-context-rl/`

## Reviewers

- `citation_auditor`
- `technical_skeptic`
- `execution_risk_reviewer`

## Review questions

- Are there unsupported or over-strong claims relative to the local note and claim ledger?
- Is the technical core novel and coherent, or does it rely on hand-matched toy structure?
- Is the implementation slice a defensible test of the spec, or is the baseline / config too weak?
- Are risks, baselines, calibration hooks, and validation logic specific enough?

## Expected outputs

- `reviews/in-context-rl/citation_auditor.md`
- `reviews/in-context-rl/technical_skeptic.md`
- `reviews/in-context-rl/execution_risk_reviewer.md`

## Patch principle

- Keep fixes scoped.
- Prefer tightening claims, acceptance criteria, and validation language over expanding implementation scope.
- Accept open risks explicitly where the current slice cannot honestly resolve them.
