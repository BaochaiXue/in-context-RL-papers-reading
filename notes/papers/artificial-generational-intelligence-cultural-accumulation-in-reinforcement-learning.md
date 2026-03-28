# Artificial Generational Intelligence: Cultural Accumulation in Reinforcement Learning

- Paper folder: `papers/Artificial Generational Intelligence Cultural Accumulation in Reinforcement Learning`
- Note slug: `artificial-generational-intelligence-cultural-accumulation-in-reinforcement-learning`

## Full citation
Jonathan Cook, Chris Lu, Edward Hughes, Joel Z. Leibo, Jakob Foerster. Artificial Generational Intelligence: Cultural Accumulation in Reinforcement Learning. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/Artificial Generational Intelligence Cultural Accumulation in Reinforcement Learning/neurips_2024.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: Cultural accumulation drives the open-ended and diverse progress in capabilities spanning human history. It builds an expanding body of knowledge and skills by combining individual exploration with inter-generational information transmission.
- Core mechanism: 提出跨代知识传递的 RL 训练范式，把文化积累拆成 in-context accumulation 和 in-weights accumulation 两条路径。
- Primary bottleneck: 核心难点是模仿与独立探索的平衡；过强或过弱的社会学习都会破坏累积效应。
- Evaluated on: 在需要部分可观测探索的 Memory Sequence 等任务上，与同经验预算的单生命周期学习者比较累计收益。
- Key failure mode: 当 oracle 过于可靠或过于不可靠时，文化积累会受阻；primacy bias 过强时还需要 reset 等额外机制。

## Problem setting
Cultural accumulation drives the open-ended and diverse progress in capabilities spanning human history. It builds an expanding body of knowledge and skills by combining individual exploration with inter-generational information transmission. Despite its widespread success among humans, the capacity for artificial learning agents to accumulate culture remains under-explored.

## Method summary
提出跨代知识传递的 RL 训练范式，把文化积累拆成 in-context accumulation 和 in-weights accumulation 两条路径。

## Datasets / tasks / benchmarks
在需要部分可观测探索的 Memory Sequence 等任务上，与同经验预算的单生命周期学习者比较累计收益。

## Strongest results
figure [t] figures/ica_memseq.png Left : In-context accumulation during evaluation on Memory Sequence . Right : Evaluation results following training with different oracle accuracies. figure For each of our experiments, we use a Simplified Structured State Space Model (S5) modified for RL to encode memory, building on the PureJaxRL codebase . This model architecture runs asymptotically faster than Transformers in sequence length and outperforms RNNs in memory tasks .

## Failure modes or limitations
当 oracle 过于可靠或过于不可靠时，文化积累会受阻；primacy bias 过强时还需要 reset 等额外机制。

## Evidence anchors
- Introduction
- Background
- Partially-Observable Stochastic Games
- Partially-Observable Markov Decision Processes
- Meta-RL
- Generational Training
- Problem Statement
- Environments
- Cultural Accumulation in RL
- In-Context Accumulation
- Training
- Evaluation
- In-Weights Accumulation
- Results
- In-Context Results
- In-Weights Results
- Related Work
- Conclusion
- Acknowledgments
- In-Weights Accumulation
- In-Weights Accumulation in TSP
- Selective Social Learning
- Further Environment Details
- Memory Sequence
- Goal Sequence
- TSP
- Architecture Details
- textit Memory Sequence
- textit Goal Sequence
- Hyperparameters
- textit Memory Sequence
- textit Goal Sequence
- Compute Resources

## Tags
`benchmark` `transformers` `sequence-models` `meta-rl` `exploration` `memory` `systems` `sequence-modeling`
