#!/usr/bin/env python3
"""Harm tags stay valid and in sync. See okf/harm-ladder.md."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LADDER = [
    "sounds-like-a-machine",
    "loses-the-reader",
    "diminishes-people",
    "manipulates-donors",
    "misrepresents-facts",
    "endangers-a-person",
]
PROMPT_DIRS = [ROOT / "tests" / "prompts", ROOT / "tests" / "prompts" / "pool"]


def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError(f"{path} has no frontmatter")
    return match.group(1)


def list_field(fm: str, name: str) -> list[str] | None:
    match = re.search(rf"^{name}:\s*\[(.*?)\]\s*$", fm, re.MULTILINE)
    if not match:
        return None
    return re.findall(r"[\w-]+", match.group(1))


def scalar_field(fm: str, name: str) -> str | None:
    match = re.search(rf"^{name}:\s*(\S+)\s*$", fm, re.MULTILINE)
    return match.group(1) if match else None


def rule_files() -> dict[str, Path]:
    return {
        p.stem: p
        for p in sorted((ROOT / "okf").glob("*/rules/*.md"))
        if p.name != "index.md"
    }


def rule_harms() -> dict[str, list[str]]:
    return {slug: list_field(frontmatter(p), "harm") for slug, p in rule_files().items()}


def by_severity(harms: set[str]) -> list[str]:
    return sorted(harms, key=LADDER.index, reverse=True)


def prompt_files() -> list[Path]:
    return [p for d in PROMPT_DIRS for p in sorted(d.glob("[0-9]*.md"))]


class HarmTagTests(unittest.TestCase):
    def test_every_rule_has_valid_harm(self):
        for slug, harms in rule_harms().items():
            self.assertIsNotNone(harms, f"{slug} has no harm field")
            for h in harms:
                self.assertIn(h, LADDER, f"{slug}: unknown harm {h}")
            self.assertEqual(harms, by_severity(set(harms)), f"{slug}: list most severe first")

    def test_only_grading_markers_have_no_harm(self):
        for slug, harms in rule_harms().items():
            if not harms:
                tags = list_field(frontmatter(rule_files()[slug]), "tags") or []
                self.assertIn("grading-marker", tags, f"{slug}: empty harm on a writing rule")

    def test_prompt_harm_is_derived_from_rules(self):
        harms = rule_harms()
        for path in prompt_files():
            fm = frontmatter(path)
            rules = list_field(fm, "rules")
            expected = by_severity({h for r in rules for h in harms[r]})
            self.assertEqual(list_field(fm, "harm"), expected, f"{path.name}: harm drifted from rules")
            self.assertEqual(
                scalar_field(fm, "harm_max"),
                expected[0] if expected else "none",
                f"{path.name}: harm_max",
            )

    def test_prompt_meta_json_matches_prompt_files(self):
        meta = {m["id"]: m for m in json.loads((ROOT / "tests" / "prompt-meta-45.json").read_text())}
        for path in sorted((ROOT / "tests" / "prompts").glob("[0-9]*.md")):
            fm = frontmatter(path)
            entry = meta[scalar_field(fm, "id")]
            self.assertEqual(list_field(f"harm: {entry['harm']}", "harm"), list_field(fm, "harm"), path.name)
            self.assertEqual(entry["harm_max"], scalar_field(fm, "harm_max"), path.name)


if __name__ == "__main__":
    unittest.main()
