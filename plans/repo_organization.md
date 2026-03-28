# Repository Organization

## Goal

Reorganize the repository into a clearer research-to-build workspace without deleting user artifacts.

## Principles

- Keep the current canonical topic path explicit: `in-context-rl`
- Prefer archiving over deletion for old or duplicate artifacts
- Separate:
  - canonical workflow artifacts
  - generated caches
  - legacy proposal snapshots
- Keep run/build commands working after the cleanup

## Canonical structure

- `papers/`: local paper folders and source material
- `notes/`: per-paper notes, claim ledgers, tables
- `synthesis/`: topic-scoped synthesis
- `proposal/`: topic-scoped proposal artifacts
- `specs/`: topic-scoped build specs
- `src/`, `tests/`, `scripts/`, `artifacts/`: implementation slice
- `plans/`: durable rollout plans
- `cache/`: generated or intermediate parse artifacts
- `reviews/`: topic-scoped skeptical review reports
- `legacy/`: archived root-era artifacts kept for reference

## This cleanup should do

- archive duplicate root proposal artifacts
- archive old root-level proposal subtree artifacts
- move loose generated JSON intermediates into `cache/`
- rewrite READMEs so the canonical workflow is obvious

## This cleanup should not do

- delete papers, notes, synthesis, proposal, or implementation artifacts
- change the meaning of the current `in-context-rl` slice
- silently remove old files without leaving an archived location
