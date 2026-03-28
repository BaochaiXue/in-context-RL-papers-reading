# Title / 标题

**Toward Testable In-Context Reinforcement Learning: Explicit Algorithmic State, Experience Compilation, and Belief-Calibrated Adaptation under Shift**

# Abstract / 摘要

这个仓库中的本地证据表明，in-context reinforcement learning（ICRL）已经不再是单一方法下的现象。Sequence-model distillation、supervised pretraining、大规模 meta-RL，以及 LLM-style prompting 都已经展示了在不进行 test-time weight updates 的情况下出现某种形式的 adaptation [@laskin2022ad; @lee2023dpt; @adaptive2023ada; @monea2024llms]。但是，同一批本地文献也暴露了三个持续存在的 gap。第一，mechanistic work 支持 RL-like 的 forward-pass computation，但并没有识别出一个可测试的 internal adaptive state [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp]。第二，context handling 仍然主要是 heuristic：filtering、retrieval 和 long-context scaling 虽然有帮助，但并没有验证 experience 应该如何被压缩、修订或失效化 [@chen2025lhf; @schmied2024radt; @shi2023cec; @elawady2024relic]。第三，在 negative evidence、弱 coverage 和 distribution shift 下，robustness 仍然很脆弱 [@krishnamurthy2024explore; @nie2024evolve; @dong2024sad; @tarasov2025qlearning]。  

因此，这份 proposal 推进的是一个 coherent research program，而不是 benchmark collage。核心 thesis 是：ICRL 应该被视为一个 **testable algorithmic state** 问题。Aim 1 识别 adaptation 所依赖的 candidate state variables。Aim 2 围绕这些变量构建 **experience compilation** 与 adaptive-memory architecture。Aim 3 在 distribution shift 下验证 **belief-calibrated adaptation**，并且只在前两阶段成功后才进入 bounded multimodal 和 embodied extension。预期贡献并不是声称已经达到 general adaptive intelligence，而是为从 black-box adaptive behavior 走向 interpretable、falsifiable、且更 robust 的 ICRL 建立一条 grounded path。

**当前 build 对齐说明。** 这个仓库中的实现**并没有**实现完整的三大 aims。当前可执行 slice 是一个受控的 hidden-task bandit proxy，它覆盖的是 Aim 1，以及 Aim 3 中一个很窄的 calibration-oriented 子集。它**尚未**实现 Aim 2 中描述的 `experience compilation` 或 revisable-memory 组件，而且当前 comparator 只是一个 sanity baseline，而不是 matched-capacity 的 opaque-history model。

# Introduction / 引言

ICRL 的核心承诺很直接：一个固定参数的 agent 应该能够在部署过程中通过 conditioning on interaction history 来改进，而不需要进行昂贵的 online gradient updates。本地 notes 已经表明，这个承诺在多个方法族里都是真实存在的。Algorithm Distillation（AD）证明了 causal Transformer 可以蒸馏 source RL algorithm，并在新任务中进行 in-context adaptation [@laskin2022ad]。随后，supervised pretraining 也表明，在合适的 task families 下，action-prediction objectives 同样能够诱导出 in-context adaptation [@lee2023dpt; @lin2023decisionmakers]。在更大尺度上，AdA 把 black-box meta-RL 推到了 open-ended task spaces，并展示了 human-timescale adaptation [@adaptive2023ada]。LLM-oriented 工作则进一步表明，reward-conditioned 或 prompt-conditioned adaptation 甚至可以出现在 language-model settings 中 [@monea2024llms; @krishnamurthy2024explore]。

但是，本地 synthesis 也同样清楚地表明，领域在 empirical existence 上走得比在 scientific understanding 上更快。最强的 open issue 已经不是 adaptive behavior 能否出现，而是：什么样的 internal state 让这种 adaptation 成为可能，raw experience 应该如何被转换成该 state，以及这种 state 是否真的能在 closed-loop settings 里提升 robustness。这也是为什么本 proposal 不是围绕一串 domains 或 backbones 来组织，而是围绕一个 causal thesis 来组织：

1. adaptive behavior 依赖一组 candidate internal state variables；
2. raw trajectories 应该被转换成用这些 state 表达的 revisable memory；
3. robustness under shift 应该通过 explicit belief、uncertainty 与 failure recovery 来检验。

这对应三个对齐的 pillars：

1. **Aim 1:** 识别 in-context adaptation 的 candidate **algorithmic state**；
2. **Aim 2:** 围绕该 state 构建 **experience compilation** 与 adaptive memory；
3. **Aim 3:** 在 distribution shift 下验证 **belief-calibrated adaptation**。

# Literature Review and Research Gaps / 文献综述与研究空白

## Adaptation exists, but the mechanism is still opaque / adaptation 已经存在，但 mechanism 仍然不透明

本地 corpus 支持这样一个判断：ICRL 在 sequence-model、meta-RL 与 LLM-based settings 中都已经经验性成立 [@laskin2022ad; @lee2023dpt; @adaptive2023ada; @monea2024llms]。与此同时，mechanistic 与 theoretical work 只部分解释了模型内部到底发生了什么。本地 notes 中关于 provable supervised pretraining、TD-style forward-pass learning、sparse autoencoder analysis 以及 partial-MDP inference 的工作，都指向了 RL-like internal computations，但并没有支持一个 settled minimal state decomposition [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp]。因此，当前证据支持的是一个 mechanism gap，而不是一套已经完成的 theory。

## Objective design is no longer secondary / objective design 已经不再是次要问题

本地 method layer 明确显示出一个转向：不再假设总有干净的 optimal supervision。DIT 用 weighted pseudo-labels 替代 optimal action labels [@dong2024dit]。State-Action Distillation（SAD）表明，即便是 random-policy data，在 trust-horizon 约束下也可能有用 [@dong2024sad]。Reward-prediction Decision Transformers 和 offline RL objectives 则进一步表明，value-oriented 或 reward-oriented targets 可以超越 pure action imitation [@mukherjee2024rewardpredictiondt; @tarasov2025qlearning]。这些 notes 共同表明，objective mismatch 是 primary bottleneck，而不是末端调参问题。

## Context handling is helpful, but still under-specified / context handling 有帮助，但仍未被充分定义

Filtering、retrieval 和 curriculum 在本地 corpus 中确实都有帮助，但它们并没有真正回答“history 的正确接口到底是什么”。LHF 通过选择更好的 learning histories 提升了多个 ICRL backbones [@chen2025lhf]。RA-DT 展示了 retrieval gains，但同时也让 memory 与 learning 的界限保持模糊 [@schmied2024radt]。Cross-Episodic Curriculum 以及若干 long-context systems paper 则分别从 context ordering 或更高效的 processing 入手 [@shi2023cec; @elawady2024relic; @huang2024decisionmamba; @lu2023ssmrl; @beck2024xlstm; @dao2023flashattention2]。然而，本地证据仍未验证 history 应该如何被压缩、修订与失效化，才能真正服务 decision making。

## Evaluation is exposing robustness failures faster than it is resolving them / evaluation 暴露 robustness failure 的速度，快于解决它们的速度

本地 evaluation stack 仍然主要集中在 bandits、grid worlds、DarkRoom-like tasks 和 procedural benchmarks 上，尽管 embodied 与 multimodal 任务已经开始对 frontier 形成压力 [@laskin2022ad; @krishnamurthy2024explore; @tarasov2025qlearning; @elawady2024relic]。LMAct 表明，long multimodal context 并不会稳定地转化为 competent action policy [@ruoss2024lmact]。LLM exploration 相关 notes 也反复暴露出 negative-evidence failure 与 prompt brittleness [@krishnamurthy2024explore; @nie2024evolve]。因此，本地 gaps 可以被压缩为四个问题：

1. internal adaptive state 到底是什么；
2. raw experience 如何变成 usable memory；
3. objective 应如何表示 value、uncertainty 与 negative evidence；
4. 在不过度依赖 scalar return 的前提下，adaptation under shift 应如何被评估。

# Specific Aims / Three Pillars / 具体目标 / 三大主线

## Aim 1: Identify candidate algorithmic state for in-context adaptation / 识别 in-context adaptation 的 candidate algorithmic state

- **Scientific question:** 哪些 candidate latent quantities 会因果性地支撑 in-context adaptation？显式 state 是否能优于一个 matched 的 opaque latent？
- **Core hypothesis:** 针对 value、uncertainty、task belief 和 delayed credit 的显式 candidate state variables，相比 opaque history-conditioned state，将在 controlled shift 下提升 intervention fidelity、calibration 与 regret。
- **Why prior work is insufficient:** 本地 mechanistic 与 theoretical notes 支持 RL-like 的 forward-pass computation，但并没有建立一个 minimal 或 testable 的 internal state；它们主要证明的是 existence，而不是 controllable mechanism [@lin2023decisionmakers; @wang2024td; @demircan2024sae; @jiang2023partialmdp]。
- **Approach sketch:** 使用可控的 synthetic 与 procedural tasks，在其中直接扰动 reward timing、hidden task identity 和 uncertainty。训练 matched-capacity 的 models，对比“有显式 candidate state heads”和“没有显式 heads”的版本。核心比较指标是 counterfactual intervention fidelity、regret under shift 与 calibration。
- **Main risks:** candidate state heads 可能只是镜像了一个有用的 hidden structure，却没有提供真正的解释增益。一个 shared decomposition 也可能跨 task 过于僵硬。
- **Fallback plan:** 转向 semi-structured latent models，仅保留一部分 explicit heads，或者采用 task-family-specific 的 state templates，而不是强行要求 universal decomposition。
- **Grounding:** notes: `transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining`, `transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning`, `sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models`, `learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration`; claims: `icrl-foundation-002`, `icrl-foundation-004`

## Aim 2: Build an experience-compiling adaptive memory architecture around explicit state / 围绕 explicit state 构建 experience-compiling adaptive memory architecture

- **Scientific question:** raw trajectory history 能否被编译成更小、可修订的 memory state，并且在 fixed context 或 compute budget 下比 raw-history conditioning 更好地保留 adaptation 所需信息？
- **Core hypothesis:** 一个用 candidate algorithmic state 来写入 event-level memory 的 context-compilation architecture，将在固定 context 或 compute budget 下优于 raw-history、filtering-only 和 retrieval-only baselines。
- **Why prior work is insufficient:** 本地 notes 表明 filtering、retrieval 和 curriculum 确实有帮助，但并没有验证 context 应如何被压缩、修订和失效化。现有 gains 仍与 memory exploitation 混杂，而不是已经证明了 genuine adaptive inference [@chen2025lhf; @schmied2024radt; @shi2023cec; @krishnamurthy2024explore]。
- **Approach sketch:** 构建一个包含 event extraction、revisable memory 和 controller conditioned on compiled state 的 architecture。与 raw-history Transformers、LHF-style filtering 和 RA-DT-style retrieval 对比。核心评估 retention under compression、invalidation under rule changes 以及 downstream decision quality。
- **Main risks:** compiler 可能学到的是 dataset shortcuts，而不是 decision-relevant abstraction；revision logic 在 task change 下也可能不稳定。本地证据同样不支持一开始就假设存在一个 universal context compiler。
- **Fallback plan:** 引入来自 task switches、sparse rewards 或 explicit rule changes 的 weak event supervision。如果 revision 仍不稳定，则退回到 read-only compressed memory，并单独判断 compression 本身是否已经能提升 adaptation。
- **Grounding:** notes: `filtering-learning-histories-enhances-in-context-reinforcement-learning`, `retrieval-augmented-decision-transformer-external-memory-for-in-context-rl`, `cross-episodic-curriculum-for-transformer-agents`, `can-large-language-models-explore-in-context`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`, `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`; claims: `icrl-foundation-003`, `icrl-method-003`, `icrl-method-004`, `icrl-contradiction-002`

## Aim 3: Validate belief-calibrated adaptation under distribution shift / 在 distribution shift 下验证 belief-calibrated adaptation

- **Scientific question:** explicit algorithmic state 与 compiled memory 的组合，是否能在 beyond toy tasks 的 setting 下，提升对 negative evidence 的处理、calibration 以及 shift 后的 recovery？
- **Core hypothesis:** 在 explicit state 和 compiled memory 之上添加 belief-calibrated decision layer，将减少 brittle exploration，并在 coverage limits、rule changes 和 bounded multimodal / embodied shifts 下提升 recovery。
- **Why prior work is insufficient:** 本地 corpus 反复显示 negative evidence、弱 coverage 与 OOD conditions 下的 failure；与此同时，richer deployment settings 又要求更多 diversity、memory 与 distillation [@krishnamurthy2024explore; @nie2024evolve; @dong2024sad; @tarasov2025qlearning; @ruoss2024lmact; @adaptive2023ada; @elawady2024relic]。
- **Approach sketch:** 在 Aim 2 architecture 上增加 conservative value 与 uncertainty outputs，并分三个阶段验证：offline 与 procedural-shift tasks、non-stationary interactive settings，以及在前两阶段成功后才进入 bounded multimodal 或 embodied tasks。核心指标包括 return、calibration、abstention-coverage tradeoff、intervention sensitivity 与 failure recovery。
- **Main risks:** calibration objectives 可能降低 reward 或使 coverage 崩塌；bounded embodied validation 仍可能依赖很重的 infrastructure。
- **Fallback plan:** 先把 calibration 保持为 diagnostic head，并在 offline 与 procedural settings 中验证；如果 embodied extension 成本仍然过高，则优先加深 non-stationary procedural stress tests。
- **Grounding:** notes: `can-large-language-models-explore-in-context`, `evolve-evaluating-and-optimizing-llms-for-exploration`, `random-policy-enables-in-context-reinforcement-learning-within-trust-horizons`, `yes-q-learning-helps-offline-in-context-rl`, `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`, `human-timescale-adaptation-in-an-open-ended-task-space`, `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`; claims: `icrl-eval-002`, `icrl-eval-003`, `icrl-eval-004`, `icrl-eval-005`, `icrl-systems-005`, `icrl-contradiction-001`, `icrl-contradiction-003`

# Methodology and System Design / 方法论与系统设计

拟议系统按三层 research architecture 组织：

1. **Explicit state estimation。** 一个 history-conditioned model 将显式暴露 value、uncertainty、task belief 与 delayed credit 的 candidate variables，同时在需要时保留 free latent channel。
2. **Experience compilation and revisable memory。** Raw trajectories 将被转换成 event-level memory updates，并能够在 task change 下执行 write、retrieve 与 invalidate。
3. **Belief-calibrated decision layer。** Decision outputs 将包含 conservative value、uncertainty，以及在低 confidence 下的可选 abstention 或 delay signals。

这个设计不是机械拼接，而是直接由本地 corpus 推导出来。Explicit-state layer 来源于 mechanism gap [@lin2023decisionmakers; @wang2024td; @demircan2024sae]。Memory layer 来源于 raw history 反复失效，而 filtering、retrieval 与 curriculum 只提供了部分补救 [@chen2025lhf; @schmied2024radt; @shi2023cec]。Systems layer 来源于 ReLIC、SSM/Mamba-style work 和 LMAct 所揭示的 long-context 与 deployment constraints [@elawady2024relic; @lu2023ssmrl; @huang2024decisionmamba; @ruoss2024lmact]。

核心 design principle 是 strict dependence，而不是 feature accumulation。如果 Aim 1 无法识别出可用的 candidate state，那么 Aim 2 就应退回 semi-structured state，而不是假装 mechanism problem 已经解决。如果 Aim 2 无法产生稳定 compilation，那么 Aim 3 也应该先在更简单的 memory model 上测试 calibrated uncertainty，而不是强推完整 pipeline。

# Evaluation Plan / 评估方案

evaluation stack 将分阶段进行，以避免 overclaiming。

## Stage 1: Controlled mechanism tests / 受控 mechanism 测试

- Environments：可编辑 reward delay、hidden task identity 和 uncertainty 的 synthetic / procedural tasks。
- Baselines：AD-style history conditioning、supervised pretraining baselines，以及 matched opaque-latent models [@laskin2022ad; @lee2023dpt]。
- Metrics：regret under shift、calibration error 与 counterfactual intervention fidelity。

## Stage 2: Offline and non-stationary adaptation / offline 与 non-stationary adaptation

- Environments：具有 variable coverage、trust-horizon limits 与 rule changes 的 offline ICRL settings。
- Baselines：DIT、SAD、LHF、RA-DT 以及 RL-objective offline ICRL [@dong2024dit; @dong2024sad; @chen2025lhf; @schmied2024radt; @tarasov2025qlearning]。
- Metrics：return、regret、retention under compression、invalidation after shift 与 failure recovery。

## Stage 3: Bounded multimodal or embodied extension / 有界的 multimodal 或 embodied 扩展

- Environments：LMAct-style 的 long multimodal demonstrations，以及 ReLIC / AdA-inspired 的 bounded embodied settings [@ruoss2024lmact; @elawady2024relic; @adaptive2023ada]。
- Baselines：relevant 的 long-context architectures 与 context-only baselines，包括 SSM / Mamba / xLSTM 或 efficient-attention variants [@lu2023ssmrl; @huang2024decisionmamba; @beck2024xlstm; @dao2023flashattention2]。
- Metrics：calibration、abstention-coverage tradeoff、adaptation lag、catastrophic failure rate，以及对 negative evidence 的 sensitivity。

这里的 evaluation principle 是：不能只凭 scalar return 宣告 success。因为本地 synthesis 已经说明，calibration、intervention sensitivity 与 recovery under shift 才是当前的 blind spots。

# Risks and Alternatives / 风险与替代方案

## Risk 1: The state hypothesis may be too rigid / state hypothesis 可能过于僵硬

- **Issue:** 本地 corpus 支持的是 candidate latent quantities，而不是 universal minimal decomposition。
- **Alternative:** 使用 semi-structured latent state，只保留较少的 explicit heads，并把 decomposition 视作 hypothesis family，而不是 theorem。

## Risk 2: Context compilation may improve efficiency without improving real adaptation / context compilation 可能只提升效率，却没有提升真实 adaptation

- **Issue:** retrieval 与 filtering 的 gains 仍可能和 memory exploitation 混杂，而不是 learning。
- **Alternative:** 引入 retention 与 invalidation tests，并在更强的 claim 之前，先与 simpler summarization baselines 直接比较。

## Risk 3: Bounded embodied validation may still be too expensive or too noisy / bounded embodied validation 仍可能成本过高或噪声过大

- **Issue:** 本地 embodied notes 表明，success 高度依赖 diversity、memory length、curriculum 与 distillation。
- **Alternative:** 把 embodied / multimodal validation 严格 gated 在前两阶段之后；如果 systems budget 成为主限制，则优先加深 non-stationary procedural evaluation。

# Expected Outcomes / 预期成果

如果成功，这个 research program 将产出：

1. 一个针对 ICRL 中 candidate **algorithmic state** 的测试框架；
2. 一个带有显式 retention 与 invalidation tests 的 **experience compilation** architecture；
3. 一个面向 distribution shift 的 **belief-calibrated adaptation** staged protocol；
4. 一个在 mechanistic claims、architectural choices 与 closed-loop validation 之间更可辩护的连接。

预期贡献并不是宣称领域已经解决了 general adaptive intelligence。更合理的预期贡献是：为固定参数模型中的 adaptive behavior 提供一个更 sharp、也更 falsifiable 的研究路径。

## Current implementation boundary / 当前实现边界

当前仓库中的 build 应该被理解为 proposal 的一个 controlled proxy，而不是整个 program 的实现。现在落地的 slice 在 hidden-task bandit 中实例化了 explicit candidate state，并记录了 calibration-oriented signals，因此最多覆盖 Aim 1 以及一层很薄的 Aim 3 proxy。它**还没有**实现 Aim 2 中的 `experience compilation` layer，也**还没有**真正的 abstention 或 safe-action policy。

# Timeline / 时间线

## Year 1

- 复现 note-backed baselines；
- formalize candidate state hypotheses；
- 构建 intervention-friendly synthetic 与 procedural tasks。

## Year 2

- 测试 explicit-state 与 opaque-latent models；
- 建立 intervention、calibration 与 regret benchmarks；
- 启动 context-compilation prototypes。

## Year 3

- 构建 revisable memory 与 state-aware controllers；
- 与 filtering、retrieval 以及 offline objective-repair baselines 对比；
- 开展 non-stationary evaluation。

## Year 4

- 如果前面阶段成功，则加入 bounded multimodal 或 embodied validation；
- 收敛 evaluation、risks 与 failure analyses；
- 把最终 program 转化为 full proposal 与 papers。

# Bibliography / 参考文献

这份 bilingual draft 的共享 bibliography 在 [references.bib](/Users/xinjiezhang/in%20context%20RL/proposal/in-context-rl/references.bib)。正文中实际引用的本地文献包括：

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
