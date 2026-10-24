#!/usr/bin/env python3
"""Render single-file versions of the standard into packaging/.

Reads okf/ in load order, strips YAML frontmatter, and writes compiled,
platform adapters, Claude skills, release zips, plugin stubs, and marketplace
manifests.

Run from the repository root: python3 scripts/build.py
Use --check to exit non-zero if outputs are stale (used by CI).
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from v011_model_text import PREAMBLE_V011, SKILL_BODY_V011
OKF = ROOT / "okf"
PKG = ROOT / "packaging"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

BASE_ORDER = [
    "standard/precedence.md",
    "standard/principles.md",
    "standard/rules/deficit-based-language.md",
    "standard/rules/terminology-mirroring.md",
    "standard/rules/organization-as-hero.md",
    "standard/rules/cognitive-accessibility.md",
    "standard/rules/style-basics.md",
    "standard/rules/fact-preservation.md",
    "standard/rules/trauma-assumption.md",
    "standard/rules/non-pathologizing.md",
    "standard/rules/rewrite.md",
    "standard/rules/over-correction.md",
    "standard/vocabulary/person-first.md",
    "standard/vocabulary/housing.md",
    "standard/vocabulary/substance-use.md",
    "standard/vocabulary/mental-health.md",
    "standard/vocabulary/disability.md",
    "standard/vocabulary/non-pathologizing.md",
    "standard/vocabulary/reporting-standards.md",
    "standard/protocols/rewrite.md",
]

TI_ORDER = [
    "trauma-informed/four-rs.md",
    "trauma-informed/six-principles.md",
    "trauma-informed/rules/urgency-exploitation.md",
    "trauma-informed/rules/trauma-exploitation-storytelling.md",
    "trauma-informed/rules/savior-framing.md",
    "trauma-informed/rules/donor-audience-rationalization.md",
    "trauma-informed/rules/identifiability-consent.md",
    "trauma-informed/rules/crisis.md",
    "trauma-informed/protocols/crisis.md",
]

HUMAN_VOICE_SOURCE = "modules/human-voice.md"

LAYERS = {
    "human-centered-language": {
        "legacy_compiled": "dignified-language.md",
        "legacy_zip": "dignified-language",
        "ti": False,
    },
    "trauma-informed-communications": {
        "legacy_compiled": "trauma-informed.md",
        "legacy_zip": "trauma-informed",
        "ti": True,
    },
}

PREAMBLE = PREAMBLE_V011

PLUGIN_DESCRIPTION = {
    "human-centered-language": (
        "Apply the human-centered language standard to any writing that describes people. "
        "Use when drafting or revising appeals, newsletters, social posts, testimony, case notes, press releases, "
        "or internal memos for an organization that serves, represents, or advocates for people. "
        "Applies person-first language, removes deficit framing, keeps the organization out of the hero role, "
        "and defaults to plain language. Also use when asked to rewrite respectfully, check for stigmatizing language, "
        "or make copy person-first."
    ),
    "trauma-informed-communications": (
        "Apply the trauma-informed standard (SAMHSA framework, editor Laura Braden) on top of the human-centered language standard. "
        "Use for any writing by or for an organization serving people affected by trauma: shelters, treatment providers, "
        "family services, survivor advocacy, community health, and their funders. Covers fundraising appeals, donor stories, "
        "newsletters, social posts, case notes, summaries, and crisis communications. "
        "Use when asked for trauma-informed writing, when donor storytelling involves people served, or when a situation is urgent or distressed."
    ),
    "human-voice": (
        "Suppress common AI writing patterns so drafts read as written by a person. Optional add-on to the human-centered language standard. "
        "Use when polishing appeals, newsletters, social posts, reports, or any copy that should not sound machine-generated. "
        "Also use when asked to make copy sound human, remove AI tells, or de-AI a draft. "
        "Does not replace human-centered or trauma-informed practices if those are also loaded."
    ),
}

MARKETPLACE_NAME = "goldendoodle-ai"
MARKETPLACE_OWNER = "GoldenDoodle AI"


def read(rel):
    text = (OKF / rel).read_text(encoding="utf-8")
    return FRONTMATTER.sub("", text, count=1).strip() + "\n"


def check_no_em_dash(text):
    if "\u2014" in text:
        raise SystemExit("Em dash found in source. House rule: none allowed.")


def render(layer_key):
    ti = LAYERS[layer_key]["ti"]
    files = BASE_ORDER + (TI_ORDER if ti else [])
    body = "\n\n".join(read(f) for f in files)
    check_no_em_dash(body)
    return PREAMBLE[layer_key] + body


def render_human_voice():
    body = read(HUMAN_VOICE_SOURCE)
    check_no_em_dash(body)
    return PREAMBLE["human-voice"] + body


def skill_md(layer_key):
    return (
        "---\n"
        f"name: {layer_key}\n"
        f"description: {PLUGIN_DESCRIPTION[layer_key]}\n"
        "license: CC-BY-4.0\n"
        "metadata:\n"
        f"  version: {VERSION}\n"
        "---\n\n"
        f"{SKILL_BODY_V011[layer_key]}"
    )


def layer_output_paths(layer_key, filename_stem):
    return [
        PKG / "compiled" / f"{filename_stem}.md",
        PKG / "claude-skill" / layer_key / "standard.md",
        PKG / "chatgpt" / f"{filename_stem}.md",
        PKG / "gemini" / f"{filename_stem}.md",
    ]


def human_voice_outputs():
    content_name = "human-voice.md"
    return [
        PKG / "compiled" / content_name,
        PKG / "claude-skill" / "human-voice" / "module.md",
        PKG / "chatgpt" / content_name,
        PKG / "gemini" / content_name,
    ]


def write_or_check(path, content, check, stale):
    path.parent.mkdir(parents=True, exist_ok=True)
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(str(path.relative_to(ROOT)))
    else:
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)} ({len(content):,} chars)")


def build_skill_zip(skill_name, check, stale):
    skill_dir = PKG / "claude-skill" / skill_name
    zip_path = PKG / "releases" / f"{skill_name}.zip"
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    if check:
        if not zip_path.exists():
            stale.append(str(zip_path.relative_to(ROOT)))
            return
        with zipfile.ZipFile(zip_path, "r") as existing:
            expected = {
                (path.relative_to(skill_dir).as_posix(), path.read_bytes())
                for path in skill_dir.iterdir()
                if path.is_file()
            }
            actual = {
                (info.filename, existing.read(info.filename))
                for info in existing.infolist()
                if not info.is_dir()
            }
            if expected != actual:
                stale.append(str(zip_path.relative_to(ROOT)))
        return

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.iterdir()):
            if path.is_file():
                zf.write(path, arcname=path.name)
    print(f"wrote {zip_path.relative_to(ROOT)}")


def write_json_or_check(path, data, check, stale):
    content = json.dumps(data, indent=2) + "\n"
    write_or_check(path, content, check, stale)


def sync_plugin_dir(skill_name, check, stale):
    """Copy skill entry files into plugins/<skill>/ for marketplace packaging."""
    src = PKG / "claude-skill" / skill_name
    dest = ROOT / "plugins" / skill_name
    dest.mkdir(parents=True, exist_ok=True)
    plugin_json = {
        "name": skill_name,
        "version": VERSION,
        "description": PLUGIN_DESCRIPTION[skill_name],
        "license": "CC-BY-4.0",
    }
    write_json_or_check(dest / "plugin.json", plugin_json, check, stale)
    for fname in src.iterdir():
        if fname.is_file():
            write_or_check(dest / fname.name, fname.read_text(encoding="utf-8"), check, stale)


def build_marketplaces(check, stale):
    plugin_entries = []
    for skill_name in ("human-centered-language", "trauma-informed-communications", "human-voice"):
        plugin_entries.append(
            {
                "name": skill_name,
                "description": PLUGIN_DESCRIPTION[skill_name],
                "version": VERSION,
                "source": f"./plugins/{skill_name}",
            }
        )

    claude_marketplace = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": MARKETPLACE_OWNER},
        "metadata": {"version": VERSION},
        "plugins": plugin_entries,
    }
    cursor_marketplace = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": MARKETPLACE_OWNER},
        "metadata": {
            "description": "Human-centered language and trauma-informed standards for mission-driven organizations",
            "version": VERSION,
        },
        "plugins": [
            {
                "name": entry["name"],
                "source": entry["source"],
                "version": VERSION,
                "description": entry["description"],
            }
            for entry in plugin_entries
        ],
    }
    agents_marketplace = {
        "name": MARKETPLACE_NAME,
        "interface": {"displayName": "GoldenDoodle AI standards"},
        "plugins": [
            {
                "name": entry["name"],
                "source": {"source": "local", "path": entry["source"]},
                "policy": {"installation": "AVAILABLE"},
                "category": "Productivity",
            }
            for entry in plugin_entries
        ],
    }

    write_json_or_check(ROOT / ".claude-plugin" / "marketplace.json", claude_marketplace, check, stale)
    write_json_or_check(ROOT / ".cursor-plugin" / "marketplace.json", cursor_marketplace, check, stale)
    write_json_or_check(ROOT / ".agents" / "plugins" / "marketplace.json", agents_marketplace, check, stale)


def main():
    check = "--check" in sys.argv
    stale = []

    for layer_key, cfg in LAYERS.items():
        content = render(layer_key)
        for out in layer_output_paths(layer_key, layer_key):
            write_or_check(out, content, check, stale)
        legacy = cfg["legacy_compiled"]
        write_or_check(PKG / "compiled" / legacy, content, check, stale)

        skill_dir = PKG / "claude-skill" / layer_key
        write_or_check(skill_dir / "standard.md", content, check, stale)
        write_or_check(skill_dir / "SKILL.md", skill_md(layer_key), check, stale)

    human_voice_content = render_human_voice()
    for out in human_voice_outputs():
        write_or_check(out, human_voice_content, check, stale)
    hv_dir = PKG / "claude-skill" / "human-voice"
    write_or_check(hv_dir / "module.md", human_voice_content, check, stale)
    write_or_check(hv_dir / "SKILL.md", skill_md("human-voice"), check, stale)

    if not check:
        for layer_key in LAYERS:
            build_skill_zip(layer_key, check=False, stale=stale)
            legacy_zip = LAYERS[layer_key]["legacy_zip"]
            if legacy_zip != layer_key:
                src_zip = PKG / "releases" / f"{layer_key}.zip"
                dest_zip = PKG / "releases" / f"{legacy_zip}.zip"
                dest_zip.write_bytes(src_zip.read_bytes())
                print(f"wrote {dest_zip.relative_to(ROOT)} (legacy alias)")
        build_skill_zip("human-voice", check=False, stale=stale)
        for skill_name in PLUGIN_DESCRIPTION:
            sync_plugin_dir(skill_name, check=False, stale=stale)
        build_marketplaces(check=False, stale=stale)
    else:
        for skill_name in PLUGIN_DESCRIPTION:
            sync_plugin_dir(skill_name, check=True, stale=stale)
        build_marketplaces(check=True, stale=stale)
        for layer_key, cfg in LAYERS.items():
            build_skill_zip(layer_key, check=True, stale=stale)
            if cfg["legacy_zip"] != layer_key:
                legacy_zip = PKG / "releases" / f"{cfg['legacy_zip']}.zip"
                if not legacy_zip.exists():
                    stale.append(str(legacy_zip.relative_to(ROOT)))
        build_skill_zip("human-voice", check=True, stale=stale)

    if check and stale:
        print("Stale compiled files (run scripts/build.py):")
        for s in stale:
            print("  " + s)
        sys.exit(1)


if __name__ == "__main__":
    main()
