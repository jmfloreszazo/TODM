# TODM research status and evidence boundaries — 28 October 2026

**TODM = Test Oracle-Driven Methodology.**

## Verified public engineering artifact

- Complete [20-page paper](../paper/TODM_Paper_v1.2.pdf), [LaTeX source](../paper/source/main.tex), references, figures and [arXiv submission checklist](../paper/ARXIV_SUBMISSION.md).
- Full [v0.4 synthetic research demo](../demo/) with Python and .NET 10 engines, five limited JSON semantic oracle profiles (SBVR, BPMN, CMMN, DMN, OCL), and 16 governance fixtures.
- Independent release gate with synthetic G2/G6 Ed25519 signatures, negative controls, revoked/unauthorized mandates, and explicit PASS / FAIL / INCONCLUSIVE outcomes.
- [Successful full Python/.NET 10 five-family parity CI](https://github.com/jmfloreszazo/TODM/actions/runs/40598991585).
- [Successful 20-page PDF LaTeX compilation](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468).
- [Verified GitHub research release v1.2](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.2) with downloadable PDF, arXiv source ZIP and full research artifact ZIP.
- [Successful full release verification](https://github.com/jmfloreszazo/TODM/actions/runs/40599015278) and [88-file SHA-256 provenance manifest](ARTIFACT_MANIFEST.json).

## Not yet demonstrated or completed

- Industrial controlled comparative experiment, peer review, or empirically established superiority.
- Complete OMG standards conformance (the five profiles are intentionally limited).
- Production IAM, independently identified real human signers, or autonomous deployment safety.
- External arXiv submission and acceptance, or a permanent archive DOI.

## Falsifiable hypothesis

Compared with conventional developer-authored acceptance tests, an independently approved and mutation-qualified oracle baseline may detect more correlated specification/implementation errors without unacceptable false positives or inconclusive rates. This is a **research hypothesis**, not a measured industrial result.

## Governance alignment

Constitutional/mandate governance (CPAG) concerns **who may act**. TODM concerns **whether the result meets an independently approved behavioral contract**. Neither replaces the other.

See [publication status](PUBLICATION_STATUS.md), [arXiv submission](../paper/ARXIV_SUBMISSION.md) and [DOI archiving](DOI_ARCHIVE.md).
