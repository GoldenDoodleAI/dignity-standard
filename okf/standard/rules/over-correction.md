---
type: rule
title: Over-correction (grading marker)
description: Grading marker for clean prompts. A violation means the standard changed output that had nothing to fix. Not a writing-time standard rule.
tags: [standard, grading-marker, judge, fidelity]
---

# Over-correction (grading marker)

**This file is for bench grading, not for model behavior at write time.** Use it when scoring whether a layer changed copy that already met the standard.

A pass on a clean prompt means the output matches the input in meaning and dignity, with no unnecessary swaps, lectures, or reframes.

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
