# Human-Timescale Adaptation in an Open-Ended Task Space

- Paper folder: `papers/Human-Timescale Adaptation in an Open-Ended Task Space`
- Note slug: `human-timescale-adaptation-in-an-open-ended-task-space`

## Full citation
Authors could not be extracted reliably from the local source. Human-Timescale Adaptation in an Open-Ended Task Space. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Human-Timescale Adaptation in an Open-Ended Task Space/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Foundation models have shown impressive adaptation and scalability in supervised and self-supervised learning problems, but so far these successes have not fully translated to reinforcement learning (RL). In this work, we demonstrate that training an RL agent at scale leads to a general in-context learning algorithm that can adapt to open-ended novel embodied 3D problems as quickly as humans.
- Core mechanism: AdA 用大规模 attention memory、自动课程和 distillation，在 XLand 2.0 中实现接近人类时间尺度的快速适应。
- Primary bottleneck: 真正瓶颈是 task-pool richness、memory length、attention 架构与蒸馏成本；黑盒 meta-RL 仍非常吃算力。
- Evaluated on: 在 XLand 2.0 的 held-out tasks 与 hand-authored probe tasks 上，比较不同架构、课程和尺度，指标是多 trial 适应得分。
- Key failure mode: ablation 显示去掉 auto-curriculum、attention 或 distillation 后，尤其在低分位任务上性能明显坍塌。

## Problem setting
Foundation models have shown impressive adaptation and scalability in supervised and self-supervised learning problems, but so far these successes have not fully translated to reinforcement learning (RL). In this work, we demonstrate that training an RL agent at scale leads to a general in-context learning algorithm that can adapt to open-ended novel embodied 3D problems as quickly as humans. In a vast space of held-out environment dynamics, our adaptive agent (AdA) displays on-the-fly hypothesis-driven exploration, efficient exploitation of acquired knowledge, and can successfully be prompted with first-person demonstrations.

## Method summary
AdA 用大规模 attention memory、自动课程和 distillation，在 XLand 2.0 中实现接近人类时间尺度的快速适应。

## Datasets / tasks / benchmarks
在 XLand 2.0 的 held-out tasks 与 hand-authored probe tasks 上，比较不同架构、课程和尺度，指标是多 trial 适应得分。

## Strongest results
Adaptation to new information across a range of timescales is a crucial ability for generally intelligent agents. Foundation models in particular have demonstrated an ability to acquire a large knowledge-base of information, and apply this rapidly to new scenarios. Thus far, they have relied mainly on supervised and self-supervised learning.

## Failure modes or limitations
ablation 显示去掉 auto-curriculum、attention 或 distillation 后，尤其在低分位任务上性能明显坍塌。

## Evidence anchors
- Introduction
- Adaptive Agent (AdA)
- Open-ended task space: XLand 2.0
- Meta-RL
- Auto-curriculum learning
- RL agent
- Distillation
- Experiments and Results
- AdA shows human-timescale adaptation
- Architecture influences performance
- Auto-curriculum learning improves performance
- Scaling the agent increases performance
- Scaling the task pool increases performance
- Distillation improves performance and enables scaling agents
- Training on more trials with skip memory enables many-shot adaptation
- AdA can leverage prompting with first-person demonstrations
- Related Work
- Conclusion
- Authors and Contributions
- Core contributors
- Partial contributors
- Sponsors
- Acknowledgements
- Appendix
- Environment Details
- XLand 2.0
- Pre-sampling tasks for training
- Evaluation
- Test scores
- Hand-authored probe tasks
- Adaptation metric
- Human data collection
- Agent Details
- Agent Architecture
- Observations
- Training Details
- Meta-RL
- Single-agent training
- Multi-agent training
- Architecture experiments
- Auto-curriculum learning
- Distillation teacher for scaling experiments
- Scaling the network
- Scaling the memory length
- Scaling the size of the task pool
- Scaling the complexity of the task pool
- Distillation enables scaling agents
- Training on more trials with skip memory
- Additional Experiments
- Multi-agent adaptation
- Conditioning on number of shots doesn't affect agents' performance
- Scaling complexity of the task pool
- Computational cost
- Repeated distillation
- Human-Timescale Adaptation
- Probe tasks
- Comparing human and agent scores on every probe task
- Quantifying stochasticity
- Prompting through first-person demonstrations

## Tags
`benchmark` `meta-rl` `exploration` `memory` `embodied`
