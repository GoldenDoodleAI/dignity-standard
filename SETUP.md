# Setup

## Creating the repository on GitHub

1. In the GoldenDoodleAI organization, create a new public repository named `dignity-standard`. Do not initialize it with a README; this folder already has one.
2. Locally:
   ```
   cd dignity-standard
   git init
   git add .
   git commit -m "Initial release: Dignified Language Standard v0.1 and Trauma-Informed layer"
   git branch -M main
   git remote add origin git@github.com:GoldenDoodleAI/dignity-standard.git
   git push -u origin main
   ```
3. In repository settings, add topics: `okf`, `trauma-informed`, `nonprofit`, `brand-voice`, `ai-guardrails`, `claude-skill`.
4. Enable Discussions. That is where practitioner feedback should land.
5. Tag the first release: `git tag v0.1.0 && git push --tags`.

## Rendering the compiled files

`packaging/compiled/` holds single-file versions of the standard for platforms that want one paste. They are generated, not hand-edited.

```
python3 scripts/build.py
```

Run this after any change under `okf/`. The GitHub Action in `.github/workflows/build.yml` does it on every push to `main` and fails the build if the compiled files are out of date.

## Loading into Claude

**Claude Project (individual or Team):** create a Project, upload every file from `okf/standard/` (and `okf/trauma-informed/` if you want that layer), and paste the contents of `packaging/claude-skill/<layer>/SKILL.md` into the Project instructions.

**Claude Skill:** copy `packaging/claude-skill/dignified-language/` or `packaging/claude-skill/trauma-informed/` into your skills directory. Each folder is self-contained.

**Claude Code:** add the compiled file to your `CLAUDE.md`, or reference the skill folder.

## Loading into ChatGPT

Create a custom GPT (or a Project) and paste `packaging/chatgpt/dignified-language.md` or `packaging/chatgpt/trauma-informed.md` into the instructions field. Upload `okf/standard/vocabulary/*.md` as knowledge files if your sector vocabulary matters.

## Loading into Gemini

Create a Gem and paste `packaging/gemini/dignified-language.md` or `packaging/gemini/trauma-informed.md` as its instructions.

## Loading into anything else

Point your agent at `okf/`. Every file has a `type` field in its frontmatter. Load `standard/` first, then `trauma-informed/` if applicable, then whatever `vocabulary/` files match your sector, then your own organization's voice file on top. `okf/standard/precedence.md` explains the order in which these layers apply.
