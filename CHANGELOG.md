# Changelog

## v0.2.0 (October 2026)

Rename and marketplace packaging: human-centered language standard and trauma-informed standard naming, `plugins/` stubs, and marketplace manifests (`goldendoodle-ai`, one plugin per skill). Version tracked in `VERSION`. Legacy compiled filenames `dignified-language.md` and `trauma-informed.md` kept as copies for one release.

**Bench baseline:** v0.2.0 is a **new** Human-Centered Language Benchmark baseline. Compiled preambles, titles, and packaging wording changed (including "rules" to "standards and practices" in model-facing preambles).

Docs: install-first README (folded from PR #7), public copy no longer uses the old layer label, MKTNG benchmark credit in README testing section.

## v0.1.1 (September 2026)

**Brand voice templates** (`okf/templates/voice-interview.md`, `okf/templates/voice-profile.md`): the user-facing addition. Organizations can interview a model or fill in a blank profile to build their step-9 organization voice file.

Usability and consistency pass: fix leftover OKF index and documentation gaps from the v0.1.0 usability review; wire `scripts/build.py` to keep human-voice packaging in sync with `okf/modules/human-voice.md`. Human voice remains optional evolving module standards (AI writing tells), not a shipped product; tooling forthcoming.

## v0.1.0 (September 2026)

Initial release. Extracted from the GoldenDoodle AI production system prompt and separated into the Dignified Language Standard (base) and the Trauma-Informed layer.

Known items flagged for practitioner review:
- Canonical form for people without housing. The source used three variants; this release standardizes on "people experiencing homelessness" and lists the others as acceptable.
- The sex work / trafficking vocabulary entry asks the writer to make a consent determination the model cannot make from text. Marked as requiring human judgment.
- Capitalization of Black and Indigenous moved from reporting standards to the base style rules.
