# Lmact A Benchmark For In Context Imitation Learning With Long Multimodal Demonstrations

- Paper folder: `papers/LMAct A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations`
- Note slug: `lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations`

## Full citation
Authors could not be extracted reliably from the local source. Lmact A Benchmark For In Context Imitation Learning With Long Multimodal Demonstrations. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/LMAct A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: In this paper, we present a benchmark to pressure-test today's frontier models' multimodal decision-making capabilities in the very long-context regime (up to one million tokens) and investigate whether these models can learn from large numbers of expert demonstrations in their context. We evaluate the performance of , , , , , , , and as policies across a battery of simple interactive decision-making tasks: playing tic-tac-toe, chess, and Atari, navigating grid worlds, solving crosswords, and controlling a simulated cheetah.
- Core mechanism: 构建超长上下文、多模态 demonstration 的 decision-making benchmark，专门测“知道规则但不会做”的 know-how gap。
- Primary bottleneck: 瓶颈不是上下文长度本身，而是模型无法把海量演示转化成可执行策略。
- Evaluated on: 任务包括 tic-tac-toe、chess、Atari、grid world、crossword、cheetah；核心 baseline 是多种 frontier multimodal LMs 在不同 demo 数下的得分。
- Key failure mode: 即便给数百条 demonstration 和百万 token 上下文，模型通常仍达不到专家水平；很多任务上更多 demo 几乎没帮助。

## Problem setting
In this paper, we present a benchmark to pressure-test today's frontier models' multimodal decision-making capabilities in the very long-context regime (up to one million tokens) and investigate whether these models can learn from large numbers of expert demonstrations in their context. We evaluate the performance of , , , , , , , and as policies across a battery of simple interactive decision-making tasks: playing tic-tac-toe, chess, and Atari, navigating grid worlds, solving crosswords, and controlling a simulated cheetah. We study increasing amounts of expert demonstrations in the context --- from no demonstrations to 512 full episodes.

## Method summary
构建超长上下文、多模态 demonstration 的 decision-making benchmark，专门测“知道规则但不会做”的 know-how gap。 We now describe the models we evaluate~( sec:methods:models ), our benchmark environments~( sec:methods:environments ), our prompt~( sec:methods:prompt ), and our evaluation protocol~( sec:methods:evaluation-protocol ). Full details in app:experimental-details . We now briefly describe the models we evaluate~( sec:methods:models ), our benchmark environments~( sec:methods:environments ), how we construct the prompt~( sec:methods:prompt ), and our evaluation protocol~( sec:methods:evaluation-protocol ). Full details are given in app:experimental-details .

## Datasets / tasks / benchmarks
任务包括 tic-tac-toe、chess、Atari、grid world、crossword、cheetah；核心 baseline 是多种 frontier multimodal LMs 在不同 demo 数下的得分。

## Strongest results
We now present our comprehensive empirical evaluation of the (closed-source) frontier models on our benchmark for interactive decision-making with long multimodal context. We investigate how performance changes when presenting more demonstration episodes in the context (see sec:methods:environments for a task overview and app:experimental-details:environments for details and illustrations). For each model and task, we first ablate whether to use chain-of-thought prompting and whether to show the legal actions in the prompt (results in app:additional-results:ablations ). We use one demonstration episode ( still many individual demonstration steps) for these ablations, as a compromise between lower computational demands and being representative of the in-context learning setting.

## Failure modes or limitations
即便给数百条 demonstration 和百万 token 上下文，模型通常仍达不到专家水平；很多任务上更多 demo 几乎没帮助。

## Evidence anchors
- Introduction
- Methods
- Models
- Environments
- Prompt
- Evaluation Protocol
- Results
- Best Scores Per Model/Task
- In-Context Imitation Learning
- Discussion ; & Related Work
- Conclusion
- Impact Statement
- Acknowledgments
- Related Work
- Experimental Details
- Models
- Environments
- Prompts
- Additional Results
- Ablating the Maximum Sample Length
- Replaying a Demonstration Episode
- Illegal Actions
- Hyperparameter Ablations
- Including Past Actions

## Tags
`benchmark` `meta-rl` `memory` `multimodal` `action-models`
