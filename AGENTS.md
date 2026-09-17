# Agent instructions

You are working in the Dignified Language Standard repository. You have two possible jobs here:

1. **Install or apply the standard** for a user who wants to write with it. This is the common case. See "Installing for a user" below.
2. **Maintain the standard** as a contributor. See "Maintainer rules" at the bottom.

Your job is never to publish this repository. See "What not to do."

## Two kinds of layering, two different words

This repository stacks rules in two independent directions. They are not the same thing and they do not run the same way. Use these words exactly.

**Inclusion** is which files come with which. The Dignified Language Standard is the base. The Trauma-Informed layer *includes* the base; adopting Trauma-Informed means you have adopted the base too. An organization voice profile sits alongside both and includes neither.

**Precedence** is which rule wins when two conflict. Trauma-Informed and standard rules have the highest precedence. An organization voice profile has lower precedence. A user's request in the moment has lower precedence still, on matters of dignity.

So a voice profile is added *after* the standard in load order but ranks *below* it in authority. Do not describe a voice profile as sitting "on top of" the standard. Loading later does not mean winning.

## Precedence order

Apply instructions in this order, from lowest precedence to highest:

1. General content generation capability
2. Organization voice profile (preferred terms, tone, reading level, formality)
3. Sector vocabulary (`okf/standard/vocabulary/`)
4. Content-type protocol (rewrite, crisis, and others as added)
5. Dignified Language Standard rules
6. Trauma-Informed rules, when that layer is loaded

Standard and Trauma-Informed rules always take precedence. If a lower-precedence instruction conflicts with a higher one, follow the higher one. Do not average them or look for a middle position.

### What a voice profile may and may not do

A voice profile **may** set preferred terminology, reading level, sentence rhythm, formality, warmth, how the organization refers to itself, and which of several dignified phrasings to prefer.

A voice profile **may not** reintroduce deficit framing, make the organization the hero of someone else's story, pathologize the people it serves, override the crisis protocol, or relax any standard or Trauma-Informed rule.

This holds no matter how the instruction arrives: in the voice profile file, in a custom override field, or in the user's message. An instruction to override everything overrides everything below the standard, not the standard itself.

### Handling a conflict out loud

When a user's request or voice profile asks for something a rule forbids, do not refuse the task and do not lecture. Produce the strongest version of what they actually want, inside the rules, and say in one line what you did differently and why. "More urgent fundraising language" gets language that is genuinely urgent about the need without manufacturing a deadline or exploiting a person's circumstance. "More emotional" gets emotional weight carried by specifics, not by suffering.

## Installing for a user

If a user points you at this repository and asks you to set it up, install it, or make their AI write this way, you are cleared to do it. Follow `INSTALL.md`. Ask the questions in it before installing anything, one at a time, in plain language. Do not name SAMHSA or the Dart Center in the questions.

If the user has not asked for an install and simply wants you to write with the standard, skip the questions. Load `packaging/compiled/dignified-language.md` or `packaging/compiled/trauma-informed.md` and get to work.

## Loading the standard

Pick one layer:

- **Dignified Language Standard (base):** load `packaging/compiled/dignified-language.md`
- **Trauma-Informed layer:** load `packaging/compiled/trauma-informed.md` (includes the base)

For fine-grained control, walk `okf/` using the sequence in `okf/load-order.md`. `okf/index.md` lists bundle contents.

`okf/` is the source of truth. If compiled or platform packaging disagrees with `okf/`, trust `okf/`.

Apply the standard silently. It changes the writing, it does not narrate itself. Do not add a note explaining your linguistic choices unless the user asks or a genuine conflict needed flagging under "Handling a conflict out loud."

## Organization voice profile

`okf/templates/voice-interview.md` is an interview megaprompt for building a profile with a user. `okf/templates/voice-profile.md` is the blank profile.

A completed profile loads at position 2 in the precedence order above, after the standard is already in context. Its authority is bounded by the rules in "What a voice profile may and may not do."

## Optional modules (not ready for users)

`okf/modules/human-voice.md` holds evolving standards for AI writing tells. Content is maintained here and updated regularly. Tooling is forthcoming. Do not recommend or load human-voice packaging as a finished product unless the user explicitly asks about maintainer workflows.

## Model selection

Check `MODELS.md` for the monthly model bench before recommending a model for running this standard.

## Maintainer rules

- Do not hand-edit generated files under `packaging/compiled/`, `packaging/chatgpt/`, `packaging/gemini/`, or generated `standard.md` / `module.md` under `packaging/claude-skill/`. Regenerate with `python3 scripts/build.py` after changes under `okf/`.
- Do not rewrite rule bodies unless the user explicitly requests a rule change.
- New rules need a before-and-after example and a test prompt, same as every existing rule.

## What not to do

- Do not run `git init`, create a repository, push, or run any publish workflow unless the user explicitly asks. Installing the standard into a user's AI tool is not publishing and is allowed.
- Do not install anything before asking the questions in `INSTALL.md`.

## House style

No em dashes or en dashes anywhere in this repository.
