# In Context Decision Transformer Reinforcement Learning Via Hierarchical Chain Of Thought

- Paper folder: `papers/In-Context Decision Transformer Reinforcement Learning via Hierarchical Chain-of-Thought`
- Note slug: `in-context-decision-transformer-reinforcement-learning-via-hierarchical-chain-of-thought`

## Full citation
Authors could not be extracted reliably from the local source. In Context Decision Transformer Reinforcement Learning Via Hierarchical Chain Of Thought. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/In-Context Decision Transformer Reinforcement Learning via Hierarchical Chain-of-Thought/main.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: In-context learning is a promising approach for offline reinforcement learning (RL) to handle online tasks, which can be achieved by providing task prompts. Recent works demonstrated that in-context RL could emerge with self-improvement in a trial-and-error manner when treating RL tasks as an across-episodic sequential prediction problem.
- Core mechanism: 把 across-episode RL 序列抽象为分层的 chain of experience，用高层 trial-and-error 表达降低长程成本。
- Primary bottleneck: 瓶颈在于高层 return/experience 表达是否足够准确；层次化建模一旦失真就会误导动作生成。
- Evaluated on: 在 GridWorld 的 DarkRoom 系列和 D4RL 上，与 AD/DT 类方法比较效率和性能。
- Key failure mode: 当高层经验摘要和真实 credit assignment 不一致时，分层优势会消失，甚至比直接序列建模更差。

## Problem setting
In-context learning is a promising approach for offline reinforcement learning (RL) to handle online tasks, which can be achieved by providing task prompts. Recent works demonstrated that in-context RL could emerge with self-improvement in a trial-and-error manner when treating RL tasks as an across-episodic sequential prediction problem. Despite the self-improvement not requiring gradient updates, current works still suffer from high computational costs when the across-episodic sequence increases with task horizons.

## Method summary
把 across-episode RL 序列抽象为分层的 chain of experience，用高层 trial-and-error 表达降低长程成本。 In this section, we present IDT, which models a high-level trial-and-error process through a hierarchical chain of experience, as summarized in Figure ~REF. Chain of Experience The key factors that influence our modeling on how to represent trajectories are (1) the ability of transformers to uncover meaningful patterns from multiple trajectories and (2) the capacity to improve itself conditioned on experience. The basic elements of trajectories are observations , actions , rewards , and completion token . As modeling rewards is a nontrivial task, we aim to have the model generate actions based on the target returns , which can be updated using rewards .

## Datasets / tasks / benchmarks
在 GridWorld 的 DarkRoom 系列和 D4RL 上，与 AD/DT 类方法比较效率和性能。

## Strongest results
Dataset: Grid World. ~~ In this section, we first consider the discrete control environments from the Grid World , which is a commonly used benchmark for recent in-context RL methods. The environments support many tasks that cannot be solved through zero-shot generalization after pre-training because these tasks cannot be inferred easily from the observation. The episode of each task is short enough to train a transformer-based policy with across-episodic contexts feasibly.

## Failure modes or limitations
当高层经验摘要和真实 credit assignment 不一致时，分层优势会消失，甚至比直接序列建模更差。

## Evidence anchors
- Introduction
- Related Work
- Preliminaries
- Method
- Chain of Experience
- Hierarchical Chain of Experience
- Implementation of IDT
- Experiments
- Evaluation of Computing Costs
- Grid World Results
- D4RL Results
- Case Study on the Reviewing Decisions Module
- Conclusion
- Impact Statement
- Acknowledgments
- Pseudocode of In-context Decision Transformer
- Experimental Details
- Additional Experimental Results

## Tags
`benchmark` `transformers` `meta-rl` `offline-rl` `memory` `action-models` `sequence-modeling`
