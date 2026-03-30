# Research-to-Build Workspace

This repository is organized as a literature-to-proposal-to-build workspace.

## Current canonical topic

- `in-context-rl`

## Canonical workflow

1. `papers/`
   Local paper folders and source material.
2. `notes/papers/`
   One evidence-grounded note per paper.
3. `notes/claims/in-context-rl/`
   Reusable claim ledger for the topic.
4. `synthesis/in-context-rl/`
   Topic-scoped trends, gaps, contradictions, method map, and agenda.
5. `proposal/in-context-rl/`
   Topic-scoped proposal drafts and references.
6. `specs/in-context-rl/`
   Build spec, interfaces, observability, risk register, and durable research log.
7. `src/icrl_slice/`, `tests/`, `scripts/`, `artifacts/in-context-rl/min_slice/`
   The smallest implemented vertical slice and its validation artifacts.

## Directory map

- `AGENTS.md`
  Repository rules and grounding policy.
- `papers/`
  Local paper folders.
- `notes/`
  Evidence layer.
- `synthesis/`
  Topic-scoped synthesis.
- `proposal/`
  Proposal artifacts.
- `specs/`
  Topic-scoped build specifications.
- `src/`
  Implementation code.
- `tests/`
  Automated checks.
- `scripts/`
  Validation helpers.
- `artifacts/`
  Build and validation outputs.
- `plans/`
  Durable rollout plans and decision logs.
- `cache/`
  Intermediate parsing artifacts and generated JSON helpers.
- `reviews/`
  Skeptical review reports.
- `legacy/`
  Archived root-era artifacts retained for reference.

## Current implemented slice

The current executable slice is a controlled hidden-task Bernoulli bandit proxy for `in-context-rl`, now extended with a bounded `experience compilation` mechanism.

Run:

```bash
PYTHONPATH=src python3 -m icrl_slice.run --output-dir artifacts/in-context-rl/min_slice
```

Validate:

```bash
python3 scripts/validate_icrl_slice.py --artifact-dir artifacts/in-context-rl/min_slice
```

Test:

```bash
PYTHONPATH=src python3 -m unittest tests.test_icrl_slice
```

## Scope boundary

- The current build covers:
  - explicit candidate state
  - bounded experience compilation
  - controlled task shift
  - calibration-oriented logging
- The current build does **not** yet cover:
  - universal `experience compilation`
  - proposal-scale revisable memory
  - abstention or safe action override
  - embodied validation
  - strong matched-capacity baselines

## Legacy and generated artifacts

- `legacy/` stores older root-level proposal snapshots and similar archived artifacts.
- `cache/derived/` stores generated JSON summaries and reference-mining outputs that are not part of the canonical workflow surface.

## Recommended continuation points

- Continue literature work from:
  - `notes/claims/in-context-rl/`
  - `synthesis/in-context-rl/`
  - `proposal/in-context-rl/`
- Continue build work from:
  - `specs/in-context-rl/`
  - `src/icrl_slice/`
  - `artifacts/in-context-rl/min_slice/`

## Current runtime artifacts

The current default run writes:

- `summary.json`
- `per_seed_metrics.json`
- `transitions.jsonl`
- `calibration.csv`
- `memory_contents.jsonl`
- `revision_events.jsonl`
- `smoke_check.txt`
