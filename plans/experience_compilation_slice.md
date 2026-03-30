# Experience Compilation Slice

## Goal

Implement the first bounded Aim 2 slice for `in-context-rl` without expanding to a full context compiler.

## Scope

- controlled hidden-task bandit environment only
- explicit event extraction
- compact revisable memory
- compiled-memory-conditioned action selection
- inspectable revision and invalidation behavior

## Out of scope

- universal compiler claims
- neural training
- embodied or multimodal validation
- safe-action or abstention policy

## Minimum comparisons

- `opaque_history` raw-history proxy
- `filtered_history` proxy
- `compiled_memory` slice

## Preferred extra comparison if it stays cheap

- simple `retrieval_proxy`

## Required artifacts

- summary metrics
- per-seed metrics
- transitions
- memory contents
- revision events
- smoke check

## Required validation

- tests for revision / invalidation behavior
- smoke run for end-to-end slice
- validator that checks the new artifacts and prints both gains and limitations
