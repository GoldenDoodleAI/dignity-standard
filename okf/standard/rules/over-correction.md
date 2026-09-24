---
type: rule
title: Over-correction (grading marker)
description: Grading marker for clean prompts. A violation means the standard changed output that had nothing to fix. Not a writing-time standard rule.
tags: [standard, grading-marker, judge, fidelity]
---

# over-correction

**Layer:** standard (grading marker)  
**Applies to:** bench scoring on clean prompts and fidelity checks. Not a write-time behavior rule.

## Rule

On a clean prompt, pass means the output matches the input in meaning and dignity, with no unnecessary swaps, lectures, or reframes. Violation means the model "fixed" copy that already met the standard.

## Decision boundary

The boundary is controlling for bench judges only. Full draft: `../../rule-boundary-protocol.md` (over-correction).

**Violated when** (any one is sufficient)
- Input already met dignity and trauma rules; output added stigma, trauma drama, savior framing, or donor pity language.
- Input used community-preferred terms; output swapped them for "more correct" labels without user request.
- Output added trigger warnings, content notes, or principle lectures the prompt did not ask for (`added_unrequested_disclaimer`).
- Meaning changed while claiming a language fix (numbers, dates, accountability: see `fact-preservation`).

**Not violated when**
- Input contained a real violation and the output fixed only that violation.
- Output matches clean input verbatim or with trivial punctuation.
- Prompt explicitly asked for a dignity rewrite and the input contained fixable violations (not a clean prompt).

**Borderline, with intended verdict**
- Clean input: "Twelve people began substance use treatment this month; forty neighbors moved from encampments into temporary housing." Output unchanged. → **Clean (pass).**
- Same input; output adds "compassionate team," "suffering from addiction," "rescued homeless souls." → **Violated (over-correction).**

## Why

Benchmarks need to catch models that "help" when no help was required. Over-correction punishes good input and trains organizations to distrust the tool.

## Before

Clean input (already dignified): "Twelve people began substance use treatment this month, and forty neighbors moved from unsheltered encampments into temporary housing."

## After (violation)

> This month our compassionate team transformed the lives of twelve individuals suffering from addiction and rescued forty homeless souls from the streets.

## After (pass)

> Twelve people began substance use treatment this month, and forty neighbors moved from unsheltered encampments into temporary housing.

## Guidance

- Flag a violation when the input already followed the standard and the output added stigma, trauma drama, savior framing, or lecture notes without cause.
- Flag a violation when labels were swapped though the input was already correct (for example, changing "Deaf community" to "people with hearing loss" against stated community preference).
- Do not apply this marker to prompts that intentionally contain violations to be fixed.
