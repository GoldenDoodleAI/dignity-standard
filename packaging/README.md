# Packaging (install from here)

**This folder is what you install.** Ready-to-load versions of the standard for Claude, ChatGPT, Gemini, and any model that accepts a system prompt.

Pick one layer, then use the matching file or zip:

| Layer | Compiled | ChatGPT | Gemini | Claude |
|---|---|---|---|---|
| Human-centered language (base) | `compiled/human-centered-language.md` | `chatgpt/human-centered-language.md` | `gemini/human-centered-language.md` | `releases/human-centered-language.zip` |
| Trauma-informed | `compiled/trauma-informed-communications.md` | `chatgpt/trauma-informed-communications.md` | `gemini/trauma-informed-communications.md` | `releases/trauma-informed-communications.zip` |
| Human voice (optional) | `compiled/human-voice.md` | `chatgpt/human-voice.md` | `gemini/human-voice.md` | `releases/human-voice.zip` |

**Legacy compiled aliases (one release):** `compiled/dignified-language.md` and `compiled/trauma-informed.md` match the primary files above.

Everything here is derived from `okf/`. If anything disagrees with `okf/`, **`okf/` wins** and the packaging needs regenerating.

## Layout

- `compiled/`: single-file renders for any model or RAG pipeline. Paste as system context.
- `chatgpt/`: instruction text for a ChatGPT Project.
- `gemini/`: instruction text for a Gem.
- `claude-skill/human-centered-language/` and `claude-skill/trauma-informed-communications/`: self-contained Claude skill folders. Each `SKILL.md` is the entry point and references `standard.md` in the same folder.
- `releases/`: zip archives of each Claude skill folder for upload. GitHub Release assets are preferred when available; these copies are the fallback.
- `claude-skill/human-voice/`: optional human voice module. `SKILL.md` references `module.md`.

## For maintainers: regenerate packaging

Do not hand-edit files under `compiled/`, `chatgpt/`, `gemini/`, or generated `standard.md` / `module.md` under `claude-skill/`.

`scripts/build.py` renders three targets from `okf/`:

1. **human-centered-language** (base)
2. **trauma-informed-communications** (includes base)
3. **human-voice** (optional module)

Each target writes to `compiled/`, `chatgpt/`, `gemini/`, and the matching `claude-skill/` folder. The script also rebuilds `releases/*.zip`, `plugins/*/`, and marketplace manifests under `.claude-plugin/`, `.cursor-plugin/`, and `.agents/plugins/`.

Regenerate all derived outputs after any change under `okf/`:

```
python3 scripts/build.py
```

Use `--check` to verify outputs are current without writing files.

## Intentional drift

Per-model adapters may diverge in preamble, formatting, or platform-specific framing. That is intentional. Do **not** deduplicate or merge `chatgpt/`, `gemini/`, and `compiled/` into one file. Each surface has its own consumer.
