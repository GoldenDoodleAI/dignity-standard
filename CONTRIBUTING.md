# Contributing

This standard is maintained by practitioners, not by a committee. If you work in communications for an organization that serves people and a rule here is wrong, incomplete, or missing, we want to hear it.

## What we accept

- Corrections to existing rules, with the reasoning.
- New sector vocabulary files under `okf/standard/vocabulary/`. Follow the format of the existing ones.
- New golden prompts under `tests/prompts/` that expose a failure the current rules do not catch.
- Model results for `MODELS.md`, run with the rubric in `tests/rubric.md`.

## What we do not accept

- Rules without a before/after pair. If you cannot show the difference, it is not a rule yet.
- Changes to the Trauma-Informed layer that weaken it. Sector layers may add; they may not subtract. See `okf/standard/precedence.md`.
- Anything that would require the model to make a factual determination it cannot make from the text in front of it.

## Format

Every content file starts with YAML frontmatter. `type` is required. Use `title`, `description`, and `tags`. Do not add fields that consumers will not know what to do with.

Index files (`index.md`) carry no frontmatter except the bundle root, which may only declare `okf_version: "0.2"`. Sequencing guidance belongs in [okf/load-order.md](okf/load-order.md), not in indexes.

No em dashes anywhere in this repository. It is a house rule and it is enforced.

## Regenerating packaging

After any change under `okf/`, regenerate derived outputs:

```
python3 scripts/build.py
```

This updates `packaging/compiled/`, `packaging/chatgpt/`, `packaging/gemini/`, `packaging/claude-skill/*/standard.md`, `packaging/claude-skill/human-voice/module.md`, and `packaging/releases/*.zip`. Commit the regenerated files with your pull request.

## Process

Open an issue or a discussion first for anything beyond a typo. Pull requests that change a rule should update the corresponding golden prompt or add one.

## Monthly model bench

We publish model results in [MODELS.md](MODELS.md) on a monthly cadence. If you run the golden prompts against a current model, submit results as a pull request to that file using the table format there.
