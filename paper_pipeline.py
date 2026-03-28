#!/usr/bin/env python3

from __future__ import annotations

import argparse
import gzip
import re
import shutil
import subprocess
import sys
import tarfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

VERBATIM_ENVS = ("verbatim", "lstlisting", "minted", "Verbatim")


@dataclass(frozen=True)
class Paper:
    title: str
    url: str


PAPERS: list[Paper] = [
    Paper("In-Context Reinforcement Learning via Communicative World Models", "https://arxiv.org/abs/2508.06659"),
    Paper("Reward Is Enough: LLMs Are In-Context Reinforcement Learners", "https://arxiv.org/abs/2506.06303"),
    Paper("Filtering Learning Histories Enhances In-Context Reinforcement Learning", "https://arxiv.org/pdf/2505.15143"),
    Paper("OmniRL: In-Context Reinforcement Learning by Large-Scale Meta-Training in Randomized Worlds", "https://arxiv.org/abs/2502.02869"),
    Paper("A Survey of In-Context Reinforcement Learning", "https://arxiv.org/abs/2502.07978"),
    Paper("Yes, Q-learning Helps Offline In-Context RL", "https://arxiv.org/abs/2502.17666"),
    Paper("Vintix: Action Model via In-Context Reinforcement Learning", "https://arxiv.org/abs/2501.19400"),
    Paper("Training a Generally Curious Agent", "https://arxiv.org/abs/2502.17543"),
    Paper("LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations", "https://arxiv.org/abs/2412.01441"),
    Paper("Meta-Reinforcement Learning Robust to Distributional Shift Via Performing Lifelong In-Context Learning", "https://proceedings.mlr.press/v235/xu24o.html"),
    Paper("AMAGO-2: Breaking the Multi-Task Barrier in Meta-Reinforcement Learning with Transformers", "https://arxiv.org/abs/2411.11188"),
    Paper("LLMs Are In-Context Reinforcement Learners", "https://arxiv.org/abs/2410.05362"),
    Paper("EVOLvE: Evaluating and Optimizing LLMs For Exploration", "https://arxiv.org/abs/2410.06238"),
    Paper("Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models", "https://arxiv.org/abs/2410.01280"),
    Paper("ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI", "https://arxiv.org/abs/2410.02751"),
    Paper("Retrieval-Augmented Decision Transformer: External Memory for In-context RL", "https://arxiv.org/abs/2410.07071"),
    Paper("Random Policy Enables In-Context Reinforcement Learning within Trust Horizons", "https://arxiv.org/pdf/2410.19982"),
    Paper("Artificial Generational Intelligence: Cultural Accumulation in Reinforcement Learning", "https://arxiv.org/abs/2406.00392"),
    Paper("XLand-100B: A Large-Scale Multi-Task Dataset for In-Context Reinforcement Learning", "https://arxiv.org/abs/2406.08973"),
    Paper("Decision Mamba: Reinforcement Learning via Hybrid Selective Sequence Modeling", "https://arxiv.org/abs/2406.00079"),
    Paper("Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning", "https://arxiv.org/abs/2406.05064"),
    Paper("Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning", "https://arxiv.org/abs/2405.13861"),
    Paper("In-Context Decision Transformer: Reinforcement Learning via Hierarchical Chain-of-Thought", "https://arxiv.org/abs/2405.20692"),
    Paper("In-Context Reinforcement Learning Without Optimal Action Labels", "https://openreview.net/forum?id=8Dey9wo2qA"),
    Paper("Can Large Language Models Explore In-Context?", "https://arxiv.org/abs/2403.15371"),
    Paper("Large Language Models As Evolution Strategies", "https://arxiv.org/abs/2402.18381"),
    Paper("Generalization to New Sequential Decision Making Tasks with In-Context Learning", "https://arxiv.org/abs/2312.03801"),
    Paper("Emergence of In-Context Reinforcement Learning from Noise Distillation", "https://arxiv.org/abs/2312.12275"),
    Paper("In-Context Reinforcement Learning for Variable Action Spaces", "https://arxiv.org/abs/2312.13327"),
    Paper("AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents", "https://arxiv.org/abs/2310.09971"),
    Paper("Cross-Episodic Curriculum for Transformer Agents", "https://arxiv.org/abs/2310.08549"),
    Paper("Transformers as Decision Makers: Provable In-Context Reinforcement Learning via Supervised Pretraining", "https://arxiv.org/abs/2310.08566"),
    Paper("Large Language Models as General Pattern Machines", "https://arxiv.org/abs/2307.04721"),
    Paper("First-Explore, then Exploit: Meta-Learning Intelligent Exploration", "https://arxiv.org/abs/2307.02276"),
    Paper("Supervised Pretraining Can Learn In-Context Reinforcement Learning", "https://arxiv.org/abs/2306.14892"),
    Paper("Structured State Space Models for In-Context Reinforcement Learning", "https://arxiv.org/abs/2303.03982"),
    Paper("Human-Timescale Adaptation in an Open-Ended Task Space", "https://arxiv.org/abs/2301.07608"),
    Paper("Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration", "https://arxiv.org/abs/2302.04250"),
    Paper("Towards General-Purpose In-Context Learning Agents", "https://openreview.net/forum?id=zDTqQVGgzH"),
    Paper("In-context Reinforcement Learning with Algorithm Distillation", "https://arxiv.org/abs/2210.14215"),
    Paper("Large Language Models can Implement Policy Iteration", "https://arxiv.org/abs/2210.03821"),
]


def log(message: str) -> None:
    print(message, flush=True)


def sanitize_name(name: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "", name)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or "untitled"


def safe_stem(url: str) -> str:
    parsed = urlparse(url)
    basename = Path(parsed.path).name or "download"
    return re.sub(r"[^A-Za-z0-9._-]+", "_", basename)


def request_bytes(url: str) -> bytes:
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=120) as response:
        return response.read()


def download_file(url: str, target: Path) -> None:
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=120) as response, target.open("wb") as fh:
        shutil.copyfileobj(response, fh)


def arxiv_id_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if "arxiv.org" not in parsed.netloc:
        return None
    path = parsed.path.strip("/")
    if path.startswith("abs/"):
        return path.split("/", 1)[1]
    if path.startswith("pdf/"):
        tail = path.split("/", 1)[1]
        return tail.removesuffix(".pdf")
    return None


def ensure_empty_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def detect_file_kind(path: Path) -> str:
    result = subprocess.run(
        ["file", "-b", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip().lower()


def extract_archive(archive: Path, destination: Path) -> None:
    kind = detect_file_kind(archive)
    if tarfile.is_tarfile(archive):
        with tarfile.open(archive) as tf:
            tf.extractall(destination)
        return
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(destination)
        return
    if "gzip compressed data" in kind:
        try:
            with tarfile.open(archive, mode="r:gz") as tf:
                tf.extractall(destination)
            return
        except tarfile.ReadError:
            target = destination / "source.tex"
            with gzip.open(archive, "rb") as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            return
    raise ValueError(f"Unsupported archive format for {archive}: {kind}")


def flatten_single_top_level_dir(destination: Path) -> None:
    items = list(destination.iterdir())
    if len(items) != 1 or not items[0].is_dir():
        return
    only_dir = items[0]
    temp_dir = destination.with_name(destination.name + "__tmp_flatten")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    only_dir.rename(temp_dir)
    destination.rmdir()
    destination.mkdir(parents=True, exist_ok=True)
    for child in temp_dir.iterdir():
        shutil.move(str(child), destination / child.name)
    temp_dir.rmdir()


def normalize_extracted_tree(destination: Path) -> None:
    flatten_single_top_level_dir(destination)


def find_tex_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*.tex")
        if p.is_file() and p.name != "merged_paper.tex"
    )


def score_main_tex(path: Path, text: str) -> tuple[int, int, int]:
    stem_bonus = 0 if path.stem.lower() in {"main", "paper", "ms", "article"} else 1
    docclass_bonus = 0 if "\\documentclass" in text else 1
    begin_bonus = 0 if "\\begin{document}" in text else 1
    return (docclass_bonus, begin_bonus, stem_bonus)


def choose_main_tex(tex_files: Iterable[Path]) -> Path | None:
    candidates: list[tuple[tuple[int, int, int], Path]] = []
    for path in tex_files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "\\documentclass" in text or "\\begin{document}" in text:
            candidates.append((score_main_tex(path, text), path))
    if candidates:
        candidates.sort(key=lambda item: (item[0], str(item[1])))
        return candidates[0][1]

    files = list(tex_files)
    return files[0] if files else None


def remove_comments_and_blank_lines(text: str) -> str:
    begin_pattern = re.compile(r"\\begin\{(" + "|".join(re.escape(env) for env in VERBATIM_ENVS) + r")\}")
    end_pattern = re.compile(r"\\end\{(" + "|".join(re.escape(env) for env in VERBATIM_ENVS) + r")\}")
    cleaned_lines: list[str] = []
    in_verbatim = False

    for raw_line in text.splitlines():
        line = raw_line
        if in_verbatim:
            cleaned = line.rstrip()
            if cleaned.strip():
                cleaned_lines.append(cleaned)
            if end_pattern.search(line):
                in_verbatim = False
            continue

        if begin_pattern.search(line):
            in_verbatim = True
            cleaned = line.rstrip()
            if cleaned.strip():
                cleaned_lines.append(cleaned)
            continue

        result_chars: list[str] = []
        escaped = False
        for char in line:
            if char == "%" and not escaped:
                break
            result_chars.append(char)
            escaped = (char == "\\") and not escaped
            if char != "\\":
                escaped = False

        cleaned = "".join(result_chars).rstrip()
        if cleaned.strip():
            cleaned_lines.append(cleaned)

    return "\n".join(cleaned_lines).strip() + "\n"


INPUT_PATTERN = re.compile(
    r"\\(input|include)\s*\{([^}]+)\}"
)


def resolve_include(base_dir: Path, include_ref: str) -> Path | None:
    candidate = (base_dir / include_ref).resolve()
    candidates = [candidate]
    if candidate.suffix != ".tex":
        candidates.append(candidate.with_suffix(".tex"))
    for item in candidates:
        if item.exists() and item.is_file():
            return item
    return None


def inline_tex(path: Path, visited: set[Path]) -> str:
    real = path.resolve()
    if real in visited:
        return f"% Skipped recursive include: {path.name}\n"
    visited.add(real)

    try:
        raw = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""

    output_parts: list[str] = []
    idx = 0
    for match in INPUT_PATTERN.finditer(raw):
        output_parts.append(raw[idx:match.start()])
        include_target = resolve_include(path.parent, match.group(2).strip())
        if include_target is None:
            output_parts.append(match.group(0))
        else:
            output_parts.append(inline_tex(include_target, visited))
        idx = match.end()
    output_parts.append(raw[idx:])
    visited.remove(real)
    return "".join(output_parts)


def build_merged_tex(paper_dir: Path) -> Path | None:
    tex_files = find_tex_files(paper_dir)
    if not tex_files:
        return None

    main_tex = choose_main_tex(tex_files)
    if main_tex is None:
        return None

    merged_text = inline_tex(main_tex, set())
    cleaned_text = remove_comments_and_blank_lines(merged_text)
    merged_path = paper_dir / "merged_paper.tex"
    merged_path.write_text(cleaned_text, encoding="utf-8")
    return merged_path


def openreview_pdf_url(url: str) -> str:
    parsed = urlparse(url)
    query = parsed.query
    if parsed.path.endswith("/pdf"):
        return url
    return f"https://openreview.net/pdf?{query}"


def pmlr_pdf_url(url: str) -> str:
    html = request_bytes(url).decode("utf-8", errors="ignore")
    match = re.search(r'citation_pdf_url"\s+content="([^"]+)"', html)
    if match:
        return match.group(1)
    match = re.search(r'href="([^"]+\.pdf)"', html)
    if match:
        return match.group(1)
    raise ValueError(f"Could not locate PDF URL on PMLR page: {url}")


def download_arxiv_source(paper: Paper, work_dir: Path) -> tuple[Path, bool]:
    arxiv_id = arxiv_id_from_url(paper.url)
    if arxiv_id is None:
        raise ValueError("Not an arXiv URL")

    archive = work_dir / f"{arxiv_id.replace('/', '_')}.src"
    download_file(f"https://arxiv.org/e-print/{arxiv_id}", archive)
    if archive.stat().st_size == 0:
        raise ValueError(f"Empty arXiv source for {paper.title}")
    extract_archive(archive, work_dir)
    archive.unlink(missing_ok=True)
    return work_dir, True


def download_pdf_only(paper: Paper, work_dir: Path) -> tuple[Path, bool]:
    parsed = urlparse(paper.url)
    if "openreview.net" in parsed.netloc:
        pdf_url = openreview_pdf_url(paper.url)
    elif "proceedings.mlr.press" in parsed.netloc:
        pdf_url = pmlr_pdf_url(paper.url)
    elif "arxiv.org" in parsed.netloc:
        arxiv_id = arxiv_id_from_url(paper.url)
        if arxiv_id is None:
            raise ValueError(f"Cannot derive arXiv pdf URL for {paper.url}")
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    else:
        pdf_url = paper.url

    target = work_dir / f"{safe_stem(pdf_url)}.pdf"
    download_file(pdf_url, target)
    return target, False


def process_paper(paper: Paper, papers_root: Path) -> tuple[str, bool, bool]:
    folder_name = sanitize_name(paper.title)
    destination = papers_root / folder_name
    ensure_empty_dir(destination)

    downloaded_source = False
    merged_created = False
    try:
        if arxiv_id_from_url(paper.url):
            try:
                _, downloaded_source = download_arxiv_source(paper, destination)
                normalize_extracted_tree(destination)
            except (HTTPError, URLError, ValueError, tarfile.TarError, OSError) as exc:
                log(f"[WARN] Source download failed for '{paper.title}': {exc}. Falling back to PDF.")
                ensure_empty_dir(destination)
                download_pdf_only(paper, destination)
        else:
            download_pdf_only(paper, destination)

        merged_path = build_merged_tex(destination)
        merged_created = merged_path is not None
        return paper.title, downloaded_source, merged_created
    except Exception:
        shutil.rmtree(destination, ignore_errors=True)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--title",
        action="append",
        dest="titles",
        help="Process only papers whose title exactly matches this value. Repeatable.",
    )
    parser.add_argument(
        "--rebuild-merged-only",
        action="store_true",
        help="Only rebuild merged_paper.tex in existing paper directories.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    papers_root = ROOT / "papers"
    papers_root.mkdir(parents=True, exist_ok=True)

    papers = PAPERS
    if args.titles:
        title_set = set(args.titles)
        papers = [paper for paper in PAPERS if paper.title in title_set]

    results: list[tuple[str, bool, bool]] = []
    failures: list[tuple[str, str]] = []

    for index, paper in enumerate(papers, start=1):
        log(f"[{index}/{len(papers)}] {paper.title}")
        try:
            if args.rebuild_merged_only:
                destination = papers_root / sanitize_name(paper.title)
                if not destination.exists():
                    raise FileNotFoundError(f"Paper directory not found: {destination}")
                merged_path = build_merged_tex(destination)
                result = (paper.title, False, merged_path is not None)
            else:
                result = process_paper(paper, papers_root)
            results.append(result)
            source_flag = "source" if result[1] else "pdf"
            merged_flag = "merged" if result[2] else "no-merged"
            log(f"  -> {source_flag}, {merged_flag}")
        except Exception as exc:
            failures.append((paper.title, str(exc)))
            log(f"  -> FAILED: {exc}")

    log("")
    log("Summary:")
    log(f"  processed: {len(results)}")
    log(f"  failed: {len(failures)}")
    for title, error in failures:
        log(f"  - {title}: {error}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
