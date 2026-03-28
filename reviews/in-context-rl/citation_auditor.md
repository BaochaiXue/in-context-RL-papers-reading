# Citation Auditor Review

## Findings

1. **[High] The proposal text still reads as if the implemented slice validates the proposal-level mechanism claim, but the current slice only validates a hand-structured toy proxy.** The proposal repeatedly frames the agenda around discovering a testable `algorithmic state` in fixed-weight models and then validating it under shift in a way that extends toward realistic deployment ([main_en.md](/Users/xinjiezhang/in%20context%20RL/proposal/in-context-rl/main_en.md)). The actual implementation in [Spec.md](/Users/xinjiezhang/in%20context%20RL/specs/in-context-rl/Spec.md) and [run.py](/Users/xinjiezhang/in%20context%20RL/src/icrl_slice/run.py) is a small hidden-task Bernoulli bandit where the `ExplicitStateAgent` is given the candidate task family in advance. That is a useful controlled proxy, but local evidence does not justify letting readers blur it into a broader validation of the proposal thesis.

2. **[High] The current default success story depends on a narrowed configuration that is not reflected strongly enough in the proposal-facing text.** The spec now explicitly narrows the default run to `3` arms so the explicit-state advantage is observable ([Interfaces.md](/Users/xinjiezhang/in%20context%20RL/specs/in-context-rl/Interfaces.md), [ResearchLog.md](/Users/xinjiezhang/in%20context%20RL/specs/in-context-rl/ResearchLog.md)), and the artifact summary indeed shows `explicit_state_better_on_regret: true` only for that default setting ([summary.json](/Users/xinjiezhang/in%20context%20RL/artifacts/in-context-rl/min_slice/summary.json)). This is defensible, but the proposal/spec boundary should state more plainly that the implementation demonstrates the claim only in this narrowed task family.

3. **[Medium] The proposal's literature framing is stronger than the implementation can currently support for novelty claims.** The literature review in [main_en.md](/Users/xinjiezhang/in%20context%20RL/proposal/in-context-rl/main_en.md) makes a compelling case for explicit state, context compilation, and belief-calibrated adaptation, but the shipped slice only instantiates the first and a thin piece of the third. There is no implementation of `experience compilation` beyond direct history updates, so readers could infer that the slice already exercises Aim 2 more fully than it actually does.

## What to patch

- Tighten the proposal/spec language to say the slice is a controlled proxy for the proposal agenda, not a validation of the full mechanism thesis.
- Explicitly record in the spec-facing and proposal-facing text that the default success claim is limited to the narrowed `3`-arm hidden-task family.
- Mark Aim 2 as not yet implemented in the current build slice, so the implementation is not over-read as a realization of the full three-aim program.
