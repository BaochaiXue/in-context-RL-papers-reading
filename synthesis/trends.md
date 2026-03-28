# Trends

## Scope

This synthesis uses only:

- `./notes/papers/*.md`
- `./notes/tables/method_comparison.md`
- `./notes/tables/evidence_map.md`

It does **not** introduce new claims from raw PDFs.

## Evidence-backed trends

### Trend 1: The field has shifted from static policy extraction to explicit test-time adaptation

The center of gravity has moved away from one-shot offline policy imitation and toward agents that are expected to improve during deployment from interaction history alone. This is visible in the progression from Algorithm Distillation and DPT-style notes to AdA, AMAGO, AMAGO-2, OmniRL, ReLIC, and PSBL.

Evidence-backed signals:

- `notes/papers/in-context-reinforcement-learning-with-algorithm-distillation.md` frames the core object as a distilled learning algorithm rather than a frozen expert policy.
- `notes/papers/supervised-pretraining-can-learn-in-context-reinforcement-learning.md` and `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md` both treat the pretrained model as an online decision rule operating over context.
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`, `notes/papers/amago-scalable-in-context-reinforcement-learning-for-adaptive-agents.md`, and `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md` all emphasize multi-trial or lifelong adaptation.

Interpretation:

- The main research question is no longer “can sequence models act in RL?” but “what kind of adaptive algorithm can fixed weights execute in context?”

### Trend 2: Supervision is being weakened, but objective design is becoming more important

The literature is clearly moving away from the assumption that optimal labels or strong behavior policies are always available. At the same time, notes repeatedly show that weak supervision only works when the training objective and data pipeline encode the right inductive bias.

Evidence-backed signals:

- `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md` replaces optimal action labels with weighted pseudo-labels.
- `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md` uses random-policy data within trust horizons.
- `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md` improves performance through data filtering rather than architecture changes.
- `notes/papers/yes-q-learning-helps-offline-in-context-rl.md` argues that explicit RL objectives outperform pure next-action imitation.
- `notes/papers/pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning.md` shifts from optimal-action prediction to reward prediction.

Interpretation:

- The field is converging on a view that data quality, coverage, and objective alignment are inseparable; weaker supervision is viable only if the learning signal is reshaped around value, structure, or confidence.

### Trend 3: Memory engineering has become a first-class research problem

Recent notes no longer treat context length as a detail. Instead, long-horizon adaptation is being attacked through retrieval, curriculum, state-space models, Mamba hybrids, partial updates, and attention kernel engineering.

Evidence-backed signals:

- `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md` introduces explicit retrieval over sub-trajectories.
- `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md` centers its contribution on 64k-step contexts with partial updates and Sink-KV.
- `notes/papers/structured-state-space-models-for-in-context-reinforcement-learning.md`, `notes/papers/decision-mamba-reinforcement-learning-via-hybrid-selective-sequence-modeling.md`, and `notes/papers/xlstm-extended-long-short-term-memory.md` all target sequence efficiency.
- `notes/papers/cross-episodic-curriculum-for-transformer-agents.md` shows that context ordering itself is a curriculum variable.
- `notes/papers/flashattention-2-faster-attention-with-better-parallelism-and-work-partitioning.md` shows hardware-level acceleration entering the stack.

Interpretation:

- “More context” is no longer enough; the new competition is over how to compress, reorder, retrieve, and update context under finite compute.

### Trend 4: Scale and diversity help, but they also expose adaptation-length tradeoffs

Large task pools, procedurally generated worlds, and giant datasets have become central to the area, but the notes do not describe a monotonic story. More diversity often increases asymptotic capability while slowing or destabilizing fast adaptation.

Evidence-backed signals:

- `notes/papers/xland-100b-a-large-scale-multi-task-dataset-for-in-context-reinforcement-learning.md` explicitly notes depth-related degradation despite large-scale data.
- `notes/papers/omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds.md` highlights the tradeoff between diversity and adaptation period.
- `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md` reports scaling gains with model size, memory, and task-pool richness, but only in combination with curriculum and distillation.
- `notes/papers/vintix-action-model-via-in-context-reinforcement-learning.md` shows early cross-domain transfer, but still describes the work as a first step.

Interpretation:

- Scale is necessary but not sufficient. Diversity without explicit mechanisms for uncertainty and memory management appears to buy coverage at the cost of slower in-context convergence.

### Trend 5: LLM-style in-context learning and RL-style in-context adaptation are converging

There is now a visible merge between RL sequence modeling and LLM-based inference-time self-improvement. But the local notes also make clear that this convergence is fragile: reward can help, demonstrations can help, and prompting can help, but exploration and negative evidence remain unstable.

Evidence-backed signals:

- `notes/papers/llms-are-in-context-reinforcement-learners.md` shows contextual-bandit adaptation from rewards.
- `notes/papers/reward-is-enough-llms-are-in-context-reinforcement-learners.md` reports scalar-reward-driven self-improvement across general tasks.
- `notes/papers/can-large-language-models-explore-in-context.md` finds robust failure modes for native exploration.
- `notes/papers/evolve-evaluating-and-optimizing-llms-for-exploration.md` shows that algorithmic support and distilled demonstrations help more than raw history.
- `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md` documents a strong knowing-doing gap under long multimodal context.
- `notes/papers/training-a-generally-curious-agent.md` uses synthetic interaction data and curriculum to teach exploration directly.

Interpretation:

- The LLM frontier is increasingly relevant to ICRL, but current evidence suggests that raw sequence completion does not automatically yield robust adaptive control.

## Boundary between evidence and speculation

Evidence-backed:

- The five trends above are grounded in note content and supported by explicit note files.

Speculative but motivated:

- These trends jointly suggest that the next major step is unlikely to come from a single larger model or a single larger dataset.
- Instead, the likely leverage points are explicit algorithmic state, context compilation, uncertainty-aware adaptation, and stronger closed-loop evaluation.
