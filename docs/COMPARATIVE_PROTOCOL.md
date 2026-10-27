# TODM comparative experiment — preregistration template

## Research questions

**RQ1:** Does a separately approved oracle baseline increase recall of correlated requirements/implementation defects?  
**RQ2:** What is the false-positive and inconclusive cost of independent verification?  
**RQ3:** Does the separation of authorization and conformance block unauthorized delivery even when behavior passes?  
**RQ4:** Can independent assessors reproduce the verdicts using only the archived artifact?

## Arms

A. Conventional implementation and developer-written tests.  
B. Agent-assisted specification-driven implementation and agent-written tests.  
C. TODM: approved independent baseline, qualification controls, bounded agent implementation, independent G5 and G6.

Use equivalent task descriptions, identical allowed tools/time budgets where practical, balanced task assignment and randomized order. A separate panel adjudicates ground truth, blinded to experimental arm.

## Test material

At least one greenfield, one brownfield and one AMS task. Seed correlated defects such as the EUR 10,000 / EUR 12,000 threshold divergence, forbidden state transitions, missing review steps, invariant violations and unauthorized release. Include valid controls to estimate false positives. Freeze tasks, seeds and scoring before running agents.

## Measures

Recall = true positive defects detected / all adjudicated defects.  
Precision = true positive defects detected / all positive defect reports.  
False positive rate, inconclusive rate, mutation score, requirement-to-evidence coverage, inter-rater agreement and gate-bypass success rate.

## Controls

- Version and hash all fixtures, baseline, agent instructions, executable builds and dependency locks.
- Do not allow an agent to modify the approval baseline or scoring rules.
- Separate candidate generation, oracle evaluation and ground-truth adjudication.
- Record PASS, FAIL and INCONCLUSIVE separately.
- Publish all exclusions, failed executions and deviations from protocol.
- Define sample size and stopping rule *before* collecting outcomes.

## Publication boundary

Synthetic demonstration output establishes only that the implementation behaves as coded for those fixtures. It cannot demonstrate improved defect recall over a baseline without the comparative experiment.
