# Experimental arms and comparison controls

**Status:** research design; **not observed results**. This file defines two distinct comparisons, which must never reuse ambiguous A/B/C identifiers.

## Study S1 — Agent-controlled oracle independence (primary causal comparison)

All S1 arms use **AI agents** for candidate construction and implementation tests, with matched tasks, models, CLI/harness versions and budgets where practicable.

| Arm | Candidate and implementation tests | Independent acceptance oracle | Mutation qualification | Goal |
| --- | --- | --- | --- | --- |
| **S1-A — Coupled** | Agent-generated | None; coupled agent tests only | No | Measure defects escaping the coupled pipeline |
| **S1-B — Independent** | Agent-generated | Frozen, human-governed, read-only oracle created outside the implementation agent's writable scope | No | Isolate oracle independence |
| **S1-C — Qualified** | Agent-generated | Same frozen independent oracle | Yes; frozen qualification process | Isolate contribution of oracle qualification |

The evaluator must not count a known hardcoded fixture assertion as evidence of independent effectiveness. Include clean cases, hidden defects and contradictions where available. Count **release-escaping defects** per task and variant, not only test pass rates. Define negative controls and ground-truth labels outside the agent's writable scope. A real permission-boundary test is necessary before claiming resistance to manipulation.

The primary S1 contrasts are **S1-B vs S1-A** and **S1-C vs S1-B**. Estimate defect escape, recall/precision, false alarms, inconclusive decisions, bypass attempts, review effort, latency and costs with task-level uncertainty. Randomize and preregister.

## Study S2 — Delivery-model comparison (exploratory, separate population)

| Arm | Delivery approach | Interpretation |
| --- | --- | --- |
| **S2-H — Human-led** | Human developer implementation and developer-authored tests | Optional exploratory operational comparator |
| **S2-AI — Agent-led** | Agent-assisted development with implementation-coupled tests | Agent workflow comparator |
| **S2-TODM — Governed** | Agent implementation with G2/G3/G5/G6 TODM workflow | End-to-end feasibility comparison |

S2 is **not interchangeable** with S1: human skill, effort, time budget and workflow differ. Do not pool results or describe S2 as a controlled isolation of oracle independence.

## Study S3 — Human approval effectiveness at G2

A separate human-subject pilot compares **presentation formats**, not S1/S2 implementation arms: decision table / DMN-style view, Gherkin and code or plain language. Expose exact approval content, changes, provenance and downstream impact. Capture detection of wrong rules, false rejection of correct rules, review time and confidence. An approval click alone does not establish comprehension.

## Shared preregistration and evidence controls

- Freeze tasks, sample size and rationale, primary endpoint, analysis unit, stop rule and exclusion criteria **before** recording outcomes.
- Freeze approved expected behavior independently of agent-generated candidate and tests; use blinded adjudication when possible.
- Record actor privileges, artifact hashes, tool/model identity, prompts, harness configuration and budgets.
- Preserve results for clean controls, faults, mutants that survive, FAIL, PASS, INCONCLUSIVE, abstentions, failed runs and deviations.
- Report uncertainty and costs. Bootstrap by **task**, not repeated execution row.
- Separate authorization violations from behavioral failures: passing a functional oracle cannot erase a mandate violation.
- Published synthetic fixture demonstrations are **not** an S1, S2 or S3 trial.

The canonical research-question and measurement detail is maintained in [COMPARATIVE_PROTOCOL.md](../../docs/COMPARATIVE_PROTOCOL.md); independent research submissions use [PROTOCOL.md](PROTOCOL.md).
