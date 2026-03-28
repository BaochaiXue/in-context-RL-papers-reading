# AMAGO-2: Breaking the Multi-Task Barrier in Meta-Reinforcement Learning with Transformers

- Paper folder: `papers/AMAGO-2 Breaking the Multi-Task Barrier in Meta-Reinforcement Learning with Transformers`
- Note slug: `amago-2-breaking-the-multi-task-barrier-in-meta-reinforcement-learning-with-transformers`

## Full citation
Jake Grigsby Justin Sasek, Samyak Parajuli, Daniel Adebi. AMAGO-2: Breaking the Multi-Task Barrier in Meta-Reinforcement Learning with Transformers. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/AMAGO-2 Breaking the Multi-Task Barrier in Meta-Reinforcement Learning with Transformers/main.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: Language models trained on diverse datasets unlock generalization by in-context learning. Reinforcement Learning (RL) policies can achieve a similar effect by meta-learning within the memory of a sequence model.
- Core mechanism: 把 actor/critic 的回归目标改成对 return scale 不敏感的分类式目标，去掉无标签多任务 meta-RL 中最核心的尺度失衡。
- Primary bottleneck: 真正瓶颈不是模型容量，而是多任务训练时不同任务回报尺度导致的梯度失衡和 shared critic 偏置。
- Evaluated on: 在 Meta-World ML45、Multi-Game Procgen、POPGym、Atari、BabyAI 等上验证，核心 baseline 是原始 dependent actor-critic 变体与 memory-based RL。
- Key failure mode: 论文明确说 return scaling 只能解释“部分”多任务困难；即便去掉尺度问题，其他泛化瓶颈依然存在。

## Problem setting
Language models trained on diverse datasets unlock generalization by in-context learning. Reinforcement Learning (RL) policies can achieve a similar effect by meta-learning within the memory of a sequence model. However, meta-RL research primarily focuses on adapting to minor variations of a single task.

## Method summary
把 actor/critic 的回归目标改成对 return scale 不敏感的分类式目标，去掉无标签多任务 meta-RL 中最核心的尺度失衡。

## Datasets / tasks / benchmarks
在 Meta-World ML45、Multi-Game Procgen、POPGym、Atari、BabyAI 等上验证，核心 baseline 是原始 dependent actor-critic 变体与 memory-based RL。

## Strongest results
and create four interchangeable combinations of learning updates where one or both of the actor and critic loss can be dependent or indirectly dependent on the scale of . We will compare all four update variants, although we are mainly interested in evaluating the two extremes: ``Dep. Actor, Dep. Critic'' ( , ) and ``Ind.

## Failure modes or limitations
论文明确说 return scaling 只能解释“部分”多任务困难；即便去掉尺度问题，其他泛化瓶颈依然存在。

## Evidence anchors
- Introduction
- Background
- Multi-Task Adaptation Without Task Labels
- Experiments
- Conclusion
- Implementation Details
- Additional Environment Details
- Additional Results

## Tags
`benchmark` `transformers` `meta-rl` `memory` `sequence-modeling`
