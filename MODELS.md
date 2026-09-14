# Model results

We run the golden prompts in `tests/prompts/` against current models, with and without the standard loaded, and score them with `tests/rubric.md`.

Results are dated. Model behavior changes with each release, and a model that held the standard in one quarter may not in the next.

## Latest run

No published run yet. The first results will be posted after the v0.1.0 release, covering the current Claude, GPT, and Gemini lineups and at least two open-weight models.

## How to reproduce

1. Load a layer (base or Trauma-Informed) as the system context for the model under test.
2. Run every prompt in `tests/prompts/`.
3. Score each output against `tests/rubric.md`. Record pass/fail per rule.
4. Run the same prompts with no standard loaded, as the control.
5. Submit results as a pull request to this file, with the model name, version string, date, and your scoring.

| Date | Model | Version | Layer | Rules passed | Control passed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
