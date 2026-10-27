# TODM — Test Oracle-Driven Methodology

**Human-governed AI software engineering with independent behavioral oracles.**

Author: José María Flores Zazo · Research status: **proposed methodology + synthetic proof of concept**

TODM separates two questions: **is an agent authorized to act?** and **does its output conform to a separately approved behavioral baseline?** Both are necessary for a controlled release. The construction agent cannot unilaterally approve or modify its own acceptance criteria.

## Run the published research seed

**Python 3.12+** (no external packages):

```bash
python3 -m unittest discover -s tests -v
python3 src/todm_demo.py
```

**.NET 10 SDK:**

```bash
dotnet build dotnet/Todm.Seed/Todm.Seed.csproj -c Release
dotnet run --project dotnet/Todm.Seed/Todm.Seed.csproj -c Release -- --self-test
dotnet run --project dotnet/Todm.Seed/Todm.Seed.csproj -c Release
```

[GitHub Actions](../../actions) builds the .NET project and runs Python and .NET negative controls. A green workflow is required before claiming CI verification.

## Methodology

G0 scope → G1 discover evidence → G2 approve baseline → G3 qualify oracles → G4 bounded construction → G5 independent verification → G6 release approval → G7 monitoring and change control.

Profiles: SBVR, DMN, BPMN, CMMN and OCL. **Current public seed demonstrates only a narrow JSON business-policy profile**; it is not a full interpreter of these OMG standards.

## Documentation

- [Academic research synopsis](paper/RESEARCH_SYNOPSIS.md)
- [Comparative experimental protocol](docs/COMPARATIVE_PROTOCOL.md)
- [Evidence boundaries and limitations](docs/RESEARCH_STATUS.md)
- [Synthetic business baseline](contracts/v1/policy.json)
- [Python reference](src/todm_demo.py)
- [.NET 10 seed](dotnet/Todm.Seed/Program.cs)

## Publication integrity

The full ~20-page manuscript and the more extensive v0.4 demo exist as separate research artifacts, **but are not yet fully transferred to this repository**. Do not cite the seed as proof of comparative superiority, production identity assurance or full OMG conformance. See the research synopsis for hypotheses and limitations.

The synthetic approval label in JSON does **not** represent a real human signature. A release gate in a demonstration does not enforce a production deployment environment.
