# Tests

Golden prompts and a scoring rubric for checking whether a model holds the standard.

The active **v1.2 set** is **45 prompts** in `prompts/`. Machine-readable metadata for bench tooling is in `prompt-meta-45.json`.

v1.2 (2026-10-07) retired six prompts whose text, or a near-copy, appears as a worked example in the compiled skill files (01, 02, 04, 06, 38, 42). They moved to `prompts/retired/` and are never deleted, so old results still resolve. Their replacements are 46 to 51; each carries a `replaces` field. Prompt 52 is staged in `prompts/pool/` (rotating pool, not active). The lineage record (original text, overlap evidence, replacement) is `config/prompt-lineage.yaml` in the bench repo (GoldenDoodleAI/dignity-bench). New prompts always get new numbers.

Each prompt is a realistic request a nonprofit or association communicator would make, chosen because it tempts a model to break a specific rule. Run each one with the standard loaded and again without it. Score with `rubric.md`. Record results in `MODELS.md`.

Prompts marked `layer: trauma-informed` only apply when that layer is loaded. Prompts marked `layer: standard` apply to both.

Rule files referenced in prompt frontmatter must exist under `okf/*/rules/`. CI checks resolution via `tests/test_resolve_rule.py`.
