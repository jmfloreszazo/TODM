"""Tests only of scoring arithmetic and input contract, not agent performance."""
import unittest
from score_s1 import score


def row(task, case, arm, bad, verdict):
    return {"task_id": task, "case_id": case, "arm": arm,
            "defect_present": bad, "verdict": verdict}


class ScoreS1Tests(unittest.TestCase):
    def test_counts_decisive_and_inconclusive_separately(self):
        records = [
            row("t1", "bad", "S1-A", True, "PASS"),
            row("t1", "clean", "S1-A", False, "PASS"),
            row("t1", "bad", "S1-B", True, "FAIL"),
            row("t1", "clean", "S1-B", False, "FAIL"),
            row("t1", "bad", "S1-C", True, "INCONCLUSIVE"),
            row("t1", "clean", "S1-C", False, "PASS"),
        ]
        out = score(records)["arms"]
        self.assertEqual(out["S1-A"]["fn"], 1)
        self.assertEqual(out["S1-B"]["tp"], 1)
        self.assertEqual(out["S1-B"]["fp"], 1)
        self.assertEqual(out["S1-B"]["precision_decisive_only"], 0.5)
        self.assertEqual(out["S1-C"]["inconclusive_defective"], 1)
        self.assertEqual(out["S1-C"]["conservative_potential_escapes"], 1)
        self.assertIsNone(out["S1-C"]["recall_decisive_only"])

    def test_duplicate_rejected(self):
        record = row("t", "c", "S1-A", False, "PASS")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            score([record, record])

    def test_string_ground_truth_rejected(self):
        record = row("t", "c", "S1-A", "false", "PASS")
        with self.assertRaisesRegex(ValueError, "boolean"):
            score([record])

    def test_unknown_verdict_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown verdict"):
            score([row("t", "c", "S1-A", True, "ALLOW")])

    def test_missing_fields_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing required"):
            score([{"arm": "S1-A"}])

    def test_empty_rejected(self):
        with self.assertRaisesRegex(ValueError, "nonempty"):
            score([])

    def test_zero_denominator_null(self):
        result = score([row("t", "c", "S1-A", False, "PASS")])
        self.assertIsNone(result["arms"]["S1-A"]["precision_decisive_only"])
        self.assertEqual(result["arms"]["S1-A"]["false_positive_rate_decisive_only"], 0)

    def test_tasks_count_is_not_number_of_rows(self):
        result = score([row("t", "one", "S1-A", True, "FAIL"),
                        row("t", "two", "S1-A", True, "FAIL")])
        self.assertEqual(result["arms"]["S1-A"]["tasks"], 1)


if __name__ == "__main__":
    unittest.main()
