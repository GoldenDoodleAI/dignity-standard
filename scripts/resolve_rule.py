#!/usr/bin/env python3
"""Resolve bench rule slugs to OKF rule files.

Used by dignity-bench judge loading and by CI in this repo.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULE_DIRS = (
    ROOT / "okf" / "standard" / "rules",
    ROOT / "okf" / "trauma-informed" / "rules",
)


class RuleFileNotFoundError(FileNotFoundError):
    """Referenced rule slug has no file under okf/*/rules/."""


def resolve_rule_file(slug: str) -> Path:
    """Return the path to the rule markdown file for ``slug``.

    Raises RuleFileNotFoundError if no ``{slug}.md`` exists in a rules directory.
    Raises ValueError for invalid slugs.
    """
    if not slug or not isinstance(slug, str):
        raise ValueError("rule slug must be a non-empty string")
    if slug != slug.strip():
        raise ValueError(f"invalid rule slug (whitespace): {slug!r}")
    if "/" in slug or "\\" in slug or ".." in slug:
        raise ValueError(f"invalid rule slug (path characters): {slug!r}")

    matches: list[Path] = []
    for directory in RULE_DIRS:
        candidate = directory / f"{slug}.md"
        if candidate.is_file():
            matches.append(candidate)

    if not matches:
        searched = ", ".join(str(d.relative_to(ROOT)) for d in RULE_DIRS)
        raise RuleFileNotFoundError(
            f"No rule file for slug '{slug}'. Expected {slug}.md under: {searched}"
        )
    if len(matches) > 1:
        raise RuleFileNotFoundError(
            f"Ambiguous rule slug '{slug}': multiple files: {matches}"
        )
    return matches[0]


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: resolve_rule.py <slug>", file=sys.stderr)
        return 2
    try:
        path = resolve_rule_file(args[0])
    except (RuleFileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
