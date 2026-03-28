# Filtering Learning Histories Enhances In-Context Reinforcement Learning

- Paper folder: `papers/Filtering Learning Histories Enhances In-Context Reinforcement Learning`
- Note slug: `filtering-learning-histories-enhances-in-context-reinforcement-learning`

## Full citation
Weiqin Chen, Xinjie Zhang, Dharmashankar Subramanian, Santiago Paternain. Filtering Learning Histories Enhances In-Context Reinforcement Learning. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Filtering Learning Histories Enhances In-Context Reinforcement Learning/arxiv_neurips.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Transformer models (TMs) have exhibited remarkable in-context reinforcement learning (ICRL) capabilities, allowing them to generalize to and improve in previously unseen environments without re-training or fine-tuning. This is typically accomplished by imitating the complete learning histories of a source RL algorithm over a substantial amount of pretraining environments, which, however, may transfer suboptimal behaviors inherited from the source algorithm/dataset.
- Core mechanism: 按 history 的 improvement 与 stability 进行重加权/过滤，是典型 data-centric ICRL 插件。
- Primary bottleneck: 瓶颈在于过滤准则仍是启发式，尚缺少专门针对 ICRL generalization error 的理论。
- Evaluated on: 在 DarkRoom 系列和 Meta-World ML1 机械臂任务上，与 AD、DICP、DPT 等 backbone 对比回报和鲁棒性。
- Key failure mode: discussion 明确指出还没覆盖 safe RL；在安全关键场景里，仅按 reward-history 过滤不够。

## Problem setting
Transformer models (TMs) have exhibited remarkable in-context reinforcement learning (ICRL) capabilities, allowing them to generalize to and improve in previously unseen environments without re-training or fine-tuning. This is typically accomplished by imitating the complete learning histories of a source RL algorithm over a substantial amount of pretraining environments, which, however, may transfer suboptimal behaviors inherited from the source algorithm/dataset. Therefore, in this work, we address the issue of inheriting suboptimality from the perspective of dataset preprocessing.

## Method summary
按 history 的 improvement 与 stability 进行重加权/过滤，是典型 data-centric ICRL 插件。

## Datasets / tasks / benchmarks
在 DarkRoom 系列和 Meta-World ML1 机械臂任务上，与 AD、DICP、DPT 等 backbone 对比回报和鲁棒性。

## Strongest results
We substantiate the efficacy of our LHF approach across a diverse set of environments, which are commonly considered in ICRL literature~ . These environments include discrete settings such as Darkroom, Darkroom-Permuted, Darkroom-Large, Dark Key-to-Door and continuous robotic manipulation tasks from the Meta-World-ML1 benchmark like Reach, Reach-Wall, Button-Press, Basketball, Door-Unlock, Push, Soccer, Hand-Insert . All these problems are challenging to solve in-context, as the test environments differ from the pretraining environments, while the parameters of the TM remain frozen during the test. The environmental setup is detailed in Appendix~REF.

## Failure modes or limitations
discussion 明确指出还没覆盖 safe RL；在安全关键场景里，仅按 reward-history 过滤不够。

## Evidence anchors
- Introduction
- Related Work
- In-Context Reinforcement Learning
- Learning History Filtering
- Experiments
- Collecting and Filtering Learning Histories
- Backbone ICRL Algorithms
- Numerical Results
- Sensitivity Analysis
- Discussion
- Acknowledgement
- Implementation and Experiment Details
- Collecting Learning Histories
- Backbone ICRL Algorithms
- Transformer Models
- Complete Process of ICRL via Learning History Filtering (LHF)
- Environmental Setup
- Additional Experimental Results
- ICRL with partial learning histories
- ICRL with lightweight models
- Sensitivity analysis with respect to source RL algorithm
- Computing Infrastructure
- Code

## Tags
`benchmark` `transformers` `meta-rl` `memory` `icrl` `safety`
