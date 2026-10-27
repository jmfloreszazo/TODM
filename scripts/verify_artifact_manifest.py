#!/usr/bin/env python3
"""Verify the full TODM source transfer against the SHA-256 publication manifest."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs" / "ARTIFACT_MANIFEST.json").read_text())
errors = []
for item in manifest["files"]:
    path = ROOT / item["target"]
    if not path.is_file():
        errors.append(f"MISSING: {item['target']}")
        continue
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != item["sha256"] or len(data) != item["size"]:
        errors.append(f"MISMATCH: {item['target']}: {actual}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"TODM publication source integrity: {len(manifest['files'])} files verified SHA-256")
