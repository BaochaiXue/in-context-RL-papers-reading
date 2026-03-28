# xland-100B: a large-scale multi-task dataset for in-context reinforcement learning

- Paper folder: `papers/XLand-100B A Large-Scale Multi-Task Dataset for In-Context Reinforcement Learning`
- Note slug: `xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning`

## Full citation
Alexander Nikulin, Ilya Zisman, Alexey Zemtsov, NUST MISIS, Vladislav Kurenkov. xland-100B: a large-scale multi-task dataset for in-context reinforcement learning. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/XLand-100B A Large-Scale Multi-Task Dataset for In-Context Reinforcement Learning/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Following the success of the in-context learning paradigm in large-scale language and computer vision models, the recently emerging field of in-context reinforcement learning is experiencing a rapid growth. However, its development has been held back by the lack of challenging benchmarks, as all the experiments have been carried out in simple environments and on small-scale datasets.
- Core mechanism: 提供 100B transition 的大规模 ICRL 数据集和采样工具，降低超大规模预训练门槛。
- Primary bottleneck: 尽管任务数很大，但 observation/action space 仍单一，且 latent structure 共享。
- Evaluated on: 数据集是 XLand-Trivial-20B 与 XLand-100B；用 AD、DPT 在 unseen tasks 上测平均 return 与 policy improvement。
- Key failure mode: 作者明确写到：缺少跨 domain 多样性，而且 AD 会随 ruleset 深度上升明显退化。

## Problem setting
Following the success of the in-context learning paradigm in large-scale language and computer vision models, the recently emerging field of in-context reinforcement learning is experiencing a rapid growth. However, its development has been held back by the lack of challenging benchmarks, as all the experiments have been carried out in simple environments and on small-scale datasets. We present XLand-100B , a large-scale dataset for in-context reinforcement learning based on the XLand-MiniGrid environment, as a first step to alleviate this problem.

## Method summary
提供 100B transition 的大规模 ICRL 数据集和采样工具，降低超大规模预训练门槛。

## Datasets / tasks / benchmarks
数据集是 XLand-Trivial-20B 与 XLand-100B；用 AD、DPT 在 unseen tasks 上测平均 return 与 policy improvement。

## Strongest results
In this section, we investigate whether our datasets can enable an in-context RL ability. Additionally, we demonstrate how well current in-context algorithms perform across different task complexities and outline their current limitations. We take AD and DPT for our experiments, the exact implementations details are in apndx:ad and apndx:dpt . Both methods were trained on XLand-Trivial-20B and XLand-100B with and context lengths respectively.

## Failure modes or limitations
作者明确写到：缺少跨 domain 多样性，而且 AD 会随 ruleset 深度上升明显退化。

## Evidence anchors
- Introduction
- Background
- In-Context Reinforcement Learning
- XLand-MiniGrid
- The Missing Piece For In-Context RL
- XLand-100B Dataset
- Data Format
- Data Collection
- Data Evaluation
- Experiments
- Limitations and Future Work
- Ethics Statement
- Reproducibility Statement
- Downloading the Datasets
- What is Inside Dataset?
- Compression Chunk Size Tuning
- Additional Figures of Data Collection
- Additional Figures of Data Evaluation
- AD Implementation
- DPT Implementation
- On DPT Limitations in POMDP
- Details of In-Context Evaluation
- Additional Figures of AD Performance
- Additional Figures of DPT Performance
- Rulesets Vizualization
- Grid Layouts Used for Dataset Collection
- Additional experiments on number of tasks
- Hyperparameters

## Tags
`benchmark` `meta-rl` `memory` `action-models` `icrl`
