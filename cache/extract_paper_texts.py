#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
CACHE_DIR = ROOT / "cache" / "papers"
PREFERRED_NAMES = ("paper", "main", "article", "manuscript")


def choose_main_pdf(paper_dir: Path) -> Path | None:
    top_level = sorted(paper_dir.glob("*.pdf"))
    if not top_level:
        return None

    def rank(path: Path) -> tuple[int, int, int, str]:
        stem = path.stem.lower()
        preferred = 0 if stem in PREFERRED_NAMES else 1
        depth = len(path.relative_to(paper_dir).parts)
        return (preferred, depth, len(path.name), path.name.lower())

    return sorted(top_level, key=rank)[0]


def extract_pdf(pdf_path: Path, out_path: Path) -> tuple[bool, str]:
    cmd = shutil.which("pdftotext")
    if not cmd:
        return False, "pdftotext not found"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [cmd, str(pdf_path), str(out_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip() or "pdftotext failed"
    return True, "ok"


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    failures: list[tuple[str, str]] = []

    for paper_dir in sorted(p for p in PAPERS_DIR.iterdir() if p.is_dir()):
        pdf = choose_main_pdf(paper_dir)
        if pdf is None:
            failures.append((paper_dir.name, "no pdf found"))
            continue
        out_path = CACHE_DIR / f"{paper_dir.name}.txt"
        ok, msg = extract_pdf(pdf, out_path)
        if ok:
            print(f"[ok] {paper_dir.name} -> {out_path.relative_to(ROOT)}")
        else:
            failures.append((paper_dir.name, msg))
            print(f"[fail] {paper_dir.name}: {msg}")

    if failures:
        print("\nFailures:")
        for name, msg in failures:
            print(f"- {name}: {msg}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
