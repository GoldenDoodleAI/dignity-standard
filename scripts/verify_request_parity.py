#!/usr/bin/env python3
"""Compare compiled packaging against main for bench request parity.

Mirrors dignity-bench verify_request_parity / test_cache_prefix behavior at a
high level: model-facing text is the full compiled file. Reports whether a
release needs a new bench baseline (any model-facing text change).
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Main-branch compiled filenames -> current primary compiled filenames
LAYER_MAP = (
    ("dignified-language.md", "human-centered-language.md"),
    ("trauma-informed.md", "trauma-informed-communications.md"),
    ("human-voice.md", "human-voice.md"),
)

PREAMBLE_MARKERS = (
    "# Principles",
    "# Four R's",
    "# Human voice standards",
)


def git_show_main(path: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"main:{path}"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None


def split_preamble_body(text: str) -> tuple[str, str]:
    for marker in PREAMBLE_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            return text[:idx], text[idx:]
    return text, ""


def cache_prefix(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def main() -> int:
    compiled = ROOT / "packaging" / "compiled"
    changes: list[str] = []
    preamble_changes: list[str] = []
    body_changes: list[str] = []

    for main_name, new_name in LAYER_MAP:
        main_path = f"packaging/compiled/{main_name}"
        new_path = compiled / new_name
        main_text = git_show_main(main_path)
        if main_text is None:
            changes.append(f"MISSING on main: {main_path}")
            continue
        if not new_path.exists():
            changes.append(f"MISSING on branch: {new_path.relative_to(ROOT)}")
            continue
        new_text = new_path.read_text(encoding="utf-8")
        if cache_prefix(main_text) == cache_prefix(new_text):
            continue
        main_pre, main_body = split_preamble_body(main_text)
        new_pre, new_body = split_preamble_body(new_text)
        if main_pre != new_pre:
            preamble_changes.append(f"{main_name} -> {new_name} (preamble/title)")
        if main_body != new_body:
            body_changes.append(f"{main_name} -> {new_name} (okf body)")
        if main_pre == new_pre and main_body == new_body:
            changes.append(f"{main_name} -> {new_name} (whitespace-only diff)")

    new_baseline = bool(preamble_changes or body_changes or changes)

    print("Request parity (compiled vs main)")
    print("=" * 40)
    for line in LAYER_MAP:
        print(f"  main {line[0]}  ->  branch {line[1]}")
    print()
    if not new_baseline:
        print("RESULT: PARITY OK — no model-facing text changes vs main.")
        print("NEW_BENCH_BASELINE=no")
        return 0

    print("RESULT: MODEL-FACING TEXT CHANGED vs main.")
    print("NEW_BENCH_BASELINE=yes")
    if preamble_changes:
        print("\nPreamble / title changes:")
        for item in preamble_changes:
            print(f"  - {item}")
    if body_changes:
        print("\nBody (okf-derived) changes:")
        for item in body_changes:
            print(f"  - {item}")
    if changes:
        print("\nOther:")
        for item in changes:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
