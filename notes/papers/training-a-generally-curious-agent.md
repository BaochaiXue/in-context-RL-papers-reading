# Training A Generally Curious Agent

- Paper folder: `papers/Training a Generally Curious Agent`
- Note slug: `training-a-generally-curious-agent`

## Full citation
Authors could not be extracted reliably from the local source. Training A Generally Curious Agent. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/Training a Generally Curious Agent/main.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: Efficient exploration is essential for intelligent systems interacting with their environment, but existing language models often fall short in scenarios that require strategic information gathering. In this paper, we present , a fine-tuning approach that enables language models to develop general decision-making capabilities that are not confined to particular environments.
- Core mechanism: 用 synthetic interaction data 和 curriculum 微调 LLM，学习可迁移的泛化探索策略。
- Primary bottleneck: 训练高度依赖 rejection sampling 和强 base model；curriculum 质量又受 task clustering 影响。
- Evaluated on: 在多类 synthetic interactive tasks 上测试 zero-shot transfer，与无课程或弱训练设置比较多轮决策表现。
- Key failure mode: discussion 直接指出：没有强基座模型时表现会差；task cluster 质量差也会使 curriculum 失效。

## Problem setting
Efficient exploration is essential for intelligent systems interacting with their environment, but existing language models often fall short in scenarios that require strategic information gathering. In this paper, we present , a fine-tuning approach that enables language models to develop general decision-making capabilities that are not confined to particular environments. By training on synthetic interaction data from different tasks that require diverse strategies, teaches models to explore and adapt their behavior on a new task based on environment feedback in-context without more gradient updates.

## Method summary
用 synthetic interaction data 和 curriculum 微调 LLM，学习可迁移的泛化探索策略。

## Datasets / tasks / benchmarks
在多类 synthetic interactive tasks 上测试 zero-shot transfer，与无课程或弱训练设置比较多轮决策表现。

## Strongest results
In this paper, we presented a scalable fine-tuning method to improve multi-turn decision making abilities of LLMs. Moreover, we showed that the strategies learned by the LLM from our method can generalize zero-shot to unseen tasks. There are a few limitations to our approach.

## Failure modes or limitations
discussion 直接指出：没有强基座模型时表现会差；task cluster 质量差也会使 curriculum 失效。

## Evidence anchors
- Introduction
- Preliminary
- ours
- Empirical Results
- Analysis
- Related Works
- Discussion
- Impact Statement
- Reproducibility Statement
- Acknowledgement
- Note on Curiosity
- Details on Task Design
- Summary of Task Groups
- Note on Task Prompts
- Note on Text-based Games
- Comparison of action and observation spaces between the task groups
- Details of Individual Task Groups
- Twenty Questions
- Guess My City
- Customer Service
- Murder Mystery
- Wordle
- Cellular Automata
- Mastermind
- Battleship
- Minesweeper
- Bandit Best Arm Selection
- Details of Training Dataset Construction
- Note about Task Environment Hacking
- More on LLM Inference Settings
- Additional Experimental Details
- Public Release of Code, Model and Dataset
- More Details on Curriculum Learning
- More Empirical Results
- Success Rate Comparison with More Baselines
- Task Efficiency Comparison with More Baselines
- ours
- ours
- More Performance Metrics
- More Results on Generalization
- Evaluation on LMRL-Gym split
- Experiments on Modified Wordle to Further Test Generalization
- Ablation Study over Different Finetuning Stages of ; ours
- Finetuning on regular multiturn data does not help
- Performance comparison between different starting models
- Details on Standard Benchmarks
- Limitations of ; ours
- Example Trajectories

## Tags
`benchmark` `llm` `meta-rl` `exploration` `bandits` `memory` `action-models` `icrl`
