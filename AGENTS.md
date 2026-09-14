# Agent instructions

You are working in the Dignified Language Standard repository. Your job is to apply or maintain the standard, not to publish the repo.

## Loading the standard

Pick one layer:

- **Dignified Language Standard (base):** load `packaging/compiled/dignified-language.md`
- **Trauma-Informed layer:** load `packaging/compiled/trauma-informed.md` (includes the base)

For fine-grained control, walk `okf/` using the sequence in [okf/load-order.md](okf/load-order.md). [okf/index.md](okf/index.md) lists bundle contents.

`okf/` is the source of truth. If compiled or platform packaging disagrees with `okf/`, trust `okf/`.

## What not to do

- Do not run git init, create-repo, push, or other publish/setup workflows unless the user explicitly asks.
- Do not hand-edit generated files under `packaging/compiled/`, `packaging/chatgpt/`, or `packaging/gemini/`. Regenerate with `python3 scripts/build.py` after changes under `okf/`.
- Do not rewrite rule bodies unless the user explicitly requests a rule change.

## House style

No em dashes or en dashes anywhere in this repository.

## Model selection

Check [MODELS.md](MODELS.md) for the monthly model bench before recommending a model for running this standard.
