# Proof card: dignity-standard companion (dignity-bench v1.1 Stage 0)

**Repo:** GoldenDoodleAI/dignity-standard  
**Branch:** `cursor/stage0-rule-boundaries-9cf1`  
**PR:** #12 (draft)  
**Date:** 2026-09-24  
**Agent:** Forge (Cursor Cloud)

## Scope

Companion work for dignity-bench v1.1 Stage 0: frozen **45-prompt** set from Scott's Mini pack, rule decision boundaries, and loud rule-file resolution. No dignity-bench runner changes in this repo.

## Done

| Item | Evidence |
|------|----------|
| **45-prompt frozen set** (replaces legacy ~12 on `main`) | `tests/prompts/*.md` (45 files); Scott names present: `39-dv-donor-story`, `07-recovery-fellowship`, `24-deaf-meetup`, `25-autistic-peer-group` |
| Prompt metadata | `tests/prompt-meta-45.json` |
| `savior-framing` Scott borderline pair | Survivor-led + services list → **Clean**; donor-as-rescuer closer → **Violated** in `okf/trauma-informed/rules/savior-framing.md` |
| Orphan rules **Decision boundary** | `fact-preservation`, `trauma-assumption`, `over-correction`, `identifiability-consent`; drafts in `okf/rule-boundary-protocol.md` |
| `resolve_rule_file` fails loud | `scripts/resolve_rule.py`; all 15 rule slugs in the 45-prompt set resolve in CI |
| Packaging regenerated | `python3 scripts/build.py` |

## Verification (no API spend)

```bash
python3 -m unittest tests/test_resolve_rule.py -v
python3 scripts/build.py --check
ls tests/prompts/*.md | wc -l   # expect 45
```

## Explicitly NOT RUN

- No OpenRouter, Anthropic, OpenAI, or Google generate/chat calls
- No dignity-bench judge dry-run or `--estimate` (dignity-bench repo)

## Source

Prompt pack: `dignity-45-prompts-pack.tgz` (Scott Mini export, 2026-09-24). OKF decision-boundary edits applied on top of existing `main` rule files (pack OKF not copied wholesale, to preserve Stage 0 boundary work).

## Sign-off

Forge — build/configure/report only; zero contestant or judge API spend.
