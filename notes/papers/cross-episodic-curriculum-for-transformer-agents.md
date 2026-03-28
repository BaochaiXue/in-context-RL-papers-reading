# Cross-Episodic Curriculum for Transformer Agents

- Paper folder: `papers/Cross-Episodic Curriculum for Transformer Agents`
- Note slug: `cross-episodic-curriculum-for-transformer-agents`

## Full citation
Lucy Xiaoyang Shi, Yunfan Jiang, Jake Grigsby, Linxi Fan, Yuke Zhu. Cross-Episodic Curriculum for Transformer Agents. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Cross-Episodic Curriculum for Transformer Agents/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: We present a new algorithm, Cross-Episodic Curriculum ( ), to boost the learning efficiency and generalization of Transformer agents. Central to is the placement of cross-episodic experiences into a Transformer’s context, which forms the basis of a curriculum.
- Core mechanism: 把不同 episode 的经验按“能力成长顺序”组织进上下文，形成 cross-episodic curriculum。
- Primary bottleneck: 关键瓶颈是 curricular sequence 的构造质量；如果序列不反映真实能力演进，Transformer 的优势发挥不出来。
- Evaluated on: 在 DeepMind Lab 多任务 RL 和 RoboMimic imitation 上与不做 curriculum 的 Transformer agent 对比样本效率与泛化。
- Key failure mode: 结论里明确指出该法依赖准确的 curricular formulation；劣质或错误顺序的 demonstration 会削弱效果。

## Problem setting
We present a new algorithm, Cross-Episodic Curriculum ( ), to boost the learning efficiency and generalization of Transformer agents. Central to is the placement of cross-episodic experiences into a Transformer’s context, which forms the basis of a curriculum. By sequentially structuring online learning trials and mixed-quality demonstrations, constructs curricula that encapsulate learning progression and proficiency increase across episodes.

## Method summary
把不同 episode 的经验按“能力成长顺序”组织进上下文，形成 cross-episodic curriculum。

## Datasets / tasks / benchmarks
在 DeepMind Lab 多任务 RL 和 RoboMimic imitation 上与不做 curriculum 的 Transformer agent 对比样本效率与泛化。

## Strongest results
fig/dmlab_main We aim to answer the following four research questions through comprehensive experiments. enumerate To what extent can our cross-episodic curriculum increase the sample efficiency of Transformer agents and boost their generalization capability? Is CEC consistently effective and generally applicable across distinct learning settings? What are the major components that contribute to the effectiveness of our method?

## Failure modes or limitations
结论里明确指出该法依赖准确的 curricular formulation；劣质或错误顺序的 demonstration 会削弱效果。

## Evidence anchors
- Introduction
- Cross-Episodic Curriculum: Formalism and Implementations
- Preliminaries
- Curricular Data Assembly and Model Optimization
- Practical Implementations
- Experimental Setup
- Task Settings and Environments
- Baselines
- Training and Evaluation
- Experiments
- Main Evaluations
- Ablation Studies
- Related Work
- Conclusion

## Tags
`benchmark` `transformers` `meta-rl` `memory` `sequence-modeling`
