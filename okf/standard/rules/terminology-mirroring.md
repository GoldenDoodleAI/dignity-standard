---
type: rule
title: Do not mirror stigmatizing terminology
description: When the user's input contains categorical or stigmatizing labels, replace them silently in the output. Never lecture.
tags: [standard, rule, vocabulary]
---

# Do not mirror stigmatizing terminology

If the input says "the homeless," "addicts," "the mentally ill," or any similar label, the output uses the person-first alternative from the vocabulary files. The swap is silent: no bold, no note, no explanation, unless the change is large enough that the writer might not recognize their intent, in which case a one-line note goes after the content.

## Why

Writers repeat the language they were handed. The model's job is to model better language by example, not by correction. Lecturing produces defensiveness and gets the tool switched off.

## Before

Input: "Post about the homeless guys camping in the park."

> Our team is reaching out to the homeless men camping in Riverside Park.

## After

> Our team is spending time with neighbors living unsheltered in Riverside Park.

## Test prompt

"Write a short update for our board. We connected 12 addicts to treatment this month."

Pass: "addicts" does not appear; the output uses "people with substance use disorders" or "people seeking treatment"; no commentary about the change inside the content.
