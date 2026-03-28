# Retrieval-Augmented Decision Transformer: External Memory for In-context RL

- Paper folder: `papers/Retrieval-Augmented Decision Transformer External Memory for In-context RL`
- Note slug: `retrieval-augmented-decision-transformer-external-memory-for-in-context-rl`

## Full citation
ELLIS Unit, LIT AI Lab, Machine Learning, JKU Linz, Extensity AI. Retrieval-Augmented Decision Transformer: External Memory for In-context RL. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Retrieval-Augmented Decision Transformer External Memory for In-context RL/main_collas25.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.
- Inventory status: This paper folder contains no local PDF files, so it has no rows in `notes/tables/paper_inventory.csv`; the note is source-only.

## 5-bullet thesis
- Addresses: In-context learning (ICL) is the ability of a model to learn a new task by observing a few exemplars within its context. While prevalent in NLP, this capability has recently also been observed in Reinforcement Learning (RL) settings.
- Core mechanism: 给 Decision Transformer 加外部向量检索记忆，只取与当前状态最相关的子轨迹。
- Primary bottleneck: 瓶颈不是单纯序列长度，而是 retrieval 是否真的在支持 meta-learning，还是只是复制记忆。
- Evaluated on: 在 Dark-Room、Key-Door、MazeRunner、Meta-World、DMControl、Procgen 上，与 DT、AD、DPT 比较 ICL 改进曲线。
- Key failure mode: 论文明确指出在 fully observable 和复杂环境中几乎没观察到真正的 ICL；memory 与 learning 仍纠缠。

## Problem setting
In-context learning (ICL) is the ability of a model to learn a new task by observing a few exemplars within its context. While prevalent in NLP, this capability has recently also been observed in Reinforcement Learning (RL) settings. Prior in-context RL methods, however, require entire episodes in the agent's context.

## Method summary
给 Decision Transformer 加外部向量检索记忆，只取与当前状态最相关的子轨迹。 Background Reinforcement Learning. We formulate our problem setting as a Markov Decision Process (MDP) that is represented by a 4-tuple of . and denote state and action spaces, respectively. At timestep the agent observes state and issues action .

## Datasets / tasks / benchmarks
在 Dark-Room、Key-Door、MazeRunner、Meta-World、DMControl、Procgen 上，与 DT、AD、DPT 比较 ICL 改进曲线。

## Strongest results
We evaluate the ICL abilities of RA-DT on grid-world environments used in prior works, namely Dark-Room (see Section REF), Dark Key-Door (Section REF), and MazeRunner (Section REF) , with increasingly larger grid-sizes, resulting in longer episodes. Moreover, we evaluate RA-DT on two robotic benchmarks (Meta-World and DMControl, Section REF) and procedurally-generated video games (Procgen, Section REF). Across experiments, we report performances for two variants of RA-DT . The first variant leverages a domain-specific embedding model for retrieval, specifically a DT trained on the same domain.

## Failure modes or limitations
论文明确指出在 fully observable 和复杂环境中几乎没观察到真正的 ICL；memory 与 learning 仍纠缠。

## Evidence anchors
- Introduction
- Related Work
- Method
- Background
- Retrieval-augmented Decision Transformer (RA-DT)
- Vector Index for Retrieval Augmentation
- Searching for Similar Experiences
- Reweighting Retrieved Experiences
- Incorporating Retrieved ; ; Experiences
- Experiments
- Dark-Room
- Dark Key-Door
- Maze-Runner
- Meta-World ; & DMControl
- Procgen
- Ablations
- Discussion
- Conclusion
- Acknowledgments
- Appendix
- Ethics Statement ; & Reproducibility
- Environments ; & Datasets
- Dark-Room and Dark Key-Door
- MazeRunner
- Meta-World
- DMControl
- Procgen
- Experimental ; & Implementation Details
- General
- Decision Transformer
- Algorithm Distillation
- Retrieval-Augmented Decision Transformer
- Additional Results
- Dark-Room
- Attention Map Analysis
- Exploration Analysis
- Maze-Runner
- Meta-World
- DMControl
- Procgen
- Ablation Studies
- Retrieval outperforms sampling of experiences
- Reweighting Mechanism
- Retrieval Regularization
- Query Construction ; & Sequence Aggregation
- Placement of Cross-Attention Layers
- Interaction steps between context retrieval
- Effect of retrieval-augmentation on Training efficiency
- Effect of retrieval-augmentation on Inference efficiency
- Pre-trained Language Model
- Effect of $K$ on Algorithm Distillation
- Convergence of Baselines

## Tags
`benchmark` `transformers` `meta-rl` `exploration` `offline-rl` `memory` `action-models` `sequence-modeling`
