# Title

**Toward Testable In-Context Reinforcement Learning: Explicit Algorithmic State, Experience Compilation, and Belief-Calibrated Adaptation under Shift**

# Abstract

Local evidence in this repository shows that in-context reinforcement learning (ICRL) is no longer a single-method phenomenon. Sequence-model distillation, supervised pretraining, large-scale meta-RL, and LLM-style prompting all exhibit forms of adaptation without test-time weight updates [@laskin2022ad; @lee2023dpt; @adaptive2023ada; @monea2024llms]. However, the same local corpus also exposes three persistent gaps. First, mechanistic work supports RL-like forward-pass computation, but does not identify a testable internal adaptive state [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp]. Second, context handling remains heuristic: filtering, retrieval, and long-context scaling help, but they do not yet validate how experience should be compressed, revised, or invalidated [@chen2025lhf; @schmied2024radt; @shi2023cec; @elawady2024relic]. Third, robustness under negative evidence, weak coverage, and distribution shift remains brittle [@krishnamurthy2024explore; @nie2024evolve; @dong2024sad; @tarasov2025qlearning].  

This proposal advances one coherent program rather than a benchmark collage. The central thesis is that ICRL should be treated as a problem of **testable algorithmic state**. Aim 1 identifies candidate state variables for adaptation. Aim 2 builds an **experience compilation** and adaptive-memory architecture around those variables. Aim 3 validates **belief-calibrated adaptation** under shift, with bounded multimodal and embodied extension only after earlier stages succeed. The expected outcome is not a claim of general adaptive intelligence, but a grounded path from black-box adaptive behavior to interpretable, falsifiable, and more robust ICRL.

# Introduction

The central promise of ICRL is appealing: an agent with fixed weights should improve during deployment by conditioning on interaction history rather than by performing expensive online gradient updates. Local notes already show that this promise is real across several families of methods. Algorithm Distillation (AD) demonstrated that a causal Transformer can distill a source RL algorithm and adapt within new tasks [@laskin2022ad]. Supervised pretraining then showed that in-context adaptation can also emerge from action-prediction objectives under suitable task families [@lee2023dpt; @lin2023decisionmakers]. At larger scale, AdA pushed black-box meta-RL to open-ended task spaces with human-timescale adaptation [@adaptive2023ada]. LLM-oriented work further showed that reward-conditioned or prompt-conditioned adaptation can appear even in language-model settings [@monea2024llms; @krishnamurthy2024explore].

Yet the local synthesis also makes clear that the field has moved faster on empirical existence than on scientific understanding. The strongest open issue is not whether adaptive behavior can appear, but what internal state makes it possible, how raw experience should be converted into that state, and whether such state improves robustness in closed-loop settings. That is why this proposal does not organize itself around a list of domains or backbones. It is organized around one causal thesis:

1. adaptive behavior depends on a small set of candidate internal state variables;
2. raw trajectories should be converted into revisable memory in terms of that state;
3. robustness under shift should be tested through explicit belief, uncertainty, and failure recovery.

This produces three aligned pillars:

1. **Aim 1:** identify candidate **algorithmic state** for in-context adaptation;
2. **Aim 2:** build **experience compilation** and adaptive memory around that state;
3. **Aim 3:** validate **belief-calibrated adaptation** under distribution shift.

# Literature Review and Research Gaps

## Adaptation exists, but the mechanism is still opaque

The local corpus supports that ICRL is empirically present across sequence-model, meta-RL, and LLM-based settings [@laskin2022ad; @lee2023dpt; @adaptive2023ada; @monea2024llms]. At the same time, mechanistic and theoretical work only partially explains what is happening inside the model. Local notes on provable supervised pretraining, TD-style forward-pass learning, sparse autoencoder analysis, and partial-MDP inference all point to RL-like internal computations, but not to a settled minimal state decomposition [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp]. The evidence therefore supports a mechanism gap, not a completed theory.

## Objective design is no longer secondary

The local method layer shows a clear shift away from assuming clean optimal supervision. DIT replaces optimal action labels with weighted pseudo-labels [@dong2024dit]. State-Action Distillation (SAD) demonstrates that even random-policy data can help under a trust-horizon regime [@dong2024sad]. Reward-prediction Decision Transformers and offline RL objectives further indicate that value- or reward-oriented targets can outperform pure action imitation [@mukherjee2024rewardpredictiondt; @tarasov2025qlearning]. These notes jointly suggest that objective mismatch is a primary bottleneck rather than a downstream tuning issue.

## Context handling is helpful, but still under-specified

Filtering, retrieval, and curriculum all help in the local corpus, but they do not settle what the right interface to history should be. LHF improves multiple ICRL backbones by selecting better learning histories [@chen2025lhf]. RA-DT shows retrieval gains but also leaves memory and learning confounded [@schmied2024radt]. Cross-Episodic Curriculum and several long-context systems papers address how context is organized or processed more efficiently [@shi2023cec; @elawady2024relic; @huang2024decisionmamba; @lu2023ssmrl; @beck2024xlstm; @dao2023flashattention2]. Still, the local evidence does not yet validate how history should be compressed, revised, or invalidated for decision making.

## Evaluation is exposing robustness failures faster than it is resolving them

The local evaluation stack remains dominated by bandits, grid worlds, DarkRoom-like tasks, and procedural benchmarks, even as embodied and multimodal tasks begin to stress the frontier [@laskin2022ad; @krishnamurthy2024explore; @tarasov2025qlearning; @elawady2024relic]. LMAct shows that long multimodal context does not reliably become competent action policy [@ruoss2024lmact]. LLM exploration notes repeatedly expose negative-evidence failures and prompt brittleness [@krishnamurthy2024explore; @nie2024evolve]. The local gaps therefore cluster around four unresolved questions:

1. what the internal adaptive state is;
2. how raw experience becomes usable memory;
3. how objectives should represent value, uncertainty, and negative evidence;
4. how to evaluate adaptation under shift without over-relying on scalar return alone.

# Specific Aims / Three Pillars

## Aim 1: Identify candidate algorithmic state for in-context adaptation

- **Scientific question:** Which candidate latent quantities causally support in-context adaptation, and can explicit state outperform a matched opaque latent?
- **Core hypothesis:** Explicit candidate state variables for value, uncertainty, task belief, and delayed credit will improve intervention fidelity, calibration, and regret under controlled shift relative to opaque history-conditioned state.
- **Why prior work is insufficient:** Local mechanistic and theoretical notes support RL-like forward-pass computation, but they do not establish a minimal or testable internal state; they mainly show existence rather than controllable mechanism [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp].
- **Approach sketch:** Use controlled synthetic and procedural tasks where reward timing, hidden task identity, and uncertainty can be perturbed. Train matched-capacity models with and without explicit candidate state heads. Evaluate counterfactual intervention fidelity, calibration, and regret under controlled shift.
- **Main risks:** Candidate state heads may mirror useful hidden structure without adding genuine explanatory value. One shared decomposition may also be too rigid.
- **Fallback plan:** Move to semi-structured latent models with only a subset of explicit heads, or use task-family-specific state templates instead of enforcing one universal decomposition.
- **Grounding:** notes: `transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining`, `transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning`, `sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models`, `learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration`; claims: `icrl-foundation-002`, `icrl-foundation-004`

## Aim 2: Build an experience-compiling adaptive memory architecture around explicit state

- **Scientific question:** Can raw trajectory history be compiled into a smaller, revisable memory state that preserves the information needed for adaptation better than raw-history conditioning?
- **Core hypothesis:** A context-compilation architecture that writes event-level memory in terms of candidate algorithmic state will outperform raw-history, filtering-only, and retrieval-only baselines at fixed context or compute budget.
- **Why prior work is insufficient:** Local notes show that filtering, retrieval, and curriculum help, but they do not validate how context should be compressed, revised, or invalidated. Existing gains are still confounded with memory exploitation rather than genuine adaptive inference [@chen2025lhf; @schmied2024radt; @shi2023cec; @krishnamurthy2024explore].
- **Approach sketch:** Build an architecture with event extraction, revisable memory, and a controller conditioned on compiled state. Compare against raw-history Transformers, LHF-style filtering, and RA-DT-style retrieval. Evaluate retention under compression, invalidation under rule changes, and downstream decision quality.
- **Main risks:** The compiler may learn shortcuts rather than decision-relevant abstraction, and revision logic may be unstable under changing tasks.
- **Fallback plan:** Introduce weak event supervision from sparse rewards or explicit rule changes. If revision remains unstable, fall back to read-only compressed memory and isolate whether compression alone already helps.
- **Grounding:** notes: `filtering-learning-histories-enhances-in-context-reinforcement-learning`, `retrieval-augmented-decision-transformer-external-memory-for-in-context-rl`, `cross-episodic-curriculum-for-transformer-agents`, `can-large-language-models-explore-in-context`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`, `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`; claims: `icrl-foundation-003`, `icrl-method-003`, `icrl-method-004`, `icrl-contradiction-002`

## Aim 3: Validate belief-calibrated adaptation under distribution shift

- **Scientific question:** Does combining explicit algorithmic state with compiled memory improve negative-evidence handling, calibration, and recovery under shift in a way that survives beyond toy tasks?
- **Core hypothesis:** A belief-calibrated decision layer on top of explicit state and compiled memory will reduce brittle exploration and improve recovery under coverage limits, rule changes, and bounded multimodal or embodied shifts.
- **Why prior work is insufficient:** The local corpus shows repeated failure under negative evidence, weak coverage, and OOD conditions, while also showing that richer deployment settings require more diversity, memory, and distillation [@krishnamurthy2024explore; @nie2024evolve; @dong2024sad; @tarasov2025qlearning; @ruoss2024lmact; @adaptive2023ada; @elawady2024relic].
- **Approach sketch:** Add conservative value and uncertainty outputs to the Aim 2 architecture and validate in three stages: offline and procedural-shift tasks, non-stationary interactive settings, and bounded multimodal or embodied tasks if earlier stages succeed. Measure return together with calibration, abstention-coverage tradeoffs, intervention sensitivity, and failure recovery.
- **Main risks:** Calibration objectives may reduce reward or collapse coverage. Bounded embodied validation may still depend on heavy infrastructure.
- **Fallback plan:** Keep calibration first as a diagnostic head in offline and procedural settings; deepen non-stationary stress tests if embodied extension remains too expensive.
- **Grounding:** notes: `can-large-language-models-explore-in-context`, `evolve-evaluating-and-optimizing-llms-for-exploration`, `random-policy-enables-in-context-reinforcement-learning-within-trust-horizons`, `yes-q-learning-helps-offline-in-context-rl`, `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`, `human-timescale-adaptation-in-an-open-ended-task-space`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`; claims: `icrl-eval-002`, `icrl-eval-003`, `icrl-eval-004`, `icrl-eval-005`, `icrl-systems-005`, `icrl-contradiction-001`, `icrl-contradiction-003`

# Methodology and System Design

The proposed system is organized as a three-layer research architecture.

1. **Explicit state estimation.** A history-conditioned model will expose candidate variables for value, uncertainty, task belief, and delayed credit, while preserving a free latent channel when needed.
2. **Experience compilation and revisable memory.** Raw trajectories will be converted into event-level memory updates that can be written, retrieved, and invalidated under task changes.
3. **Belief-calibrated decision layer.** Decision outputs will include conservative value, uncertainty, and optional abstention or delay signals under low confidence.

This design is grounded in the local corpus rather than assembled mechanically. The explicit-state layer is motivated by the mechanism gap [@lin2023decisionmakers; @wang2024td; @demircan2024sae]. The memory layer is motivated by the repeated failure of raw history and the partial success of filtering, retrieval, and curriculum [@chen2025lhf; @schmied2024radt; @shi2023cec]. The systems layer is motivated by long-context and deployment constraints shown in ReLIC, SSM/Mamba-style work, and LMAct [@elawady2024relic; @lu2023ssmrl; @huang2024decisionmamba; @ruoss2024lmact].

The design principle is strict dependence rather than feature accumulation. If Aim 1 fails to identify usable candidate state, Aim 2 falls back to semi-structured state rather than pretending the mechanism problem is solved. If Aim 2 fails to produce stable compilation, Aim 3 will still test calibrated uncertainty on simpler memory models rather than forcing a full pipeline.

# Evaluation Plan

The evaluation stack is staged to avoid overclaiming.

## Stage 1: Controlled mechanism tests

- Environments: synthetic and procedural tasks with editable reward delay, hidden task identity, and uncertainty.
- Baselines: AD-style history conditioning, supervised pretraining baselines, and matched opaque-latent models [@laskin2022ad; @lee2023dpt].
- Metrics: regret under shift, calibration error, and counterfactual intervention fidelity.

## Stage 2: Offline and non-stationary adaptation

- Environments: offline ICRL settings with variable coverage, trust-horizon limits, and rule changes.
- Baselines: DIT, SAD, LHF, RA-DT, and RL-objective offline ICRL [@dong2024dit; @dong2024sad; @chen2025lhf; @schmied2024radt; @tarasov2025qlearning].
- Metrics: return, regret, retention under compression, invalidation after shift, and failure recovery.

## Stage 3: Bounded multimodal or embodied extension

- Environments: LMAct-style long multimodal demonstrations and ReLIC- or AdA-inspired bounded embodied settings [@ruoss2024lmact; @elawady2024relic; @adaptive2023ada].
- Baselines: long-context architectures and context-only baselines, including SSM/Mamba/xLSTM or efficient-attention variants where relevant [@lu2023ssmrl; @huang2024decisionmamba; @beck2024xlstm; @dao2023flashattention2].
- Metrics: calibration, abstention-coverage tradeoff, adaptation lag, catastrophic failure rate, and sensitivity to negative evidence.

The evaluation principle is that success cannot be declared from scalar return alone. The proposal treats calibration, intervention sensitivity, and recovery under shift as first-class criteria because the local synthesis shows that these are current blind spots.

# Risks and Alternatives

## Risk 1: The state hypothesis may be too rigid

- **Issue:** The local corpus supports candidate latent quantities, not a universal minimal decomposition.
- **Alternative:** Use semi-structured latent state with a smaller number of explicit heads and treat decomposition as a family of hypotheses rather than a theorem.

## Risk 2: Context compilation may improve efficiency without improving real adaptation

- **Issue:** Retrieval and filtering gains can still be confounded with memory exploitation rather than learning.
- **Alternative:** Use retention and invalidation tests, and compare directly against simpler summarization baselines before claiming stronger adaptation.

## Risk 3: Bounded embodied validation may still be too expensive or too noisy

- **Issue:** Local embodied notes show substantial dependence on diversity, memory length, curriculum, and distillation.
- **Alternative:** Keep embodied and multimodal validation gated behind earlier milestones, and deepen non-stationary procedural evaluation if the systems budget becomes the limiting factor.

# Expected Outcomes

If successful, this research program will deliver:

1. a test bed for candidate **algorithmic state** in ICRL;
2. an **experience compilation** architecture with explicit retention and invalidation tests;
3. a staged protocol for **belief-calibrated adaptation** under distribution shift;
4. a more defensible link between mechanistic claims, architectural choices, and closed-loop validation.

The expected contribution is not a claim that the field has solved general adaptive intelligence. The expected contribution is a sharper and more falsifiable account of how to study adaptive behavior in fixed-weight models.

# Timeline

## Year 1

- reproduce note-backed baselines;
- formalize candidate state hypotheses;
- build intervention-friendly synthetic and procedural tasks.

## Year 2

- test explicit-state versus opaque-latent models;
- establish intervention, calibration, and regret benchmarks;
- begin context-compilation prototypes.

## Year 3

- build revisable memory and state-aware controllers;
- benchmark against filtering, retrieval, and offline objective-repair baselines;
- stage non-stationary evaluation.

## Year 4

- add bounded multimodal or embodied validation if earlier stages succeed;
- consolidate evaluation, risks, and failure analyses;
- translate the final program into full proposal and paper outputs.

# Bibliography

The shared bibliography for this bilingual draft is in [references.bib](/Users/xinjiezhang/in%20context%20RL/proposal/in-context-rl/references.bib). Cited local references:

- `laskin2022ad`: Michael Laskin et al. *In-Context Reinforcement Learning with Algorithm Distillation* (2022).
- `lee2023dpt`: Jonathan N. Lee et al. *Supervised Pretraining Can Learn In-Context Reinforcement Learning* (2023).
- `lin2023decisionmakers`: Licong Lin, Yu Bai, Song Mei. *Transformers as Decision Makers: Provable In-Context Reinforcement Learning via Supervised Pretraining* (2023).
- `wang2024td`: Jiuqi Wang et al. *Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning* (2024).
- `demircan2024sae`: Can Demircan et al. *Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models* (2024).
- `dong2024dit`: Juncheng Dong et al. *In-Context Reinforcement Learning Without Optimal Action Labels* (2024).
- `dong2024sad`: Weiqin Chen, Santiago Paternain. *Random Policy Enables In-Context Reinforcement Learning within Trust Horizons* (2024).
- `chen2025lhf`: Weiqin Chen et al. *Filtering Learning Histories Enhances In-Context Reinforcement Learning* (2025).
- `tarasov2025qlearning`: Denis Tarasov et al. *Yes, Q-learning Helps Offline In-Context RL* (2025).
- `schmied2024radt`: Thomas Schmied et al. *Retrieval-Augmented Decision Transformer: External Memory for In-Context RL* (2024).
- `ruoss2024lmact`: Anian Ruoss et al. *LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations* (2024).
- `krishnamurthy2024explore`: Akshay Krishnamurthy et al. *Can Large Language Models Explore In-Context?* (2024).
- `nie2024evolve`: Allen Nie et al. *EVOLvE: Evaluating and Optimizing LLMs For Exploration* (2024).
- `monea2024llms`: Giovanni Monea et al. *LLMs Are In-Context Reinforcement Learners* (2024).
- `adaptive2023ada`: Adaptive Agent Team et al. *Human-Timescale Adaptation in an Open-Ended Task Space* (2023).
- `elawady2024relic`: Ahmad Elawady et al. *ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI* (2024).
- `jiang2023partialmdp`: Chentian Jiang, Nan Rosemary Ke, Hado van Hasselt. *Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration* (2023).
- `mukherjee2024rewardpredictiondt`: Subhojyoti Mukherjee et al. *Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning* (2024).
- `lu2023ssmrl`: Chris Lu et al. *Structured State Space Models for In-Context Reinforcement Learning* (2023).
- `huang2024decisionmamba`: Sili Huang et al. *Decision Mamba: Reinforcement Learning via Hybrid Selective Sequence Modeling* (2024).
- `beck2024xlstm`: Maximilian Beck et al. *xLSTM: Extended Long Short-Term Memory* (2024).
- `dao2023flashattention2`: Tri Dao. *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning* (2023).
- `shi2023cec`: Lucy Xiaoyang Shi et al. *Cross-Episodic Curriculum for Transformer Agents* (2023).
