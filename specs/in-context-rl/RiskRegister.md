# Risk Register

## R1. The slice may be too toy to say anything meaningful

- Impact: high
- Likelihood: medium
- Mitigation: frame the slice explicitly as a controlled proxy, not a full validation of the agenda

## R2. The explicit-state agent may win only because the environment matches its inductive bias

- Impact: high
- Likelihood: high
- Mitigation: report this as a limitation and include a simple shift intervention to reduce trivial overfitting

## R3. The opaque baseline may be too weak

- Impact: medium
- Likelihood: medium
- Mitigation: keep the baseline simple but not random; use empirical reward history and recency-weighted action values

## R4. Calibration signals may be noisy in short runs

- Impact: medium
- Likelihood: medium
- Mitigation: report calibration with explicit caveats and keep the metric simple

## R5. Success may be overstated

- Impact: high
- Likelihood: medium
- Mitigation: do not claim more than the validation artifacts justify; write residual uncertainty into `ResearchLog.md`

## R6. Uncertainty hooks may be mistaken for a safe action policy

- Impact: high
- Likelihood: medium
- Mitigation: state explicitly that the current slice logs calibration and uncertainty but does not yet implement abstention or action gating

## R7. Uncertainty is measured but not policy-constraining

- Impact: medium
- Likelihood: high
- Mitigation: state clearly that calibration is observational in this slice; defer abstention or safe action gating to a later stage

## R8. The compiled-memory gain may reflect environment matching rather than a general mechanism

- Impact: high
- Likelihood: high
- Mitigation: state clearly that the slice is a bounded event-driven proxy and compare it against multiple simple baselines rather than a single weak comparator
