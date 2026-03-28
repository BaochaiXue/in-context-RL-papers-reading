# Method Map

## Scope

This map clusters methods using only:

- `notes/papers/*.md`
- `notes/claims/in-context-rl/*.yaml`
- `notes/tables/method_comparison.md`
- `notes/tables/evidence_map.md`

## Evidence-backed method clusters

| Cluster | Representative local notes | Core mechanism | What it is strongest at | Persistent limitation | Support claims |
|---|---|---|---|---|---|
| Distilled learning algorithms | `in-context-reinforcement-learning-with-algorithm-distillation`, `supervised-pretraining-can-learn-in-context-reinforcement-learning`, `transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining` | Learn a history-conditioned decision rule from trajectories or supervised rollouts | Establishing that in-context adaptation exists at all | Internal mechanism remains opaque; imitation target can be misaligned | `icrl-foundation-001`, `icrl-foundation-002`, `icrl-method-001` |
| Objective repair for offline ICRL | `in-context-reinforcement-learning-without-optimal-action-labels`, `random-policy-enables-in-context-reinforcement-learning-within-trust-horizons`, `pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning`, `yes-q-learning-helps-offline-in-context-rl` | Replace pure imitation with weighted, reward-prediction, trust-horizon, or RL-style objectives | Making weaker supervision viable and improving offline performance | Still coverage-sensitive; not a clean answer to uncertainty or OOD failure | `icrl-method-001`, `icrl-method-002`, `icrl-contradiction-003` |
| Context shaping and memory selection | `filtering-learning-histories-enhances-in-context-reinforcement-learning`, `retrieval-augmented-decision-transformer-external-memory-for-in-context-rl`, `cross-episodic-curriculum-for-transformer-agents` | Filter, retrieve, reorder, or otherwise structure context before action generation | Improving usability of context without changing the task definition | Does not by itself prove genuine online learning | `icrl-method-003`, `icrl-foundation-003`, `icrl-contradiction-002` |
| Long-context systems engineering | `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`, `decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling`, `structured-state-space-models-for-in-context-reinforcement-learning`, `xlstm-extended-long-short-term-memory`, `flashattention-2-faster-attention-with-better-parallelism-and-work-partitioning` | Cheaper sequence backbones, kernel optimization, or partial updates to extend usable history length | Reducing the cost of long-history processing | Efficiency gains do not remove the need for stronger adaptive objectives or better context semantics | `icrl-method-004`, `icrl-systems-001` |
| LLM-style in-context RL and exploration | `llms-are-in-context-reinforcement-learners`, `reward-is-enough-llms-are-in-context-reinforcement-learners`, `can-large-language-models-explore-in-context`, `evolve-evaluating-and-optimizing-llms-for-exploration` | Use prompt context and reward feedback to adapt without weight updates | Exposing the overlap between language-model ICL and RL-style adaptation | Native exploration and negative-evidence handling remain unstable | `icrl-foundation-001`, `icrl-eval-003`, `icrl-eval-004` |
| Interface-robust and cross-domain adaptation | `in-context-reinforcement-learning-for-variable-action-spaces`, `in-context-reinforcement-learning-via-communicative-world-models`, `vintix-action-model-via-in-context-reinforcement-learning` | Learn action semantics or interface-agnostic context representations | Broadening adaptation beyond fixed action heads | Cross-interface robustness is still partial and setup-dependent | `icrl-method-005`, `icrl-systems-003` |
| Large-scale open-world and embodied adaptation | `human-timescale-adaptation-in-an-open-ended-task-space`, `omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds`, `xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations` | Combine scale, task diversity, long context, and richer deployment settings | Stress-testing adaptation in broader environments | Adaptation speed, memorization, and multimodal knowing-doing gaps remain serious | `icrl-systems-002`, `icrl-systems-005`, `icrl-eval-005` |

## Method-cluster reading

Evidence-backed:

- The map shows a field splitting into three coupled layers:
  - methods that establish adaptation exists,
  - methods that repair objectives or context handling,
  - systems that try to scale those behaviors to harder settings.

- The clusters are linked by recurring bottlenecks, not isolated islands:
  - objective mismatch,
  - context usability,
  - compute cost,
  - interface brittleness,
  - negative-evidence failure.

Forward-looking interpretation:

- The most plausible next-step architectures will likely need to combine one mechanism-facing hypothesis, one context-handling strategy, and one robustness-oriented evaluation stack. That sentence is an interpretation of the method map, not a claim directly extracted from a single note.
