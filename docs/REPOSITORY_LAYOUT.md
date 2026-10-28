# Repository layout (current and target)

| Current path | Role | Proposed disposition |
|---|---|---|
| `src/`, `dotnet/` | Introductory Python and .NET seeds | Keep working until imports, CI and docs can migrate safely |
| `demo/src/`, `demo/samples/`, `demo/tests/` | Full .NET implementation and tests | Eventually consolidate under `src/dotnet/` and `tests/dotnet/` |
| `demo/scripts/` | Reference Python engine and reproducibility tools | Eventually consolidate under `src/python/` and `scripts/` |
| `contracts/`, `demo/contracts/`, `research-models/` | Contract and model profiles | Preserve schema identifiers; organize after dependency mapping |
| `demo/results/` | Research evidence and reports | Retain all tracked evidence, with provenance |
| `paper/` | Manuscripts, PDF and LaTeX | Preserve previous editions; add versioned v1.5 artifacts |
| `.github/workflows/` | Authoritative CI/CD | Consolidate and validate before deleting any duplicate workflow files |
| `demo/.github/workflows/` | Nested workflow templates | Review before removal; GitHub only executes root workflows |

This document describes a migration target, not a completed reorganization.
