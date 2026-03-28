# Spec

## Topic

`in-context-rl`

## Title

**Minimum Vertical Slice: Testable Algorithmic State on a Hidden-Task Bandit**

## Goal

Build the smallest defensible end-to-end slice that demonstrates the core approved agenda claim in a controlled setting:

- an agent with explicit candidate state should adapt more effectively than an opaque history-only baseline
- the slice must surface regret, calibration, and intervention-sensitive behavior

## Core claim for this slice

In a controlled hidden-task Bernoulli bandit environment, an `explicit-state` agent that tracks belief, value, and uncertainty should outperform an `opaque-history` heuristic baseline on regret and calibration-oriented metrics under task shifts.

## Smallest vertical slice

The slice consists of:

1. a hidden-task Bernoulli bandit environment with optional mid-run task shifts
2. an `OpaqueHistoryAgent` baseline that consumes history but does not maintain explicit typed state
3. an `ExplicitStateAgent` that maintains:
   - task-belief estimate
   - arm-value estimate
   - uncertainty estimate
4. an experiment runner that evaluates both agents over repeated seeds and writes validation artifacts
5. tests, smoke checks, logs, and calibration outputs

The default run configuration should remain intentionally small enough that the explicit-state advantage is observable in the controlled task family, rather than being obscured by a broader task interface than this minimum slice is meant to cover.

## Non-goals

- no neural training stack
- no large-scale embodied or multimodal validation
- no attempt to prove the full research program
- no claim that the toy slice solves general ICRL

## Acceptance criteria

- a single command runs the slice end-to-end
- output artifacts are written under `artifacts/in-context-rl/min_slice/`
- summary artifacts include:
  - cumulative regret
  - average reward
  - calibration-oriented metrics
  - shift recovery statistics
- tests and a smoke check pass
- `ResearchLog.md` states what changed and what remains uncertain

## Boundaries

- this slice is only a controlled proxy for Aim 1 / Aim 3 style questions
- any success claim must be limited to this environment family
- the current implementation does **not** realize the proposal's Aim 2 `experience compilation` architecture
- uncertainty outputs in the current slice are observational diagnostics, not a full safe-action or abstention policy
- the current implementation does **not** implement Aim 2 style `experience compilation` or revisable memory
- the current `OpaqueHistoryAgent` is a sanity baseline, not a strong matched-capacity comparator
