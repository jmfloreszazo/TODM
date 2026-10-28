# TODM — Test Oracle-Driven Methodology | Research Artifact v1.4

**Version 1.4.0** (the five JSON oracle profiles and fixed fixture schema originated in the v0.4 prototype; historical v0.4 evidence is retained unchanged). An executable, synthetic companion to the TODM methodological paper.** It illustrates why authorized agent action and correct software behavior are different acceptance predicates. It is **not a production governance solution**, not an industrial study, and not five complete OMG engines.

## Reproduce in one command

Requirements: Python 3.12+, OpenSSL with Ed25519; .NET 10 SDK **only** for the optional C# check.

```bash
python3 scripts/reproduce.py
```

The command runs oracle qualification, 16 governance fixtures, signed G2/G6 verification, negative controls, and a fail-closed release gate; evidence is written to `results/reproducibility-v1.4.json`.

```bash
python3 scripts/audit_release.py --case GF-01-greenfield-approved --json  # synthetic allow; exit 0
python3 scripts/audit_release.py --case GF-03-wrong-threshold --json    # blocked; exit 2
bash scripts/run.sh                                                 # optional .NET 10 parity
```

## Repository structure

- `contracts/v1`: five **limited JSON semantic profiles**, not full standards engines; manifest and file hashes.
- `assurance/`: Ed25519 signed synthetic G2/G6 approvals, public demo keys, limitations.
- `governance/`: fixed mandate/authorization fixtures, no real IAM.
- `scenarios/`: greenfield, brownfield, AMS, boundary and high-risk inputs.
- `scripts/`: Python reference, adversarial tests, gate CLI, and reproducibility runner.
- `src/`, `samples/`, `tests/`: .NET 10 reference and smoke/parity harness.
- `results/`: generated JSON evidence; `dashboard/`: offline visualization.
- `docs/ARTIFACT_EVALUATION.md`: evaluation, reproduction and limitations.
- `../.github/workflows/full-demo.yml`: repository-level Python/.NET 10 full-demo CI; `../.github/workflows/ci.yml`: smaller seed CI. The bundled `demo/.github/workflows/ci.yml` is a standalone template, not an active workflow in this repository.

**Methodological contribution:** G0–G7 lifecycle, human-approved independent oracle baseline, qualified oracles, fail/inconclusive semantics, bounded delegation and independent release authorization. **Scientific status:** method proposed; synthetic engineering acceptance demonstrated; comparative effectiveness not established.
