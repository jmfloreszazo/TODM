#!/usr/bin/env python3
"""Validate repository-local Markdown links without network access.

HTTP(S) links and fragment-only links are intentionally outside this check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXCLUDE = {".git", ".venv", "bin", "obj", "__pycache__", "node_modules"}
failures: list[str] = []
checked = 0

for md in sorted(ROOT.rglob("*.md")):
    if any(part in EXCLUDE for part in md.relative_to(ROOT).parts):
        continue
    source = md.read_text(encoding="utf-8")
    # Fenced code blocks are not Markdown link targets.
    source = re.sub(r"(?ms)^\s*```.*?^\s*```", "", source)
    for match in LINK.finditer(source):
        raw = match.group(1).strip()
        url = urlsplit(raw)
        if url.scheme or raw.startswith(("#", "//")):
            continue
        target = unquote(url.path)
        if not target:
            continue
        checked += 1
        resolved = (md.parent / target).resolve()
        if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
            failures.append(f"{md.relative_to(ROOT)} -> {raw}")

if failures:
    print("Broken repository-relative Markdown links:", file=sys.stderr)
    for item in failures:
        print(f"  {item}", file=sys.stderr)
    raise SystemExit(1)
print(f"OK: {checked} repository-relative Markdown links verified")
