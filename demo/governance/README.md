# CPAG/TODM two-plane governance demonstrator

This fixture layer separates **permission to act** (synthetic CPAG-style mandate checks) from **correctness of results** (TODM oracle checks). It is a conceptual integration; **not** a full implementation of CPAG or an identity/authorization product.

`mandates.json` defines time-limited permissions. `fixtures.json` supplies deterministic scenarios, agent actions, and release approvals. A fixed evaluation instant makes experiments reproducible. A **release** occurs only as a JSON verdict `SIMULATED_ALLOW`; no external deployment or privilege grant occurs.

The Python runner (`scripts/governance.py`) and C# runner (`src/Todm.Governance`) consume the same fixtures. They must agree on oracle, authority, and release verdicts. `scripts/verify_all.py` also checks baseline tampering, unknown principals, revoked mandates, and missing evidence.

**Security boundary:** JSON files in the same checkout can be edited by the same user. Digest checks alone are not a signature. Production use requires separately protected baseline approvals, verifiable identities, independent authorization enforcement, protected CI environments, and auditable release approval.
