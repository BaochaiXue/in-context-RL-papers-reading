# Paper Notes Rollout

## Goal

Create one grounded note per paper folder under `./notes/papers`, plus inventory and evidence artifacts under `./notes/tables`, without writing a global survey yet.

## Steps

1. Enumerate all paper folders and all PDFs under `./papers`.
2. Reuse cached text extraction under `./cache/papers` where available.
3. Use `merged_paper.tex` as the primary source when a folder has source text but no main PDF.
4. Refresh or repair one note per paper folder with:
   - full citation
   - 5-bullet thesis
   - problem setting
   - method summary
   - datasets / benchmarks / tasks
   - strongest results
   - failure modes or limitations
   - evidence anchors
   - tags
5. Generate:
   - `notes/tables/paper_inventory.csv`
   - `notes/tables/method_comparison.md`
   - `notes/tables/evidence_map.md`
6. Validate:
   - one note per paper folder
   - every PDF maps to exactly one note in the inventory
   - unresolved parsing issues are explicitly listed

## Current session focus

- Scope: improve the evidence quality of `notes/papers/*.md` without writing any global survey.
- Execution mode: parallel `paper_reader` batches over disjoint paper sets; main thread merges and validates.
- Named-skill fallback: `$read-paper` is not available in this repo, so the equivalent workflow is manual PDF/source verification plus cache reuse.

## Batch strategy

- Partition unique note slugs from `notes/tables/paper_inventory.csv` into disjoint batches.
- Each batch must:
  - verify cached text against the local PDF when a main PDF exists;
  - fall back to local source files when the inventory marks the paper as `source-only`;
  - return repaired note content plus explicit parse gaps.

## Validation gate for this run

- Every unique `note_slug` in the inventory must map to exactly one note file under `notes/papers/`.
- Every note must contain all required sections.
- A note built from imperfect parsing must say exactly what is missing.
- Global missing-note and parse-issue lists must be explicit in `notes/tables/evidence_map.md`.
