# TODM — Test Oracle-Driven Methodology

**A human-governed, tool-agnostic methodology for AI software engineering.**

Author: **José María Flores Zazo** · Status: **methodological research proposal + synthetic reproducible demonstration**.

TODM separates **who is authorized to act** from **whether the resulting software satisfies independently approved business behavior**. Agents can propose requirements, implement code and suggest tests, but cannot unilaterally approve or change the oracle baseline used to judge their work.

## Verified public research release

**[TODM Research Artifact v1.3 — audited GitHub Release](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.3)** contains the compiled 20-page PDF, a standalone arXiv LaTeX source ZIP, and a full research artifact ZIP. Its release workflow re-ran the 88-file SHA-256 integrity check and full Python/.NET 10 governance parity successfully: [verified release run](https://github.com/jmfloreszazo/TODM/actions/runs/40599015278).

**This GitHub release is not an arXiv submission or a DOI registration.**

See the [28 October technical audit](docs/AUDIT_2026-10-28.md) and [documentation integrity CI](.github/workflows/docs-integrity.yml).

## Read the complete article

- **[Full English research paper — PDF](paper/TODM_Paper_v1.2.pdf)** (automatically compiled from LaTeX and committed by GitHub Actions).
- [Complete manuscript in Markdown](paper/TODM_Paper_v1.2.md).
- [LaTeX source, figures and references](paper/source/).
- [How the paper is built and arXiv submission status](paper/README.md).
- [Paper compilation workflow](.github/workflows/paper-pdf.yml).

## Reproduce the complete research demo

The [full demo v0.4](demo/) contains a Python reference, a C#/.NET 10 implementation, five limited oracle-family profiles, 16 synthetic governance scenarios, public verification keys, synthetic G2/G6 attestations, negative controls and a research protocol.

```bash
cd demo
python3 scripts/reproduce.py
bash scripts/run.sh        # requires .NET 10 SDK and Python 3
```

**Verified in GitHub Actions:** [full Python/.NET 10 demo and 16-fixture five-family parity](https://github.com/jmfloreszazo/TODM/actions/runs/40598241342).

The smaller [Python seed](src/todm_demo.py) and [.NET 10 seed](dotnet/Todm.Seed/) remain as introductory examples. Their [16 shared policy fixtures](tests/fixtures/policy-cases.json) are separate from the 16 full governance scenarios.

## Eight methodological gates

| Gate | Activity | Approval / outcome |
|---|---|---|
| G0 | Scope and risk | Authorized mandate |
| G1 | Evidence discovery | Classified evidence |
| G2 | Baseline construction | Accountable human approval |
| G3 | Oracle qualification | Mutation and negative controls |
| G4 | Bounded AI construction | Candidate with provenance |
| G5 | Independent verification | PASS / FAIL / INCONCLUSIVE |
| G6 | Release governance | Separate authorization |
| G7 | Drift and evolution | Controlled baseline revision |

**Model families:** SBVR vocabulary and rules, DMN decisions, BPMN processes, CMMN cases, OCL invariants. Only **declared, limited JSON semantic profiles** are implemented here; this repository does not claim complete OMG conformance.

**Applicability:** greenfield, brownfield modernization (incremental or single cutover), and application maintenance (AMS).

## Evidence and scientific limitations

- The 16-case parity tests are **synthetic engineering acceptance**, not a controlled industrial comparison.
- Demo signatures do **not** prove the identity or authority of real people.
- No comparative superiority, complete standards implementation or production deployment enforcement is claimed.
- The complete paper defines falsifiable hypotheses and an experimental protocol; a peer-reviewed empirical study is still required.
- No DOI or arXiv acceptance is claimed until independently confirmed.

See [research status](docs/PUBLICATION_STATUS.md), [comparative protocol](docs/COMPARATIVE_PROTOCOL.md), [full experiment plan](docs/EXPERIMENT_COMPARISON.md) and [GitHub Actions](https://github.com/jmfloreszazo/TODM/actions).

## Citation and license

[Software citation metadata](CITATION.cff) · [MIT license](LICENSE). Please cite an immutable commit hash until a versioned archive DOI is available.
