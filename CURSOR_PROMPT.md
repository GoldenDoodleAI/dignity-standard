# Cursor prompt (if you prefer to push from Cursor)

Paste the following into Cursor with this folder open:

---

This folder is the initial release of the Dignified Language Standard, an open OKF-format language standard with a Trauma-Informed layer, maintained by GoldenDoodle AI.

Do the following, in order, and stop after each step for confirmation:

1. Run `python3 scripts/build.py --check` and confirm it exits 0. If it fails, run `python3 scripts/build.py` and show me the diff.
2. Initialize git, commit everything as "Initial release: Dignified Language Standard v0.1 and Trauma-Informed layer", set the branch to main.
3. Add the remote `git@github.com:GoldenDoodleAI/dignity-standard.git` and push. The repository must already exist on GitHub (public, empty, no README).
4. Tag `v0.1.0` and push tags.
5. Tell me which repository settings still need to be set by hand: topics (okf, trauma-informed, nonprofit, brand-voice, ai-guardrails, claude-skill), Discussions enabled, and a short description: "An open, machine-readable standard for how organizations talk about people. Dignified Language base plus a certified Trauma-Informed layer. Loads into Claude, ChatGPT, Gemini, and any agent."

Do not edit any content under okf/. Do not hand-edit anything under packaging/; it is generated.
