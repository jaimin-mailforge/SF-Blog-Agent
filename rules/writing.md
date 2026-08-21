# Forge Blog Writing Rules

How we write. Product facts, pricing, and positioning live in `rules/positioning.md`. The production process lives in `rules/process.md`.

Every rule below carries an enforcement tag:

- `[LINT]` a script checks it. You do not need to hold it in your head, but do not fight it either.
- `[JUDGE]` a reviewer with fresh eyes checks it. Write toward it deliberately.
- `[HUMAN]` Jaimin checks it before publishing. Flag anything uncertain.

A rule with no tag does not exist. If you want a new rule, it needs a tag first.

This file is written under its own rules. If you find an em dash, a banned word, or a 30-word sentence in here, that is a bug worth reporting.

---

## 1. Who is writing

Every piece is written by Frank Sondors, co-founder and CEO of Salesforge. He is the default and only byline.

Frank runs cold email and LinkedIn outreach for a living. He has:

- Set up domains, mailboxes, and DNS records with his own hands
- Burned domains and learned from it
- Tested most tools in this market, not just read about them
- Real opinions, real numbers, and real complaints

The reader should think: this is advice from someone who actually does this work.

Never write as a brand. Never write as a marketing team. Never write in an anonymous corporate voice.

The founder byline and the practitioner voice fit together. Frank can credibly claim broad hands-on experience across this category. That widens what the truth rules in section 7 allow, but it does not remove them.

---

## 2. Voice `[LINT]` `[JUDGE]`

**The hard rule, and it governs every other rule in this file.** Fixed by Jaimin on 2026-08-13.

> Active voice, first person point of view wherever it makes sense, authentic human voice. Absolutely no AI slop, no fluff, simple sentences and simple English. Content is factual and accurate, based on research.

Six words of that carry the weight, so read them as tests you can fail:

- **Active voice.** Name the doer. "Expandi charges per seat", not "a per-seat charge is applied".
- **First person where it makes sense.** "I" for what Frank did or saw. Not forced into a sentence that has no person in it.
- **Authentic human voice.** A practitioner talking, not a brand announcing.
- **No AI slop, no fluff.** Every sentence carries a fact, a number, an opinion, or a decision. If cutting a sentence loses the reader nothing, it was slop. Sentences that describe the article, the data, or the reviewers instead of presenting the content are the most common form of it. See the banned narrator framings in section 5.
- **Simple sentences, simple English.** One idea per sentence, everyday words. See sections 3 and 6.
- **Factual and accurate, based on research.** Every claim traces to the brief, to `rules/positioning.md`, or to `rules/observations.md`. Nothing traces to a plausible-sounding guess. See section 7.

The numbered rules:

1. First person "I" only. Never "we", "our", or "us". `[LINT]`
2. Active voice. Passive is acceptable only when the actor genuinely does not matter. If you can name the doer, name them. `[JUDGE]`
3. Write like you talk. If you would not say the sentence out loud to a colleague, rewrite it. `[JUDGE]`
4. Contractions are good: I've, it's, don't, that's, you'll. `[JUDGE]`
5. Starting a sentence with And, But, or So is fine. People do it. `[JUDGE]`
6. Talk to the reader with "you". "You'll need about 10 mailboxes for this volume." `[JUDGE]`

**The practitioner sentence, and it is a shape not a sentiment.** `[LINT]` `[JUDGE]` Added by Jaimin on 2026-08-20, after a draft that satisfied "first person where it makes sense" on the count and still read like a bibliography.

> **I + present-tense verb + object + a "when" or "because" clause.**

That is the whole pattern, and the approved RocketReach article runs it six times:

> "I point most RocketReach buyers at it first because it turns two invoices into one."
> "I reach for it when the ICP has an EU postcode."
> "I recommend Uplead when the RocketReach complaint is specifically about bounces."

The clause is the part that carries the experience. "I recommend Uplead" is a preference. "I recommend Uplead when the complaint is specifically about bounces" is a decision rule, and only somebody who has made the decision more than once can write the second half.

**What fails this rule is not an absent "I". It is an "I" that never leads.** The Expandi draft carried 25 first-person sentences against the approved article's 21, so it passed on density and failed on position. Fifteen of the 25 parked the narrator in a trailing clause to license a superlative: "the widest I've seen", "no other vendor I checked publishes them", "the most expensive configuration I priced", "the cleanest agency structure I found". Section 20 has banned that since 2026-08-19 with a cap of two per article. The checker landed 2026-08-20 as `trailing-superlative-i` and immediately found all fifteen, so the rule was unenforced for a full review cycle. The approved article scores 1.

Test a first-person sentence by deleting the "I" clause. If the sentence still says everything it said, the narrator was decoration and the clause should go. If the sentence loses its decision, the narrator was doing work.

---

## 3. Sentences and paragraphs `[LINT]`

**Rewritten 2026-08-19, calibrated against the editor-approved RocketReach article.** The old rule set a 12-to-20-word target and a hard 25-word ceiling. That is a mathematical instruction to write the middle, and it worked: the Expandi draft cleared the ceiling to literally zero violations and read flat. Measured side by side, both articles sit at a 13-word mean. The difference is spread.

| | Approved | Expandi draft |
|---|---|---|
| Mean sentence | 13.1 | 13.0 |
| Standard deviation | **8.55** | 5.82 |
| Six words or fewer | **28.0%** | 13.9% |
| Over 25 words | **10.3%** | 0.0% |

- **Aim at 12 to 20 words, and treat 25 as a soft target, not a wall.** Go past it when the sentence earns it.
- **Hard ceiling: 45 words, and the linter blocks it.** Nothing in a body paragraph needs 45.
- **The floors matter as much as the ceiling, and the linter checks all three.** Standard deviation of sentence length at least 7.0, at least 18% of sentences at six words or fewer, at least 5% over 25 words. Prose that never breaks 25 words by aiming everything at 15 fails this rule with zero over-25 findings. That is the intended behaviour.
- **A short sentence is a complete sentence.** `[LINT]` `[JUDGE]` Added by Jaimin on 2026-08-19, after the six-word floor above got satisfied with fragments instead of sentences. Every short sentence needs a subject and a finite verb. An imperative counts, because the subject is understood: "Stay put." is a sentence, "Genuinely." is not.

    What the floor produced when it was chased carelessly, all of it now removed from the Expandi draft:

    > "Expandi is a good one. **Genuinely.**"
    > "They're unhappy with the bill. **All of it.**"
    > "You pay for the seat. **Connected or not.**"
    > "Each piece exists elsewhere. **In fragments.**"
    > "The deliverability tooling surprised me. **At that price.**"
    > "Salesforge Growth is $80 flat. **Same five LinkedIn senders.**"
    > "So a three-rep team is $186 a month of slots. **Before the plan itself.**"

    Each one is an adverb or a noun phrase bolted onto the sentence before it with a period. It reads as emphasis and it is padding. Fourteen of them went into one draft in a single pass, which is what the pattern does once you start.

    **The banned shape, specifically.** Two or three consecutive verbless noun phrases used as a drumbeat. This is the most recognisable AI tell in the file and it survived a whole review cycle:

    > "One sequence. One set of exit rules. Not two campaigns and a spreadsheet to reconcile who is in which."

    No main verb in any of the three. Rewritten with a subject and a verb doing the work:

    > "That gives you one set of exit rules across both channels. You don't run two campaigns and then reconcile a spreadsheet to work out which prospect is in which one."

    **How to hit the floor honestly.** Split a sentence where both halves stand alone, and keep the left half short. "Expandi has one self-serve plan, and Business runs $79 per seat per month billed annually" becomes two sentences, the first of them five words. That is a real short sentence. Eleven of those splits carried the Expandi draft back over the floor after the fragments came out.

    **What the linter can and cannot do here.** `sentence-fragment` is a heuristic with no parser behind it, so it is tuned to never block good prose and therefore misses about half the cases. It catches "Genuinely." and "All of it." It does not catch "Two caveats." or "In fragments.", because an inflected word inside them reads as a possible verb. Do not treat a clean linter run as proof. Read the draft.

- **One argument per section, developed and then qualified.** `[LINT]` `[JUDGE]` Added by Jaimin on 2026-08-20. This is the rule the Expandi draft broke hardest, and no sentence-level metric caught it: measured against the approved article the draft had *higher* subordination, *more* connective openers and *fewer* runs of short parallel sentences. It still read as disconnected, because every paragraph announced a new frame.

    What the Salesforge section did across nine paragraphs:

    > "The branching is what matters." ... "Two things behind it come from the rest of the stack." ... "The billing unit matters most." ... "Pricing runs on active contacts and email volume instead of per mailbox or per seat."

    Four topic announcements in one section. Each is a competent sentence and each starts a different article. The reader is handed a new frame every forty words and never learns where any of the previous ones went. That is what "the sentences are not interconnected" means in practice, and adding connectives to the front of them makes it worse, not better, because a "So" on a sentence that does not follow is a lie about the logic.

    **The shape that works,** from the approved article's Apollo section, which runs one argument for its whole length:

    | Move | The sentence |
    |---|---|
    | State it | "I point most RocketReach buyers at it first because it turns two invoices into one." |
    | Develop it, with the numbers doing the work | "If you were paying RocketReach $829 a year for data and a separate cold email tool, Apollo's $49 to $79 per seat starts looking like fewer bills to reconcile." |
    | Qualify it | "However, Apollo has database depth concerns." |
    | Land the real cost | "Most importantly, the per-seat pricing scales fast once you get past 5 to 10 reps." |

    State it, develop it to its consequence, qualify it honestly. Three moves, one argument. A tool section does not need a second argument and cannot hold one.

    **Banned shapes, because each one restarts the article.** `[LINT]` The linter counts them as `frame-restart` and caps them at two per article. The approved article scores zero.

    > "X is what matters." / "X matters most." / "The X is the part worth understanding." / "Two things behind it..." / "There are three reasons." / "X is the second gate." / "What differs is..."

    If a section genuinely has two things to say, the second one is a consequence of the first and should be written as one. If it is not a consequence, it belongs in a different section.

- **Paragraphs chain. They do not sit side by side.** `[JUDGE]` Added 2026-08-20 alongside the rule above, because it is the same defect one level down. The second sentence of a paragraph develops the first rather than listing another fact about the same subject. The next paragraph opens on something the previous paragraph established, and names it rather than pointing at it with a bare "that" or "it".

    Discourse markers are allowed where the logic is real and nowhere else: However, Then, So, Most importantly, The catch, Which is why. A marker in front of a sentence that does not follow from the one before it is the cheap version of continuity and reads worse than no marker at all.

- **Name the doer.** `[JUDGE]` See section 2. This belongs next to the fragment rule because the two fail together: a verbless sentence has no actor in it by definition. When a vendor withholds something, the vendor is the subject. "HeyReach does not document it", never "whether email replies land there is not documented".

- **A long sentence has to be a list, not a weld.** It may run long when it enumerates: "Every deal is a quote, annual-only, and reported contracts run $15,000 to $60,000 a year depending on seats, credits, and whether you take the Diamond tier." It may not when it fuses two complete statements with a comma and an "and".
- A bolded label followed by a colon does not count toward sentence length, whether it opens a bullet or a paragraph. "**Bounce Shield:**" is a label, not part of the sentence.
- One idea per sentence. If an "and" joins two full thoughts, split it.
- **Open a section with two sentences under eight words before any sentence over twenty.** The short pair buys the licence to sprawl. "Buying it is a project. Cognism does not publish pricing." Then the 31-word unpacking.
- **Paragraphs: 60 words maximum. Sentence count is not capped.** The old 1-to-3-sentence cap inverted its own purpose, which is the five-second skim test. A 74-word three-sentence paragraph passed it while a 28-word four-sentence pricing paragraph failed, and it made the approved article's best paragraph illegal, six short sentences that resolve a contradiction for the reader.
- New idea means new paragraph. A paragraph over 60 words is usually two ideas.
- A direct-answer FAQ paragraph is exempt from the word cap. "Yes." plus three supporting sentences is the shape section 16 asks for.
- Skim test: if a section cannot be skimmed in 5 seconds, rewrite it.

**Section length.** Fixed by Jaimin on 2026-08-13. Diagnosis sections stay short and to the point. That covers "Why people leave [Competitor]", "Why people look for [Competitor] alternatives", and any H2 whose job is to name a problem rather than review a product.

- **Two short paragraphs per subsection is enough.** The linter warns past two.
- One point per subsection. The H3 says what the problem is, the two paragraphs say what it costs the reader, and the section ends.
- No third paragraph adding a comparison, a caveat, and a scaled-up example. Pick the strongest one.
- The arithmetic goes in the paragraph that needs it, not in a paragraph of its own.

---

## 4. Punctuation `[LINT]`

- No em dashes. Not once. Use a comma, a period, or a colon.
- No semicolons. Split into two sentences.
- No en dashes in prose. Use "to" in ranges: "$3 to $2 per mailbox".
- No exclamation marks in body copy. One in an intro or a CTA is the maximum, and it is rarely needed.
- Rhetorical questions: one or two per article.
- Normal quotes, normal commas. No emojis.

---

## 5. Banned words and phrases `[LINT]`

**Banned words**

seamless, seamlessly, robust, leverage (as a verb), empower, streamline, unlock, elevate, ensure, ensures, moreover, furthermore, additionally, cutting-edge, next-generation, game-changer, hassle-free, guesswork, delve, landscape (figurative), realm, harness, supercharge, revolutionize, effortlessly, comprehensive, holistic, innovative, state-of-the-art, utilize (say "use")

**Banned figurative verbs**

Do not give a product or a feature a body. When the subject of the sentence is a tool, a feature, or a plan, do not use: sits, puts, pulls, lives, rests, boasts, weaves, flows, houses.

- Wrong: "The warmup tool sits inside the dashboard."
- Right: "You find the warmup tool inside the dashboard."
- Wrong: "The extension pulls data from LinkedIn."
- Right: "The extension gets emails from LinkedIn profiles."

A person can still pull a list or put a domain into a workspace. The ban applies when the product is the actor.

**Banned phrases**

- "in today's world" and "in today's fast-paced environment"
- "all-in-one solution"
- "best-in-class"
- "take your outreach to the next level"
- "look no further"
- "it's worth noting that"
- "whether you're a X or Y", in any version
- "dive into" and "let's dive in"
- "at the end of the day", once per article maximum, only if it reads naturally
- "This feature allows you to..."
- "what makes", "the answer is", "what separates", "here's the thing"

**Banned narrator framings**

These are shapes, not words, so read for them separately.

- Literary metaphor: "a tale of two X", "the story of X is", "two versions of the same product"
- Journalist wrap-up: "tells the real story", "speaks volumes", "says it all"
- Narrator preamble: "the honest read is", "the real question is", "what the patterns add up to"
- Writing about the article: "the most useful signal in this review", "the rest of this post covers", "below I will walk through"

If a sentence describes the article, the data, or the reviewers rather than presenting the content, cut it.

**Banned patterns** `[JUDGE]`

- Formal transitions between paragraphs. Just start the next thought.
- **Competitor pros and cons stay within one of balanced, unless the extra con cites evidence.** `[LINT]` Decided by Jaimin on 2026-08-19, replacing the old flat ban on four against four.

    The editor-approved RocketReach article runs every one of its eight competitors at 4:4 or 5:5 and puts all its imbalance in the house product at 8:1. The reasoning holds: bias in the Forge cons cell is discounted by every reader who sees it, while bias in a rival's table is where trust actually leaks. A reader who knows Dripify well and sees us shading it stops believing the other seven.

    So a competitor may run net-negative by two or more only when a con cell cites something checkable: a con-tag mention count, a review score, a sub-score, or a share. Meet Alfred at 2 pros against 5 cons is fine, because the cons carry 3.4 on G2, 2.8 on Capterra and a 1.9 support score. The same shape with four cons of pure judgement is not.

    Extra **pros** are not covered by this. Handing a competitor a fifth pro costs us nothing and the reader nothing.

    The routed Forge product is exempt, and its single con states the limit and stops. Never rebut the con inside the con cell: "No free plan" and not "No free plan, a 14-day free trial is available".
- Three-item lists in every sentence. "Fast, reliable, and scalable" is a tell.
- Repeating the product name at the start of consecutive sentences.
- Every paragraph the same length.

---

## 5a. AI framings, and the one index for all of them `[LINT]` `[JUDGE]`

**Added by Jaimin on 2026-08-21: strictly avoid typical AI framings.** Read this section
before drafting. It is deliberately the single place that names all of them, because they
were previously spread across two data files, three rule sections and two linter checks,
and a drafting session had no one thing to read.

**What the measurement found first, because it changes how to use this section.** Twenty-five
candidate framings were counted across the editor-approved article, our Expandi draft and
three published articles. Almost nothing hit. "that said" appeared once in one article and
"source of truth" twice in one draft. Structural tells scored zero: no punchline
paragraphs, no negation-then-correction pairs in the Expandi draft against one in the
approved article, colon-explainers level at two each.

So this is a **preventive** list, not a repair list. The earlier passes already removed
these: the fragment rule in section 3 killed the punchline paragraph, the through-line
rule killed the cleft, and the banned-word file killed the vocabulary. Do not go looking
for a problem in a clean draft. Section 6 records that four separate metrics said our
prose was fine when a human said otherwise, and adding a fifth is the trap, not the fix.

### Enforced, and the linter blocks on them

New entries added 2026-08-21, all verified to fire zero times on the editor-approved
article before being added:

`lint/data/banned-words.txt` gains **leverage** in all its forms, and **landscape**.

`lint/data/banned-phrases.txt` gains: more than just, when it comes to, that said, with
that said, think of it as, the bottom line, in summary, to sum up, the good news is,
here's where it gets, deep dive, under the hood, heavy lifting, move the needle, in the
world of, the reality is, the truth is, one thing is clear, battle-tested.

Each one has an unambiguous slop reading and no legitimate twin, which is the bar for a
hard ban. A banned phrase is an ERROR and blocks a write, so a false positive costs more
than a missed instance.

### Deliberately NOT banned

**"at scale" is allowed.** The approved article uses it three times and it is ordinary
vocabulary for this reader. Banning it would flag the benchmark, which is the mistake an
intro paragraph-count check made on the same day.

**"whether you're X or Y" stays a judgment call.** As an audience hedge it is pure slop:
"whether you're a solo founder or an agency, this tool scales with you." As a plan
comparison it is useful and precise: "whether you're on Pro or Growth". Same construction,
opposite value, so a hard ban would block the good one.

**"navigate" stays allowed.** "Navigating the dashboard" is real UI language. Only
"navigating the landscape" is slop, and `landscape` is banned on its own.

**"source of truth" was banned on 2026-08-21 and unbanned the same hour.** It caught two
genuine instances, and then both turned out to be correct usage: "I use it when the CRM is
the source of truth" and a Klenty feature label. Single source of truth is how CRM vendors
describe themselves, so it is this reader's own vocabulary, and section 6 removed the
layman-language rule precisely to stop us stripping that out. Banning it would have been
that rule coming back in through the side door, one section later in the same file. Worth
recording because it is the easiest mistake to repeat: a phrase can be corporate jargon
and still be the plain word for the person reading.

### Judgment calls, no checker, read for them

- **The false contrast.** "It's not just X, it's Y." "This isn't a feature, it's a
  philosophy." The construction promises a reveal and delivers a synonym. State the thing.
- **The rhetorical question as a paragraph opener.** "So what does this mean for your
  team?" Nobody asked. Answer the question instead of staging it.
- **The rule of three, used as rhythm rather than as a list.** "Faster, cheaper, and more
  reliable." Three adjectives with no figures behind them is one adjective's worth of
  information. Section 6 already wants the number.
- **The analogy reflex.** "Think of it as a Swiss Army knife for outreach." Banned as a
  phrase now, but the reflex outlives the phrasing. Describe the mechanism.
- **Hedge stacking.** "may potentially help improve" is three hedges for one claim. Pick
  one or drop it.
- **The summary that adds nothing.** A closing sentence that restates the paragraph in
  shorter words. If cutting it loses the reader nothing, it was slop. See section 2.

### Already enforced elsewhere, listed here so this is a real index

| Framing | Where it lives | Checker |
|---|---|---|
| Verbless punchline, drumbeat fragments | Section 3 | `sentence-fragment` |
| A new frame every paragraph | Section 3 | `frame-restart` |
| "I" trailing a superlative as a citation | Sections 2 and 20 | `trailing-superlative-i` |
| Narrator describing the article or the data | Section 5 | `banned-phrase` |
| Defining a thing by what it is not | Section 6 | `define-by-negation` |
| Comparisons that die when quoted off the page | Section 17 | `unscoped-comparison` |
| Intro proving what the next section proves | Section 9d | `intro-duplicates-next` |
| Marketing vocabulary with no referent | Section 5 | `banned-word` |

If a framing is not in this table and not in the two lists above, it is a judgment call
and the linter will not save you. Read the draft.

---

## 6. Preferred language `[JUDGE]` `[LINT]`

**Partly enforced since 2026-08-13.** `define-by-negation` counts "rather than", "instead of" and bare ", not". One is fine, thirty is a tic. The Expandi draft ran 28.

Small everyday verbs and concrete nouns: set up, run, send, check, connect, fix, break, cost, save, switch, land in the inbox, burn a domain.

- "it took me 10 minutes" beats "the setup process is quick"
- "you pay $48 a month" beats "affordable pricing options"
- "my reply rate went from 2% to 9%" beats "significantly improved results"

Numbers make writing believable. Use exact prices, times, counts, and ratings with review counts.

**Removed 2026-08-21: "Layman language only."** It said "plain everyday words a
non-marketer would say, and if a word would slow down a reader who sees it once,
replace it." Jaimin cut it because it was producing oversimplified words, and the
measurement below says he is right: we already use *fewer* long words than the
editor-approved article, so the rule was pushing further in a direction we had
overshot. Stripping `deliverability` down to "getting into the inbox" every time does
not make the writing clearer to a founder buying outreach software. It makes it sound
like it was written for somebody else.

What replaces it: **use the precise word when the precise word is the plain one for
this reader.** The audience runs cold email and LinkedIn for a living. `Deliverability`,
`per-seat`, `waterfall enrichment`, `session-token auth` and `warm up` are their
everyday vocabulary, not jargon. Explain a term the first time if it is genuinely
niche, then use it. What section 6 still bans is unchanged and is a different thing:
marketing abstraction with no referent, "affordable pricing options", "significantly
improved results", "robust solution". Those are not hard words. They are empty ones.

**Simple sentence structure and simple vocabulary.** `[JUDGE]` Restated by Jaimin on
2026-08-21 alongside section 9d, then narrowed the same day when the measurement came
back. Measured before writing a rule for it:

| | Approved article | Expandi draft |
|---|---|---|
| Words of four or more syllables | 3.4% | **2.6%** |
| Words of three syllables | 8.1% | **5.6%** |
| Sentences opening on a subordinate clause | 3.0% | **1.6%** |
| Sentences with three or more clauses | 3.0% | **1.4%** |
| Subject separated from its verb by an insertion | 0.0% | 0.0% |

We are already simpler than the benchmark on every measure, and on vocabulary we are
simpler by a third. **So there is deliberately no vocabulary or structure checker, and
nobody should build one.** A syllable ceiling would fire on `personalization`,
`deliverability`, `invitations` and `infrastructure`, which are this reader's own
vocabulary. A clause-count ceiling would fire on the pricing sentences that carry three
figures, which is the shape those sentences need.

Read the table the other way round too. The gap on four-syllable words is not a score we
are winning. It is the measurement that got "Layman language only" deleted.

This is the fourth time a plausible-sounding metric has said our prose was fine when a
human said it was not, or said it was worse when it was better. Connective openers,
back-reference, subordination and short-sentence runs all did the same thing before
section 3's through-line rule found the real defect one level up. **When prose reads
wrong and every sentence-level metric says it is fine, the defect is at the paragraph,
the section, or the substance. Look there.** Do not add a fifth metric.

**No trailing add-on clauses.** Do not write a main clause, then a comma, then a tail. That shape reads as machine-written.

- Wrong: "Full setup takes under five minutes, and the guided flow calculates how many domains you need based on your target volume."
- Right: "Full setup takes under five minutes. The guided flow works out how many domains you need for your target volume."
- Wrong: "Domain forwarding: Visitors to your secondary domains land on your main site, set up inside the platform."
- Right: "Domain forwarding: Point your secondary domains at your main site."

Start with the action. Keep one thought. End the sentence. Feature bullets follow the same rule.

---

## 7. Truth rules `[LINT]` `[HUMAN]`

This is the most important section in the file. Absolute claims destroy trust, and invented specifics are worse.

1. **Every product claim must be verifiable against `rules/positioning.md`.** If the positioning file does not support it, do not write it. Ask.
2. **No absolute guarantees.** Never write "the bill never moved", "always lands in the inbox", "guaranteed replies", "zero spam", "100% placement".
3. **Two claim types, handled differently.**
   - **Product facts** (pricing, features, limits, plan contents): state them plainly and exactly, from the positioning file.
   - **Outcomes** (reply rates, deliverability, meetings, savings): frame as observed experience. "Has come down." "Has been steady." "Climbed noticeably." "Stayed predictable as we grew."
4. **Mark every placeholder number.** When you need a figure you do not have, write it as `[[FIGURE: reply rate for the 40-mailbox setup]]` so Jaimin replaces it before publishing. `[LINT]` blocks publishing while any `[[FIGURE:` marker remains.
5. **When unsure, say less.** "Deliverability has been steady for us" is safe. "100% inbox placement" is not.
6. **Competitor pricing comes from the vendor's live pricing page only.** Never from G2, Capterra, TrustRadius, a listicle, Reddit, an AI summary, or one of our own older articles. Re-check on every rewrite. Record the URL you used.

The fix pattern:

- Risky: "We scaled to 20 mailboxes and the bill never moved."
- Safe: "I scaled to 20 mailboxes and paid nothing extra for them, because Salesforge does not price per mailbox or per sender. That kept costs predictable as the team grew."

---

## 8. How to sound human `[JUDGE]`

1. **First-hand moments**, two to three per article. "I uploaded a 5,000-contact list on a Tuesday and the enrichment finished before my coffee did."
2. **Small real complaints**, including about our own products. "The dashboard felt cluttered in my first week." One real flaw earns more trust than ten compliments.
3. **Opinions.** "I think the Growth plan is the only one worth buying past 5,000 contacts."
4. **Conditional honesty.** "If you send under 500 emails a month, you do not need this yet."
5. **Light asides**, once or twice per article. "(No, I counted.)"
6. **Admissions of limits.** "I have not tested their enterprise plan, so I cannot speak to it."
7. **Constructive framing for negatives.** Name the issue, its impact, and a fix. Mild, specific, professional.

Human does not mean fake typos, deliberate grammar mistakes, lowercase "i", or manufactured flaws. Human means specific, honest, and conversational.

---

## 9. Structure: listicle, "Best X tools"

1. **Intro**, 3 to 6 short paragraphs. Open on the problem or a personal moment. Never "in this article we will". Say how many tools you tested and why most did not make it.
2. **How I chose.** Your criteria as a short list. Be specific: what you tested, for how long, what you measured.
3. **TL;DR.** One bullet per tool, in the article's running order. See section 9a for the fixed shape.
4. **Comparison table.** The HTML template in `assets/comparison-table.html`. See section 14.
5. **Tool sections.** The routed Forge product first and deepest. See section 9b for the fixed skeleton.
6. **"Which one should you pick?"** Answer by use case, not by hype.
7. **FAQs.** Minimum 5, direct answer in the first sentence of each.

---

## 9a. The TL;DR block `[LINT]`

Fixed by Jaimin on 2026-08-13. The linter blocks any TL;DR bullet that misses the shape.

**Tool name, colon, then "Best for".** Every bullet, no exceptions.

    - **[Salesforge](#salesforge):** Best for GTM teams and Agencies running LinkedIn plus
      email plus AI in one platform, with unlimited mailboxes and unlimited LinkedIn senders
      on Growth. Primebox™ unifies replies across every channel, and Warmforge warm up is
      bundled at no extra cost.

Rules for the bullet:

- The tool name is a jumplink to its section, and it carries the colon.
- **No price figures in the TL;DR.** `[LINT]` Fixed by Jaimin on 2026-08-19. Not a rate, not a currency figure, not "from $40 a month billed annually". The block routes by buyer, and price is a different axis that already has two homes: the comparison table's starting-price row and each tool's own pricing section.

    Three reasons, and the third is the one that decided it.

    First, a price in the TL;DR competes with the routing job. A reader scanning eight bullets for "which of these is me" does not want to be doing arithmetic at the same time.

    Second, prices go stale faster than anything else in an article. Carrying one in the TL;DR as well as the table and the pricing section means the same figure lives in three places, so a single vendor change makes two of them wrong. The Expandi draft had Waalaxy's rate in ten places, and correcting it was a ten-edit job that a reviewer had to check ten times.

    Third, AI Overviews lift the TL;DR bullet whole. A bullet that gets quoted into an AI answer with a rate that changed last month is the worst version of being cited.

    **Relative price claims are still fine**, because they do not go stale the same way and they do real routing work. "at the cheapest entry price" and "at the lowest price I found" both stay. What goes is the number.

    Non-price limits that decide fit also stay, and often they are the better thing to put in the freed-up space. "The entry tier caps you at 300 invitations a month" tells a reader more about whether Waalaxy suits them than "$16 per user per month billed annually" does.

- **The opener comes from a closed set of four.** `[LINT]` Widened by Jaimin on 2026-08-19 from the single mandatory "Best for". Permitted: **"Best for"**, **"Best overall for"**, **"Cheapest pick for"**, **"Best if you want"**. Nothing else. Not "runs", not "charges", not "is the cheapest".

    The set stays closed because AI Overviews lift the bullet whole, so a predictable shape is the point. It was widened because the editor-approved RocketReach article used all four, and a tool whose entire case is price routes better with "Cheapest pick for email-only lookups" than with a forced ninth "Best for".
- Then who it is for, in the words a buyer would use about themselves.
- Then one or two sentences on the mechanics that earn that fit. Named features, real numbers.
- Then the annual price where the article is price-led. See section 9c.
- No "Not for" clause. See section 13.

The point of the fixed shape is that this block is what AI Overviews and Perplexity lift. A bullet that opens on the buyer is quotable as a recommendation. A bullet that opens on a feature is not.

---

## 9b. The tool section skeleton `[LINT]`

Every product section in a listicle, an alternatives post, or a category page uses this order.

1. **H2:** "N. [Tool Name]"
2. **Best for:** one line, the buyer in their own words, never "everyone". For Salesforge this line always opens "Best for GTM teams and Agencies". See `rules/positioning.md`.
3. **G2 Rating:** "X out of 5 (N reviews)".
4. **A plain explainer sentence, and it opens the prose.** "[Tool] is a [what kind of tool] that [what it does]." Say what the thing is before you say what is interesting about it. A reader who has never heard of the tool must be able to follow the second paragraph.
5. **2 to 4 more paragraphs.** The mechanics, the billing unit, the trade-off, one specific first-hand moment where `rules/observations.md` funds one.
5b. **The first-person verdict, one sentence, in every tool section.** `[JUDGE]` Added 2026-08-19. It goes after the explainer and the mechanism paragraph, before the caveat. The approved RocketReach article carries one in 8 of its 9 sections. The Expandi draft carried one in 0 of 8, which is why its narrator reads as a bibliography rather than a practitioner.

    The shape: **I [recommend / reach for / point buyers at / put] [tool] when [the reader's condition].**

    > "I reach for it when the ICP has an EU postcode."
    > "I recommend Uplead when the RocketReach complaint is specifically about bounces."
    > "I point most RocketReach buyers at it first because it turns two invoices into one."

    A grep for `I (recommend|reach for|point|put|pick|choose|prefer|think)` returned six hits in the approved article and **zero** in our 7,800-word draft. The draft had all the same conditions, in second person, with the recommender stripped out of the front: "If you run LinkedIn outreach for clients across a lot of accounts". Same information, and nobody is doing the recommending.

    **Also required: one first-person opinion per article with no number in it.** "I have complicated feelings about it." Cheapest rule in this file to satisfy, because `rules/observations.md` cannot gate an opinion that carries no figure.

6. **H3 "Key features".** 5 to 8 bullets for a competitor. For the routed Forge product, **one bullet per must-cover feature in that product's section of `rules/forge-positioning-guidelines.md`, and the same number of bullets as that section lists.** Colon after the feature name. See below.
7. **H3 "Pros and cons".** A two-column table, lopsided and honest. For Salesforge the cons column carries exactly one point. See `rules/positioning.md`.
8. **H3 "Pricing".** Annual rates only. See section 9c.
9. **H3 "What real users say".** One line, and only one. See below.

**The plain explainer, rule 4, is the one that gets skipped.** Opening on the most interesting fact reads well to someone who already knows the category and loses everyone else. Explain, then argue.

- Wrong: "Every other tool on this list runs email and LinkedIn as two campaigns you keep in step by hand."
- Right: "Salesforge is a multichannel outreach tool that runs cold email and LinkedIn as two channels of one sequence." Then the contrast.

**Key features bullets carry a colon after the feature name.** `[LINT]`

- Right: "Flat per-sender pricing with free unlimited users: The vendor FAQ is explicit that teammates, VAs and clients are not charged for."
- Wrong: "Flat per-sender pricing with free unlimited users. The vendor FAQ is explicit..."

The feature name is the bolded part and it is a name, not a sentence. Then the colon, then what it does in one or two sentences.

**The bullet count is not yours to choose. It is the length of the must-cover list.** Fixed by Jaimin on 2026-08-13.

Work out which list governs before writing the section:

- **The routed product's own section in `rules/forge-positioning-guidelines.md` is the checklist.** For a LinkedIn-focused article that is "Salesforge: LinkedIn", which lists 12 must-cover features, so the key features carry 12 bullets. For a cold email article it is "Salesforge: Cold Email". For a multichannel piece it is "Salesforge: Multichannel", and that one also requires the Category A and Leaning B framing.
- **One bullet per feature, using the doc's feature name.** Reword for cadence, never for meaning.
- **Shuffle the order between articles.** The doc says so directly. Lead with whatever the article is about, so a LinkedIn piece opens on the six native LinkedIn actions rather than on unlimited mailboxes.
- **Supporting products are not entries on that list.** Warmforge, the Leadsforge Company Followers search and the infrastructure products belong in the prose, the pricing paragraph, or the Final Verdict. The playbook names them separately for exactly this reason.

**Never bundle must-covers behind one label.** Two failures on the Expandi draft, both caused by it. The first pass hid A/B testing, the API and MCP inside an Agent Frank bullet, and campaign analytics and the followers search were never written at all. The second pass still merged the API, Integrations and MCP CLI into one bullet, which read as complete and was three features short. Count the bullets against the doc, then check each name.

**The ratings section is one line of prose, and it carries its citation.** `[LINT]` Fixed by Jaimin on 2026-08-13, amended 2026-08-19.

**Amendment.** The one-line rule was stripping our citations. The approved RocketReach article carries **20 external links against our 0**: for each of its nine tools it links the G2 product page on the rating sentence, then a permalink to one specific numbered review under a captioned screenshot. It also links the incumbent's own refund policy on the two sentences that accuse. A review screenshot and its source link are not a second line of prose. What stays banned is prose under the rating: no con-tag breakdown, no one-star arithmetic, no reading of what the reviews cluster on. Those live in the pros and cons cells.

Every rating line carries the review count. "G2 puts Salesforge at 4.6 from 137 reviews", never "Salesforge holds 4.6 out of 5 on G2". A rating with no denominator is the weakest form of the claim, and the approved article gets this wrong in all nine sections while arguing elsewhere that sample size matters.

**Any accusation sourced to a document the vendor published must link that document.** Our draft cites Expandi's pricing-page footnote, its purchased-versus-connected seat clause and its own Smartlead guide, and links none of the three. That is the cheapest credibility fix available to us.

    ### What real users say

    G2 puts Salesforge at 4.6 from 137 reviews.

Nothing else goes in that section. No con-tag breakdown, no one-star arithmetic, no reading of what the reviews cluster on. Jaimin adds review screenshots by hand directly below that line, and prose underneath it gets in the way. The linter blocks a second line.

Complaint themes still belong in the article. Put them where they are load-bearing: in the cons column, in the pricing paragraph when the complaint is about price, or in the "Best for" line when the complaint decides who should walk away.

---

## 9c. Pricing in prose and tables `[LINT]`

**Annual rates only, everywhere, for every tool.** Fixed by Jaimin on 2026-08-13. The full rule and its edge cases are in `rules/positioning.md` under "Annual format only". The short version:

- Pricing tables carry one price column and it is the annual one. The linter blocks a "Billed monthly" or "Billed quarterly" column header.
- Prose says "$39 per user per month billed annually". Never "$59 monthly, $39 annually".
- Cost-at-scale math runs on annual rates end to end.
- **One saving line is allowed under a pricing table.** `[LINT]` Added by Jaimin on 2026-08-19. It may name the monthly rate for the sole purpose of showing the annual discount: "Monthly is $48, so the annual plan saves two months." No monthly column, no monthly row, one line. The editor-approved RocketReach article ran a monthly row beside the annual one to make the same point, which reintroduces the ambiguity this rule exists to remove. The line does the job without the column.

**When a vendor publishes no price.** `[LINT]` `[HUMAN]` Added by Jaimin on 2026-08-19. Some vendors are quote-only, Cognism and ZoomInfo among them, and until now this rule made "custom pricing, sales contact required" the only compliant thing we could write about them. That is worse for the reader than a labelled range.

- Say plainly that the vendor does not publish pricing. That sentence comes first, always.
- A range may follow **only** if it comes from a named third-party source **with a sample size**, and it is labelled as reported rather than published. "Cognism does not publish pricing. Reported contracts run $15,000 to $60,000 a year."
- Link the source. An unlinked reported range is a guess with a decimal point.
- Use the same range in every section of the article. The approved article printed "$15,000 to $60,000-plus" in one place and "$14,995 to $45,000" in another, for the same vendor.
- Never launder a reported range into a published one, and never collapse a range into a single figure.
- A reported range never goes in the comparison table's price cell. That cell carries vendor-published rates or "Not published".

---

## 9d. The introduction `[JUDGE]` `[LINT]`

**Added by Jaimin on 2026-08-21.** Section 9 already sets the intro's shape, 3 to 6
short paragraphs, open on the problem, never "in this article we will". That governs
form. This section governs substance, because a correctly shaped intro can still be
the weakest part of the page.

> Well-researched, matching search intent, addressing common pain points.

Three tests, and the intro fails if it misses any.

**1. It matches what the SERP says the query means, not what we assume it means.**
The brief's SERP section is the authority. Read it before writing a word of the intro.
On the Expandi keyword the brief found intent blending: a competitor ranks third with a
*review* page and Google reads the query as partly a review, so the winning page has to
evaluate the competitor and not only list alternatives. An intro written on the
assumption "they already decided, get to the list" would have been wrong on that
keyword and right on a different one. You cannot know which without reading the SERP.

**2. It names the reader's situation before it argues anything.** The reader has to see
their own week in the first two paragraphs. The approved RocketReach article spends
three paragraphs on a click sequence the reader performs from memory, "pick SaaS, pick
Series A to B, pick United States, hit search, wait, scroll, uncheck the ones that don't
fit, export", before it makes a single claim. That recognition is what buys the rest of
the page. The brief's JTBD line is usually the raw material for it, and on the Expandi
article it was written and then never used: "my email lives in a separate tool" and
"without doubling my bill or my tabs" are the reader's own words about their own day.

**3. Pain points are plural, they come from the evidence, and they arrive compressed.**
`[LINT]` The approved article names five in one sentence: bounces on verified emails,
credits burning on bad data, unused credits forfeited at cancellation, auto-renewals
firing without warning, and a database that runs thin outside US tech. Then one line
lands it: "Every RocketReach buyer eventually runs into at least one."

The Expandi draft named one, the bill, and then proved it across six of nine paragraphs.
Meanwhile the brief carried three verified pains and a fourth piece of evidence sitting
unused. **Minimum two distinct pain points in the intro, each traceable to the brief.**
Counting them is a judgment call and the linter does not pretend to. What it does
check is the failure below, `intro-duplicates-next`, plus the paragraph shape.

**A collision to know about, found by `lint/sections.py` on 2026-08-21.** This section
wants plural pain points and section 3 bans "Two things..." and "Three things..." as frame
restarts. Writing "Three things send people looking anyway" satisfies 9d and trips 3.

The ban is right and this section is right, because the banned shape is announcing an
enumeration and then not delivering it, which is what "Two things behind it come from the
rest of the stack" did. An intro that says "three things" and then delivers all three is
not the same defect. But no checker can tell those apart, so the shape stays banned and
the intro signals plurality without counting out loud: "The reasons people leave are all
on Expandi's own pages", then the reasons. Same information, no banned opener.

**And the intro does not prove what the next section proves.** This is the specific
failure to watch. The Expandi intro ran the $79 to $136.50 arithmetic in three
paragraphs, and "Why People Leave Expandi" then ran the identical arithmetic
immediately after, at more length and with the sources. The intro should have named the
number once and moved on. An intro that duplicates the section beneath it has no reason
to exist, and the reader feels the repetition even if they cannot name it.

**Close on the promise.** What was checked, and what the reader is getting. "I've
tested 15 RocketReach alternatives, evaluated each on several criteria, and shortlisted
the top 9." Ours said "Eight made the list" as an aside, after the methodology sentence.
State the promise plainly and put it last, where it hands off to the TL;DR.

---

## 10. Structure: alternatives post, "X alternatives"

1. **Intro.** Acknowledge the competitor is a good tool. Then give the true reasons people look elsewhere: price jumps, seat limits, missing channels, deliverability trouble.
2. **"Why people leave [Competitor]".** 3 to 5 specific reasons drawn from real public complaints, never invented. One H3 per reason, two short paragraphs each. See the section-length rule in section 3.
3. **TL;DR and comparison table**, same rules as the listicle. See sections 9a and 14.
4. **The Forge product first and deepest.** Frame it as "why I moved" or "what I found", not "why it is better".
5. **Other alternatives**, same skeleton as section 9b, each matched to a reader type.
6. **"When [Competitor] is still the better choice".** Always include this. It is the highest-trust section in the post, and it is not optional.
7. **FAQs.** Minimum 5.

---

## 11. Structure: VS post, "X vs Y"

1. **TL;DR near the top**, 3 to 5 sentences. Give the verdict by use case immediately.
2. **Comparison table.** Mandatory. See section 14.
3. **Section by section, by job:** deliverability, pricing, sending limits, LinkedIn, reply management, support. Say which tool wins each one and why.
4. **Pricing math.** "For 10,000 contacts, X costs $Y a month and Z costs $W a month."
5. **Final verdict by reader type.** Commit. Never "both are great".
6. **FAQs.** Minimum 5.

---

## 12. Structure: review or product post

1. What the tool is, in two plain sentences.
2. How I tested it: duration, volume, what I measured.
3. Feature walkthrough in the order a user meets them. Steps and before-and-after examples where they help.
4. Pricing with real numbers.
5. Pros and cons, lopsided and honest.
6. Who should use it. The reader who should walk away is routed in the verdict, never in a "Not for" label. See section 13.
7. Verdict and one CTA.
8. FAQs. Minimum 5.

---

## 13. Who it's for `[LINT]` `[JUDGE]`

**No per-tool "Not for:" line. Ever.** Fixed by Jaimin on 2026-08-13, reversing the rule that stood here earlier the same day. The linter blocks the line on sight.

The line was required in every product section, then made optional, and is now banned outright. Three shapes are gone with it:

- `**Not for:** anyone who wants LinkedIn on its own.`
- `**Not for:** anyone sending real email volume.`
- Any bolded disqualifier label under a tool's H2, whatever it is called.

**Disqualification still has to happen.** It moves to the three places where it reads as advice instead of a warning label:

1. **The Best for line.** Naming the buyer precisely already excludes everyone else. "Best for solo operators and two-person teams who want native email at the lowest price" tells a fifteen-person team to keep reading.
2. **The cons column.** A real limitation stated plainly does the disqualifying work. "One mailbox per account, capped at 200 emails a day" is the disqualifier for anyone sending volume.
3. **The Final Verdict, and "When [Competitor] is still the better choice".** These route by reader type across the whole article, including the reader who should not buy anything on the list.

An article that never tells a reader to walk away still fails this rule. What changed is the mechanism, not the obligation.

Why it matters, unchanged: readers trust a writer who tells them to walk away, and LLM recommendations are personalised to the person asking, so their prompt carries company size, budget, and deal size. Content that names the fit precisely can be matched to the right person. Honest disqualification is how we get recommended. It just belongs in prose a reader can act on, not in a label under every heading.

---

## 14. Comparison table `[LINT]`

Almost every article needs one. Use the HTML template in `assets/comparison-table.html` exactly. Do not retype the CSS and do not substitute a markdown table.

- The routed Forge product column carries `class="highlight-col"` on its `<th>` and on every `<td>`, plus the "Best Overall" badge.
- The Forge product header links to its signup URL.
- The purple highlight stays whichever Forge product is routed. Only the label and the link change.
- **Ship the full CSS block every time.** Fixed by Jaimin on 2026-08-13. The `<style>` block in the template goes into the article verbatim, every article, no trimming and no "the site already has these styles". Copy the file, do not retype it.
- Up to 6 tool columns plus the Feature column, so 7 in total. An alternatives post includes the incumbent as one of the 6, because a reader comparing alternatives needs the thing they are leaving in the table.
- Every tool name in the table is a jumplink to its section. The routed Forge product links to its signup URL instead.
- Cells state what the tool actually is, in one to three lines. "No, email only" beats an X mark. "Yes, native. 6 LinkedIn actions with conditional branching" beats a check mark.
- **No semicolons in cells.** Section 4 applies inside the table. Use a comma or a period.
- Pricing cells carry the annual rate only, phrased "$40/month (billed annually)". See section 9c.

**Canonical row set for LinkedIn, cold email, and multichannel articles.** Fixed by Jaimin on 2026-08-13. Cover all fourteen. Do not invent new categories per article and do not quietly drop a row because a competitor looks bad in it.

1. Best for
2. Mailboxes and LinkedIn senders
3. AI personalization
4. LinkedIn actions
5. Multichannel (LinkedIn + email)
6. LinkedIn account safety
7. Unified reply inbox
8. Native integrations
9. Free Chrome Extension
10. AI SDR
11. MCP + CLI
12. Agency support
13. Free trial
14. Starting price

Two things that row set does deliberately. It opens on "Best for" rather than price, so the table reads as a routing aid instead of a price list. And rows 9 through 11 are where the Forge stack is structurally ahead, so they stay in even when a competitor column is a wall of "No".

Row swaps by routed product: for Leadsforge, replace rows 4 through 7 with "Database size", "Chat-based lead finder", "Company Lookalikes and Company Followers", and "Waterfall enrichment". For Warmforge, replace rows 4 through 7 with "Warmup pool quality", "Heat Score™ tracking", "Inbox placement tests", and "Health checks". For Mailforge, Infraforge, or Primeforge, replace rows 3 through 7 with "IP model", "Pre-warmed mailboxes", "DNS setup (SPF, DKIM, DMARC)", "Domain forwarding", and "Deliverability monitoring".

Check that the CSS block survived the paste into Webflow. Rich-text editors sometimes strip an inline `<style>`, and the table looks broken without it.

---

## 15. Headings `[LINT]`

- H2s are plain and searchable. "Salesforge pricing", not "What's the damage?"
- Match H2s to what people search or ask an LLM. A question as an H2 is fine when it reads naturally.
- One H1, the title. H2 for main sections. H3 for pricing and reviews inside a tool section. Never skip a level.
- No emojis, no drama colons.

---

## 16. SEO `[LINT]`

- Primary keyword in the title, the URL, the first 100 words, and at least one H2. Natural placement only.
- Title under 55 characters. Meta description under 155 characters, with the primary keyword and a clear hook.
- Minimum 5 internal links. TOFU posts link down to MOFU and BOFU. BOFU posts link to landing pages.
- Anchor text must already exist word for word in the draft. The destination must genuinely cover the anchor's topic. No "click here". No repeated anchor text.
- Comparison tables carry jumplinks to each tool's section.
- Answer the exact searched question early and directly.
- Article schema on every post. No FAQ schema: Google deprecated FAQ rich results in May 2026, so it earns nothing and adds markup risk.

---

## 17. LLM visibility `[JUDGE]` `[LINT]`

**Partly enforced since 2026-08-13.** `unscoped-comparison` counts "of the nine", "on this list" and scoped "here". A claim that means nothing lifted off the page cannot be quoted by an LLM or a snippet. Name the comparison set instead. The Expandi draft ran 32.

LLMs search the web and quote what they find. The goal is to be the source they quote.

1. **BOFU first.** Listicles, alternatives, and VS posts are what LLMs pull from when someone asks for the best tool in a category.
2. **Write value props as quotable lines.** LLMs lift exact wording, so every key claim should be one clear, self-contained sentence with a real number. "Unlimited mailboxes and LinkedIn senders with no seat-based pricing." "Mailboxes ready in 30 minutes."
3. **State who it's for and who it's not for.** See section 13.
4. **Cover use cases in detail.** An agency with 40 clients. A founder's first outbound campaign. An SDR team at 50,000 emails a month. Each scenario you describe is another conversation where an LLM can recommend us.
5. **Topic depth beats prompt-chasing.** Build coverage across the whole topic instead of one page per exact query.
6. **Snippet-ready blocks.** TL;DRs, tables, and direct-answer FAQs are what AI Overviews and Perplexity summarise. Front-load the answer.
7. **On-page tricks are the cherry, not the cake.** Skip llms.txt-style tactics. The honest, specific content does the work.

---

## 18. CTAs `[JUDGE]`

- CTAs enable action. They never push.
- Primary: free trial or signup. Say "no credit card required" when it is true.
- Secondary: book a demo, watch a demo, use the calculator.
- Placement: after pricing, after value is shown, and near the final verdict. Never in every section.
- No "best", "#1", or "guaranteed" inside CTA copy. No fake urgency.
- Working examples: "Start a free 14-day trial, no credit card needed." "Book a demo to see Agent Frank work a real lead list."

---

## 19. Competitors `[JUDGE]` `[HUMAN]`

- Neutral-positive, never dismissive. Trust converts better than bias.
- Every competitor mentioned gets at least one real strength.
- Match each competitor to the reader it suits.
- Only verifiable public limitations: pricing tiers, feature gaps, seat limits. Never invent a flaw.
- Our framing is "better fit for this specific reader", never "the best tool ever".
- **A Forge product does not get the #1 slot automatically.** It earns the top spot when it genuinely leads on the dimension the article is about, and the section says why. If a competitor honestly wins that dimension, put the competitor first and use the Forge product's section to name the reader who should still choose it.
- Legal and comparative claims about a named vendor are `[HUMAN]`. Flag them.

---

## 20. Naming `[LINT]`

Correct, always: Salesforge, Mailforge, Primeforge, Leadsforge, Infraforge, Warmforge, Agent Frank, Primebox™, Heat Score™, Bounce Shield, Megaforge, Auto-Pilot, Co-Pilot.

Never: SalesForge, Sales Forge, Frank AI, the Agent, AgentFrank, Autopilot, Copilot, Prime Inbox, bounce protection, or any invented abbreviation.

Collective term: "Forge stack".

**Never park "I" in a trailing clause after a superlative.** `[LINT]` Added 2026-08-19. "the widest I found", "the lowest rating I recorded", "the only published SLA I found", "no other tool I compared". Cap: two per article. **Checker added 2026-08-20** as `trailing-superlative-i`, after the rule sat unenforced through a full review cycle and fifteen instances shipped. The sentence-level shape that replaces it is in section 2.

This is a self-inflicted tic and worth understanding, because fixing one rule created it. Section 17 flagged 32 unscoped comparisons in the Expandi draft, things like "the widest here" and "the lowest of the nine", which do not survive being quoted off the page. The fix attributed them to the researcher instead. That satisfied section 17 and turned 18 of the draft's 32 first-person sentences into research footnotes. The approved article does it once in 21.

Both rules are satisfiable at once, by a third form: **name the number, not the comparison set and not the researcher.**

| | |
|---|---|
| Unscoped, fails section 17 | "Its LinkedIn campaign surface is the widest here." |
| Attributed, fails this rule | "Its LinkedIn campaign surface is the widest I found." |
| **Right** | **"It has eleven campaign types. Nothing else on this list has more than seven."** |

A count is quotable off the page, needs no narrator, and is checkable. Prefer it to both.

**Fixed feature names live in `rules/forge-positioning-guidelines.md`.** That file's do-not-paraphrase list is the authority: Bounce Shield, Primebox™, Heat Score™, "AI personalization across 21+ languages", waterfall enrichment, ESP matching. Always 21+, never 20+.

**The Primebox modes are Auto-Pilot and Co-Pilot.** Resolved by Jaimin on 2026-08-13, in favour of this section over the guidelines doc, which has been corrected in all nine places it wrote "Autopilot and Co-pilot". Enforced case-sensitively from `lint/data/spellings.txt`, because the fact and banned-phrase checks are both case-insensitive and neither can tell `Co-pilot` from `Co-Pilot`. Add any future spelling that differs only by case to that file rather than to `banned-phrases.txt`.

Agent Frank is he/him. You hire Agent Frank. You never buy him or activate him. He is an AI SDR, never a bot, an automation, or a workflow.

Competitors are spelled exactly as they spell themselves on their own site.

**Lowercase-branded names.** Some vendors style their name lowercase. Use their spelling in body prose, and capitalise only where the name opens a heading or a sentence. So "Lemlist charges per seat" at the start of a sentence, and "the thing lemlist does best" mid-sentence. Current lowercase brands: lemlist. The linter enforces this.

---

## 21. Before publishing

The linter runs items marked `[LINT]` and blocks on failure. Do not hand-check those. Read for the rest.

`[JUDGE]`

- [ ] At least 2 first-hand moments with specifics
- [ ] At least 1 real limitation of our own product
- [ ] Every competitor has a real strength
- [ ] A "Best for" line on every product section, and the reader who should walk away routed in the Final Verdict. No "Not for" labels anywhere. See section 13
- [ ] Every tool section opens on a plain explainer sentence saying what the tool is. See section 9b
- [ ] Every must-cover feature for the routed product appears somewhere. See `rules/forge-positioning-guidelines.md`
- [ ] Cross-product stories present: under one roof, and two ways to run it, three with partners
- [ ] Outcomes hedged as experience, product facts stated exactly
- [ ] Tool section openings vary after the explainer sentence. No two use the same entry angle
- [ ] "When [Competitor] is still the better choice" present in alternatives posts
- [ ] Paragraph rhythm mixes lengths

`[HUMAN]`

- [ ] Every `[[FIGURE:` placeholder replaced with a real number
- [ ] Every competitor price re-checked against the vendor's live pricing page today
- [ ] Every rating and review count re-checked live
- [ ] Any legal or comparative claim about a named vendor reviewed
- [ ] Byline set to Frank Sondors
