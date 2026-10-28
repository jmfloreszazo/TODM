#!/usr/bin/env python3
"""Synthetic approval binding. NOT identity authentication or access enforcement."""
import hashlib
import json
from dataclasses import dataclass

def digest(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

@dataclass(frozen=True)
class Approval:
    expected_sha256: str
    scope: str
    approver: str
    approved: bool

def release_decision(payload, approval, scope, verdict, mandate_allowed):
    if mandate_allowed is not True:
        return "BLOCK", "MANDATE_DENIED"
    if approval.approved is not True or not approval.approver:
        return "BLOCK", "APPROVAL_MISSING"
    if not isinstance(scope, str) or scope != approval.scope:
        return "BLOCK", "SCOPE_MISMATCH"
    try:
        observed = digest(payload)
    except (TypeError, ValueError):
        return "BLOCK", "INVALID_PAYLOAD"
    if observed != approval.expected_sha256:
        return "BLOCK", "APPROVED_PAYLOAD_CHANGED"
    if verdict not in ("PASS", "FAIL", "INCONCLUSIVE"):
        return "BLOCK", "INVALID_VERDICT"
    if verdict != "PASS":
        return "BLOCK", verdict
    return "ALLOW", "ALL_CHECKS_PASSED"

def example():
    rule = {"rule": "expense-cap", "currency": "EUR", "max": 10000}
    approval = Approval(digest(rule), "expense-release", "synthetic-owner", True)
    variants = {
        "positive": release_decision(rule, approval, "expense-release", "PASS", True),
        "wrong_threshold": release_decision({**rule, "max": 12000}, approval, "expense-release", "PASS", True),
        "inconclusive": release_decision(rule, approval, "expense-release", "INCONCLUSIVE", True),
        "unauthorized": release_decision(rule, approval, "expense-release", "PASS", False),
    }
    return {"synthetic": True, "identity_authenticated": False,
            "cases": {name: {"decision": result[0], "reason": result[1]}
                      for name, result in variants.items()}}

if __name__ == "__main__":
    print(json.dumps(example(), indent=2, sort_keys=True))
