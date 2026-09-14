# Changelog

## v0.1.1 (September 2026)

**Brand voice templates** (`okf/templates/voice-interview.md`, `okf/templates/voice-profile.md`): the user-facing addition. Organizations can interview a model or fill in a blank profile to build their step-9 organization voice file.

Usability and consistency pass: fix leftover OKF index and documentation gaps from the v0.1.0 usability review; wire `scripts/build.py` to keep human-voice packaging in sync with `okf/modules/human-voice.md`. Human voice remains optional evolving module standards (AI writing tells), not a shipped product; tooling forthcoming.

## v0.1.0 (September 2026)

Initial release. Extracted from the GoldenDoodle AI production system prompt and separated into the Dignified Language Standard (base) and the Trauma-Informed layer.

Known items flagged for practitioner review:
- Canonical form for people without housing. The source used three variants; this release standardizes on "people experiencing homelessness" and lists the others as acceptable.
- The sex work / trafficking vocabulary entry asks the writer to make a consent determination the model cannot make from text. Marked as requiring human judgment.
- Capitalization of Black and Indigenous moved from reporting standards to the base style rules.
