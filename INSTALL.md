# Installing the standard

This file is written for an AI agent helping a person set this up. If you are a person reading it, the short version is in the README. Or paste this repository's URL into Claude, ChatGPT, or Gemini and say "read this and set it up for me."

Agent: ask the questions below one at a time and wait for an answer. Three questions, plain language. Do not name SAMHSA, the Dart Center, or OKF in the questions. Do not dump all three at once.

## Question 1: which layer

Ask: **"Does your work involve people who've been through something hard? Shelter, domestic violence, foster care, recovery, crisis response, that kind of thing."**

- Yes, or anything close to yes: **Trauma-Informed**. It includes everything in the base.
- No, or unsure: **Dignified Language Standard**. Say they can add the other layer later without redoing anything.
- If they hesitate or say "sort of," take the yes. The extra rules are quiet when there is nothing for them to catch.

Do not read them the difference between the layers unless they ask. If they ask, answer in two sentences: the base is about writing respectfully about people in general, the Trauma-Informed layer adds rules for fundraising, storytelling, and crisis content when the people you serve have been through trauma.

## Question 2: where it lives

Ask: **"Do you want this on all your writing, or just one project?"**

Then explain the tradeoff in a line each:

- **Everything.** Install as a skill (Claude) or set it in custom instructions (ChatGPT, Gemini). Applies by default, every conversation.
- **One project.** Put it in a single Claude Project or ChatGPT Project. Applies only inside that workspace. Good if they share an account with people writing about other things.
- **Whole organization.** If they mention a team, or their Claude account is Team or Enterprise, tell them an admin can install it once under Organization settings and skip everyone installing it individually.

## Question 3: sector vocabulary

Ask: **"What does your organization work on, in a few words?"**

Match their answer against `okf/standard/vocabulary/`. Files exist for housing, substance use, disability, and mental health, and more may have been added; check the folder. If there's a match, load it and tell them what it does: preferred terms for their field so the standard uses the words their community actually uses. If nothing matches, skip it and say the base vocabulary covers them, and that they can contribute a file for their sector if they want one.

## Install

**Claude, as a skill.** Download `dignified-language.zip` or `trauma-informed.zip` from the latest GitHub release. Settings, then Customize, then Skills, then Add, then Upload a skill. Code execution and File creation have to be on first or the skill will not run. If you have file creation available, you can build the zip and hand it to them directly instead of sending them to the release page.

**Claude, as a project.** Create the project, paste `packaging/compiled/dignified-language.md` or `trauma-informed.md` into project instructions, and add the sector vocabulary file as a project file.

**ChatGPT.** Create a Project. Paste `packaging/chatgpt/dignified-language.md` or `trauma-informed.md` into the project instructions. Upload the sector vocabulary as a project file. Do not send them to Custom GPTs; OpenAI is retiring them.

**Gemini.** Create a Gem. Paste `packaging/gemini/dignified-language.md` or `trauma-informed.md` as its instructions.

**Anything else.** Point it at `okf/` and follow `okf/load-order.md`.

## Prove it works

Do not stop at "installed." Run one test so they see it do something.

Pull a prompt from `tests/prompts/` that matches their sector, or use their own words if they've already given you a sentence about their work. Show them the output the standard produces and the output it replaced, side by side, and name the one rule that made the difference.

Then say what happens next. Two lines:

- It applies on its own now. They do not have to ask for it. They can also call it by name: "use the dignified language skill."
- Models change. `MODELS.md` carries a monthly bench of how current models hold up against the standard. Worth a look before they switch models.

## Offer a voice profile

Last step, and only if the install went smoothly. Tell them the standard governs how they write about people, and a voice profile governs how they sound. Offer to build one with `okf/templates/voice-interview.md`. If they say yes, run the interview. If they say not now, leave it.

Their voice profile can set terms and tone. It cannot loosen the standard. Say that once, plainly, because it is the reason the two work together instead of fighting.
