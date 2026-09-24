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

    def test_all_frozen_45_prompt_rules_resolve(self):
        import re

        prompts_dir = ROOT / "tests" / "prompts"
        slugs: set[str] = set()
        for path in sorted(prompts_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            match = re.search(r"^rules:\s*\[(.*?)\]", text, re.MULTILINE)
            self.assertIsNotNone(match, f"no rules frontmatter in {path.name}")
            slugs.update(re.findall(r"[\w-]+", match.group(1)))
        self.assertEqual(len(list(prompts_dir.glob("*.md"))), 45)
        for slug in sorted(slugs):
            resolve_rule_file(slug)


if __name__ == "__main__":
    unittest.main()
