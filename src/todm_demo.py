"""Minimal, dependency-free TODM research seed. Not a complete OMG interpreter."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "contracts" / "v1" / "policy.json"
PASS, FAIL, INCONCLUSIVE = "PASS", "FAIL", "INCONCLUSIVE"

def baseline_digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def load_baseline():
    raw = POLICY.read_bytes()
    policy = json.loads(raw)
    if policy.get("kind") != "SYNTHETIC_APPROVED_BASELINE":
        raise ValueError("Unrecognized baseline")
    return policy, baseline_digest(raw)

def evaluate(observation: dict, policy: dict) -> dict:
    required = ("amount", "customerActive", "risk", "decision")
    missing = [key for key in required if key not in observation]
    if missing:
        return {"verdict": INCONCLUSIVE, "reason": "missing evidence: " + ",".join(missing)}
    amount = observation["amount"]
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount < 0:
        return {"verdict": INCONCLUSIVE, "reason": "invalid amount"}
    if observation["customerActive"] is False:
        expected = policy["inactiveCustomerDecision"]
    elif observation["risk"] == "high" or amount > policy["reviewAbove"]:
        expected = policy["highRiskDecision"]
    else:
        expected = "APPROVE"
    actual = observation["decision"]
    return {
        "verdict": PASS if actual == expected else FAIL,
        "expected": expected,
        "actual": actual,
        "reason": "oracle result, independent of builder assertion"
    }

def release_gate(oracle: dict, *, mandate_active: bool, approval_g6: bool,
                 baseline_sha256: str, approved_baseline_sha256: str) -> dict:
    checks = {
        "oracle_pass": oracle.get("verdict") == PASS,
        "mandate_active": mandate_active is True,
        "release_approved": approval_g6 is True,
        "baseline_unchanged": baseline_sha256 == approved_baseline_sha256,
    }
    return {"decision": "ALLOW" if all(checks.values()) else "BLOCK", "checks": checks}

def demo():
    policy, digest = load_baseline()
    case = {"amount": 11000, "customerActive": True, "risk": "low", "decision": "APPROVE"}
    oracle = evaluate(case, policy)
    gate = release_gate(oracle, mandate_active=True, approval_g6=True,
                        baseline_sha256=digest, approved_baseline_sha256=digest)
    print(json.dumps({"kind": "SYNTHETIC_TODM_DEMO", "oracle": oracle,
                      "release": gate}, indent=2))
    assert oracle["verdict"] == FAIL and gate["decision"] == "BLOCK"

if __name__ == "__main__":
    demo()
