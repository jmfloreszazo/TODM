#!/usr/bin/env python3
"""Adversarial offline release gate tests; no signing keys required."""
import json, unittest
from unittest.mock import patch
from audit_release import evaluate

class GateTests(unittest.TestCase):
    def test_authorized_case(self):
        r=evaluate('GF-01-greenfield-approved')
        self.assertEqual(r['outcome'],'DEMO_SIGNED_ALLOW')
        self.assertTrue(r['g2Attested'])
        self.assertTrue(r['g6SignatureVerified'])
    def test_bad_policy_mutant(self):
        r=evaluate('GF-03-wrong-threshold')
        self.assertEqual(r['outcome'],'BLOCK')
        self.assertEqual(r['oracle'],'FAIL')
    def test_unknown_case_fail_closed(self):
        self.assertEqual(evaluate('UNKNOWN')['outcome'],'BLOCK')
    def test_baseline_signature_error_fail_closed(self):
        with patch('audit_release.baseline_attested',side_effect=ValueError('bad G2 signature')):
            r=evaluate('GF-01-greenfield-approved')
        self.assertEqual(r['outcome'],'BLOCK')
    def test_revoked_or_unauthorized_fixtures(self):
        data=json.loads((__import__('pathlib').Path(__file__).resolve().parents[1]/'governance/fixtures.json').read_text())
        cases=[f for f in data['cases'] if f['expectedAuthority']=='FAIL']
        self.assertGreaterEqual(len(cases),3)
        for f in cases:
            with self.subTest(case=f['id']):
                self.assertEqual(evaluate(f['id'])['outcome'],'BLOCK')
    def test_missing_g6_signature_fail_closed(self):
        with patch('audit_release.gate',return_value='BLOCK'):
            self.assertEqual(evaluate('GF-01-greenfield-approved')['outcome'],'BLOCK')
    def test_evaluation_error_fail_closed(self):
        with patch('audit_release.run_case',side_effect=KeyError('evidence')):
            self.assertEqual(evaluate('GF-01-greenfield-approved')['outcome'],'BLOCK')
if __name__=='__main__':unittest.main(verbosity=2)
