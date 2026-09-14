# Dignified Language Standard

An open, machine-readable standard for how organizations talk about people, with a certified Trauma-Informed layer on top.

Maintained by [GoldenDoodle AI](https://goldendoodleai.com). Editor: Laura Braden.

## Quick Start

**Pick a layer:** If the people you serve have been affected by trauma (shelter, DV program, foster care nonprofit), use **Trauma-Informed**. It includes the base standard automatically. Otherwise, use the **Dignified Language Standard** on its own.

| Path | How to load |
|---|---|
| **Claude** | Download a skill zip from `packaging/releases/` (or [GitHub Releases](https://github.com/GoldenDoodleAI/dignity-standard/releases) when published). Upload under Settings → Customize → Skills. Or tell Claude to fetch this repo and set up the skill for you. |
| **ChatGPT** | Create a Project. Paste `packaging/chatgpt/dignified-language.md` or `trauma-informed.md` into project instructions. Upload sector vocabulary from `okf/standard/vocabulary/` if needed. |
| **Gemini** | Create a Gem. Paste `packaging/gemini/dignified-language.md` or `trauma-informed.md` as its instructions. |
| **Compiled (any model)** | Paste `packaging/compiled/dignified-language.md` or `trauma-informed.md` as system context. |
| **Brand voice** | Interview: paste `okf/templates/voice-interview.md`. Blank profile: copy `okf/templates/voice-profile.md`. |
| **Cursor / repo agent** | Read [AGENTS.md](AGENTS.md). Load `packaging/compiled/` or follow `okf/load-order.md`. |

Per-model packaging files are intentionally separate. They may drift slightly in preamble or formatting; `okf/` is the source of truth.

**Agents already at this repo:** load `packaging/compiled/dignified-language.md` or `packaging/compiled/trauma-informed.md`, or walk `okf/` using [okf/load-order.md](okf/load-order.md). Do not run setup or git publish steps.

Model behavior changes with each release. Before choosing a model, check the monthly bench in [MODELS.md](MODELS.md).

## What this is

Most organizations that serve people have opinions about language. Very few have written them down in a form an AI model can follow. This repository is that form.

It is a directory of markdown files with YAML frontmatter, following the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) conventions, so it can be loaded into Claude, ChatGPT, Gemini, an open-weight model, or any agent that reads files. Humans can read it too. That is the point.

There are two entry points:

**The Dignified Language Standard** (`okf/standard/`) is the base. Person-first language, no deficit framing, the organization is never the hero, plain language by default, and reporting standards for sensitive topics. Any organization that cares how it speaks about people can adopt it. A medical association, a housing coalition, and a trade group can all run on it.

**The Trauma-Informed layer** (`okf/trauma-informed/`) sits on top of the base and requires it. It adds SAMHSA's Four R's and Six Principles, four additional rules aimed at fundraising and storytelling, and a Crisis protocol. It is written for organizations serving people affected by trauma and for the communicators who work alongside them.

The base is a subset of the Trauma-Informed layer, not a lighter version of it. If you adopt Trauma-Informed, you have adopted the base.

## Connecting this to your AI tools

### Claude (claude.ai)

1. Download `dignified-language.zip` or `trauma-informed.zip` from `packaging/releases/` (or [GitHub Releases](https://github.com/GoldenDoodleAI/dignity-standard/releases) when published). Each zip contains `SKILL.md` and `standard.md`.
2. In Claude, go to **Settings → Customize → Skills**. If Code execution and File creation are not already on, turn them on first; skills will not run without them.
3. Click **Add**, then **Upload a skill**, and select the zip.
4. Toggle it on. Claude will apply the standard automatically to writing about the people you serve, or you can invoke it directly: "use the dignified language skill."

Faster option, if your Claude has web browsing and file creation on: tell it to fetch this repo and set up the Trauma-Informed or Dignified Language skill for you. Claude can pull the files and hand you a button to save it; no zip download needed.

On a Claude Team or Enterprise plan, an admin can provision this for the whole organization at once under **Organization settings → Skills**, so nobody has to install it individually.

### ChatGPT

1. Create a Project.
2. Open the project's settings and paste the contents of `packaging/chatgpt/dignified-language.md` or `trauma-informed.md` into the project instructions field.
3. If your sector has its own vocabulary file under `okf/standard/vocabulary/` (housing, disability, substance use, mental health), upload it too as a project file.

(Custom GPTs are not the recommended path here. OpenAI has stopped new GPT creation for personal accounts and is retiring the feature entirely through the rest of 2026. Projects is the stable option.)

### Gemini

1. Create a Gem.
2. Paste `packaging/gemini/dignified-language.md` or `trauma-informed.md` as its instructions.

### Any other agent or RAG pipeline

Point it at the `okf/` folder directly. [okf/load-order.md](okf/load-order.md) gives the load sequence. [okf/index.md](okf/index.md) lists the bundle contents.

## Repository layout

```
okf/
  index.md             Bundle directory listing (OKF v0.2)
  load-order.md        Sequencing playbook for consumers
  standard/            The Dignified Language Standard (base)
    principles.md      What the standard is for
    precedence.md      How these rules interact with brand voice and user requests
    rules/             One file per rule, each with before/after and a test prompt
    vocabulary/        Swappable sector vocabulary (housing, substance use, ...)
    protocols/         Rewrite protocol
  trauma-informed/     The certified Trauma-Informed layer (requires standard/)
    four-rs.md
    six-principles.md
    rules/             Fundraising and storytelling rules
    protocols/         Crisis protocol
  modules/             Optional add-ons
  templates/           Brand voice templates (profile blank + interview megaprompt)
packaging/             Ready-to-load versions for each platform
tests/                 Golden prompts and the scoring rubric
scripts/               Build script that renders packaging/
```

**Optional modules:** Human voice (`okf/modules/human-voice.md`) is evolving standards for AI writing tells; tooling forthcoming. Packaging exists for maintainers; not a finished product.

## Model behavior

Instructions land differently across models and change with each release. We run the prompts in `tests/` against current models monthly and publish results in [MODELS.md](MODELS.md). If you are choosing a model to run this standard on, read that first.

## Contributing

Rules change when practitioners say they should. See [CONTRIBUTING.md](CONTRIBUTING.md). Sector vocabulary contributions are especially welcome.

## License

Content (everything under `okf/`, `packaging/`, `tests/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, adapt it, credit GoldenDoodle AI.
Code (`scripts/`): MIT.

SAMHSA's trauma-informed framework is a work of the United States government and is in the public domain. Reporting standards reference the Dart Center for Journalism and Trauma; their guidance is cited, not reproduced.
