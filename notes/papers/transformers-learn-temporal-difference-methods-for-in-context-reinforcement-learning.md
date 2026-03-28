# Transformers Can Learn Temporal Difference Methods for In-Context Reinforcement Learning

- Paper folder: `papers/Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning`
- Note slug: `transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning`

## Full citation
Jiuqi Wang, Hadi Daneshmand, Shangtong Zhang. Transformers Can Learn Temporal Difference Methods for In-Context Reinforcement Learning. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Traditionally, reinforcement learning (RL) agents learn to solve new tasks by updating their neural network parameters through interactions with the task environment. However, recent works demonstrate that some RL agents, after certain pretraining procedures, can learn to solve unseen new tasks without parameter updates, a phenomenon known as in-context reinforcement learning (ICRL).
- Core mechanism: 证明并实证展示 Transformer 在 forward pass 中能自然实现 TD(0) 等 in-context 评估算法。
- Primary bottleneck: 局限于 policy evaluation，且理论分析依赖 linear attention 等简化假设。
- Evaluated on: 在 Boyan chain 和 CartPole 等任务上验证，与多任务 TD 预训练和理论构造对比。
- Key failure mode: 作者明确列出四个限制：只做 policy evaluation、线性化简化、需要合成任务、未扩展到 Atari/DeepMindLab。

## Problem setting
Traditionally, reinforcement learning (RL) agents learn to solve new tasks by updating their neural network parameters through interactions with the task environment. However, recent works demonstrate that some RL agents, after certain pretraining procedures, can learn to solve unseen new tasks without parameter updates, a phenomenon known as in-context reinforcement learning (ICRL). The empirical success of ICRL is widely attributed to the hypothesis that the forward pass of the pretrained agent neural network implements an RL algorithm.

## Method summary
证明并实证展示 Transformer 在 forward pass 中能自然实现 TD(0) 等 in-context 评估算法。

## Datasets / tasks / benchmarks
在 Boyan chain 和 CartPole 等任务上验证，与多任务 TD 预训练和理论构造对比。

## Strongest results
This work makes the first step towards white-boxing the mechanism of ICRL under reinforcement pretraining, focusing specifically on policy evaluation. We provide constructive proof that transformers can implement multiple temporal difference algorithms in the forward pass for in-context policy evaluation. Additionally, we theoretically and empirically show that the parameters enabling in-context policy evaluation emerge naturally through multi-task TD pretraining.

## Failure modes or limitations
作者明确列出四个限制：只做 policy evaluation、线性化简化、需要合成任务、未扩展到 Atari/DeepMindLab。

## Evidence anchors
- Introduction
- Related Works
- Background
- Transformers Can Implement In-Context TD(0)
- Transformers Do Implement In-Context TD(0)
- Transformers Can Implement More RL Algorithms
- Conclusion
- Acknowledgements
- Proofs
- Proof of Theorem~; ref thm: TD(0)
- Proof of Corollary~; ref cor one layer
- Proof of Theorem~; ref thm: fixed point analysis
- Proof of Corollary~; ref corollary: true RG
- Proof of Corollary~; ref thm: TD(0) lambda
- Proof of Theorem~; ref thm two head average reward TD
- Experimental Details of Figure~; ref fig: icrl demo
- Boyan's Chain Evaluation Task Generation
- Additional Experiments with Linear Transformers
- Experiment Setup
- Trained Transformer Element-wise Convergence Metrics
- Trained Transformer and Batch TD Comparison Metrics
- Nonlinear Attention
- Experiments with CartPole Environment
- CartPole Evaluation Task Generation
- Experimental Results of Pre-training with CartPole
- Investigation of In-Context TD with RNN
- Theoretical Analysis of Linear RNN
- Multi-task TD with Deep RNN
- Numerical Verification of Proofs

## Tags
`benchmark` `transformers` `meta-rl` `memory` `theory` `action-models` `icrl`
