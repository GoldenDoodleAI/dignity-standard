---
type: Playbook
title: Load order
description: Sequencing guidance for any consumer loading the OKF bundle.
---

# Load order

Follow this sequence when loading the bundle into an agent, RAG pipeline, or compiled render.

## Base standard (`standard/`)

1. `standard/precedence.md` and `standard/principles.md`
2. `standard/rules/*.md` in this order:
   - `deficit-based-language.md`
   - `terminology-mirroring.md`
   - `organization-as-hero.md`
   - `cognitive-accessibility.md`
   - `style-basics.md`
3. `standard/vocabulary/*.md` (only the sector files that apply):
   - `person-first.md`
   - `housing.md`
   - `substance-use.md`
   - `mental-health.md`
   - `disability.md`
   - `non-pathologizing.md`
   - `reporting-standards.md`
4. `standard/protocols/rewrite.md`

## Trauma-Informed layer (`trauma-informed/`)

Load only if adopting the certified layer. Requires everything in `standard/` underneath it.

5. `trauma-informed/four-rs.md` and `trauma-informed/six-principles.md`
6. `trauma-informed/rules/*.md` in this order:
   - `urgency-exploitation.md`
   - `trauma-exploitation-storytelling.md`
   - `savior-framing.md`
   - `donor-audience-rationalization.md`
7. `trauma-informed/protocols/crisis.md`

## Optional modules (`modules/`)

8. `modules/*.md` as needed (none are required for conformance)

## Organization voice

9. Your organization's voice file, which may add preferred terms and tone but may not override anything above it.

Precedence for the Trauma-Informed layer: it sits above the base standard and above any brand voice. A brand voice may not relax it.
