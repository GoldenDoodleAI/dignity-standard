#!/usr/bin/env python3
"""Render single-file versions of the standard into packaging/.

Reads okf/ in load order, strips YAML frontmatter, and writes:
  packaging/compiled/dignified-language.md
  packaging/compiled/trauma-informed.md
  packaging/claude-skill/<layer>/standard.md
  packaging/chatgpt/<layer>.md
  packaging/gemini/<layer>.md

Run from the repository root: python3 scripts/build.py
Use --check to exit non-zero if outputs are stale (used by CI).
"""
import re
import sys
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
}


def read(rel):
    text = (OKF / rel).read_text(encoding="utf-8")
    return FRONTMATTER.sub("", text, count=1).strip() + "\n"


def render(layer):
    files = BASE_ORDER + (TI_ORDER if layer == "trauma-informed" else [])
    body = "\n\n".join(read(f) for f in files)
    if "\u2014" in body:
        raise SystemExit("Em dash found in source. House rule: none allowed.")
    return PREAMBLE[layer] + body


def outputs(layer):
    return [
        PKG / "compiled" / f"{layer}.md",
        PKG / "claude-skill" / layer / "standard.md",
        PKG / "chatgpt" / f"{layer}.md",
        PKG / "gemini" / f"{layer}.md",
    ]


def main():
    check = "--check" in sys.argv
    stale = []
    for layer in ("dignified-language", "trauma-informed"):
        content = render(layer)
        for out in outputs(layer):
            out.parent.mkdir(parents=True, exist_ok=True)
            if check:
                if not out.exists() or out.read_text(encoding="utf-8") != content:
                    stale.append(str(out.relative_to(ROOT)))
            else:
                out.write_text(content, encoding="utf-8")
                print(f"wrote {out.relative_to(ROOT)} ({len(content):,} chars)")
    if check and stale:
        print("Stale compiled files (run scripts/build.py):")
        for s in stale:
            print("  " + s)
        sys.exit(1)


if __name__ == "__main__":
    main()
