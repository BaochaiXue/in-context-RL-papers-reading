# Bilingual Proposal Draft

## Files

- `main_en.md`: English original
- `main_zh.md`: faithful Chinese translation
- `references.bib`: shared bibliography for both drafts
- `specific_aims.md`: agenda-to-aims bridge used as the direct drafting input

## Grounding

- The drafts are grounded in:
  - `synthesis/in-context-rl/*.md`
  - `proposal/in-context-rl/specific_aims.md`
  - `notes/claims/in-context-rl/*.yaml`
  - `notes/papers/*.md`
- No citations were introduced beyond locally read papers already represented in the note layer.

## Language policy

- `main_en.md` is the canonical original.
- `main_zh.md` is a faithful translation of `main_en.md`.
- The Chinese version preserves English terminology such as `algorithmic state`, `experience compilation`, `belief-calibrated adaptation`, `distribution shift`, `retrieval`, `calibration`, and `abstention`.

## Citation policy

- Citation keys in both drafts use Pandoc-style `[@key]` notation.
- All keys used in the drafts resolve in `references.bib`.
- The bibliography is traceable to local notes and existing repository references only.

## Build note

- This delivery is a bilingual proposal draft in Markdown, not yet a compiled LaTeX/PDF artifact.
- If needed, the next step is to convert `main_en.md` and `main_zh.md` into aligned `main_en.tex` and `main_zh.tex`, then compile both PDFs against the shared `references.bib`.
