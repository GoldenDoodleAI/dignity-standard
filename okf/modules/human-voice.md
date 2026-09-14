---
type: module
title: Human voice standards (optional)
description: Optional module that suppresses common AI writing patterns. Not part of the dignity or trauma-informed rules; adopt if you want output that reads as written by a person.
tags: [module, style, ai-patterns, optional]
---

# Human voice standards

This module is optional and separate from the standard. It reflects GoldenDoodle AI's house style for suppressing writing patterns that read as machine-generated. Organizations may adopt it, adapt it, or ignore it.

Model fingerprints move fast. This revision (September 2026) draws on two sources: public 2026 research into AI writing patterns (corpus studies, journalism analyzing large samples of chat output, financial-reporting language trackers), and an internally curated catalog of chat-register tics observed directly in production output. Nothing from the original version was retracted. Every word on the original vocabulary list is still independently confirmed as a live tell. What the original version lacked was coverage above the single-word level: the phrases and sentence shapes that show up even when the vocabulary is clean.

## Vocabulary

Do not use: delve, tapestry, landscape (as metaphor), realm, beacon, leverage (as a verb), harness (as a verb), foster, robust, pivotal, transformative, groundbreaking, cutting-edge, multifaceted, intricate, cornerstone, paramount, navigate (as metaphor), illuminate, nuanced, unprecedented, game-changing, revolutionary.

Added this revision, confirmed current across multiple 2026 corpus studies: crucial, utilize, comprehensive, showcase, boast / boasts, meticulous(ly), notably, testament (to), garner, bolster, spearhead, catalyst, myriad, plethora, streamline, unlock, embark (on a journey), weave / woven (as a metaphor for combining things), ecosystem (as a vague metaphor for "market" or "community"), synergy, seamless, effortlessly, empower, elevate, holistic, dive (into), whilst, quintessence.

A caution on this list specifically: some of these words (harness, leverage, unlock) were considered borderline acceptable as recently as 2024 and are now flagged consistently. Treat this as a living list, not a fixed one. If a word here stops tripping anyone up in a year, it can come out. If a clean word starts showing up in every AI draft you read, it goes in.

## Punctuation

No em dashes. No en dashes either. Do not substitute parentheses as a workaround, that just relocates the same tic. Use a comma, a period, or restructure the sentence.

## Transitions and filler phrases

Do not open with "in today's [adjective] world," "in today's fast-paced landscape," or any variant.

Cut on sight: furthermore, moreover, additionally (as sentence openers), it's worth noting, it's important to note, needless to say, at the end of the day (as filler, not as a literal time reference), moving forward (as filler), when it comes to (as a hedge before the actual point), in the realm of, in the world of, as we navigate, let's dive in, let's unpack, take a deep dive, it just works (as an unearned claim of ease).

## Structure

**Negative parallelism.** The construction "it's not X, it's Y" (and its variants: "it's less about X and more about Y," "not because X, but because Y," "this isn't a bug, it's a feature," "it's not just X, it's a masterclass") is currently the single most-flagged AI sentence pattern in circulation, tracked across corporate filings, news writing, and chat logs. It shows up so often that it now has its own name in general use. Avoid it and its triple-negation cousin ("not A, not B, but C"). State Y. Trust the reader to infer what it replaces.

**Two-word sermon sentences stacked for drama.** "Not a hack. A shift. No notes." One short fragment for punch is fine. Three or more short declarative fragments in a row, each restating the last at a higher register, is the tell.

**Coaching cadence.** A cluster of instructive asides that tell the reader how to feel about what they just read, rather than just saying the thing: "sit with this," "unpack," "read that again, slowly," "let that sink in." Right register for a workshop, wrong register for almost everything else.

**Escalating triads.** The problem with three-item lists isn't the number three. It's that AI tends to make the third item a grander, more abstract restatement of the second ("it saves time, reduces errors, and transforms how your organization thinks"). Two or four items are fine. So is one, if it's the one that actually matters. If you keep three, make sure the third item adds real information instead of just raising the emotional register.

**Rhetorical question openers.** A model asking itself a question and immediately answering it ("So what does this mean for you? It means...") is a stalling pattern, not a rhetorical device. State the point directly.

**Recursive summarizing.** Watch for a document that summarizes itself at every level: each paragraph previews what it's about to say, each section recaps what it just said, and the piece closes with a summary of the summary. Say a thing once, where it belongs.

**Repeated sentence openings.** Several sentences in a row starting with the same clause ("They assume users will pay. They assume developers will build. They assume ecosystems will emerge.") reads as a template, not a rhythm. Vary the opening.

**Sentence-length monotony.** AI prose tends to sit in a narrow, metronomic band, most sentences landing in roughly the same word-count range with little variance. Human prose has more burst: a short, flat sentence next to a longer one that actually does some work. If every sentence in a paragraph is close to the same length, that's a tell independent of any single word choice.

Also carried over from the original version:

- Vary paragraph length. One sentence is fine. So is eight.
- Do not end with a paragraph that restates the body.

## Formatting

**Structured lists that sound like a helpful assistant.** Bullets where every item is grammatically identical and each one just restates the section header in slightly different words read as generated, not written. If a list could have been produced by filling in a template, rewrite it as prose, or vary the items so they're doing genuinely different jobs.

**Bolded list lead-ins.** Every bullet starting with a bolded phrase that restates its own header is common enough in AI-generated docs to be a recognizable habit. It's a weaker signal than it used to be, since plenty of people now format this way on purpose, but don't let it be the only structure a document ever uses.

**Title slides and headers in heavy italic serif.** A visual tell more than a prose one, most common in slide decks and one-pagers built alongside written copy. Flag it if it shows up in a deck accompanying this content.

## Tone

- Use contractions.
- Mix sentence rhythm.
- Take positions where the content calls for them. False balance reads as evasion.
- Filler adverbs like "genuinely," "quietly," "truly," and "simply" placed in front of a claim to make it feel more sincere are doing no work. Cut them or replace the sentence with something that earns the sincerity on its own.

## Assistant-voice tics

These matter most for chat, social, and email modes, where content sometimes drafts in a more conversational register than a web page or article would.

Cut on sight: load-bearing (insight / tweet / thought / code / feeling) · the quiet part is · zoom out · no notes · rest is noise · and honestly? · the takeaway? · that's the whole ballgame · let that sink in · hot take: · nobody talks about this, but it's the thing that actually matters · unpopular opinion? maybe · read that again, slowly · this is the part where it clicks · if you know, you know · you're absolutely right · that's on me · just say the word / say the word · good catch · I want you to sit with this · [X] is doing a lot of work here · here's where I would push back · you're right to push back on that · I need to own that · fair hit · let me reframe · one thing to flag · your assumption becomes the architecture · that's what talks · "the signal" used as a vibe word for "what matters"

Also watch for over-agreement before the actual point ("you're absolutely right, and...") and reflexive praise openers ("good catch," "great question") used as filler before the real response starts.

## Emoji

No emoji used as a substitute for the actual content of a claim, and no decorative emoji in front of list items in formal or persuasive copy. Emoji in social copy should follow the organization's own voice file, not default AI habit.

## Specifics

- Never fabricate statistics, citations, or quotes. If real data is not available, say so.
- No "studies show" or "experts agree" without a named, verifiable source.
- Flag speculation as speculation.

## Enthusiasm and hedging

- Do not call something "exciting" or "remarkable" without a concrete reason attached.
- One qualifier per claim, maximum, and only when the uncertainty is real.

## A note on over-correcting

Chasing every pattern on this list mechanically produces its own kind of sameness: writing so scrubbed of common constructions that it loses rhythm and personality in a new way. None of these patterns are automatically disqualifying on their own; a human writer can use "it's not X, it's Y" and mean it. The point of this module is a genuine editing pass by a person with judgment, not a search-and-replace exercise aimed at fooling a detector. If a rule here makes a true sentence worse, drop the rule for that sentence.

## Maintenance

Model fingerprints change with each release. This list is dated to the current release of the standard and is expected to be revised. This revision (September 2026) added structural patterns (negative parallelism, escalating triads, sentence-length monotony, coaching cadence) and a full chat-register phrase catalog that were largely absent from the prior version, which covered vocabulary only. No prior entries were retracted.

Contributions of newly observed patterns are welcome; include the model and version where the pattern was observed, and note whether the entry is vocabulary, phrase, or structural, since each decays at a different rate.