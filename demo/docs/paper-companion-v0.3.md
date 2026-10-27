# TODM paper companion — verified scope, v0.3

**Paper:** *TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering* (v1.1). This is a **synthetic executable artifact**, not a field study.

## New evidence

The prior Python reference evaluates five narrowly scoped JSON oracle families and sixteen synthetic two-plane fixtures. v0.3 adds Ed25519 **detached signatures** over the G2 manifest digest and individual G6 demo approvals. It includes 10 adversarial qualification tests for invalid/missing signatures, baseline changes, wrong digest, and approval replay. These demonstrate cryptographic binding *within this local reference harness*; they do **not** establish human identity, organizational authority, or unbypassable production deployment.

## Reproduction

```
python3 scripts/verify_all.py
python3 scripts/signed_assurance.py
python3 scripts/verify_signed.py
```

Requires Python 3.10+, OpenSSL with Ed25519. .NET 10 compilation and Python/.NET parity remain to be verified in a .NET-enabled environment. See `docs/research-protocol-v0.3.md` for the proposed empirical study, and `assurance/README.md` for the threat model.

## Suggested publication paragraph

> We provide a synthetic executable companion implementing five limited JSON-based oracle profiles, deterministic positive and negative controls, a two-plane authorization/verification demonstration, and detached Ed25519 signatures binding a versioned oracle manifest and fixture-specific release approvals. The Python reference and adversarial qualification checks are reproducible from the supplied archive. This prototype illustrates the proposed methodological controls but does not validate their comparative effectiveness or the identity of real human approvers. Full OMG conformance, .NET execution parity, real identity integration, and industrial deployment remain outside the validated scope.
