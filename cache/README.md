# Cache

This directory stores lightweight intermediate artifacts for local literature work.

## PDF text extraction

Use:

```bash
python3 cache/extract_paper_texts.py
```

Behavior:

- scans `./papers/*`
- chooses one main PDF per paper directory
- uses local `pdftotext`
- writes plain text outputs to `./cache/papers/`

It intentionally avoids recursive extraction of every figure PDF.

## Derived artifacts

- `derived/`
  Generated JSON summaries, reference-mining outputs, and other helper artifacts retained for reuse.

These files are cache-like intermediates, not canonical evidence outputs.
