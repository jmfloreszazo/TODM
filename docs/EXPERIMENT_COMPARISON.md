# Proposed independent evaluation: methodology versus conventional practice

## Primary hypothesis

A human-approved, independently executed oracle baseline detects correlated implementation-and-test defects more reliably than a workflow whose tests and expected outcomes derive from the same agent-generated specification.

## Design

Three arms: (A) conventional SDD/TDD/BDD with independent reviewer as normally practiced; (B) agent implementation and agent-authored tests; (C) TODM with approved oracle baseline and mutation qualification. The comparison must avoid a straw-man baseline: conventional teams can use independent acceptance tests too.

## Sampling and evaluation

Balanced greenfield, brownfield and AMS tasks; multiple seeds; randomized assignment; independent blinded adjudication; pre-registered stop rule and exclusions. Include benign decoys and wrong-interpretation mutants. No synthetic fixture is treated as a real-world observation.

## Primary measures

Defect recall and precision; false-positive and inconclusive rates; mutation score, requirements-to-evidence traceability and independent-review agreement.

## Failure cases

A human can approve an incorrect oracle; independent oracles can share training data, domain assumptions or implementation errors; a passing oracle is not permission to deploy; a valid signed approval does not prove real-world human identity.

## Data and artifact policy

Archive the exact tested commit, full command output, toolchain versions, all failed and inconclusive cases, and a checksum manifest. Do not claim causal improvement until the experiment is complete.
