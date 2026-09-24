# Tests

Golden prompts and a scoring rubric for checking whether a model holds the standard.

The frozen **v1.1 set** is **45 prompts** in `prompts/` (numbered `01` through `45`). Machine-readable metadata for bench tooling is in `prompt-meta-45.json`.

Each prompt is a realistic request a nonprofit or association communicator would make, chosen because it tempts a model to break a specific rule. Run each one with the standard loaded and again without it. Score with `rubric.md`. Record results in `MODELS.md`.

Prompts marked `layer: trauma-informed` only apply when that layer is loaded. Prompts marked `layer: standard` apply to both.

Rule files referenced in prompt frontmatter must exist under `okf/*/rules/`. CI checks resolution via `tests/test_resolve_rule.py`.
