import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from todm_demo import PASS, FAIL, INCONCLUSIVE, load_baseline, evaluate, release_gate

class TestTODM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy, cls.digest = load_baseline()

    def oracle(self, **updates):
        case = {"amount": 9000, "customerActive": True, "risk": "low", "decision": "APPROVE"}
        case.update(updates)
        return evaluate(case, self.policy)

    def gate(self, oracle=None, **updates):
        args = dict(mandate_active=True, approval_g6=True,
                    baseline_sha256=self.digest, approved_baseline_sha256=self.digest)
        args.update(updates)
        return release_gate(oracle or self.oracle(), **args)

    def test_correct_greenfield(self):
        self.assertEqual(self.oracle()["verdict"], PASS)

    def test_threshold_boundary_exact(self):
        self.assertEqual(self.oracle(amount=10000)["verdict"], PASS)

    def test_wrong_threshold_mutant(self):
        self.assertEqual(self.oracle(amount=11000)["verdict"], FAIL)

    def test_high_risk_review(self):
        self.assertEqual(self.oracle(risk="high", decision="REVIEW")["verdict"], PASS)

    def test_inactive_customer(self):
        self.assertEqual(self.oracle(customerActive=False, decision="REJECT")["verdict"], PASS)

    def test_incomplete_evidence(self):
        self.assertEqual(evaluate({"decision": "APPROVE"}, self.policy)["verdict"], INCONCLUSIVE)

    def test_wrong_behavior_blocks(self):
        self.assertEqual(self.gate(self.oracle(amount=11000))["decision"], "BLOCK")

    def test_revoked_agent_blocks_correct_software(self):
        self.assertEqual(self.gate(mandate_active=False)["decision"], "BLOCK")

    def test_no_release_approval_blocks(self):
        self.assertEqual(self.gate(approval_g6=False)["decision"], "BLOCK")

    def test_baseline_tampering_blocks(self):
        self.assertEqual(self.gate(baseline_sha256="tampered")["decision"], "BLOCK")

    def test_correct_and_authorized_allows(self):
        self.assertEqual(self.gate()["decision"], "ALLOW")

if __name__ == "__main__":
    unittest.main()
