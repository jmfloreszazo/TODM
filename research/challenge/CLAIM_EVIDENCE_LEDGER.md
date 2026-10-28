# TODM claim-to-evidence ledger (working, PR #5)

**Scope:** inspected repository documents at `research/open-challenge-v1` on 2026-10-28. This is a **source inspection**, not an execution audit, independent evaluation, or certification. Track observations, supporting links, and remaining checks separately. PR #5 head at inspection start: `bd9aa8389d7039a99cdcbd61c7eeeb9c4be785c2`; base `9714369e06da25b4c4a309862e8884d49183c403`. Subsequent commits will advance this head.

| ID | Public claim / boundary | Evidence currently inspected | Evidence level | Remaining verification |
| --- | --- | --- | --- | --- |
| C01 | TODM = **Test Oracle-Driven Methodology**, separating authority from correctness | [README](../../README.md), [citation](../../CITATION.cff) | Wording verified in source | Check repo About/topics and all manuscripts independently |
| C02 | G0–G7, three-way PASS/FAIL/INCONCLUSIVE, fail-closed release | [README](../../README.md), [demo limitations](../../demo/docs/limitations.md) | Design/docs inspected | Re-run positive, negative and inconclusive test cases; archive logs |
| C03 | Synthetic Python/.NET 10 reference demo, not a real agent pipeline | [limitations](../../demo/docs/limitations.md) | Scope limitation explicit | Execute reproducibility scripts and clean SDK build in pinned environment |
| C04 | Five standards-inspired JSON profiles; **not** OMG-compliant execution engines | [README](../../README.md), [limitations](../../demo/docs/limitations.md) | Explicit design boundary | Inventory profile semantics and qualify against independent reference cases |
| C05 | 16 synthetic governance fixtures | [README](../../README.md), [limitations](../../demo/docs/limitations.md) | Described, not independently counted here | Enumerate fixtures and clarify distinct '16 case' sets |
| C06 | Python/.NET parity reportedly passed a historical GitHub Actions run | [limitations](../../demo/docs/limitations.md) links to [run 40650709906](https://github.com/jmfloreszazo/TODM/actions/runs/40650709906) | **Repository assertion**, not independently inspected logs | Inspect run conclusion, SHA, artifact and compare it to release commit |
| C07 | v1.5.0 release / Zenodo DOI 10.5281/zenodo.23725201 | [publication status](../../docs/PUBLICATION_STATUS.md), [citation metadata](../../CITATION.cff) | **Repo metadata assertion** only | Verify GitHub release files and external Zenodo record; compare release SHA/DOI metadata |
| C08 | No arXiv ID, no independent experiment or industrial replication claimed | [publication status](../../docs/PUBLICATION_STATUS.md), [challenge protocol](PROTOCOL.md) | Explicit non-claim | Recheck on any release/update |
| C09 | Synthetic G6 approval is a boolean; signatures do not prove human identity | [limitations](../../demo/docs/limitations.md) | Explicit limitation | Implement actor permission-boundary controls and human approval evidence |
| C10 | Reproducible independent superiority or higher recall | [comparative protocol](../../docs/COMPARATIVE_PROTOCOL.md) states this is **not established** | **Hypothesis only** | Preregister controlled study and analyze all outcomes |
| C11 | Synthetic SHA-256 manifest enforces a trusted baseline | [limitations](../../demo/docs/limitations.md) explicitly explains model+manifest co-edit bypass | **Not supported** as security claim | Denied-write / allowed-write control using distinct credentials and protected trust roots |
| C12 | Independent oracles protect from shared wrong assumptions | [challenge protocol](PROTOCOL.md) proposes it | **Research hypothesis** | Blind independent ground truth, clean controls, precision and recall |
| C13 | Human G2 approval verifies understanding of proposed oracles | Current [protocol](PROTOCOL.md) does **not** establish this | **Not demonstrated** | Run preregistered G2 reviewer detection pilot |

## Evidence rule

- **Documented** = repository text asserts or defines something; not proof that the software executes.
- **Executed** = command, environment, exit status, inputs and immutable output recorded.
- **Independently replicated** = another evaluator runs a frozen artifact without silent repair.
- **Experimentally supported** = frozen protocol, controls, independent adjudication, negative findings and uncertainty analysis.
- **Production enforced** = permissions demonstrably prevent the disallowed operation under the tested threat model. Never infer this from a passing unit test or agent prompt.

## Open audit checklist

- [ ] Verify GitHub PR/release state and commit SHA against the archived files.
- [ ] Verify DOI record externally, not only in CITATION.cff.
- [ ] Inspect applicable CI checks at current PR head and capture results.
- [ ] Run demo and parity commands on a pinned environment.
- [ ] Inspect public About, topics and README for naming/version mismatches.
- [ ] Reconcile historical version references in paper, demo and release.
- [ ] Review figures, source links and manuscript/PDF parity.

Nothing above claims those unchecked tasks have passed.
