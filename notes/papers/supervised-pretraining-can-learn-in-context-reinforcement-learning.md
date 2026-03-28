# Supervised Pretraining Can Learn In-Context Reinforcement Learning

- Paper folder: `papers/Supervised Pretraining Can Learn In-Context Reinforcement Learning`
- Note slug: `supervised-pretraining-can-learn-in-context-reinforcement-learning`

## Full citation
Jonathan N. Lee, Annie Xie, Aldo Pacchiano, Yash Chandak, Chelsea Finn, Ofir Nachum, Emma Brunskill. Supervised Pretraining Can Learn In-Context Reinforcement Learning. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Supervised Pretraining Can Learn In-Context Reinforcement Learning/intro.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Large transformer models trained on diverse datasets have shown a remarkable ability to learn in-context , achieving high few-shot performance on tasks they were not explicitly trained to solve. In this paper, we study the in-context learning capabilities of transformers in decision-making problems, i.e., reinforcement learning (RL) for bandits and Markov decision processes.
- Core mechanism: DPT 用最优动作监督预训练 Transformer，在 bandit 和 MDP 中诱发 posterior-sampling 式决策。
- Primary bottleneck: 主要限制是预训练需要最优动作或很强 teacher，而且真正长 horizon 实现仍困难。
- Evaluated on: 在 bandit、MDP、Dark Room、MiniWorld 上，与经典 RL 算法和 teacher-generated 数据对比。
- Key failure mode: discussion 明确指出 optimal-action requirement 仍是限制；多任务决策数据如何更好利用仍是开放问题。

## Problem setting
Large transformer models trained on diverse datasets have shown a remarkable ability to learn in-context , achieving high few-shot performance on tasks they were not explicitly trained to solve. In this paper, we study the in-context learning capabilities of transformers in decision-making problems, i.e., reinforcement learning (RL) for bandits and Markov decision processes. To do so, we introduce and study Decision-Pretrained Transformer ( DPT ), a supervised pretraining method where the transformer predicts an optimal action given a query state and an in-context dataset of interactions, across a diverse set of tasks.

## Method summary
DPT 用最优动作监督预训练 Transformer，在 bandit 和 MDP 中诱发 posterior-sampling 式决策。

## Datasets / tasks / benchmarks
在 bandit、MDP、Dark Room、MiniWorld 上，与经典 RL 算法和 teacher-generated 数据对比。

## Strongest results
Environments. We consider environments that require targeted exploration to solve the task. The first is Dark Room~ , a 2D discrete environment where the agent must locate the unknown goal location in a room, and only receives a reward of when at the goal. We hold out a set of goals for generalization evaluation.

## Failure modes or limitations
discussion 明确指出 optimal-action requirement 仍是限制；多任务决策数据如何更好利用仍是开放问题。

## Evidence anchors
- Introduction
- Related Work
- In-Context Learning Model
- Learning in Bandits
- Learning in Markov Decision Processes
- Experimental Setup
- Main Results
- Learning from Algorithm-Generated Policies and Rollouts
- Theory
- History-Dependent Pretraining and Assumptions
- Main Results
- Discussion
- Additional Related Work
- Implementation and Experiment Details
- DPT Architecture: Formal Description
- Implementation Details
- Bandit algorithms
- RL Algorithms
- Bandit Pretraining and Testing
- MDP Environment Details
- MDP Pretraining Datasets
- Additional Experimental Results
- Bandits
- Markov Decision Processes
- Sensitivity Analysis
- Additional Theory and Omitted Proofs
- Posterior Sampling
- Proof of Theorem~; ref thm:main
- Proof of Corollary~; ref cor:mdp
- Proof of Corollary~; ref cor:lin
- Proof of Proposition~; ref prop:invariance

## Tags
`benchmark` `transformers` `meta-rl` `exploration` `bandits` `memory` `theory` `action-models`
