# Bilingual Proposal Rollout

## Goal

Draft a bilingual research proposal for `in-context-rl` with:

- an English original
- a faithful Chinese translation that preserves English terminology

## Inputs

- `AGENTS.md`
- `synthesis/in-context-rl/*.md`
- `proposal/in-context-rl/specific_aims.md`
- `notes/claims/in-context-rl/*.yaml`
- `notes/papers/*.md`

## Outputs

- `proposal/in-context-rl/main_en.md`
- `proposal/in-context-rl/main_zh.md`
- `proposal/in-context-rl/references.bib`
- `proposal/in-context-rl/README.md`

## Rules

- Draft the English original first.
- Keep the Chinese translation structurally aligned with the English original.
- Preserve English terminology in the Chinese version.
- Cite only locally read papers.
- Do not invent references or citation keys.
- Do not overclaim beyond the local evidence.

## Validation gate

- Both language versions exist.
- Required sections exist in both versions:
  - Title
  - Abstract
  - Introduction
  - Literature Review and Research Gaps
  - Specific Aims / Three Pillars
  - Methodology and System Design
  - Evaluation Plan
  - Risks and Alternatives
  - Expected Outcomes
  - Timeline
  - Bibliography
- Citation keys used in the drafts resolve in `proposal/in-context-rl/references.bib`.
- The Chinese version remains a faithful translation rather than a rewritten variant.
