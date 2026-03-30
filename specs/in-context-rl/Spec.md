# Spec

## Topic

`in-context-rl`

## Title

**Bounded Experience Compilation Slice on a Hidden-Task Bandit**

## Goal

Build the smallest defensible Aim 2 milestone in a controlled setting:

- add a bounded `experience compilation` mechanism
- surface revision and invalidation behavior explicitly
- compare compiled memory against raw-history and simple proxy baselines
- expose both gains and limitations through validation artifacts

## Core claim for this slice

In a controlled hidden-task Bernoulli bandit environment, a bounded `compiled_memory` agent that extracts events, writes revisable memory, and conditions decisions on that compact memory should demonstrate inspectable revision behavior and produce an informative comparison against raw-history and simple proxy baselines.

## Smallest vertical slice

The slice consists of:

1. a hidden-task Bernoulli bandit environment with optional mid-run task shifts
2. an `OpaqueHistoryAgent` raw-history proxy
3. a `FilteredHistoryAgent` simple filtering proxy
4. a `RetrievalProxyAgent` simple recent-event retrieval proxy
5. an `ExplicitStateAgent` retained from the earlier slice for comparison continuity
6. a `CompiledMemoryAgent` that maintains:
   - extracted events
   - compact revisable memory
   - task-belief estimate
   - arm-value estimate
   - uncertainty estimate
7. an experiment runner that evaluates the bounded comparison set and writes validation artifacts
8. tests, smoke checks, logs, calibration outputs, memory traces, and revision-event logs

The default run configuration should remain intentionally small enough that compiled-memory behavior is observable in the controlled task family, rather than being obscured by a broader task interface than this bounded slice is meant to cover.

## Non-goals

- no neural training stack
- no large-scale embodied or multimodal validation
- no attempt to prove the full research program
- no claim that the toy slice solves general ICRL
- no claim of a universal context compiler

## Acceptance criteria

- a single command runs the slice end-to-end
- output artifacts are written under `artifacts/in-context-rl/min_slice/`
- summary artifacts include:
  - cumulative regret
  - average reward
  - calibration-oriented metrics
  - shift recovery statistics
  - memory-event counts
  - revision-event counts
- `memory_contents.jsonl` and `revision_events.jsonl` exist
- validation output must expose both gains and limitations relative to the comparison set
- tests and a smoke check pass
- `ResearchLog.md` states what changed and what remains uncertain

## Boundaries

- this slice is only a controlled proxy for Aim 2 plus links back to Aim 1 / partial Aim 3 questions
- any success claim must be limited to this environment family
- the current implementation is a bounded event-driven proxy, not a full proposal-scale `experience compilation` architecture
- uncertainty outputs in the current slice are observational diagnostics, not a full safe-action or abstention policy
- the current `OpaqueHistoryAgent` is a sanity baseline, not a strong matched-capacity comparator
