# TODM — Test Oracle-Driven Methodology

> **AI agents can write code. Who verifies that the code is actually right?**

**TODM makes AI-generated software accountable to independently approved business behavior.** It separates permission to act from proof of correctness, using executable test oracles, human-governed baselines, and fail-closed release gates.

[![Full research demo](https://github.com/jmfloreszazo/TODM/actions/workflows/full-demo.yml/badge.svg?branch=main)](https://github.com/jmfloreszazo/TODM/actions/workflows/full-demo.yml)
[![Cross-language CI](https://github.com/jmfloreszazo/TODM/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jmfloreszazo/TODM/actions/workflows/ci.yml)
[![Paper PDF](https://github.com/jmfloreszazo/TODM/actions/workflows/paper-pdf.yml/badge.svg?branch=main)](https://github.com/jmfloreszazo/TODM/actions/workflows/paper-pdf.yml)
[![Docs integrity](https://github.com/jmfloreszazo/TODM/actions/workflows/docs-integrity.yml/badge.svg?branch=main)](https://github.com/jmfloreszazo/TODM/actions/workflows/docs-integrity.yml)
[![License: MIT](https://img.shields.io/github/license/jmfloreszazo/TODM)](LICENSE)

**Research status:** proposed methodology + reproducible **synthetic** Python/.NET 10 engineering demonstration. Not a production-certified governance platform or an industrial effectiveness study.

## The problem in 30 seconds

An AI agent writes the implementation. Another AI agent writes the tests. Both may inherit **the same wrong assumption**. All tests pass — and the software is still wrong.

**TODM changes the acceptance question:**

| Without an independent oracle | With TODM |
| --- | --- |
| “Did the generated tests pass?” | “Does the result satisfy independently approved business behavior?” |
| The agent can influence both implementation and expected result | Human-governed baseline separates the expected result from construction |
| A green build may be mistaken for approval | Verification and release authorization are separate decisions |
| Ambiguous evidence may be silently accepted | **PASS / FAIL / INCONCLUSIVE**, with fail-closed release |

## See it fail safely — runnable demo

**Requirements:** Python 3.12+ and OpenSSL; optional .NET 10 SDK for cross-language parity.

```bash
git clone https://github.com/jmfloreszazo/TODM.git
cd TODM/demo
python3 scripts/reproduce.py
python3 scripts/audit_release.py --case GF-01-greenfield-approved --json
python3 scripts/audit_release.py --case GF-03-wrong-threshold --json
```

The final command is an **expected denial** (exit code 2). It demonstrates the release gate blocking a candidate that violates the baseline. The positive example exits 0. For optional .NET 10 parity: `bash scripts/run.sh`.

**What you can inspect:** [synthetic evidence](demo/results/), [16 governance scenarios](demo/governance/fixtures.json), [five limited model profiles](demo/contracts/v1/), [offline dashboard](demo/dashboard/index.html), [evaluation guide](demo/docs/ARTIFACT_EVALUATION.md).

## How it works

```text
BUSINESS AUTHORITY             AI CONSTRUCTION              INDEPENDENT VERIFICATION
Approve expected behavior ──► Agent implements candidate ──► Compare against approved oracles
        │                             │                                │
   Versioned baseline            Provenance trail                PASS / FAIL / INCONCLUSIVE
        └─────────────────────────────┴────────────────────────────────┘
                             SEPARATE RELEASE AUTHORIZATION
```

TODM defines eight gates: **G0** scope and risk, **G1** evidence discovery, **G2** baseline approval, **G3** oracle qualification, **G4** bounded AI construction, **G5** independent verification, **G6** release authorization, and **G7** controlled drift and evolution.

**Standards-inspired oracle families:** SBVR (business vocabulary/rules), DMN (decisions), BPMN (processes), CMMN (cases), and OCL (invariants). The demo implements **limited JSON semantic profiles**, not complete OMG engines or certified standards conformance.

## Who is this for?

- **CTOs and engineering leaders:** distinguish faster code generation from evidence of trustworthy delivery.
- **Software architects:** establish independent acceptance contracts for agentic development.
- **Modernization teams:** compare legacy and replacement behavior before a controlled cutover.
- **AI governance and assurance teams:** connect authorization, provenance, verification and release decisions.
- **Researchers:** challenge falsifiable hypotheses with the [comparative protocol](docs/COMPARATIVE_PROTOCOL.md).

## Read the research and inspect the evidence

- **[v1.5 manuscript (Markdown)](paper/TODM_Paper_v1.5.md)** · [v1.5 LaTeX source](paper/source/v1.5.tex) · [PDF build workflow](.github/workflows/paper-pdf.yml)
- **[Complete v1.4 paper (PDF)](paper/TODM_Paper_v1.4.pdf)** · [Markdown manuscript](paper/TODM_Paper_v1.4.md) · [LaTeX source](paper/source/)
- [Research and publication status](docs/PUBLICATION_STATUS.md) · [limitations](demo/docs/limitations.md)
- [Full reproducibility instructions](demo/README.md) · [historical v0.4 model profiles](research-models/v0.4/)
- [Migration plan towards v1.5.0](docs/V1.5_MIGRATION_PLAN.md) · [repository layout](docs/REPOSITORY_LAYOUT.md)

**Current published research release:** [v1.5.0](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.5.0) · [Zenodo DOI](https://doi.org/10.5281/zenodo.23725201). Publication does not imply independent scientific validation.

## What this does *not* claim

The 16 governance fixtures are synthetic acceptance checks, not independent industrial evidence. Demo signatures do not establish real-world human identity. No comparative superiority, full standards implementation, production enforcement or arXiv acceptance is asserted. The Zenodo DOI identifies the deposited artifact; it does not certify scientific validity. See the [evaluation protocol](docs/COMPARATIVE_PROTOCOL.md) and [publication status](docs/PUBLICATION_STATUS.md).

## Independent research challenge

Researchers are invited to reproduce, falsify, compare, or independently transfer the method. See the [TODM Open Research Challenge](research/challenge/README.md), [draft protocol](research/challenge/PROTOCOL.md), and [evaluation report template](research/challenge/RESULT_TEMPLATE.md). Negative and inconclusive findings are welcome; no independent validation is claimed.

## Join the work

If your team builds AI-generated software, try the negative-control demo and ask: **who approves the expected result, and can the agent change that approval?**

Open an [issue](https://github.com/jmfloreszazo/TODM/issues) with a counterexample, a missing oracle condition, a reproducibility defect or a modernization scenario. Contributions should preserve evidence provenance and include executable tests.

**Author:** José María Flores Zazo · [Website](https://jmfloreszazo.com) · [Citation](CITATION.cff) · [MIT License](LICENSE)

> **The goal is not to trust an agent more. It is to need less blind trust in its output.**
