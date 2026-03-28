# Decision Mamba: Reinforcement Learning via Hybrid Selective Sequence Modeling

- Paper folder: `papers/Decision Mamba Reinforcement Learning via Hybrid Selective Sequence Modeling`
- Note slug: `decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling`

## Full citation
Key Laboratory, Symbolic Computation, Knowledge Engineering, Artificial Intelligence, High Performance Computing. Decision Mamba: Reinforcement Learning via Hybrid Selective Sequence Modeling. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Decision Mamba Reinforcement Learning via Hybrid Selective Sequence Modeling/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Recent works have shown the remarkable superiority of transformer models in reinforcement learning (RL), where the decision-making problem is formulated as sequential generation. Transformer-based agents could emerge with self-improvement in online environments by providing task contexts, such as multiple trajectories, called in-context RL.
- Core mechanism: 用 Mamba 处理长程依赖、生成高价值子目标，再用 Transformer 做高质量动作预测，形成 DM-H 混合结构。
- Primary bottleneck: 瓶颈在于长程效率和短程精度的折中；子目标生成质量一旦不足，后续 Transformer 也会被带偏。
- Evaluated on: 在 D4RL、GridWorld、T-maze 等长短期任务上，与 Decision Transformer 和纯 Mamba 变体比较回报。
- Key failure mode: 若任务缺少清晰长程结构，或子目标本身学得差，混合结构的收益会明显下降。

## Problem setting
Recent works have shown the remarkable superiority of transformer models in reinforcement learning (RL), where the decision-making problem is formulated as sequential generation. Transformer-based agents could emerge with self-improvement in online environments by providing task contexts, such as multiple trajectories, called in-context RL. However, due to the quadratic computation complexity of attention in transformers, current in-context RL methods suffer from huge computational costs as the task horizon increases.

## Method summary
用 Mamba 处理长程依赖、生成高价值子目标，再用 Transformer 做高质量动作预测，形成 DM-H 混合结构。 In this section, we first compare Mamba and transformer models in the D4RL dataset, and investigate the potential of Mamba in RL tasks. Then, We present DM-H, which can handle long-term dependencies from contexts with high effectiveness and efficiency, as shown in Figure~REF. Mamba vs. Transformer in RL tasks We first consider the Algorithm Distillation (AD) as the baseline, which is a classic in-context RL method using a transformer as the backbone .

## Datasets / tasks / benchmarks
在 D4RL、GridWorld、T-maze 等长短期任务上，与 Decision Transformer 和纯 Mamba 变体比较回报。

## Strongest results
In this section, we will introduce datasets and baselines in Section~REF. Then, in Section~REF, Section~REF, Section~REF, and REF, we report the comparison results, ablation study, and parameters sensitivity analysis. In Appendix~REF, we report additional results about offline training time, online testing time, and ablation study. Environmental Settings Dataset: Grid World.

## Failure modes or limitations
若任务缺少清晰长程结构，或子目标本身学得差，混合结构的收益会明显下降。

## Evidence anchors
- Introduction
- Related Work
- Preliminaries
- Method
- Mamba vs. Transformer in RL tasks
- Decision Mamba-Hybrid
- Decision Mamba-Hybrid with Valuable Sub-goals
- Implementation of DM-H
- Experiments
- Environmental Settings
- Grid World Results
- Tmaze Results
- D4RL Results
- Ablation Study and Parameter Sensitivity Analysis
- Conclusion, Limitations, and Broader Impacts
- Pseudocode of Decision Mamba-Hybrid
- Experimental Details
- Additional Experimental Results
- NeurIPS Paper Checklist

## Tags
`benchmark` `transformers` `sequence-models` `meta-rl` `offline-rl` `memory` `systems` `sequence-modeling`
