# In-Context Reinforcement Learning via Communicative World Models

- Paper folder: `papers/In-Context Reinforcement Learning via Communicative World Models`
- Note slug: `in-context-reinforcement-learning-via-communicative-world-models`

## Full citation
Fernando Martinez-Lopez, Author Name, First Author Name. In-Context Reinforcement Learning via Communicative World Models. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/In-Context Reinforcement Learning via Communicative World Models/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Reinforcement learning (RL) agents often struggle to generalize to new tasks and contexts without updating their parameters, mainly because their learned representations and policies are overfit to the specifics of their training environments. To boost agents' in-context RL (ICRL) ability, this work formulates ICRL as a two-agent emergent communication problem and introduces CORAL (Communicative Representation for Adaptive RL), a framework that learns a transferable communicative context by decoupling latent representation learning from control.
- Core mechanism: CORAL 把 ICRL 变成 emergent communication 问题，先训练 world model 信息代理，再让控制代理读消息适应。
- Primary bottleneck: 固定维度的 dense message 是主要瓶颈；需要更高维或可组合推理时，协议可能不够表达。
- Evaluated on: 在 unseen sparse-reward 环境中，与 PPO 和等价 world-model baseline 比较 sample efficiency 与 zero-shot。
- Key failure mode: 作者在 limitation 里明确指出，高维输入或需要 compositional communication 的任务会超出当前 fixed message protocol 的能力。

## Problem setting
Reinforcement learning (RL) agents often struggle to generalize to new tasks and contexts without updating their parameters, mainly because their learned representations and policies are overfit to the specifics of their training environments. To boost agents' in-context RL (ICRL) ability, this work formulates ICRL as a two-agent emergent communication problem and introduces CORAL (Communicative Representation for Adaptive RL), a framework that learns a transferable communicative context by decoupling latent representation learning from control. In CORAL, an Information Agent (IA) is pre-trained as a world model on a diverse distribution of tasks.

## Method summary
CORAL 把 ICRL 变成 emergent communication 问题，先训练 world model 信息代理，再让控制代理读消息适应。 The challenge of enabling intelligent agents to generalize and rapidly adapt to new situations is a central pursuit in reinforcement learning. Standard end-to-end paradigms, where a single reward signal shapes a monolithic network, can be remarkably effective~ but often yield representations that are overly specialized to the training task, hindering generalization. This has motivated research into decoupled approaches where general-purpose representations are learned via self-supervised objectives~ . While these methods can produce robust features, they may not be optimally tailored for the specific downstream control task.

## Datasets / tasks / benchmarks
在 unseen sparse-reward 环境中，与 PPO 和等价 world-model baseline 比较 sample efficiency 与 zero-shot。

## Strongest results
figure* [t] Figures/lc.pdf -5pt In-context adaptation with a pre-trained Information Agent. Learning curves show the mean episodic return ( confidence interval) across 30 multiple seeds for a randomly initialized Control Agent paired with a pre-trained, frozen CORAL IA. 923BE5 CORAL demonstrates higher sample efficiency and asymptotic performance compared to a 339332 standard PPO and an DD264A equivalent World Model across a variety of unseen environments. -5pt figure* We conduct a series of experiments designed to validate our central hypothesis: a pre-trained communicative prior, learned via CORAL, can enable rapid in-context adaptation by providing a rich, task-relevant learning signal in environments where such information is otherwise unavailable.

## Failure modes or limitations
作者在 limitation 里明确指出，高维输入或需要 compositional communication 的任务会超出当前 fixed message protocol 的能力。

## Evidence anchors
- Introduction
- Preliminaries
- Methodology
- CORAL Agents and Emergent Communication
- Pre-training the Communicative Representation
- The Information Agent as a Communicative World Model
- Multi-Environment Training for Generalization
- Deployment for Rapid In-Context Adaptation
- Experimental Results
- Accelerated Control Learning via In-Context Communication
- Integrated In-Context Communication and Control for Zero-Shot Generalization
- Analysis of the Emergent Communicative Protocol
- Related Works
- Conclusion
- Appendix
- Code availability
- Limitations and Future Work
- Experiment Setup and Hyperparameters
- Pre-training Environment Distribution
- Neural Network Architectures and Hyperparameters
- Quantitative Analysis Details
- Statistical Significance Testing
- Time-to-Threshold (TTT) Calculation
- Ablation Studies
- Importance of Message Coherence
- Information Agent Architecture
- Message Dimensionality

## Tags
`benchmark` `meta-rl` `memory` `world-models` `icrl`
