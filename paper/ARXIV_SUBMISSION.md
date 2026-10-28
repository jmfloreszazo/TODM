# arXiv submission package — author checklist

**Status:** Complete candidate source package and compiled PDF are publicly available. **Not submitted to or accepted by arXiv.**

## Files

- [Compiled 20-page manuscript PDF](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_Paper_v1.4.pdf)
- [Standalone LaTeX source ZIP for arXiv](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_arXiv_source_v1.4.zip)
- [Full research artifact](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_Research_Artifact_v1.4.0.zip)
- [Verified paper compilation](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468)

## Suggested metadata (review before submitting)

**Title:** TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering

**Subtitle:** A Tool-Agnostic, Falsifiable Method for Greenfield Development, Brownfield Modernization, and Application Management

**Author:** José María Flores Zazo

**Primary subject area to consider:** Computer Science — Software Engineering (`cs.SE`). Category eligibility and any endorsement requirement are decided by arXiv, not this repository.

**Keywords:** test oracle problem; software engineering methodology; AI coding agents; model-based testing; human oversight; agent governance; legacy modernization; software maintenance; mutation testing; behavioral contracts.

**Abstract:** Use the exact abstract from `paper/source/main.tex`; do not substitute promotional claims or synthetic engineering results as empirical findings.

## Submission steps requiring the author

1. Sign in to your own [arXiv submission account](https://arxiv.org/submit).
2. Check account/category eligibility, possible endorsement and current submission policies.
3. Select the appropriate submission license. **No license choice has been made on your behalf.**
4. Upload the source ZIP, allow arXiv to compile it and inspect every page, figure and reference.
5. Enter exact author/title/abstract/subject metadata, code availability URL and relevant comments.
6. Submit and wait for arXiv moderation; record the resulting arXiv ID **only after acceptance/announcement**.
7. Add the verified arXiv ID to the paper metadata, repository README and `CITATION.cff`.

## Claim boundaries

The manuscript presents a proposed method and a synthetic, deterministic demonstration. It does not report a randomized industrial trial or establish causal superiority over existing SDD/TDD/BDD practices. Five OMG-inspired semantic profiles are limited JSON implementations, not certified standard engines.

## Rebuild

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The GitHub Actions workflow compiles the PDF and publishes a release artifact automatically.
