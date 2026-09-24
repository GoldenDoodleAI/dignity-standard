# Proof card: dignity-standard companion (dignity-bench v1.1 Stage 0)

**Repo:** GoldenDoodleAI/dignity-standard  
**Branch:** `cursor/stage0-rule-boundaries-9cf1`  
**Date:** 2026-09-24  
**Agent:** Forge (Cursor Cloud)

## Scope (this PR only)

Companion work for dignity-bench v1.1 Stage 0 rule resolution. No dignity-bench code in this repository.

## Done

| Item | Evidence |
|------|----------|
| `savior-framing` Scott borderline pair (survivor-led + services list = clean; same close with donor-as-rescuer = violated) | `okf/trauma-informed/rules/savior-framing.md` |
| Orphan rules carry **Decision boundary** sections (draft source: `okf/rule-boundary-protocol.md`) | `fact-preservation`, `trauma-assumption`, `identifiability-consent`, `over-correction` |
| `resolve_rule_file` fails loud on missing slug | `scripts/resolve_rule.py`, `tests/test_resolve_rule.py` |
| Packaging regenerated | `python3 scripts/build.py` |

## Verification (no API spend)

```bash
python3 -m unittest tests/test_resolve_rule.py -v
python3 scripts/build.py --check
python3 scripts/resolve_rule.py fact-preservation
python3 scripts/resolve_rule.py self-explanation  # expect exit 1 + message
```

## Explicitly NOT RUN

- No OpenRouter, Anthropic, OpenAI, or Google generate/chat calls
- No dignity-bench judge dry-run (lives in dignity-bench repo)
- No `--estimate` or calibration matrix (dignity-bench Stage 0 sections 5–7)

## Frozen set respected

- No edits under `tests/prompts/` (prompt wording unchanged)

## Sign-off

Forge — build/configure/report only; zero contestant or judge API spend.
