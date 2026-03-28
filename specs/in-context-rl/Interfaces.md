# Interfaces

## CLI entrypoint

Primary run command:

```bash
PYTHONPATH=src python3 -m icrl_slice.run --output-dir artifacts/in-context-rl/min_slice
```

## Runtime arguments

- `--seeds`: number of random seeds, default `16`
- `--episodes`: number of episodes per seed, default `24`
- `--horizon`: steps per episode, default `20`
- `--arms`: number of arms, default `3`
- `--shift-episode`: episode index at which the hidden task changes, default `12`
- `--output-dir`: artifact directory

## Code interfaces

### `HiddenTaskBandit`

- `reset(task_id: int | None = None) -> observation`
- `step(action: int) -> (reward: float, info: dict)`
- `intervene(task_id: int) -> None`

### `OpaqueHistoryAgent`

- `reset(num_arms: int) -> None`
- `act() -> int`
- `update(action: int, reward: float) -> None`
- `snapshot() -> dict`

### `ExplicitStateAgent`

- `reset(num_arms: int, num_tasks: int) -> None`
- `act() -> int`
- `update(action: int, reward: float) -> None`
- `snapshot() -> dict`

## Output artifacts

- `summary.json`
- `per_seed_metrics.json`
- `transitions.jsonl`
- `calibration.csv`
- `smoke_check.txt`

## Intended consumer

- local research iteration
- skeptical review
- later extension into stronger training-based slices
