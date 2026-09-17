# Packaging (install from here)

**This folder is what you install.** Ready-to-load versions of the standard for Claude, ChatGPT, Gemini, and any model that accepts a system prompt.

Pick one layer, then use the matching file or zip:

| Layer | Compiled | ChatGPT | Gemini | Claude |
|---|---|---|---|---|
| Dignified Language (base) | `compiled/dignified-language.md` | `chatgpt/dignified-language.md` | `gemini/dignified-language.md` | `releases/dignified-language.zip` |
| Trauma-Informed | `compiled/trauma-informed.md` | `chatgpt/trauma-informed.md` | `gemini/trauma-informed.md` | `releases/trauma-informed.zip` |

Everything here is derived from `okf/`. If anything disagrees with `okf/`, **`okf/` wins** and the packaging needs regenerating.

## Layout

- `compiled/`: single-file renders for any model or RAG pipeline. Paste as system context.
- `chatgpt/`: instruction text for a ChatGPT Project.
- `gemini/`: instruction text for a Gem.
- `claude-skill/dignified-language/` and `claude-skill/trauma-informed/`: self-contained Claude skill folders. Each `SKILL.md` is the entry point and references `standard.md` in the same folder.
- `releases/`: zip archives of each Claude skill folder for upload. GitHub Release assets are preferred when available; these copies are the fallback.
- `claude-skill/human-voice/`: maintainer-only packaging for the evolving human-voice module. `SKILL.md` references `module.md`. Not a layer, not a shipped product surface.

## For maintainers: regenerate packaging

Do not hand-edit files under `compiled/`, `chatgpt/`, `gemini/`, or generated `standard.md` / `module.md` under `claude-skill/`.

`scripts/build.py` renders three targets from `okf/`:

1. **dignified-language** (base layer)
2. **trauma-informed** (certified layer, includes base)
3. **human-voice** (optional evolving module, not a layer)

The two layers are the ready product surfaces. Human-voice packaging is regenerated when `okf/modules/human-voice.md` changes so maintainers can keep compiled copies in sync. That is maintenance, not a product launch; end-user tooling for human voice is forthcoming.

Each target writes to `compiled/`, `chatgpt/`, `gemini/`, and the matching `claude-skill/` folder. The script also rebuilds `releases/*.zip` from the Claude skill folders.

## Intentional drift

Per-model adapters may diverge in preamble, formatting, or platform-specific framing. That is intentional. Do **not** deduplicate or merge `chatgpt/`, `gemini/`, and `compiled/` into one file. Each surface has its own consumer.

Regenerate all derived outputs after any change under `okf/`:

```
python3 scripts/build.py
```

Use `--check` to verify outputs are current without writing files.
