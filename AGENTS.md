# Repository purpose

This repo is a literature-to-proposal workspace.

The goal is to turn local papers in `./papers` into:

1. evidence-grounded paper notes,
2. cross-paper synthesis,
3. research directions,
4. a proposal PDF.

## Directory contract

- `papers/`: local paper folders and source PDFs
- `notes/papers/`: one markdown note per paper
- `notes/tables/`: comparison tables, inventories, and matrices
- `synthesis/`: trend summaries, gaps, rankings, and idea documents
- `proposal/`: LaTeX sources and compiled proposal artifacts
- `plans/`: task plans, milestones, and decision logs
- `cache/`: extracted text and lightweight parsing intermediates

## Grounding rules

- Never cite a paper unless you have read the local PDF end-to-end.
- Do not infer paper details from title or abstract alone.
- Every claim about a paper should be anchored when possible to a section, figure, table, experiment, or appendix.
- Separate evidence, interpretation, and speculation.
- If a PDF cannot be parsed reliably, say so explicitly and use a lightweight fallback.

## PDF handling rules

- `./papers` may contain both main paper PDFs and auxiliary figure PDFs.
- When extracting text, prefer one main PDF per paper folder rather than recursively processing every PDF.
- Prefer top-level PDFs in each paper directory.
- If multiple top-level PDFs exist, prefer filenames such as `paper.pdf`, `main.pdf`, `article.pdf`, or the shortest plausible manuscript filename.
- Use `pdftotext` when available; avoid adding heavy dependencies unless clearly necessary.
- Cache extracted text under `./cache` so later tasks can reuse it.

## Workflow rules

- For large tasks, first create or update a plan file under `./plans`.
- Do not write a global survey before per-paper notes exist.
- Reuse existing notes before re-reading papers.
- Keep diffs scoped and avoid unrelated edits.
- Do not delete user files unless explicitly asked.

## Reasoning policy

- For literature review, synthesis, proposal drafting, skeptical review, and research-planning tasks, default to the highest available reasoning setting (`reasoning_effort = xhigh`) for the main agent and any spawned subagents.
- Only reduce reasoning effort if the user explicitly asks for a faster/lighter pass or if a specific tool/model path does not support `xhigh`.

## Output quality

- Prefer concise markdown with explicit headings.
- Use comparison tables when synthesizing many papers.
- Research ideas must map to concrete gaps from local notes.
- Avoid generic ideas like "use more data" or "use a larger model" unless justified by a precise bottleneck.

## Proposal rules

- Proposal artifacts must be written under `./proposal`.
- Citations in the proposal must trace back to papers already read locally.
- If LaTeX is used, compile it and fix build errors until a PDF is produced.

## Done means

A task is not done unless the requested artifacts exist on disk and basic validation has been run.
