# A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI

- Paper folder: `papers/ReLIC A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI`
- Note slug: `relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai`

## Full citation
Ahmad Elawady Gunjan Chhablani Ram, Ramrakhya Karmesh Yadav, Georgia Tech. A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/ReLIC A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: =-1 Intelligent embodied agents need to quickly adapt to new scenarios by integrating long histories of experience into decision-making. For instance, a robot in an unfamiliar house initially wouldn't know the locations of objects needed for tasks and might perform inefficiently.
- Core mechanism: 用 partial updates 和 Sink-KV 把 visual embodied ICRL 的上下文扩到 64k steps。
- Primary bottleneck: 需要避免任务被记忆化；同时 RL 训练代价极高，长上下文注意力仍然昂贵。
- Evaluated on: 在新的 embodied navigation benchmark 以及 DarkRoom/MiniWorld 上，与多种 meta-RL/ICRL baseline 比较成功率与效率。
- Key failure mode: 结论明确说如果训练分布不够多样、模型能直接过拟合任务，就没有动机学会利用 context。

## Problem setting
=-1 Intelligent embodied agents need to quickly adapt to new scenarios by integrating long histories of experience into decision-making. For instance, a robot in an unfamiliar house initially wouldn't know the locations of objects needed for tasks and might perform inefficiently. However, as it gathers more experience, it should learn the layout of its environment and remember where objects are, allowing it to complete new tasks more efficiently.

## Method summary
用 partial updates 和 Sink-KV 把 visual embodied ICRL 的上下文扩到 64k steps。 -5pt We introduce ( ) which enables agents to in-context adapt to new episodes without any re-training. is built using a transformer policy architecture that operates over a long sequence of multi-episode observations and is trained with online RL. The novelty of is changing the base RL algorithm to more frequently update the policy with increasingly longer contexts within a policy rollout and adding to give the model the ability to avoid attending to low-information context. sec:problem provides the general problem setting of adapting to new episodes.

## Datasets / tasks / benchmarks
在新的 embodied navigation benchmark 以及 DarkRoom/MiniWorld 上，与多种 meta-RL/ICRL baseline 比较成功率与效率。

## Strongest results
We first introduce the ( ) task we use to study in-context learning for embodied navigation. Next, we analyze how enables in-context learning on this task and outperforms prior work and baselines. We then analyze ablations of and analyze its behaviors. We also show is capable of few-shot imitation learning.

## Failure modes or limitations
结论明确说如果训练分布不够多样、模型能直接过拟合任务，就没有动机学会利用 context。

## Evidence anchors
- Introduction
- Related Work
- Method
- Problem Setting
- method Policy Architecture
- method Learning
- Implementation Details
- Experiments
- task: ; Task
- In-Context Learning on ; task
- method Ablations and Analysis
- Emergent Few-Shot Imitation Learning
- Darkroom and Miniworld
- Conclusion and Limitations
- Acknowledgements
- Additional ; task Details
- Additional Method Details
- Model training
- Hyperparameters
- Darkroom and Miniworld Hyperparameters
- More Experiments
- method per Object Type
- Analyzing Attention Scores
- Impact of Episode Shuffling
- Ablations in Miniworld and Darkroom
- Training with 64k Context Length
- Visual encoder finetuning
- Sink KV
- Motivation
- Solutions
- sinkv variants

## Tags
`benchmark` `transformers` `meta-rl` `memory` `embodied` `icrl` `sequence-modeling`
