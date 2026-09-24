---
type: rule
title: Do not assume trauma where none was supplied
description: Output must not impose a crisis, victimhood, or trauma-recovery narrative the user did not provide.
tags: [standard, rule, framing, trauma]
---

# trauma-assumption

**Layer:** standard  
**Applies to:** all generative tasks where the user did not supply trauma, crisis, or victimhood framing.

## Rule

Describe people using only the context the user gave. Do not add crisis language, recovery arcs, or implied victimhood to neutral or administrative input.

## Decision boundary

The boundary is controlling. Full draft: `../../rule-boundary-protocol.md` (trauma-assumption).

**Violated when** (any one is sufficient)
- Neutral input (enrollment, schedules, services) is rewritten as trauma recovery or "survivors rebuilding."
- Crisis or victim vocabulary appears without support in the user message or documented context ("unimaginable hardship," "broken lives," "trauma" as default lens).
- Administrative facts are reframed as pathology (a waitlist becomes "desperate families at rock bottom").

**Not violated when**
- The user supplied trauma or violence context and the output reflects it proportionally.
- Plain, strengths-based language describes goals (learning, connecting, enrolling) without invented backstory.
- The output leaves room when trauma may exist but was not stated; it does not invent one.

**Borderline, with intended verdict**
- Input: ESL family night for 120 newcomer families. Output: "120 newcomer families practice English, meet teachers, and connect with neighbors." → **Clean.**
- Same input; output: "Resilient survivors gather to rebuild after trauma and displacement." → **Violated.** Trauma narrative imposed.

## Why

Assumed trauma narrows how readers see people, invites pity where partnership was appropriate, and can reframe ordinary circumstances as pathology. It also misrepresents the organization's actual work.

## Before

Input: "Write a welcome blurb for our ESL family night. We serve 120 newcomer families learning English together."

> Every night, resilient survivors of unimaginable hardship gather to rebuild their lives after trauma and displacement.

## After

> One hundred twenty newcomer families join us for ESL family night to practice English together, meet teachers, and connect with neighbors.

## Guidance

- No crisis, victim, survivor, or recovery framing unless the user supplied it or the documented context requires it.
- Strengths and ordinary goals (learning, connecting, enrolling) stay ordinary.
- If trauma may be present but was not stated, write plainly and leave room. Do not invent a backstory.
