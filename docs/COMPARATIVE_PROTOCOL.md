# TODM comparative research — preregistration template (unexecuted)

> **Status:** design only. No study registered or results observed here. Arm identifiers are defined in [research/challenge/BASELINES.md](../research/challenge/BASELINES.md); do not silently change them after collecting outcomes.

## Research questions

- **S1-RQ1:** Does a separately governed, read-only oracle reduce defects escaping an AI agent's implementation-coupled tests (**S1-B versus S1-A**)?
- **S1-RQ2:** Does mutation qualification add defect-detection value beyond an independent oracle (**S1-C versus S1-B**)?
- **S1-RQ3:** How do independent checks affect false positives, INCONCLUSIVE, time, USD and human effort?
- **S1-RQ4:** Do real permission boundaries prevent unauthorized oracle modification or release despite functional tests passing?
- **S2-RQ:** Can a human-led/agent-led/governed delivery comparison be executed fairly? Treat S2 as exploratory until skill and budget confounding are addressed.
- **S3-RQ:** Can business reviewers detect errors in AI-proposed G2 oracle baselines, and does presentation format influence detection and review time?

## Preregistration fields — must be frozen before measurement

| Field | Required declaration |
| --- | --- |
| Frozen preregistration ID, timestamp, version, commit and archive hash | **TBD before study** |
| Primary study and contrast | S1; choose and preregister S1-B vs S1-A (or justify different primary) |
| Primary outcome and definition | **TBD**: ideally task-level escaped seeded defects, independent ground truth |
| Unit of randomization / analysis | **TBD**; default independent task, not repeated run |
| Target sample size, power / precision rationale | **TBD**; no invented target N |
| Stopping rule, interim analysis, exclusions | **TBD**; fixed before runs |
| Tasks and risk strata | **TBD**; include greenfield, brownfield, AMS, clean and defective cases |
| Ground truth owner, conflicts, adjudication process | **TBD** independent of agent and oracle author where possible |
| Models, CLI versions, tooling, prompts and budgets | **TBD**; exact binaries/configuration/hashes |
| Randomization, counterbalancing and seeds | **TBD** |
| Planned intervals and correction for multiple contrasts | **TBD** |
| Data release, privacy, cost currency and limitations | **TBD** |

A plan with TBDs is not a completed preregistration. Freeze it as an immutable version **before** any study runs; publish deviations as separate amendments.

## S1 agent-arm definitions

- **S1-A — Coupled**: AI implementation and agent-written tests; no independent acceptance oracle.
- **S1-B — Independent**: identical AI construction path, independently governed acceptance oracle frozen outside writable agent scope; no mutation qualification.
- **S1-C — Qualified**: same independent oracle as S1-B, plus mutation qualification frozen before evaluation.

Keep task inputs, model settings and budgets comparable; measure/reveal the extra time/cost imposed by TODM rather than concealing it. Reject any trial where the agent accesses hidden test answers or can write the oracle baseline without recorded exception. Log rejected writes separately from prompt-level refusal. Include both nondefective controls and defects unknown to the candidate agent.

## Independent ground truth and oracle provenance

Preserve three separate roles and repositories/permission domains when possible:

1. **Expected behavior authority (G2):** named domain owner approves an exact content digest and scope, with timestamp and evidence; agent proposals are allowed but never self-approved. If payload changes, approval expires.
2. **Candidate producer (G4):** AI agent can modify candidate code and its own tests but cannot write the approved oracle or scoring rules.
3. **Independent adjudicator:** a separate evaluator prepares hidden clean and defective cases; signs or hashes their labels and records conflicts before observing each arm's result.

If any role is shared, disclose conflicts and categorize the study as partially independent. Do not put expected gate verdicts in the implementation agent's input, or let an evaluator derive truth from the same assertion being graded.

## Measures and analysis

Record raw TP, FP, FN, TN when applicable, and explicitly define what constitutes a single defect and matching rule. Report recall, precision, specificity/false-positive rate, escaped defects per task, INCONCLUSIVE, mutation score, rule-coverage evidence, override/mandate-bypass success rate, operator time, latency, token count and currency costs. Denominators and undefined metrics must be visible.

Estimate uncertainty at the **task** level (e.g. cluster bootstrap by independent task; document paired design); do not treat reruns or multiple mutations of one task as independent projects. Present all task-level rows, deviations, exclusions and negative/null findings. Authorization and behavioral verdicts are **two separate dimensions**.

## S2 delivery comparison

If undertaken, identify arms as **S2-H**, **S2-AI**, **S2-TODM** only, and document developer expertise and workflow confounders. Never reuse S1-A/B/C labels for human-versus-agent comparisons or combine arms into a single causal effect.

## S3 G2 human-review pilot

Obtain documented informed participation and avoid sensitive information. Pilot recruitment of 6–10 external reviewers (if feasible) is exploratory, not a generalizable power claim. Preregister randomized/counterbalanced presentation in DMN-style table, Gherkin, and code/plain-language versions of the same rule; control for reviewer familiarity. Insert known incorrect and correct proposals. Present exact rule, approved digest, evidence sources and business consequences; approvals must specify scope and expiry. Measure wrong-rule detection rate, false rejection, time, confidence and inter-rater agreement. Distinguish a real approval from simulated G6 booleans. Describe observer bias and learning/carryover effects.

## Reproducibility and publication boundaries

Archive frozen task specifications, reference-rule hashes, source commit, environment, commands, failure logs, results and analysis script. Publish aggregate and suitably anonymized individual data. Do not assert measured superiority, valid human oversight, complete OMG conformance or production protection until independently evidenced. An archival DOI is not an endorsement.

See [claim-evidence ledger](../research/challenge/CLAIM_EVIDENCE_LEDGER.md).
