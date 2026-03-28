# Contradictions

## Scope

This document summarizes unresolved tensions using only:

- `notes/claims/in-context-rl/contradictions.yaml`
- `notes/claims/in-context-rl/*.yaml`
- supporting note files already cited in the claim ledger

It does **not** attempt to resolve the tensions with new proposal prose.

## Evidence-backed tensions

### Tension 1: More diversity helps generalization, but can slow or destabilize adaptation

Tension statement:

- Larger task diversity improves coverage and asymptotic capability, yet the same local evidence shows that more diverse task pools can lengthen adaptation or expose failure on harder rulesets.

Support records:

- `icrl-systems-002`
- `icrl-eval-005`
- `icrl-contradiction-001`

Representative note support:

- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`
- `notes/papers/omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds.md`
- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`

Why unresolved:

- The local corpus does not yet specify when diversity improves the internal adaptation mechanism itself, as opposed to only broadening training coverage.

### Tension 2: Memory engineering helps, but does not prove online learning

Tension statement:

- Retrieval, filtering, and long context frequently improve behavior, but the local notes do not support treating those gains as proof that the model is updating beliefs in a genuinely learning-like way.

Support records:

- `icrl-method-003`
- `icrl-foundation-003`
- `icrl-contradiction-002`

Representative note support:

- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`

Why unresolved:

- The local evidence demonstrates usefulness of memory manipulation, but not a clean boundary between retrieval, compression, and genuine online inference.

### Tension 3: Supervised pretraining works surprisingly well, but objective mismatch remains

Tension statement:

- The local corpus shows that supervised pretraining can induce strong in-context behavior, while also showing that those same imitation-style objectives remain misaligned with offline RL and exploration-heavy regimes.

Support records:

- `icrl-foundation-001`
- `icrl-method-001`
- `icrl-method-002`
- `icrl-contradiction-003`

Representative note support:

- `notes/papers/supervised-pretraining-can-learn-in-context-reinforcement-learning.md`
- `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`

Why unresolved:

- The local evidence supports both sides: supervised pretraining is not a dead end, but neither is it a principled answer to value, uncertainty, or coverage problems.

## Boundary between evidence and interpretation

Evidence-backed:

- The three tensions above are directly traceable to contradiction records in the local claim ledger.

Interpretation:

- These tensions suggest that future work should prioritize conditional statements and falsifiable tests rather than sweeping claims such as “scale solves adaptation” or “memory solves learning.” This is an interpretive lesson drawn from the contradiction set, not a direct empirical result.
