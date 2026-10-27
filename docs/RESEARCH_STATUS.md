# Research status and evidence boundaries

**TODM = Test Oracle-Driven Methodology.**

## Available in this GitHub repository

- Method lifecycle G0–G7 described in the root README.
- Minimal Python standard-library demonstrator for a human-approved (synthetically represented) oracle baseline.
- Negative controls for incorrect threshold, revoked mandate, missing approval, missing evidence and tampered policy.
- GitHub Actions workflow that runs those tests on push and pull requests.

## Not yet demonstrated here

- Independent industrial comparative experiment.
- Complete OMG standards interpretation of SBVR, BPMN, CMMN, DMN and OCL.
- Production identity management or independently verified human signers.
- Parity with the separate .NET 10 reference implementation.
- Publicly archived, immutable research artifact with DOI.

## Experimental hypothesis

Compared with a conventional implementation and developer-authored acceptance tests, a separately approved and qualified oracle baseline should detect more correlated specification/implementation errors, without unacceptable false positives or inconclusive rates.

A valid comparison needs the same tasks, fixed seed defects, blinded independent assessment, predeclared stopping criteria and a public artifact manifest. This is a **hypothesis**, not an observed result.

## Governance alignment

Constitutional/mandate governance (CPAG) concerns **who is allowed to act**. TODM concerns **whether the result satisfies an independently approved behavioral contract**. Neither substitutes for the other.
