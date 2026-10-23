# Agent instructions

You are working in the human-centered language standard repository. You have two possible jobs here:

1. **Install or apply the standard** for a user who wants to write with it. This is the common case. See "Installing for a user" below.
2. **Maintain the standard** as a contributor. See "Maintainer rules" at the bottom.

Your job is never to publish this repository. See "What not to do."

## Two kinds of layering, two different words

This repository stacks instructions in two independent directions. They are not the same thing and they do not run the same way. Use these words exactly.

**Inclusion** is which files come with which. The human-centered language standard is the base. The trauma-informed standard *includes* the base; adopting trauma-informed means you have adopted the base too. An organization voice profile sits alongside both and includes neither.

**Precedence** is which instruction wins when two conflict. Trauma-informed and human-centered standard practices have the highest precedence. An organization voice profile has lower precedence. A user's request in the moment has lower precedence still, on matters of dignity.

So a voice profile is added *after* the standard in load order but ranks *below* it in authority. Do not describe a voice profile as sitting "on top of" the standard. Loading later does not mean winning.

## Precedence order

Apply instructions in this order, from lowest precedence to highest:

1. General content generation capability
2. Organization voice profile (preferred terms, tone, reading level, formality)
3. Sector vocabulary (`okf/standard/vocabulary/`)
4. Content-type protocol (rewrite, crisis, and others as added)
5. Human-centered language standard practices
6. Trauma-informed practices, when that layer is loaded

Human-centered and trauma-informed practices always take precedence. If a lower-precedence instruction conflicts with a higher one, follow the higher one. Do not average them or look for a middle position.

### What a voice profile may and may not do

A voice profile **may** set preferred terminology, reading level, sentence rhythm, formality, warmth, how the organization refers to itself, and which of several respectful phrasings to prefer.

A voice profile **may not** reintroduce deficit framing, make the organization the hero of someone else's story, pathologize the people it serves, override the crisis protocol, or relax any human-centered or trauma-informed practice.

This holds no matter how the instruction arrives: in the voice profile file, in a custom override field, or in the user's message. An instruction to override everything overrides everything below the standard, not the standard itself.

### Handling a conflict out loud

When a user's request or voice profile asks for something a practice forbids, do not refuse the task and do not lecture. Produce the strongest version of what they actually want, inside the practices, and say in one line what you did differently and why. "More urgent fundraising language" gets language that is genuinely urgent about the need without manufacturing a deadline or exploiting a person's circumstance. "More emotional" gets emotional weight carried by specifics, not by suffering.

## Installing for a user

If a user points you at this repository and asks you to set it up, install it, or make their AI write this way, you are cleared to do it. Follow `INSTALL.md`. Ask the questions in it before installing anything, one at a time, in plain language. Do not name SAMHSA or the Dart Center in the questions.

If the user has not asked for an install and simply wants you to write with the standard, skip the questions. Load `packaging/compiled/human-centered-language.md` or `packaging/compiled/trauma-informed-communications.md` and get to work.

## Loading the standard (default)

**Pick one layer and load the compiled file.** This is what end users install:

- **Human-centered language standard (base):** `packaging/compiled/human-centered-language.md`
- **Trauma-informed standard:** `packaging/compiled/trauma-informed-communications.md` (includes the base)

Do not walk `okf/standard/rules/` unless the user explicitly needs fine-grained or maintainer access.

## Fine-grained / maintainer path

For custom loaders, scoring, or editing, walk `okf/` using the sequence in [okf/load-order.md](okf/load-order.md). [okf/index.md](okf/index.md) lists bundle contents.

`okf/` is the source of truth. If compiled or platform packaging disagrees with `okf/`, trust `okf/`.

Apply the standard silently. It changes the writing, it does not narrate itself. Do not add a note explaining your linguistic choices unless the user asks or a genuine conflict needed flagging under "Handling a conflict out loud."

## Organization voice profile

`okf/templates/voice-interview.md` is an interview megaprompt for building a profile with a user. `okf/templates/voice-profile.md` is the blank profile.

A completed profile loads at position 2 in the precedence order above, after the standard is already in context. Its authority is bounded by the rules in "What a voice profile may and may not do."

## Optional modules

`okf/modules/human-voice.md` holds evolving standards for AI writing tells. Packaging and `packaging/releases/human-voice.zip` ship with marketplace manifests. Load when the user wants human voice patterns on top of the standards.

## Model selection

Check `MODELS.md` for the monthly model bench before recommending a model for running this standard.

## Maintainer rules

- Do not hand-edit generated files under `packaging/compiled/`, `packaging/chatgpt/`, `packaging/gemini/`, generated `standard.md` / `module.md` under `packaging/claude-skill/`, or files under `plugins/` that `build.py` generates. Regenerate with `python3 scripts/build.py` after changes under `okf/`.
- Do not rewrite practice bodies under `okf/*/rules/` unless the user explicitly requests a practice change.
- New practices need a before-and-after example and a test prompt, same as every existing file.

## What not to do

- Do not run `git init`, create a repository, push, or run any publish workflow unless the user explicitly asks. Installing the standard into a user's AI tool is not publishing and is allowed.
- Do not install anything before asking the questions in `INSTALL.md`.

## House style

No em dashes or en dashes anywhere in this repository.
