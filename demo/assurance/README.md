# Detached cryptographic assurance (research demonstration)

This layer authenticates G2 baseline digest and G6 fixture-specific approvals with **Ed25519 signatures** verified by OpenSSL. Public verification keys are included. Private signing keys are deliberately **excluded from the distributed repository**. The test fixtures were signed with freshly generated **synthetic demonstration keys**: no real person authenticated, no trusted CA or IdP was involved, and no production release protection is installed.

- `python3 scripts/signed_assurance.py`: 16 two-plane fixtures with signed gate decisions.
- `python3 scripts/verify_signed.py`: 10 tests covering positive, fail-closed, tamper, wrong digest, replay binding.
- G2 signatures bind the manifest SHA-256; `load_baseline()` validates each contract file's digest.
- G6 signatures bind **case ID + G2 digest + approver role**, so a signature for one case cannot authorize another.
- Signature verification requires `openssl` with Ed25519 support. The public key is a pinned *demo* trust anchor, not a verified organizational identity.

**Threat model limitations:** local administrators can replace public keys, modify Python gate code, or bypass the demo CLI; timestamps, certificate chains, append-only logs, real revocation checks, real human approval, artifact attestations and protected CI environments are not implemented. This is cryptographic integrity in a controlled demo, **not non-bypassable enterprise enforcement**.
