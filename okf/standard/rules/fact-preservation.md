---
type: rule
title: Preserve facts and accountability
description: Required figures, dates, and events survive the rewrite. Softening a number or accountability statement into vagueness is a violation.
tags: [standard, rule, rewrite, fidelity]
---

# fact-preservation

**Layer:** standard  
**Applies to:** rewrite tasks, summaries, and any output that must preserve user-supplied facts.

## Rule

Required figures, dates, names, events, and accountability statements survive the rewrite. Person-first or dignity reframes change labels, not facts.

## Decision boundary

The boundary is controlling. Full draft: `../../rule-boundary-protocol.md` (fact-preservation).

**Violated when** (any one is sufficient)
- A specific count in the input becomes a vague quantifier ("15" → "several," "dozens").
- A specific date or month becomes "recently," "last year," or is dropped when the input required it.
- An accountability claim is softened or erased ("leadership never checked zoning" → "process gaps before launch").
- A required name, program title, or legal finding in the input is removed without an explicit user request to shorten and name what to cut.

**Not violated when**
- Labels change while numbers and dates stay exact.
- The user asked for a shorter summary and named what to omit; omitted facts are not scored.
- Plain-language paraphrase keeps the same fact ("October 12" → "Oct. 12").

**Borderline, with intended verdict**
- Input: "Pilot suspended Oct 12; 15 families returned to shelter; leadership never verified zoning." Output keeps dates and count but replaces "never verified zoning" with "zoning was not confirmed before launch." → **Clean.** Accountability remains; wording shifted, not erased.
- Same input; output: "The pilot ended recently after a regulatory issue. Several families went back to shelter." → **Violated.** Count, date, and accountability are gone.

## Why

Organizations depend on accurate records for decisions, compliance, and trust. A rewrite that quietly drops a number or blurs responsibility looks polished but misleads the reader and the board.

## Before

Input: "Pilot housing program suspended Oct 12 after zoning stop-order. 15 families moved back to emergency shelter. Staff say leadership never checked zoning before launch."

> The pilot housing program ended recently after a regulatory issue. Several families returned to shelter. There were some process gaps before launch.

## After

> The pilot housing program was suspended on October 12 after a zoning stop-order. Fifteen families moved back to emergency shelter. Staff report that leadership did not verify zoning before launch.

## Guidance

- Counts, dates, and named events in the input appear in the output unless the user explicitly asked for a shorter summary and named what to cut.
- "Several" does not replace "15." "Recently" does not replace "Oct 12." "Process gaps" does not replace "never checked zoning."
- Person-first or dignity reframes change labels, not facts. A missed deadline stays a missed deadline.
