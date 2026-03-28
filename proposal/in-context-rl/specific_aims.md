# Specific Aims

## Topic

`in-context-rl`

## Program title

**Testable Algorithmic State for Adaptive Agents**

## Program thesis

The local corpus supports that in-context adaptation is real, but it does not yet explain which internal state variables make adaptation work, how raw experience should be converted into that state, or whether such state improves closed-loop robustness under shift. The strongest agenda is therefore to move from black-box adaptive behavior to a testable algorithmic-state program.

Grounding:

- Claims: `icrl-foundation-001`, `icrl-foundation-002`, `icrl-foundation-003`, `icrl-foundation-004`, `icrl-method-003`, `icrl-eval-004`

## Specific Aim 1: Identify candidate algorithmic state for in-context adaptation

- **Scientific question:** Which candidate latent quantities causally support in-context adaptation, and can explicit state outperform a matched opaque latent?
- **Core hypothesis:** Explicit candidate state variables for value, uncertainty, task belief, and delayed credit will improve intervention fidelity, calibration, and regret under controlled shift relative to opaque history-conditioned state.
- **Why prior work is insufficient:** Local mechanistic and theoretical notes support RL-like forward-pass computation, but they do not establish a minimal or testable internal state; they mainly show existence rather than controllable mechanism.
- **Approach sketch:** Start with controlled synthetic and procedural tasks where reward timing, hidden task identity, and uncertainty can be perturbed. Train matched-capacity models with and without explicit candidate state heads. Compare them on counterfactual intervention fidelity, regret under shift, and calibration. This aim connects mechanism to architecture by making state explicit, and connects to closed-loop validation by testing whether state survives online perturbations.
- **Main risks:** Candidate state heads may mirror useful hidden structure without adding genuine explanatory power. The decomposition may also be too rigid across tasks, and the local evidence does not justify assuming one universal minimal state in advance.
- **Fallback plan:** Move to a semi-structured latent with only a subset of explicit heads and keep the requirement that those heads remain intervention-testable. If one shared decomposition is too rigid, evaluate task-family-specific state templates instead of forcing a universal one.
- **Supporting note files:** `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`, `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`, `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`, `notes/papers/learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration.md`, `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`
- **Supporting claim IDs:** `icrl-foundation-002`, `icrl-foundation-004`

## Specific Aim 2: Build a context-compiling adaptive memory architecture around explicit state

- **Scientific question:** Can raw trajectory history be compiled into a smaller, revisable memory state that preserves the information needed for adaptation better than raw-history conditioning?
- **Core hypothesis:** A context-compilation architecture that writes event-level memory in terms of candidate algorithmic state will outperform raw-history, filtering-only, and retrieval-only baselines at fixed context or compute budget.
- **Why prior work is insufficient:** Local notes show that filtering, retrieval, and curriculum help, but they do not validate how context should be compressed, revised, or invalidated. Existing gains are still confounded with memory exploitation rather than genuine adaptive inference.
- **Approach sketch:** Build an architecture with three parts: event extraction, revisable memory, and a controller conditioned on compiled state. Compare against raw-history Transformers, LHF-style filtering, and RA-DT-style retrieval. Evaluate retention under compression, invalidation under rule changes, and downstream decision quality. This aim connects mechanism to architecture by using state-aware memory writes, and connects to system validation through non-stationary memory-revision tests.
- **Main risks:** The compiler may simply learn dataset shortcuts, or revision logic may become unstable under changing tasks. The local evidence also does not justify assuming one universal context compiler that dominates every task family.
- **Fallback plan:** Introduce weak event supervision from task switches, sparse rewards, or explicit rule changes. If full revision is unstable, fall back to read-only compressed memory and isolate whether compression alone already improves adaptation.
- **Supporting note files:** `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`, `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`, `notes/papers/cross-episodic-curriculum-for-transformer-agents.md`, `notes/papers/can-large-language-models-explore-in-context.md`, `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`, `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- **Supporting claim IDs:** `icrl-foundation-003`, `icrl-method-003`, `icrl-method-004`, `icrl-contradiction-002`

## Specific Aim 3: Validate belief-calibrated adaptation under distribution shift

- **Scientific question:** Does combining explicit algorithmic state with compiled memory improve negative-evidence handling, calibration, and recovery under shift in a way that survives beyond toy tasks?
- **Core hypothesis:** A belief-calibrated decision layer on top of explicit state and compiled memory will reduce brittle exploration and improve recovery under coverage limits, rule changes, and bounded multimodal or embodied shifts.
- **Why prior work is insufficient:** The local corpus shows repeated failure under negative evidence, weak coverage, and OOD conditions, while also showing that richer deployment settings require more diversity, memory, and distillation. Existing evaluation still overweights scalar return and underweights calibration and abstention.
- **Approach sketch:** Add conservative value and uncertainty outputs to the Aim 2 architecture and validate in three stages: offline and procedural-shift tasks, non-stationary interactive settings, and bounded multimodal or embodied tasks if earlier stages succeed. Measure return alongside calibration, abstention-coverage tradeoffs, intervention sensitivity, and failure recovery. This aim links mechanism to architecture by forcing explicit uncertainty use, and links to closed-loop validation through staged shift testing.
- **Main risks:** Calibration objectives may harm reward or collapse coverage; bounded embodied validation may still depend on heavy infrastructure.
- **Fallback plan:** If abstention-aware action selection is unstable, keep calibration as a diagnostic head first and validate it in offline and procedural settings before bounded embodied extension. If embodied validation is too costly, deepen non-stationary procedural stress tests instead.
- **Supporting note files:** `notes/papers/can-large-language-models-explore-in-context.md`, `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`, `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`, `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`, `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`, `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`, `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- **Supporting claim IDs:** `icrl-eval-002`, `icrl-eval-003`, `icrl-eval-004`, `icrl-eval-005`, `icrl-systems-005`, `icrl-contradiction-001`, `icrl-contradiction-003`

## Why this program is not a mechanical A+B combination

The program is organized around one causal thesis:

1. identify the adaptive state,
2. build architecture around that state,
3. test whether that state supports robust closed-loop adaptation.

This makes the three aims mutually dependent rather than parallel themes.
