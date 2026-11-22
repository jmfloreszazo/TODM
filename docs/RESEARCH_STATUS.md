# TODM research status and evidence boundaries — 22 November 2026

**TODM = Test Oracle-Driven Methodology.**

## Verified public engineering artifact

- Current [14-page paper v1.6](../paper/TODM_Paper_v1.6.pdf), [LaTeX source](../paper/source/v1.6.tex), references, figures and [arXiv submission checklist](../paper/ARXIV_SUBMISSION.md).
- Full [v1.5.0 synthetic research demo](../demo/) with Python and .NET 10 engines, five limited JSON semantic oracle profiles (SBVR, BPMN, CMMN, DMN, OCL), and 16 governance fixtures. This software archive is separate from paper v1.6.
- Independent release gate with synthetic G2/G6 Ed25519 signatures, negative controls, revoked/unauthorized mandates, and explicit PASS / FAIL / INCONCLUSIVE outcomes.
- [Historical successful full Python/.NET 10 five-family parity CI](https://github.com/jmfloreszazo/TODM/actions/runs/40598991585); this is not a new v1.6 experiment.
- [Successful v1.6 PDF compilation and paper publication](https://github.com/jmfloreszazo/TODM/actions/runs/45042445444).
- [Paper v1.6 release](https://github.com/jmfloreszazo/TODM/releases/tag/todm-paper-v1.6) with PDF, Markdown, source ZIP, provenance and checksums; [software/research v1.5.0 archive](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.5.0) with the full reproducibility bundle.
- [84-file historical SHA-256 provenance manifest](ARTIFACT_MANIFEST.json), retained unchanged and checked by the v1.6 paper build.

## Not yet demonstrated or completed

- Industrial controlled comparative experiment, peer review, or empirically established superiority.
- Complete OMG standards conformance (the five profiles are intentionally limited).
- Production IAM, independently identified real human signers, or autonomous deployment safety.
- External arXiv submission and acceptance; no separate DOI has been verified for paper v1.6. The v1.5.0 software archive already has DOI [10.5281/zenodo.23725201](https://doi.org/10.5281/zenodo.23725201).

## Falsifiable hypothesis

Compared with conventional developer-authored acceptance tests, an independently approved and mutation-qualified oracle baseline may detect more correlated specification/implementation errors without unacceptable false positives or inconclusive rates. This is a **research hypothesis**, not a measured industrial result.

## Governance alignment

Constitutional/mandate governance (CPAG) concerns **who may act**. TODM concerns **whether the result meets an independently approved behavioral contract**. Neither replaces the other.

See [publication status](PUBLICATION_STATUS.md), [arXiv submission](../paper/ARXIV_SUBMISSION.md) and [DOI archiving](DOI_ARCHIVE.md).

**Version tracks:** [paper v1.6 and software v1.5.0](VERSIONING.md); the historical v0.4 fixture schema remains separate from both.
