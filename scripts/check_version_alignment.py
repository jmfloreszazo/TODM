#!/usr/bin/env python3
"""Assert that the public TODM paper, demo, citation and release are v1.4.0."""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--allow-uncompiled-pdf", action="store_true", help="PR checks do not require the generated PDF to be current")
args = parser.parse_args()
errors = []

def expect(path: str, fragments: tuple[str, ...] = ()) -> None:
    file = ROOT / path
    if not file.is_file() or file.stat().st_size == 0:
        errors.append(f"Missing or empty: {path}")
        return
    if fragments:
        content = file.read_text(encoding="utf-8")
        for fragment in fragments:
            if fragment not in content:
                errors.append(f"{path}: missing expected text {fragment!r}")

expect("VERSION", ("1.4.0",))
expect("CITATION.cff", ('version: "1.4.0"', "todm-research-v1.4.0/TODM_Paper_v1.4.pdf"))
expect("README.md", ("TODM_Paper_v1.4.pdf", "TODM_Paper_v1.4.md", "full demo v1.4", "todm-research-v1.4.0"))
expect("paper/source/main.tex", ("Research artifact companion, v1.4",))
expect("paper/TODM_Paper_v1.4.md", ("version 1.4",))
expect("paper/README.md", ("TODM_Paper_v1.4.pdf", "TODM_Paper_v1.4.md"))
expect("demo/README.md", ("Research Artifact v1.4", "reproducibility-v1.4.json"))
expect("demo/scripts/reproduce.py", ("'version':'1.4.0'", "reproducibility-v1.4.json", "'profileSchemaVersion':'0.4.0'"))
expect("docs/VERSIONING.md", ("1.4.0", "profile"))
expect(".github/workflows/full-demo.yml", ("TODM v1.4 full research artifact", "reproducibility-v1.4.json"))
expect(".github/workflows/paper-pdf.yml", ("TODM_Paper_v1.4.pdf", "TODM_arXiv_source_v1.4.zip"))
expect(".github/workflows/release.yml", ("todm-research-v1.4.0", "TODM_Paper_v1.4.pdf", "TODM_Research_Artifact_v1.4.0.zip"))
expect("paper/ARXIV_SUBMISSION.md", ("todm-research-v1.4.0/TODM_Paper_v1.4.pdf",))
if not args.allow_uncompiled_pdf:
    expect("paper/TODM_Paper_v1.4.pdf")
if errors:
    raise SystemExit("\n".join(errors))
print("OK: TODM methodology, paper, demo, citation and release aligned to v1.4.0")
