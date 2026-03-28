# Research Directions

## Scope

This document converts the local synthesis into candidate research agendas using only:

- `synthesis/in-context-rl/*.md`
- `notes/claims/in-context-rl/*.yaml`
- `notes/papers/*.md`
- `notes/tables/*.md`

It does **not** introduce new claims from raw PDFs.

## Design rule

The agenda must be sharper than a benchmark collage. Each candidate below is organized around a single causal thesis, not a loose bundle of papers.

## Candidate agendas

### Agenda A: Testable Algorithmic State for Adaptive Agents

Central thesis:

- The core blocker in ICRL is not merely scale or memory length, but the absence of a testable account of the internal adaptive state that drives behavior.

Mechanism focus:

- Make candidate latent quantities such as value, uncertainty, task belief, and delayed credit explicit and test whether they causally improve adaptation.

Methodology focus:

- Build explicit state heads plus a context-compilation architecture that writes and revises memory in terms of those candidate state variables.

Closed-loop validation focus:

- Evaluate whether explicit state and compiled memory improve recovery under negative evidence, distribution shift, and bounded embodied settings.

Why this is not mechanical stitching:

- The memory architecture is not added for its own sake; it is justified as the implementation consequence of a mechanism hypothesis.

Grounding:

- Claims: `icrl-foundation-002`, `icrl-foundation-003`, `icrl-foundation-004`, `icrl-method-003`, `icrl-eval-004`, `icrl-systems-005`
- Notes: `transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning`, `sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models`, `retrieval-augmented-decision-transformer-external-memory-for-in-context-rl`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`, `can-large-language-models-explore-in-context`

### Agenda B: Objective-Repair for Offline-to-Online Adaptation

Central thesis:

- The main reason current ICRL pipelines plateau is that they inherit action-imitation objectives that are misaligned with value estimation, coverage uncertainty, and exploration.

Mechanism focus:

- Study how value-oriented, reward-oriented, and trust-constrained targets change the latent adaptation behavior of the model.

Methodology focus:

- Build a unified offline-to-online objective family that combines relabeling, trust-horizon control, and conservative value learning.

Closed-loop validation focus:

- Test whether the repaired objectives improve OOD robustness, negative-evidence handling, and calibration under fixed-history versus no-history settings.

Why this is not mechanical stitching:

- The agenda is centered on one question: whether objective mismatch is the dominant causal bottleneck.

Grounding:

- Claims: `icrl-method-001`, `icrl-method-002`, `icrl-contradiction-003`, `icrl-eval-004`, `icrl-systems-004`
- Notes: `in-context-reinforcement-learning-without-optimal-action-labels`, `random-policy-enables-in-context-reinforcement-learning-within-trust-horizons`, `yes-q-learning-helps-offline-in-context-rl`, `pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning`

### Agenda C: Interface-Robust Multimodal Adaptive Control

Central thesis:

- What blocks broader generalization is not only memory or objectives, but the lack of interface-robust action semantics across variable action spaces, modalities, and control formats.

Mechanism focus:

- Learn a latent action-semantic layer that separates task adaptation from surface action vocabulary.

Methodology focus:

- Build interface-agnostic controllers using action-semantic embeddings, communicative contextors, and multimodal affordance summaries.

Closed-loop validation focus:

- Evaluate transfer across action-set shifts, multimodal demonstrations, and cross-domain control tasks.

Why this is not mechanical stitching:

- The connecting thesis is interface invariance, not just “multimodal plus variable action spaces.”

Grounding:

- Claims: `icrl-method-005`, `icrl-systems-003`, `icrl-systems-005`, `icrl-eval-003`
- Notes: `in-context-reinforcement-learning-for-variable-action-spaces`, `in-context-reinforcement-learning-via-communicative-world-models`, `vintix-action-model-via-in-context-reinforcement-learning`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`

### Agenda D: Scalable Context Systems under Shift

Central thesis:

- The decisive bottleneck for real deployment is whether adaptive memory systems can stay useful under long horizons, distribution shift, and compute constraints.

Mechanism focus:

- Characterize when memory revisions, retrieval, and long-context backbones are beneficial versus when they become shortcut systems.

Methodology focus:

- Develop a systems stack for retention, invalidation, and selective retrieval under fixed compute budgets.

Closed-loop validation focus:

- Stress-test under non-stationary task generators, long-context embodied rollouts, and compute-constrained settings.

Why this is not mechanical stitching:

- The central question is system reliability under shift, not just memory plus scaling.

Grounding:

- Claims: `icrl-method-003`, `icrl-method-004`, `icrl-systems-001`, `icrl-systems-002`, `icrl-contradiction-001`, `icrl-contradiction-002`
- Notes: `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`, `decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling`, `structured-state-space-models-for-in-context-reinforcement-learning`, `omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds`, `xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning`

## Selected agenda

### Chosen agenda: Agenda A — Testable Algorithmic State for Adaptive Agents

Why this is the strongest agenda:

1. It addresses the deepest mechanism gap in the local synthesis rather than optimizing around a symptom.
2. It gives a clean causal chain:
   - identify the latent adaptive state,
   - implement architecture around that state,
   - validate whether that state actually supports better closed-loop adaptation.
3. It subsumes the most important method and evaluation pressures without becoming a grab-bag:
   - context handling,
   - uncertainty,
   - shift robustness,
   - bounded embodied validation.

Why the other agendas are weaker:

- Agenda B is scientifically strong, but it risks becoming an objective-engineering program without resolving the deeper state question.
- Agenda C is high-value, but too dependent on interface and multimodal setup quality to be the best primary spine.
- Agenda D is useful and realistic, but it is closer to a systems agenda than a mechanism-driven research program.

## Agenda structure

The selected agenda is organized as a strict mechanism-to-system chain:

1. **Aim 1:** Identify candidate algorithmic state and test it causally.
2. **Aim 2:** Build a context-compiling adaptive memory architecture around that state.
3. **Aim 3:** Validate belief-calibrated adaptation under shift, with bounded multimodal or embodied extension.

This is sharper than A+B combination because each downstream component is justified by the causal burden of the previous one.
