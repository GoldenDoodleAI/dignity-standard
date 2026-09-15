# Models

The tested roster and judge panel are defined in the bench repo's `models.yaml`: https://github.com/GoldenDoodleAI/test-bench/blob/main/models.yaml. This file is a pointer so the standard repo stays about the standard. The judge panel is in `judges.yaml` in the same bench repo.

Roster principles (full reasoning in the bench METHODOLOGY.md):

- Current production models at each vendor's small, mid, and flagship tier, plus open-weight models with meaningful third-party hosting.
- Concrete model slugs only; no `latest` aliases.
- Open-weight providers are pinned at the start of a series and never changed mid-series.
- Grok is tested but never judges, because the maintainers' agent infrastructure runs on it.
- Judges are chosen on Judgemark v4 and are deliberately a generation behind the roster: they are the instrument, not the subject.

Last roster confirmation against the OpenRouter catalog: 2026-09-14.
