# Research Gaps

## Scope

This gap analysis uses only:

- `notes/papers/*.md`
- `notes/claims/in-context-rl/*.yaml`
- `notes/tables/method_comparison.md`
- `notes/tables/evidence_map.md`
- `notes/tables/note_coverage.md`

No gap below is introduced without support from local claims or notes.

## Evidence-backed deep gaps

## Theory

### G1. There is still no testable notion of algorithmic state for ICRL

Problem:

- The local corpus supports the existence of RL-like forward-pass computations, but not a shared, testable account of which latent quantities are necessary for adaptation.

Support claims:

- `icrl-foundation-002`
- `icrl-foundation-004`

Representative note support:

- `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`
- `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`
- `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`

Why it matters:

- Without an explicit state hypothesis, mechanism claims remain descriptive rather than controllable.

### G2. Memory gains and genuine online learning are still confounded

Problem:

- The local notes repeatedly show that retrieval or long demonstrations can help, but they do not establish when those gains reflect true in-context learning rather than memory exploitation.

Support claims:

- `icrl-foundation-003`
- `icrl-contradiction-002`

Representative note support:

- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- `notes/papers/a-survey-of-in-context-reinforcement-learning.md`

Why it matters:

- This blocks stronger causal claims about “learning algorithms in the forward pass.”

## Methodology

### G3. Objective mismatch is unresolved

Problem:

- Strong in-context behavior can emerge from supervised pretraining, but several local notes also show that pure imitation remains poorly aligned with offline RL, uncertainty, and exploration bottlenecks.

Support claims:

- `icrl-method-001`
- `icrl-method-002`
- `icrl-contradiction-003`

Representative note support:

- `notes/papers/supervised-pretraining-can-learn-in-context-reinforcement-learning.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`

Why it matters:

- Better sequence modeling does not guarantee better adaptive decision making.

### G4. The field still lacks a validated mechanism for compressing, revising, and invalidating context

Problem:

- Local notes support the usefulness of filtering, retrieval, and curriculum, but not a validated account of how history should be turned into a compact, revisable decision state.

Support claims:

- `icrl-method-003`
- `icrl-method-004`

Representative note support:

- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/cross-episodic-curriculum-for-transformer-agents.md`
- `notes/papers/can-large-language-models-explore-in-context.md`

Why it matters:

- Context usefulness, not just context length, is becoming the practical bottleneck.

Boundary note:

- The stronger claim that one universal compiler should dominate all settings remains weak and is therefore not used here as evidence.

### G5. Interface-robust action modeling remains underdeveloped

Problem:

- Variable action spaces, cross-domain action transfer, and communicative/world-model approaches all indicate that fixed action heads are too narrow for broader adaptation.

Support claims:

- `icrl-method-005`
- `icrl-systems-003`

Representative note support:

- `notes/papers/in-context-reinforcement-learning-for-variable-action-spaces.md`
- `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`
- `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`

Why it matters:

- Interface brittleness limits any claim of general adaptive competence.

## Evaluation

### G6. The benchmark mix is still structurally narrow

Problem:

- Much of the local evaluation stack is still concentrated in bandits, grid worlds, DarkRoom-like tasks, and procedural environments, with fewer irreversible or high-risk decision settings.

Support claims:

- `icrl-eval-001`

Representative note support:

- `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`
- `notes/papers/can-large-language-models-explore-in-context.md`
- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`

Why it matters:

- Adaptive competence can look strong in stylized regimes while still failing in richer closed-loop settings.

### G7. Evaluation overuses scalar return-style metrics

Problem:

- Calibration, abstention, intervention sensitivity, and recovery after shift are still far less common than return, regret, and success rate.

Support claims:

- `icrl-eval-002`

Representative note support:

- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`
- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`

Why it matters:

- A method can score well on average return while still being overconfident or unsafe.

### G8. Negative evidence and OOD failure are still first-order weaknesses

Problem:

- The local corpus repeatedly identifies failure under negative episodes, poor coverage, and shifted dynamics, but these remain more observed than solved.

Support claims:

- `icrl-eval-004`

Representative note support:

- `notes/papers/can-large-language-models-explore-in-context.md`
- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`

Why it matters:

- This is where deployment-facing brittleness is most visible today.

## Systems and data

### G9. Long-context adaptation remains too expensive and too delicate

Problem:

- Local systems papers repeatedly optimize memory cost, partial updates, or efficient attention, which indicates that long-context adaptation is still far from a solved infrastructure problem.

Support claims:

- `icrl-systems-001`

Representative note support:

- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling.md`
- `notes/papers/structured-state-space-models-for-in-context-reinforcement-learning.md`
- `notes/papers/xlstm-extended-long-short-term-memory.md`

Why it matters:

- If adaptation only works with very heavy memory pipelines, it will remain difficult to deploy broadly.

### G10. Scale and diversity create a tradeoff rather than a clean solution

Problem:

- Larger task pools and datasets improve asymptotic coverage, but they also lengthen adaptation or expose new generalization limits.

Support claims:

- `icrl-systems-002`
- `icrl-eval-005`
- `icrl-contradiction-001`

Representative note support:

- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`
- `notes/papers/omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds.md`
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`

Why it matters:

- “Use more tasks” is not a sufficient recipe; the adaptation-speed penalty itself becomes part of the problem.

### G11. Strong-teacher or curated-generator dependence persists

Problem:

- Even papers that weaken supervision still often depend on a useful demonstrator, a strong generator, or careful curriculum design.

Support claims:

- `icrl-systems-004`

Representative note support:

- `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`
- `notes/papers/supervised-pretraining-can-learn-in-context-reinforcement-learning.md`
- `notes/papers/pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning.md`
- `notes/papers/training-a-generally-curious-agent.md`

Why it matters:

- The field still lacks a general recipe for building adaptive behavior from weak, messy experience alone.

### G12. Multimodal and embodied deployment remains fragile

Problem:

- The local frontier notes show that embodied and multimodal deployment still relies on carefully engineered long-context recipes, distillation, or curriculum.

Support claims:

- `icrl-systems-005`
- `icrl-eval-003`

Representative note support:

- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`

Why it matters:

- The most realistic settings are currently the least stable ones.

## Forward-looking interpretation

The evidence-backed gaps above suggest that the next high-leverage work will likely focus on explicit internal state, stronger context construction, uncertainty-aware adaptation, and more adversarial evaluation. That sentence is an interpretation of the gap set rather than a direct claim from any single local note.
