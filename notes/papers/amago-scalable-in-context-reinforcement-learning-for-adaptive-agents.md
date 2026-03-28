# AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents

- Paper folder: `papers/AMAGO Scalable In-Context Reinforcement Learning for Adaptive Agents`
- Note slug: `amago-scalable-in-context-reinforcement-learning-for-adaptive-agents`

## Full citation
Jake Grigsby, Yuke Zhu. AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/AMAGO Scalable In-Context Reinforcement Learning for Adaptive Agents/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: We introduce AMAGO, an in-context Reinforcement Learning (RL) agent that uses sequence models to tackle the challenges of generalization, long-term memory, and meta-learning. Recent works have shown that off-policy learning can make in-context RL with recurrent policies viable.
- Core mechanism: 用 off-policy 长上下文 Transformer 覆盖整段 rollout，并结合多目标 hindsight relabeling，把 in-context RL 扩展到长记忆和稀疏奖励场景。
- Primary bottleneck: 主要瓶颈是 context length、discount horizon、以及长序列 Transformer 的训练稳定性和 recall 能力。
- Evaluated on: 评估在 long-term memory、meta-learning、goal-conditioned procedurally generated domains 上，与 recurrent/meta-RL/off-policy baselines 比较成功率与适应表现。
- Key failure mode: 如果任务本身不真正需要长时适应，长上下文收益会缩小；方法也依赖足够丰富的稀疏奖励数据和 relabeling 设计。

## Problem setting
We introduce AMAGO, an in-context Reinforcement Learning (RL) agent that uses sequence models to tackle the challenges of generalization, long-term memory, and meta-learning. Recent works have shown that off-policy learning can make in-context RL with recurrent policies viable. Nonetheless, these approaches require extensive tuning and limit scalability by creating key bottlenecks in agents' memory capacity, planning horizon, and model size.

## Method summary
用 off-policy 长上下文 Transformer 覆盖整段 rollout，并结合多目标 hindsight relabeling，把 in-context RL 扩展到长记忆和稀疏奖励场景。 We aim to extend the limits of off-policy in-context RL's three main barriers: 1) the memory limit or context length , 2) the value discount factor , and 3) the size and recall of our sequence model. Transformers are a strong solution to the last challenge and may be able to address all three barriers if we were able to learn from long context lengths and select actions for at test time. In principle, this would allow agents to remember and plan for long adaptation windows in order to scale to more challenging problems while removing the need to tune trade-offs between stability and context length. AMAGO overcomes several challenges to make this possible.

## Datasets / tasks / benchmarks
评估在 long-term memory、meta-learning、goal-conditioned procedurally generated domains 上，与 recurrent/meta-RL/off-policy baselines 比较成功率与适应表现。

## Strongest results
-3mm Our experiments are divided into two parts. First, we evaluate our agent in a variety of existing long-term memory, generalization, and meta-learning environments. We then explore the combination of AMAGO's adaptive memory and hindsight instruction relabeling in multi-task domains with procedurally generated environments. Additional results, details, and discussion for each of our experiments can be found in Appendix REF.

## Failure modes or limitations
如果任务本身不真正需要长时适应，长上下文收益会缩小；方法也依赖足够丰富的稀疏奖励数据和 relabeling 设计。

## Evidence anchors
- Introduction
- Related Work
- Background and Problem Formulation
- Method
- Experiments
- Long-Term Memory, Generalization, and Meta-Learning
- Goal-Conditioned Environment Adaptation
- Conclusion
- Acknowledgments
- AMAGO Details
- Sharing a Single Sequence Model in Off-Policy RL
- Base Actor-Critic Update
- AMAGO Architecture
- Relabeling with Goal Importance Sampling
- Experimental Details and Further Analysis
- POPGym
- Additional Memory and Multi-Episodic Meta-RL Results
- Package Delivery
- Environment and Task Details
- Additional Results and Analysis
- MazeRunner
- Environment and Task Details
- Additional Results and Analysis
- Crafter
- Environment and Task Details
- Additional Results and Analysis
- Policy Architecture and Training Details

## Tags
`benchmark` `transformers` `meta-rl` `exploration` `memory` `action-models` `icrl` `sequence-modeling`
