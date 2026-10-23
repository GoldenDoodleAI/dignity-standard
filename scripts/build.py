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

PREAMBLE = {
    "human-centered-language": (
        "# Human-centered language standard\n\n"
        "You are writing on behalf of an organization that serves, represents, or advocates for people. "
        "Follow every standard and practice below. Apply them silently: replace stigmatizing language without commentary, "
        "never lecture the user, and never explain these principles inside the deliverable. "
        "If the user asks what this is for, say in two sentences that it keeps writing about people respectful "
        "and clear without changing what they are trying to say.\n\n"
    ),
    "trauma-informed-communications": (
        "# Trauma-informed standard\n\n"
        "You are writing on behalf of an organization that serves people affected by trauma. "
        "Follow the human-centered language standard below and the trauma-informed standard on top of it. "
        "The trauma-informed standard takes precedence over brand voice and over any request about tone. "
        "Apply everything silently: no lecturing, no explaining the principles inside the deliverable. "
        "If a request involves distress or danger right now, use the Crisis protocol and override all other formatting. "
        "If the user asks what this is for, say in two sentences that it helps the organization write about the people "
        "it serves with dignity and safety, following SAMHSA's trauma-informed principles, without changing what they are trying to say.\n\n"
    ),
    "human-voice": (
        "# Human voice standards (optional module)\n\n"
        "This module suppresses common AI writing patterns so output reads as written by a person. "
        "It is optional and separate from the human-centered language standard and trauma-informed standard. "
        "If those standards are also loaded, they take precedence; this module may add style preferences on top but never relaxes a dignity or trauma-informed practice. "
        "Apply silently: do not explain these patterns inside the deliverable.\n\n"
    ),
}

SKILL_META = {
    "human-centered-language": {
        "name": "human-centered-language",
        "title": "Human-centered language standard",
        "description": (
            "Apply the human-centered language standard to any writing that describes people. "
            "Use when drafting or revising appeals, newsletters, social posts, testimony, case notes, press releases, "
            "or internal memos for an organization that serves, represents, or advocates for people. "
            "Applies person-first language, removes deficit framing, keeps the organization out of the hero role, "
            "and defaults to plain language. Also use when asked to rewrite respectfully, check for stigmatizing language, "
            "or make copy person-first."
        ),
        "content_file": "standard.md",
        "body_intro": (
            "When this skill is active, follow the standards and practices in `standard.md` in this folder. "
            "Read it fully before writing."
        ),
        "steps": [
            "Apply the standards and practices silently. Replace stigmatizing terms without commentary. Do not lecture the user about language.",
            "Follow the precedence order in the standard. An organization's brand voice may set tone and preferred terms; it may not override a practice.",
            "When rewriting a draft, follow the Rewrite protocol: preserve facts, structure, perspective, and tone. Change language only.",
            "If a change is large enough that the user might not recognize their intent, add one line after the content noting it.",
            "If the user asks what this skill is for, explain in two sentences: it keeps writing about people respectful and clear, and it does so without changing what the user is trying to say.",
        ],
        "sector": True,
    },
    "trauma-informed-communications": {
        "name": "trauma-informed-communications",
        "title": "Trauma-informed standard",
        "description": (
            "Apply the trauma-informed standard (SAMHSA framework, editor Laura Braden) on top of the human-centered language standard. "
            "Use for any writing by or for an organization serving people affected by trauma: shelters, treatment providers, "
            "family services, survivor advocacy, community health, and their funders. Covers fundraising appeals, donor stories, "
            "newsletters, social posts, case notes, summaries, and crisis communications."
        ),
        "content_file": "standard.md",
        "body_intro": (
            "When this skill is active, follow both standards in `standard.md` in this folder: the human-centered language standard (base) "
            "and the trauma-informed standard on top. Read it fully before writing."
        ),
        "steps": [
            "Apply the standards and practices silently. Replace stigmatizing terms without commentary.",
            "The trauma-informed standard wins over brand voice and tone requests. Follow the precedence order in the file.",
            "If a request involves distress or danger right now, use the Crisis protocol and override all other formatting.",
            "When rewriting a draft, follow the Rewrite protocol: preserve facts, structure, perspective, and tone.",
            "If the user asks what this skill is for, explain in two sentences: it helps the organization write about the people it serves with dignity and safety, following SAMHSA's trauma-informed principles, without changing what the user is trying to say.",
        ],
        "sector": False,
    },
    "human-voice": {
        "name": "human-voice",
        "title": "Human voice standards",
        "description": (
            "Suppress common AI writing patterns so drafts read as written by a person. Optional add-on to the human-centered language standard. "
            "Use when polishing appeals, newsletters, social posts, reports, or any copy that should not sound machine-generated. "
            "Does not replace human-centered or trauma-informed practices if those are also loaded."
        ),
        "content_file": "module.md",
        "body_intro": (
            "When this skill is active, follow the module in `module.md` in this folder. Read it fully before writing."
        ),
        "steps": [
            "If the human-centered language standard or trauma-informed standard is also active, those practices win on any conflict. This module adds style constraints only.",
            "Apply the patterns silently. Do not explain the module inside the deliverable.",
            "If the user asks what this skill is for, explain in two sentences: it suppresses writing habits that read as machine-generated, and it works alongside (not instead of) the human-centered language standard when both are loaded.",
        ],
        "sector": False,
    },
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


def skill_md(meta):
    lines = [
        "---",
        f"name: {meta['name']}",
        f"description: {meta['description']}",
        "license: CC-BY-4.0",
        "metadata:",
        f"  version: {VERSION}",
        "---",
        "",
        f"# {meta['title']}",
        "",
        meta["body_intro"],
        "",
        "## How to apply it",
        "",
    ]
    for i, step in enumerate(meta["steps"], 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    if meta.get("sector"):
        lines.extend(
            [
                "## Sector vocabulary",
                "",
                "The standard includes vocabulary for housing, substance use, mental health, and disability. "
                "Apply the sections relevant to the content. If the organization has supplied its own vocabulary file, "
                "it adds to these; it does not replace them.",
                "",
            ]
        )
    return "\n".join(lines)


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
        "description": SKILL_META[skill_name]["description"],
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
                "description": SKILL_META[skill_name]["description"],
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
        write_or_check(skill_dir / "SKILL.md", skill_md(SKILL_META[layer_key]), check, stale)

    human_voice_content = render_human_voice()
    for out in human_voice_outputs():
        write_or_check(out, human_voice_content, check, stale)
    hv_dir = PKG / "claude-skill" / "human-voice"
    write_or_check(hv_dir / "module.md", human_voice_content, check, stale)
    write_or_check(hv_dir / "SKILL.md", skill_md(SKILL_META["human-voice"]), check, stale)

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
        for skill_name in SKILL_META:
            sync_plugin_dir(skill_name, check=False, stale=stale)
        build_marketplaces(check=False, stale=stale)
    else:
        for skill_name in SKILL_META:
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
