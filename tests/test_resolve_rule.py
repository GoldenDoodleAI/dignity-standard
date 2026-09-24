#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.resolve_rule import RuleFileNotFoundError, resolve_rule_file


class ResolveRuleFileTests(unittest.TestCase):
    def test_resolves_standard_rule(self):
        path = resolve_rule_file("fact-preservation")
        self.assertEqual(
            path, ROOT / "okf" / "standard" / "rules" / "fact-preservation.md"
        )

    def test_resolves_trauma_informed_rule(self):
        path = resolve_rule_file("savior-framing")
        self.assertEqual(
            path,
            ROOT / "okf" / "trauma-informed" / "rules" / "savior-framing.md",
        )

    def test_missing_rule_fails_loud(self):
        with self.assertRaises(RuleFileNotFoundError) as ctx:
            resolve_rule_file("self-explanation")
        self.assertIn("self-explanation", str(ctx.exception))
        self.assertIn("No rule file", str(ctx.exception))

    def test_invalid_slug_rejected(self):
        with self.assertRaises(ValueError):
            resolve_rule_file("../escape")
        with self.assertRaises(ValueError):
            resolve_rule_file("")


if __name__ == "__main__":
    unittest.main()
