#!/usr/bin/env python3
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

FORBIDDEN_IN_NEW_TEXT = (
    "HCL",
    "Dignity Bench",
    "Dignity Standard",
    "Dignified Language",
    "Human-Centered Language AI",
    "core layer",
    "certified",
)

MARKETPLACE_PATHS = (
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / ".cursor-plugin" / "marketplace.json",
    ROOT / ".agents" / "plugins" / "marketplace.json",
)

EXPECTED_PLUGINS = (
    "human-centered-language",
    "trauma-informed-communications",
    "human-voice",
)


def skill_frontmatter_for_denylist(skill_md: str) -> str:
    """Scan only name/description in SKILL frontmatter.

    The markdown body is frozen v0.1.1 install copy and may contain retired
    brand strings; the body is exempt from the denylist (see PR body).
    """
    parts = skill_md.split("---\n", 2)
    if len(parts) < 2:
        return skill_md
    lines = []
    for line in parts[1].splitlines():
        if line.startswith("name:") or line.startswith("description:"):
            lines.append(line)
    return "\n".join(lines)


class ManifestTests(unittest.TestCase):
    def test_version_file(self):
        self.assertRegex(VERSION, r"^\d+\.\d+\.\d+$")

    def test_marketplace_files_exist(self):
        for path in MARKETPLACE_PATHS:
            self.assertTrue(path.is_file(), f"missing {path}")

    def test_marketplace_name_and_plugins(self):
        for path in MARKETPLACE_PATHS:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data.get("name"), "goldendoodle-ai")
            plugins = data.get("plugins") or []
            names = [p.get("name") for p in plugins]
            self.assertEqual(names, list(EXPECTED_PLUGINS))
            for plugin in plugins:
                policy = plugin.get("policy") or {}
                self.assertNotEqual(
                    policy.get("defaultEnabled"),
                    False,
                    f"{plugin.get('name')} must not set defaultEnabled:false",
                )

    def test_plugin_dirs_and_versions(self):
        for name in EXPECTED_PLUGINS:
            plugin_dir = ROOT / "plugins" / name
            plugin_json = plugin_dir / "plugin.json"
            self.assertTrue(plugin_json.is_file(), plugin_dir)
            meta = json.loads(plugin_json.read_text(encoding="utf-8"))
            self.assertEqual(meta.get("version"), VERSION)
            skill_md = plugin_dir / "SKILL.md"
            self.assertTrue(skill_md.is_file())
            text = skill_md.read_text(encoding="utf-8")
            self.assertIn(f"version: {VERSION}", text)
            self.assertIn("license: CC-BY-4.0", text)

    def test_forbidden_strings_in_marketplace_and_plugins(self):
        paths = list(MARKETPLACE_PATHS)
        for name in EXPECTED_PLUGINS:
            paths.append(ROOT / "plugins" / name / "plugin.json")
            paths.append(ROOT / "plugins" / name / "SKILL.md")
            paths.append(ROOT / "packaging" / "claude-skill" / name / "SKILL.md")
        for path in paths:
            raw = path.read_text(encoding="utf-8")
            text = (
                skill_frontmatter_for_denylist(raw)
                if path.name == "SKILL.md"
                else raw
            )
            for forbidden in FORBIDDEN_IN_NEW_TEXT:
                self.assertNotIn(
                    forbidden,
                    text,
                    f"{forbidden} found in {path.relative_to(ROOT)}",
                )

    def test_human_voice_release_zip_exists(self):
        zip_path = ROOT / "packaging" / "releases" / "human-voice.zip"
        self.assertTrue(zip_path.is_file())


if __name__ == "__main__":
    unittest.main()
