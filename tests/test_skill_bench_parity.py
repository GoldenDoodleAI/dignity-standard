#!/usr/bin/env python3
"""Bench parity for Claude/plugin skill bundles.

The weekly bench sends packaging/compiled/*.md as the system message. Installed
users load the skill zip: SKILL.md (install instructions) plus standard.md or
module.md (the same bytes as the compiled file). This module enforces:

1. standard.md / module.md in each bundle is byte-identical to the matching
   packaging/compiled/*.md (what the bench tests).
2. SKILL.md markdown body (after YAML frontmatter) is byte-identical to the
   frozen v0.1.1 install copy (main @ 432ddd4), keyed by the v0.2 folder names.
"""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG = ROOT / "packaging"
SCRIPTS = ROOT / "scripts"

# Load frozen bodies without importing scripts.build (side effects).
_spec = importlib.util.spec_from_file_location("v011_model_text", SCRIPTS / "v011_model_text.py")
_v011 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_v011)
SKILL_BODY_V011 = _v011.SKILL_BODY_V011

LAYER_COMPILED = {
    "human-centered-language": "human-centered-language.md",
    "trauma-informed-communications": "trauma-informed-communications.md",
}

SKILL_LOCATIONS = (
    ("packaging/claude-skill",),
    ("plugins",),
)


def skill_markdown_body(skill_md: str) -> str:
    parts = skill_md.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md missing YAML frontmatter")
    return parts[2].lstrip("\n")


class SkillBenchParityTests(unittest.TestCase):
    def test_compiled_matches_skill_payload_files(self):
        """Byte compare: compiled output == standard.md / module.md in each bundle."""
        for layer, compiled_name in LAYER_COMPILED.items():
            compiled = (PKG / "compiled" / compiled_name).read_bytes()
            for parent, in SKILL_LOCATIONS:
                standard = ROOT / parent / layer / "standard.md"
                self.assertTrue(standard.is_file(), standard)
                self.assertEqual(
                    compiled,
                    standard.read_bytes(),
                    f"{compiled_name} must match {standard.relative_to(ROOT)}",
                )

        hv_compiled = (PKG / "compiled" / "human-voice.md").read_bytes()
        for parent, in SKILL_LOCATIONS:
            module = ROOT / parent / "human-voice" / "module.md"
            self.assertEqual(
                hv_compiled,
                module.read_bytes(),
                f"human-voice.md must match {module.relative_to(ROOT)}",
            )

    def test_skill_body_matches_v011_install_copy(self):
        """SKILL.md body only: frozen v0.1.1 install instructions (bench-aligned substance)."""
        for layer, expected_body in SKILL_BODY_V011.items():
            for parent, in SKILL_LOCATIONS:
                skill_path = ROOT / parent / layer / "SKILL.md"
                self.assertTrue(skill_path.is_file(), skill_path)
                actual = skill_markdown_body(skill_path.read_text(encoding="utf-8"))
                self.assertEqual(
                    expected_body,
                    actual,
                    f"SKILL body drift in {skill_path.relative_to(ROOT)}",
                )


if __name__ == "__main__":
    unittest.main()
