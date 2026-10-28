#!/usr/bin/env python3
"""Score frozen S1 agent-oracle outcomes; never generate experimental observations.

Input: JSON array of independently labelled case-level records. This program
does NOT establish the validity of labels or the independence of the oracle.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ARMS = ("S1-A", "S1-B", "S1-C")
VERDICTS = ("PASS", "FAIL", "INCONCLUSIVE")
REQUIRED = {"task_id", "case_id", "arm", "defect_present", "verdict"}


def score(records: list[dict]) -> dict:
    if not isinstance(records, list) or not records:
        raise ValueError("Expected a nonempty list of case-level observations")
    seen: set[tuple[str, str, str]] = set()
    counters = {arm: defaultdict(int) for arm in ARMS}
    tasks = {arm: set() for arm in ARMS}
    for index, record in enumerate(records):
        if not isinstance(record, dict) or not REQUIRED.issubset(record):
            raise ValueError(f"Record {index} missing required fields")
        task, case, arm = record["task_id"], record["case_id"], record["arm"]
        if not all(isinstance(value, str) and value.strip() for value in (task, case)):
            raise ValueError(f"Record {index} has invalid task/case ID")
        if arm not in ARMS:
            raise ValueError(f"Unknown S1 arm: {arm!r}")
        if type(record["defect_present"]) is not bool:
            raise ValueError("defect_present must be boolean, not text or number")
        verdict = record["verdict"]
        if verdict not in VERDICTS:
            raise ValueError(f"Unknown verdict: {verdict!r}")
        key = (task, case, arm)
        if key in seen:
            raise ValueError(f"Duplicate case/arm record: {key}")
        seen.add(key)
        tasks[arm].add(task)
        counts = counters[arm]
        counts["total"] += 1
        if verdict == "INCONCLUSIVE":
            counts["inconclusive"] += 1
            counts["inconclusive_defective" if record["defect_present"]
                   else "inconclusive_clean"] += 1
        elif record["defect_present"]:
            counts["tp" if verdict == "FAIL" else "fn"] += 1
        else:
            counts["fp" if verdict == "FAIL" else "tn"] += 1

    output = {"schema_version": "1.0", "study": "S1", "source": "supplied-observations",
              "independent_ground_truth_verified": False, "arms": {}}
    for arm, counts in counters.items():
        tp, fp, fn, tn = (counts[k] for k in ("tp", "fp", "fn", "tn"))
        output["arms"][arm] = {
            **{k: counts[k] for k in ("total", "tp", "fp", "fn", "tn",
                                     "inconclusive", "inconclusive_defective",
                                     "inconclusive_clean")},
            "tasks": len(tasks[arm]),
            "recall_decisive_only": tp / (tp + fn) if tp + fn else None,
            "precision_decisive_only": tp / (tp + fp) if tp + fp else None,
            "false_positive_rate_decisive_only": fp / (fp + tn) if fp + tn else None,
            "inconclusive_rate": counts["inconclusive"] / counts["total"] if counts["total"] else None,
            "observed_escape_lower_bound": fn,
            "conservative_potential_escapes": fn + counts["inconclusive_defective"],
        }
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("observations", type=Path,
                        help="JSON array; observations must come from an independent study")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = score(json.loads(args.observations.read_text(encoding="utf-8")))
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
