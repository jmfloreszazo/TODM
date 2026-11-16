#!/usr/bin/env python3
"""Render v2.0 LaTeX sources as readable GitHub Markdown (requires Pandoc)."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper/source"

def pandoc(text: str) -> str:
    return subprocess.run(
        ["pandoc", "-f", "latex", "-t", "gfm", "--wrap=none", "--citeproc",
         "--bibliography=references.bib", "--bibliography=references-v2.0.bib"],
        input=text, text=True, capture_output=True, check=True, cwd=SOURCE,
    ).stdout

def normalize(text: str) -> str:
    opening = r"\begin{tabularx}{\linewidth}{"
    while opening in text:
        start = text.index(opening)
        end = start + len(opening)
        depth = 1
        while depth:
            depth += (text[end] == "{") - (text[end] == "}")
            end += 1
        tail = text.index(r"\end{tabularx}", end)
        table = text[end:tail]
        row = next(row for row in table.splitlines() if "&" in row)
        cols = "l" * (row.count("&") + 1)
        text = text[:start] + r"\begin{tabular}{" + cols + "}" + table + r"\end{tabular}" + text[tail + len(r"\end{tabularx}"):]
    text = re.sub(r"\\begin\{description\}\[[^\]]*\]", "", text)
    text = text.replace(r"\end{description}", "")
    text = re.sub(r"\\item\[([^\]]+)\]", lambda m: r"\paragraph{" + m[1] + "}", text)
    return text

def render(stem: str, target: str, title: str, companion: str) -> None:
    original = (SOURCE / (stem + ".tex")).read_text()
    result = pandoc(normalize(original))
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", original, re.S)
    header = f"# {title}\n\n**Version:** 2.0 editorial draft · **Date:** 16 November 2026\n\n{companion}\n\n"
    if abstract:
        header += "## Abstract\n\n" + pandoc(abstract[1]).strip() + "\n\n"
    result = re.sub(
        r'<figure id="([^"]+)">\s*<embed src="figures/([^".]+)\.pdf" />\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        lambda m: f'<a id="{m[1]}"></a>\n\n![{m[3]}](source/figures/{m[2]}.png)\n\n*{m[3]}*',
        result, flags=re.S,
    )
    result = re.sub(r'<a href="(#[^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', result)
    result = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', result, flags=re.S)
    result = re.sub(r'<div class="definition">\s*|</div>', '', result)
    result = re.sub(r'\\label\{[^}]+\}', '', result)
    result = re.sub(r'(?m)^#### (G[0-7].*)$', r'**\1**', result)
    result = re.sub(r'\n{3,}', '\n\n', result)
    (ROOT / 'paper' / target).write_text(header + result)

if __name__ == "__main__":
    render('v2.0', 'TODM_Paper_v2.0.md',
           'TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering',
           'Editorial revision; no new empirical results. [PDF](TODM_Paper_v2.0.pdf) · [LaTeX](source/v2.0.tex) · [Supplement](TODM_Supplement_v2.0.md)')
    render('supplement-v2.0', 'TODM_Supplement_v2.0.md',
           'TODM v2.0 — Operational and Research Supplement',
           'Detailed material retained from v1.5; not new empirical evidence. [Main article](TODM_Paper_v2.0.md) · [LaTeX](source/supplement-v2.0.tex)')
