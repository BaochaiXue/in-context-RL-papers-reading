# Research Directions

## Scope

This document proposes speculative research directions grounded in:

- `./notes/papers/*.md`
- `./notes/tables/method_comparison.md`
- `./notes/tables/evidence_map.md`

Each direction is tied to explicit gaps from `research_gaps.md`.

## Direction 1: Explicit Algorithmic State for In-Context RL

### Evidence-backed premise

Local notes repeatedly suggest that sequence models are executing some latent RL computation, but none define or expose the required internal state cleanly.

Supporting notes:

- `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`
- `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`
- `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`
- `notes/papers/learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration.md`

Gaps addressed:

- `G1`, `G2`, `G3`

### Idea 1.1

- **Name:** Typed Algorithm-State Transformer
- **Core intuition:** Replace opaque hidden state with typed slots for value, uncertainty, task belief, and delayed credit so that “in-context learning” becomes a measurable internal process rather than an emergent black box.
- **Gap addressed:** `G1`, `G3`
- **Expected difficulty:** High
- **Possible experimental path:** Start on bandits and partial-MDP tasks; train with intervention losses that perturb reward timing, hidden task identity, and uncertainty; evaluate whether the typed slots predict action changes under counterfactual edits.
- **Supporting local note files:** `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`, `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`, `notes/papers/learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration.md`

### Idea 1.2

- **Name:** Counterfactual Credit Editing for ICRL
- **Core intuition:** If an ICRL agent really performs online credit assignment, then editing delayed rewards in a trajectory should induce predictable and localized changes in internal state and policy output.
- **Gap addressed:** `G1`, `G2`
- **Expected difficulty:** High
- **Possible experimental path:** Build synthetic environments where delayed rewards can be edited without changing dynamics; compare standard sequence models against a model trained with trajectory-edit consistency constraints.
- **Supporting local note files:** `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md`, `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`, `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`

### Idea 1.3

- **Name:** Memory-vs-Learning Disentanglement Suite
- **Core intuition:** Create tasks where retrieval helps but is provably insufficient unless the model also updates internal beliefs, thereby separating memory exploitation from genuine in-context adaptation.
- **Gap addressed:** `G2`
- **Expected difficulty:** Medium
- **Possible experimental path:** Design matched task families with identical retrieval opportunities but different hidden-task posteriors; compare DT/RA-DT-style retrieval systems against typed-state models.
- **Supporting local note files:** `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`, `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`, `notes/papers/a-survey-of-in-context-reinforcement-learning.md`

## Direction 2: Context Compilation and Event-Centric Memory

### Evidence-backed premise

The notes strongly indicate that raw histories are a poor interface. Better performance consistently comes from filtering, curriculum, retrieval, summarization, or structural compression.

Supporting notes:

- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`
- `notes/papers/cross-episodic-curriculum-for-transformer-agents.md`
- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`
- `notes/papers/can-large-language-models-explore-in-context.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`

Gaps addressed:

- `G2`, `G4`, `G9`

### Idea 2.1

- **Name:** Experience Compiler for Task-Sufficient Context
- **Core intuition:** Instead of feeding raw trajectories or raw demonstrations, learn a compiler that emits event tokens corresponding to task-relevant state changes, surprises, failures, and hypothesis revisions.
- **Gap addressed:** `G4`
- **Expected difficulty:** High
- **Possible experimental path:** Supervise compression using downstream regret rather than reconstruction loss; compare raw-history Transformers against compiler-based models on DarkRoom, XLand, and long multimodal demonstration tasks.
- **Supporting local note files:** `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`, `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`, `notes/papers/can-large-language-models-explore-in-context.md`

### Idea 2.2

- **Name:** Revision-Capable Episodic Memory for ICRL
- **Core intuition:** Current retrieval systems mainly fetch similar trajectories; they do not revise stale beliefs. Add explicit write, revise, and invalidate operations over retrieved memories.
- **Gap addressed:** `G2`, `G9`
- **Expected difficulty:** High
- **Possible experimental path:** Extend RA-DT-like pipelines with memory versioning and contradiction detection; test in non-stationary environments where old trajectories become misleading.
- **Supporting local note files:** `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`, `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md`, `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`

### Idea 2.3

- **Name:** Two-Timescale Sequence Backbone for Adaptive Memory
- **Core intuition:** Use a fast event-updating memory stream and a slower deliberative sequence model so the agent does not pay full Transformer cost for every token.
- **Gap addressed:** `G9`
- **Expected difficulty:** Medium
- **Possible experimental path:** Compare Mamba/SSM/xLSTM/attention hybrids on long-horizon adaptation tasks, holding context semantics fixed and varying only memory update granularity.
- **Supporting local note files:** `notes/papers/decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling.md`, `notes/papers/structured-state-space-models-for-in-context-reinforcement-learning.md`, `notes/papers/xlstm-extended-long-short-term-memory.md`, `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`

## Direction 3: Uncertainty-Aware and Negative-Evidence-Aware Adaptation

### Evidence-backed premise

Several notes converge on the same point: exploration collapses when the model cannot reason effectively about negative outcomes, insufficient coverage, or uncertainty.

Supporting notes:

- `notes/papers/can-large-language-models-explore-in-context.md`
- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md`
- `notes/papers/llms-are-in-context-reinforcement-learners.md`
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`

Gaps addressed:

- `G3`, `G5`, `G10`, `G11`

### Idea 3.1

- **Name:** Belief-Calibrated Conservative ICRL
- **Core intuition:** Merge conservative value learning with explicit epistemic belief tracking so the agent can separate “this action is bad” from “this action is unknown.”
- **Gap addressed:** `G3`, `G5`, `G10`
- **Expected difficulty:** High
- **Possible experimental path:** Start with offline ICRL settings from AD/CQL-style notes; add uncertainty-conditioned action selection and evaluate calibration, regret, and OOD recovery.
- **Supporting local note files:** `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`, `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`, `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`

### Idea 3.2

- **Name:** Negative-Episode Reasoning for LLM-Based ICRL
- **Core intuition:** Teach the model to preserve and reason over failed trials instead of filtering them out, so that failure becomes information rather than prompt noise.
- **Gap addressed:** `G3`, `G11`
- **Expected difficulty:** Medium
- **Possible experimental path:** Construct contextual-bandit and multi-step text environments with controlled negative feedback; compare positive-only prompting versus explicit failure-trace prompting and auxiliary loss variants.
- **Supporting local note files:** `notes/papers/llms-are-in-context-reinforcement-learners.md`, `notes/papers/can-large-language-models-explore-in-context.md`, `notes/papers/reward-is-enough-llms-are-in-context-reinforcement-learners.md`

### Idea 3.3

- **Name:** Adaptive Trust Horizon Learning
- **Core intuition:** Replace fixed trust horizons with learned trust horizons that expand or contract depending on uncertainty, reward delay, and task mismatch.
- **Gap addressed:** `G3`, `G5`
- **Expected difficulty:** Medium
- **Possible experimental path:** Begin with SAD-style random-policy distillation and delayed-reward tasks; learn a horizon controller and compare it to fixed trust-horizon baselines on both discrete and continuous settings.
- **Supporting local note files:** `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`, `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`, `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md`

## Direction 4: Interface-Robust Multimodal Generalist Adaptation

### Evidence-backed premise

Current notes show clear progress on generalist agents, variable action spaces, and multimodal prompts, but these capabilities remain fragmented and brittle.

Supporting notes:

- `notes/papers/in-context-reinforcement-learning-for-variable-action-spaces.md`
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`
- `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`
- `notes/papers/towards-general-purpose-in-context-learning-agents.md`

Gaps addressed:

- `G6`, `G7`, `G12`

### Idea 4.1

- **Name:** Action-Semantic Latent Interface Model
- **Core intuition:** Learn a latent action semantics layer that maps variable discrete actions, parameterized actions, and tool calls into a shared controllable representation.
- **Gap addressed:** `G6`, `G12`
- **Expected difficulty:** High
- **Possible experimental path:** Start from Headless-AD-style variable action spaces, then extend to cross-domain action-model settings such as Vintix; evaluate transfer under action vocabulary shift and reordered action sets.
- **Supporting local note files:** `notes/papers/in-context-reinforcement-learning-for-variable-action-spaces.md`, `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`, `notes/papers/towards-general-purpose-in-context-learning-agents.md`

### Idea 4.2

- **Name:** Demonstration-to-Affordance Distillation
- **Core intuition:** Convert long multimodal demonstrations into compact affordance states instead of treating them as raw imitation traces.
- **Gap addressed:** `G4`, `G6`, `G7`
- **Expected difficulty:** High
- **Possible experimental path:** Use LMAct-style tasks with paired text/image/state demonstrations; train a model to infer action-relevant affordances and compare against pure next-token imitation.
- **Supporting local note files:** `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`, `notes/papers/large-language-models-as-general-pattern-machines.md`, `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`

### Idea 4.3

- **Name:** Communicative Contextors for New Control Interfaces
- **Core intuition:** Use a frozen information agent to emit interface-neutral messages that bootstrap a fresh controller in an unseen action or observation space.
- **Gap addressed:** `G6`, `G12`
- **Expected difficulty:** Medium
- **Possible experimental path:** Extend CORAL-style communication to tasks where observation format and action vocabulary change jointly; measure zero-shot initialization gains and sample efficiency.
- **Supporting local note files:** `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`, `notes/papers/in-context-reinforcement-learning-for-variable-action-spaces.md`, `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md`

## Direction 5: OOD-, Safety-, and Embodiment-Centered Closed-Loop Evaluation

### Evidence-backed premise

The note corpus makes it clear that most current success claims live in a narrow region of the task-design space. A more serious evaluation stack is needed to surface brittle adaptation early.

Supporting notes:

- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`
- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`
- `notes/papers/omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds.md`
- `notes/papers/can-large-language-models-explore-in-context.md`

Gaps addressed:

- `G7`, `G8`, `G9`, `G10`

### Idea 5.1

- **Name:** Non-Stationary Adaptation Stress Suite
- **Core intuition:** Evaluate agents not just on held-out tasks, but on tasks that mutate mid-trial in reward logic, action semantics, or observability.
- **Gap addressed:** `G7`, `G10`
- **Expected difficulty:** Medium
- **Possible experimental path:** Build shift families on top of XLand/AnyMDP-style generators; compare adaptation lag, recovery rate, and calibration after rule changes.
- **Supporting local note files:** `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`, `notes/papers/omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds.md`, `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md`

### Idea 5.2

- **Name:** Abstention-Aware Embodied ICRL
- **Core intuition:** Let the agent explicitly decide when not to act or when to gather more evidence before acting in high-risk settings.
- **Gap addressed:** `G8`, `G10`
- **Expected difficulty:** High
- **Possible experimental path:** Add abstention or “ask for another trial” actions in ReLIC- and AdA-style embodied environments; evaluate safety-adjusted return, intervention frequency, and catastrophic error rate.
- **Supporting local note files:** `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`, `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`, `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md`

### Idea 5.3

- **Name:** Cultural and Multi-Agent Externalized Memory
- **Core intuition:** Move some adaptive state outside the individual agent and test whether explicit inter-agent memory transfer improves adaptation under sparse reward and partial observability.
- **Gap addressed:** `G2`, `G7`, `G12`
- **Expected difficulty:** Medium
- **Possible experimental path:** Combine cultural accumulation and communicative world-model ideas; compare independent learners, teacher-student transfer, and shared institutional memory under equal experience budgets.
- **Supporting local note files:** `notes/papers/artificial-generational-intelligence-cultural-accumulation-in-reinforcement-learning.md`, `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`, `notes/papers/towards-general-purpose-in-context-learning-agents.md`

## Boundary between evidence and proposal

Evidence-backed:

- Each direction is justified by recurrent note-level bottlenecks.

Speculative:

- The directions and ideas are proposals, not demonstrated facts.
- Their value depends on converting the note-backed gaps into executable experimental programs.
