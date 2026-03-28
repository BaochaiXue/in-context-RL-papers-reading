# Research Agenda Rollout

## Goal

Turn the topic-scoped synthesis for `in-context-rl` into a coherent research agenda rather than a mechanical combination of methods.

## Inputs

- `synthesis/in-context-rl/*.md`
- `notes/claims/in-context-rl/*.yaml`
- `notes/papers/*.md`
- `notes/tables/*.md`

## Outputs

- `synthesis/in-context-rl/research_directions.md`
- `synthesis/in-context-rl/idea_ranking.md`
- `proposal/in-context-rl/specific_aims.md`

## Rules

- Propose `3-5` candidate agendas.
- Compare agendas on:
  - `novelty`
  - `coherence`
  - `feasibility`
  - `leverage`
- Select one strongest agenda.
- Reject mechanical A+B stitching.
- Each selected aim must connect:
  - bottom mechanism
  - methodology / architecture
  - closed-loop system validation
- Every agenda and aim must be grounded in local notes and claim IDs.

## Validation gate

- All output files exist.
- The selected agenda is clearly chosen from the candidate set.
- Every aim lists:
  - scientific question
  - core hypothesis
  - why prior work is insufficient
  - approach sketch
  - main risks
  - fallback plan
  - supporting note files and claim IDs
- Referenced claim IDs resolve to the local claim ledger.
