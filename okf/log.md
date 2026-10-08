# OKF bundle log

## 2026-10-08 (harm tags)
* **harm-ladder.md**: Added the harm ladder: six categories from `sounds-like-a-machine` to `endangers-a-person`, so failures can be reported by what they cost. Reporting metadata only; nothing is added to the compiled skill files.
* **rules/**: Every rule file now has a `harm:` frontmatter field. `savior-framing.md` and `trauma-exploitation-storytelling.md` gained a frontmatter block to carry it. Rule bodies unchanged. `over-correction` carries `harm: []` as a grading marker.
* **tests/prompts/**: Every active prompt and the pool prompt carry `harm:` and `harm_max:`, derived from their rules. `tests/test_harm_tags.py` keeps them in sync and runs in CI. `prompt-meta-45.json` carries the same fields.

## 2026-10-08
* **SOURCES.md**: Added a root sources file. Each entry gives the citation, link, what we took from it, and which files use it. Rule and principle files now list their sources by ID in a `sources:` frontmatter field (started with the two files changed below; the rest follow).
* **standard/rules/cognitive-accessibility.md**: Added "Lead with the purpose": the first sentence or two say why the reader is getting the message and what they need to do; bad news goes there too, with background after. Ported from the V1 "No Surprises" rule, grounded in the Federal Plain Language Guidelines and the National Council trauma-informed communication checklist. Added a test prompt for a cancellation email that tempts a warm windup.
* **trauma-informed/six-principles.md**: Trustworthiness and transparency now says not to make the reader wait for the point, with the uncertainty research (de Berker et al. 2016) as the reasoning.
* Not changed: urgency rules. Organizations may still state real scarcity plainly (for example, limited camp spots).

## 2026-09-14
* **build.py integration**: Human-voice module packaging now rendered by `scripts/build.py` alongside the two layers. Removed manual-only maintenance notes from packaging docs.
* **Usability pass (continued)**: README Quick Start prefers `packaging/releases/` zips; brand voice templates and human-voice module documented for novices. OKF index links `log.md`; `okf/README.md` given proper frontmatter.

## 2026-09-13
* **templates/**: Added GoldenDoodle AI brand voice templates (`voice-profile.md`, `voice-interview.md`) so organizations can build the step-9 organization voice file without starting from scratch.
* **modules/human-voice.md, packaging/**: Shipped manual packaging for the human voice module (compiled, ChatGPT, Gemini, Claude skill zip) ahead of build-script integration.
* **Initialization**: Initial release of the Dignified Language Standard (base) and Trauma-Informed layer, extracted from the GoldenDoodle AI production system prompt into OKF bundle form.
