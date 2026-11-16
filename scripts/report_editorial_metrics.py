#!/usr/bin/env python3
"""Compare the main-body text with an identical Pandoc-based counting method."""
import json
import re
import subprocess
from pathlib import Path
from render_paper_markdown import ROOT, normalize
counts = {}
for version in ("v1.5", "v2.0"):
    text = (ROOT / f"paper/source/{version}.tex").read_text()
    body = text[text.index(r"\section{"):text.index(r"\section*{Ethics")]
    doc = text[:text.index(r"\title{")] + "\\begin{document}\n" + body + r"\end{document}"
    plain = subprocess.run(["pandoc", "-f", "latex", "-t", "plain", "--wrap=none"],
                           input=normalize(doc), text=True, capture_output=True, check=True).stdout
    counts[version] = len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", plain))
report = {
    "scope": "Introduction through Conclusions; includes tables/captions; excludes abstract, declarations, references and supplement",
    "word_counts": counts,
    "reduction_percent": round(100 * (1 - counts["v2.0"] / counts["v1.5"]), 1),
    "pandoc": subprocess.check_output(["pandoc", "--version"], text=True).splitlines()[0],
    "v2_main_sections": len(re.findall(r"\\section\{", (ROOT / "paper/source/v2.0.tex").read_text())),
}
assert report["v2_main_sections"] == 8
assert counts["v2.0"] < counts["v1.5"]
print(json.dumps(report, indent=2))
(ROOT / "paper/editorial-metrics-v2.0.json").write_text(json.dumps(report, indent=2) + "\n")
