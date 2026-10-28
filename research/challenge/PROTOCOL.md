# Independent evaluation protocol — draft v0.1

## Scope and hypotheses

H1 (reproducibility): An independent evaluator can execute the v1.5.0 synthetic demonstration and reproduce its documented decisions.

H2 (defect detection): Under a controlled comparison, independently governed oracles may detect some seeded behavioral defects that implementation-coupled tests miss. This is a hypothesis, **not an established result**.

H3 (limits): TODM may produce false positives, false negatives, or inconclusive decisions; characterize these explicitly.

## Reproducibility track

1. Record the tagged release, artifact SHA-256, OS, runtime versions and dependencies.
2. Follow the release's README and evaluation guide without changing test data.
3. Record commands, exit codes, logs, observed decisions and discrepancies.
4. Report whether reproduction succeeded, partially succeeded, or failed. Do not silently repair defects.

## Falsification track

1. State the oracle rule and expected result before modifying the candidate.
2. Introduce a documented mutation or independent counterexample.
3. Record ground truth separately from oracle output.
4. Classify detection, missed defect, false alarm, or inconclusive result.

## Comparative track

Before running: freeze scenarios, inclusion criteria, ground-truth adjudication, baselines, tool/model versions, prompts, budgets, repetitions, random seeds where applicable, and stopping rules. Avoid test-data leakage. Use identical inputs and a matched evaluation budget where feasible.

Report TP, FP, FN, TN where well-defined; precision = TP/(TP+FP), recall = TP/(TP+FN), denominators and undefined metrics, uncertainty, execution time, and actual costs. Separate per-scenario observations from aggregate claims. Do not equate passing tests with verified correctness.

## Industrial transfer track

Obtain system-owner authorization, protect sensitive data, document deployment context and confounders, and avoid claiming generalizability from one case.

## Threats to validity

Synthetic fixture selection; oracle author bias; baseline leakage; shared assumptions; mutation representativeness; unequal comparison budgets; incomplete ground truth; non-independent evaluators; environment drift; and publication bias.

## Submission and review

Use RESULT_TEMPLATE.md and link a reproducible repository or redacted evidence. Maintainers may request clarification but must not rewrite evaluators' conclusions. All results, including negative findings, remain independently attributable. Participation does not confer authorship or endorsement automatically.


## Independence and G2 assurance requirements (protocol amendment v0.2)

The original H1–H3 are retained as hypotheses, not asserted outcomes. For any proposed agent study, choose **S1** arm identifiers as defined in [BASELINES.md](BASELINES.md) and complete [the canonical preregistration](../../docs/COMPARATIVE_PROTOCOL.md) before data collection; do not use ambiguous unprefixed A/B/C arms.

**Oracle provenance:** record (a) original business policy and its independent provenance, (b) agent's proposed draft if applicable, (c) exact content and digest approved by an authorized business reviewer, (d) reviewer permissions, scope, timestamp and revocation conditions, (e) qualification tests, and (f) the separately adjudicated ground truth. Disclose shared authors, prompts, code, fixtures or privileges. A self-generated oracle or unreviewed approval click is not independent assurance.

**Evidence segregation:** freeze candidate agent permissions, approved baselines and hidden evaluation material in separate protected scopes. Keep ground-truth labels and oracle scoring rules unavailable to the candidate producer. Document any exposure or bypass. Record both legitimate allowed edits and unauthorized denied writes. Agent instructions, local hooks and self-reported refusals are not substitutes for permission enforcement.

**Human G2 pilot:** independently preregister correct/incorrect AI-proposed oracle items, presentation formats, case order, reviewer familiarity, consent, time and error-detection endpoints. Include digest-bound approval and reapproval after payload changes. Report approval of incorrect rules and rejection of correct rules separately; never interpret a fast click as proven comprehension.

**Evidence hierarchy:** a synthetic fixture demonstrates reference behavior; a CI pass demonstrates the tested workflow on that commit; independent replication demonstrates portability; controlled experiments support scoped quantitative claims; a repository security boundary supports only the threats it was tested against. Publication on Zenodo does not prove peer review.

**Change control:** preregistration and hypotheses must be immutable once trials begin. Log any deviation with a new version and reason. Publish incomplete, null and adverse results, not only successful cases.
