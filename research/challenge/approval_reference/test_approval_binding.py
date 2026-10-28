"""Unit tests for synthetic content-binding logic, not GitHub permissions."""
import unittest
from approval_binding import Approval, digest, release_decision, example

class ApprovalBindingTests(unittest.TestCase):
    def setUp(self):
        self.rule = {"rule": "expense-cap", "currency": "EUR", "max": 10000}
        self.approval = Approval(digest(self.rule), "finance", "synthetic-owner", True)

    def check(self, payload=None, scope="finance", verdict="PASS", allowed=True, approval=None):
        return release_decision(self.rule if payload is None else payload,
                                self.approval if approval is None else approval,
                                scope, verdict, allowed)

    def test_positive_control(self):
        self.assertEqual(self.check(), ("ALLOW", "ALL_CHECKS_PASSED"))

    def test_changed_threshold_is_blocked_despite_pass(self):
        self.assertEqual(self.check(payload={**self.rule, "max": 12000})[1],
                         "APPROVED_PAYLOAD_CHANGED")

    def test_canonical_key_order(self):
        self.assertEqual(digest(self.rule), digest(dict(reversed(list(self.rule.items())))))

    def test_scope_mismatch(self):
        self.assertEqual(self.check(scope="other")[1], "SCOPE_MISMATCH")

    def test_revoked_approval(self):
        revoked = Approval(digest(self.rule), "finance", "synthetic-owner", False)
        self.assertEqual(self.check(approval=revoked)[1], "APPROVAL_MISSING")

    def test_denied_mandate_overrides_functional_pass(self):
        self.assertEqual(self.check(allowed=False)[1], "MANDATE_DENIED")

    def test_fail_closed_verdicts(self):
        for verdict in ("FAIL", "INCONCLUSIVE", "UNKNOWN", ""):
            with self.subTest(verdict=verdict):
                self.assertEqual(self.check(verdict=verdict)[0], "BLOCK")

    def test_non_json_payload(self):
        self.assertEqual(self.check(payload={"max": float("nan")})[1], "INVALID_PAYLOAD")

    def test_demo_controls(self):
        cases = example()["cases"]
        self.assertEqual(cases["positive"]["decision"], "ALLOW")
        for key in ("wrong_threshold", "inconclusive", "unauthorized"):
            self.assertEqual(cases[key]["decision"], "BLOCK")

if __name__ == "__main__":
    unittest.main()
