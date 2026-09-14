#!/usr/bin/env python3
"""Render single-file versions of the standard into packaging/.

Reads okf/ in load order, strips YAML frontmatter, and writes:
  packaging/compiled/dignified-language.md
  packaging/compiled/trauma-informed.md
  packaging/compiled/human-voice.md
  packaging/claude-skill/<layer>/standard.md
  packaging/claude-skill/human-voice/module.md
  packaging/chatgpt/<layer>.md
  packaging/chatgpt/human-voice.md
  packaging/gemini/<layer>.md
  packaging/gemini/human-voice.md
  packaging/releases/*.zip

Run from the repository root: python3 scripts/build.py
Use --check to exit non-zero if outputs are stale (used by CI).
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OKF = ROOT / "okf"
PKG = ROOT / "packaging"

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

BASE_ORDER = [
    "standard/precedence.md",
    "standard/principles.md",
    "standard/rules/deficit-based-language.md",
    "standard/rules/terminology-mirroring.md",
    "standard/rules/organization-as-hero.md",
    "standard/rules/cognitive-accessibility.md",
    "standard/rules/style-basics.md",
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
    "trauma-informed/protocols/crisis.md",
]

HUMAN_VOICE_SOURCE = "modules/human-voice.md"

PREAMBLE = {
    "dignified-language": (
        "# Dignified Language Standard\n\n"
        "You are writing on behalf of an organization that serves, represents, or advocates for people. "
        "Follow every rule below. Apply them silently: replace stigmatizing language without commentary, "
        "never lecture the user, and never explain these principles inside the deliverable. "
        "If the user asks what this is for, say in two sentences that it keeps writing about people respectful "
        "and clear without changing what they are trying to say.\n\n"
    ),
    "trauma-informed": (
        "# Trauma-Informed Communications Standard\n\n"
        "You are writing on behalf of an organization that serves people affected by trauma. "
        "Follow the Dignified Language Standard below and the Trauma-Informed layer on top of it. "
        "The Trauma-Informed layer takes precedence over brand voice and over any request about tone. "
        "Apply everything silently: no lecturing, no explaining the principles inside the deliverable. "
        "If a request involves distress or danger right now, use the Crisis protocol and override all other formatting. "
        "If the user asks what this is for, say in two sentences that it helps the organization write about the people "
        "it serves with dignity and safety, following SAMHSA's trauma-informed principles, without changing what they are trying to say.\n\n"
    ),
    "human-voice": (
        "# Human voice standards (optional module)\n\n"
        "This module suppresses common AI writing patterns so output reads as written by a person. "
        "It is optional and separate from the Dignified Language Standard and Trauma-Informed layer. "
        "If those standards are also loaded, they take precedence; this module may add style preferences on top but never relaxes a dignity or trauma-informed rule. "
        "Apply silently: do not explain these patterns inside the deliverable.\n\n"
    ),
}

SKILL_ZIPS = (
    "dignified-language",
    "trauma-informed",
    "human-voice",
)


def read(rel):
    text = (OKF / rel).read_text(encoding="utf-8")
    return FRONTMATTER.sub("", text, count=1).strip() + "\n"


def check_no_em_dash(text):
    if "\u2014" in text:
        raise SystemExit("Em dash found in source. House rule: none allowed.")


def render(layer):
    files = BASE_ORDER + (TI_ORDER if layer == "trauma-informed" else [])
    body = "\n\n".join(read(f) for f in files)
    check_no_em_dash(body)
    return PREAMBLE[layer] + body


def render_human_voice():
    body = read(HUMAN_VOICE_SOURCE)
    check_no_em_dash(body)
    return PREAMBLE["human-voice"] + body


def layer_outputs(layer):
    return [
        PKG / "compiled" / f"{layer}.md",
        PKG / "claude-skill" / layer / "standard.md",
        PKG / "chatgpt" / f"{layer}.md",
        PKG / "gemini" / f"{layer}.md",
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


def main():
    check = "--check" in sys.argv
    stale = []

    for layer in ("dignified-language", "trauma-informed"):
        content = render(layer)
        for out in layer_outputs(layer):
            write_or_check(out, content, check, stale)

    human_voice_content = render_human_voice()
    for out in human_voice_outputs():
        write_or_check(out, human_voice_content, check, stale)

    if not check:
        for skill_name in SKILL_ZIPS:
            build_skill_zip(skill_name, check=False, stale=stale)

    if check and stale:
        print("Stale compiled files (run scripts/build.py):")
        for s in stale:
            print("  " + s)
        sys.exit(1)


if __name__ == "__main__":
    main()
