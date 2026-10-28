# Synthetic content-bound approval reference

This Python standard-library reference binds a synthetic business approval to the exact canonical JSON rule and a declared scope.

Run:

    python3 -m unittest discover -s research/challenge/approval_reference -p 'test_*.py' -v
    python3 research/challenge/approval_reference/approval_binding.py

The positive control allows the unchanged EUR 10,000 rule with PASS and a synthetic approval. Changing it to EUR 12,000 blocks release even if the caller supplies PASS. FAIL, INCONCLUSIVE, missing approval and mandate denial also block.

## Limitations / threat model

- The approval and business rule MUST be stored in separate permission domains. If an agent can replace the rule **and its trusted digest**, it can forge apparent consistency.
- The approver name is not authenticated; there is no real business-signoff workflow.
- Mandate and verdict are caller-supplied inputs. They MUST come from protected independent authorization and evaluation services in any real deployment.
- A passing unit test or workflow is NOT evidence of an agent write being denied by repository permissions.
- Canonical JSON is a Python-local demonstration, not a standardized cross-language canonicalization claim.
- This demo is not a DMN interpreter, a production policy decision point, nor a security assurance certification.

A future P1 acceptance test must use restricted credentials against protected oracle paths, show a rejected write, show an allowed implementation edit, and record the outcomes. Until then P1 is NOT complete.
