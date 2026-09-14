# Dignified Language Standard

An open, machine-readable standard for how organizations talk about people, with a certified Trauma-Informed layer on top.

Maintained by [GoldenDoodle AI](https://goldendoodleai.com). Editor: Laura Braden.

## What this is

Most organizations that serve people have opinions about language. Very few have written them down in a form an AI model can follow. This repository is that form.

It is a directory of markdown files with YAML frontmatter, following the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) conventions, so it can be loaded into Claude, ChatGPT, Gemini, an open-weight model, or any agent that reads files. Humans can read it too. That is the point.

There are two entry points:

**The Dignified Language Standard** (`okf/standard/`) is the base. Person-first language, no deficit framing, the organization is never the hero, plain language by default, and reporting standards for sensitive topics. Any organization that cares how it speaks about people can adopt it. A medical association, a housing coalition, and a trade group can all run on it.

**The Trauma-Informed layer** (`okf/trauma-informed/`) sits on top of the base and requires it. It adds SAMHSA's Four R's and Six Principles, four additional rules aimed at fundraising and storytelling, and a Crisis protocol. It is written for organizations serving people affected by trauma and for the communicators who work alongside them.

The base is a subset of the Trauma-Informed layer, not a lighter version of it. If you adopt Trauma-Informed, you have adopted the base.

## Quick start

Pick your platform and copy one folder.

| Platform | What to use |
|---|---|
| Claude (Projects, Skills, Claude Code) | `packaging/claude-skill/dignified-language/` or `packaging/claude-skill/trauma-informed/` |
| ChatGPT (custom GPT, Project instructions) | `packaging/chatgpt/` |
| Gemini (Gems) | `packaging/gemini/` |
| Any agent or RAG pipeline | `okf/` (the raw bundle) |
| One file, no folders | `packaging/compiled/` |

Full instructions in [SETUP.md](SETUP.md).

## Repository layout

```
okf/
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
  modules/             Optional add-ons (human voice standards)
packaging/             Ready-to-load versions for each platform
tests/                 Golden prompts and the scoring rubric
scripts/               Build script that renders packaging/compiled/
```

## Model behavior

Instructions land differently across models and change with each release. We run the prompts in `tests/` against current models and publish results in [MODELS.md](MODELS.md). If you are choosing a model to run this standard on, read that first.

## Contributing

Rules change when practitioners say they should. See [CONTRIBUTING.md](CONTRIBUTING.md). Sector vocabulary contributions are especially welcome.

## License

Content (everything under `okf/`, `packaging/`, `tests/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, adapt it, credit GoldenDoodle AI.
Code (`scripts/`): MIT.

SAMHSA's trauma-informed framework is a work of the United States government and is in the public domain. Reporting standards reference the Dart Center for Journalism and Trauma; their guidance is cited, not reproduced.
