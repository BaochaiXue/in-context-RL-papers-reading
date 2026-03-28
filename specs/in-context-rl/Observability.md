# Observability

## Required metrics

- `cumulative_regret`
- `average_reward`
- `optimal_action_rate`
- `belief_brier_score`
- `mean_selected_arm_uncertainty`
- `shift_recovery_steps`

## Transition log schema

Each row in `transitions.jsonl` should include:

- `seed`
- `agent`
- `episode`
- `timestep`
- `task_id`
- `shifted`
- `action`
- `reward`
- `optimal_arm`
- `regret`
- `belief_top_task`
- `belief_top_prob`
- `selected_arm_uncertainty`

## Calibration hook

For the `ExplicitStateAgent`, record:

- predicted probability assigned to the current top-belief task
- correctness of that belief relative to the hidden task

This supports a simple Brier-style belief calibration score.

## Smoke validation

The smoke check must verify:

- output files exist
- both agents ran
- metrics are finite
- the explicit-state agent produced belief and uncertainty fields

## Logging principle

- log enough to debug state updates and shift recovery
- avoid excessive trace size for the default run

## Current limitation

- uncertainty is currently an observational hook only
- the slice does **not** implement abstention, safe action override, or uncertainty-gated fallback behavior
