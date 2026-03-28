# Research Gaps

## Scope

This document identifies deep gaps using only:

- `./notes/papers/*.md`
- `./notes/tables/method_comparison.md`
- `./notes/tables/evidence_map.md`

## Evidence-backed deep gaps

## Theory

### G1. The field lacks a formal notion of minimal in-context algorithmic state

Problem:

- Multiple notes claim that Transformers or LLMs implement RL-like computations in context, but none establish a shared definition of the internal state variables that make adaptation work.

Evidence:

- `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`
- `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`
- `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`
- `notes/papers/learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration.md`

Why it matters:

- Without a minimal state concept, mechanism claims remain descriptive rather than controllable.

### G2. Retrieval, memory, and genuine online learning are still confounded

Problem:

- Existing work cannot cleanly distinguish whether improved performance comes from real in-context learning or from copying useful fragments of prior experience.

Evidence:

- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- `notes/papers/a-survey-of-in-context-reinforcement-learning.md`

Why it matters:

- This blocks strong claims about “learning algorithms in forward pass” in realistic environments.

### G3. Uncertainty and negative evidence are under-theorized

Problem:

- Local notes repeatedly show failure on negative episodes, trust horizons, and exploration tradeoffs, but there is no unified theory of how uncertainty should be represented and updated in context.

Evidence:

- `notes/papers/llms-are-in-context-reinforcement-learners.md`
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`
- `notes/papers/can-large-language-models-explore-in-context.md`
- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`

Why it matters:

- Exploration remains brittle because the model often cannot reason properly about what it does not know.

## Methodology

### G4. The field still lacks a principled context compiler

Problem:

- Most systems still operate on raw trajectories, lightly filtered trajectories, or retrieved sub-trajectories, rather than learning an explicit sufficient summary of interaction history.

Evidence:

- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/cross-episodic-curriculum-for-transformer-agents.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`

Why it matters:

- Long contexts help only if the right information is kept and the wrong information is discarded.

### G5. Objective mismatch remains unresolved

Problem:

- A large fraction of the field still inherits action imitation objectives from sequence modeling even when the true bottleneck is value estimation, exploration, or uncertainty calibration.

Evidence:

- `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`
- `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`
- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`
- `notes/papers/pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning.md`

Why it matters:

- Better sequence modeling does not automatically imply better adaptive decision making.

### G6. Variable interfaces and action semantics remain weakly modeled

Problem:

- Most methods assume fixed action structure, fixed observation semantics, or fixed control interfaces.

Evidence:

- `notes/papers/in-context-reinforcement-learning-for-variable-action-spaces.md`
- `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`
- `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`

Why it matters:

- Without interface-robust representations, claims of generalist adaptation remain narrow.

## Evaluation

### G7. Evaluation is still dominated by toy or structurally narrow settings

Problem:

- The local note set is rich in bandits, DarkRoom-style tasks, and stylized procedural worlds. These settings are useful, but they leave a wide gap to embodied or irreversible decision making.

Evidence:

- `notes/papers/a-survey-of-in-context-reinforcement-learning.md`
- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`

Why it matters:

- Methods can look adaptive in toy settings while still failing in real closed-loop regimes.

### G8. Return is overused as the main metric

Problem:

- Most notes emphasize reward, regret, NAUC, or success rate. Much less attention is paid to adaptation speed, calibration, intervention sensitivity, recovery after belief collapse, or abstention under uncertainty.

Evidence:

- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`
- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`
- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`

Why it matters:

- A method can have acceptable average return while still being unusable in deployment because it is slow, overconfident, or brittle.

## Systems

### G9. Long-context adaptation is still too expensive in practice

Problem:

- Notes on ReLIC, Decision Mamba, Structured SSM, xLSTM, and FlashAttention-2 all show that the field is still fighting the cost of long history processing.

Evidence:

- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling.md`
- `notes/papers/structured-state-space-models-for-in-context-reinforcement-learning.md`
- `notes/papers/xlstm-extended-long-short-term-memory.md`
- `notes/papers/flashattention-2-faster-attention-with-better-parallelism-and-work-partitioning.md`

Why it matters:

- If adaptation only works with extremely expensive memory pipelines, it will not scale to rich embodied systems.

### G10. Safe adaptation and abstention are largely missing

Problem:

- Many local notes describe OOD or sparse-reward settings, but almost none treat irreversible actions, deployment-time self-doubt, or explicit abstention as first-class design goals.

Evidence:

- `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md`
- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/can-large-language-models-explore-in-context.md`

Why it matters:

- Adaptive agents will fail in realistic environments if they cannot recognize unsafe uncertainty.

## Data / supervision

### G11. Strong-teacher dependence has not really gone away

Problem:

- Even the papers that weaken supervision often still depend on a useful demonstrator, a curriculum, or a carefully chosen data-generation process.

Evidence:

- `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`
- `notes/papers/supervised-pretraining-can-learn-in-context-reinforcement-learning.md`
- `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`
- `notes/papers/pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning.md`
- `notes/papers/training-a-generally-curious-agent.md`

Why it matters:

- The field still lacks a general recipe for building adaptive behavior from weak, diverse, messy experience.

### G12. Existing datasets still underspecify domain and interface diversity

Problem:

- Even large datasets such as XLand-100B retain shared observation/action structures and latent biases.

Evidence:

- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`
- `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`
- `notes/papers/towards-general-purpose-in-context-learning-agents.md`

Why it matters:

- This makes it hard to know whether a model learned a general adaptation mechanism or just a narrow family of interface-specific shortcuts.

## Boundary between evidence and proposal

Evidence-backed:

- The twelve gaps above are directly grounded in the local note corpus.

Speculative implication:

- Taken together, these gaps suggest that the next useful ICRL systems will need explicit internal state, better context compilation, uncertainty-aware adaptation, and more adversarial evaluation.
