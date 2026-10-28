# TODM v1.4 — Companion artifact for the methodological paper

**Companion to:** *TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering* (manuscript v1.4). **Artifact status:** synthetic proof of concept, not an empirical effectiveness study.

## Paper-to-code traceability

| Paper concept | Demonstration artifact | Status |
|---|---|---|
| G0 frame | `scenarios/*.json` | Synthetic fixed scope |
| G1 discover | `contracts/v1/*.json` plus documented policy | Synthetic, not AI discovery |
| G2 human approve/freeze | `contracts/v1/manifest.json` + model SHA-256 | **Synthetic G2/G6 demo Ed25519 signatures**, no real human identity or organizational authority |
| G3 qualify oracle | `scripts/verify_all.py`, positive controls, four mutants, incomplete evidence, tamper test | Python reference tested |
| G4 bounded construction | `samples/Todm.Candidate/*.cs` with seeded mutations | Source included; .NET build via CI |
| G5 independent verification | `src/Todm.Engine`, `scripts/reference.py` | Five *scoped JSON profiles*, not full OMG interpreters |
| G6 authorization | `governance/mandates.json`, `scripts/governance.py`, `src/Todm.Governance` | Synthetic mandates and simulated release approval |
| G7 observe/evolve | `results/*.json`, `dashboard/index.html` | Offline evidence only; no production telemetry |
| Separation of authority and correctness | Cases `GF-03`, `GF-05`, `GF-08` | Demonstrated synthetically |
| Three application profiles | `greenfield`, `brownfield`, `ams` fixtures | Same policy reused, not industrial projects |

## Publication-safe result statement

> We implemented a deterministic, synthetic reference prototype comprising five narrowly scoped JSON oracle profiles, a .NET 10 candidate application with seeded mutations, an independent Python reference evaluator, and a two-plane authorization/verification demonstration. In the Python reference execution, five positive controls passed, four seeded behavioral mutants failed, and one missing-evidence case was inconclusive. A separate set of sixteen synthetic two-plane fixtures produced five simulated release approvals and eleven blocks, including cases where behavior passed the oracles but agent authority or release approval was absent. These counts are fixture-specific acceptance checks; they do not estimate defect-detection performance, real-world agent reliability, or industrial effectiveness. The .NET code compiled and matched the Python reference for the 16 synthetic governance fixtures and five limited oracle families in the [public GitHub Actions verification](https://github.com/jmfloreszazo/TODM/actions/runs/40653338691); this is engineering acceptance, not external scientific validation.

## Critical falsification and next experiment

The strongest counterexample to TODM is *oracle circularity*: if the human-approved baseline reproduces the same wrong interpretation as the implementation, all checks can PASS. A real study must compare TODM against TDD/BDD/SDD workflows using independently adjudicated hidden defects, known-correct decoys, measured false positives, and blinded assessors. The demo's seeded mutation success is **not** evidence of such superiority.

## Reproducibility

`python3 scripts/verify_all.py` verifies the Python reference. `python3 scripts/build_dashboard.py` regenerates the offline visual. With .NET 10 SDK, `bash scripts/run.sh` builds the C# projects, executes smoke cases and both governance implementations, then checks verdict parity. See `docs/limitations.md`.
