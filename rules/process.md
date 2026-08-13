# Production Process

How an article gets made. Voice and structure live in `rules/writing.md`. Product facts live in `rules/positioning.md`.

## The one principle that holds this together

**Research writes a brief. Drafting reads only the brief.**

Steps 1 through 6 produce `research/<slug>.md`. Step 7 drafts from that brief plus the two rules files, one section per turn, in a fresh context each time. Nothing else carries over.

This matters because voice collapses when a single conversation accumulates research notes, competitor teardowns, keyword tables, and eight sections of prose. Section nine gets written by a context full of SERP data. A short turn reading a tight brief does not have that problem.

If the brief is missing something, fix the brief. Do not paste extra context into the drafting turn.

---

## Step 1: Read the existing article

Only when rewriting.

Fetch the full current article. Classify the type: listicle, alternatives, VS, or review. Then report what is weak before touching anything: structure, intro, voice, thin sections, missing features, stale pricing, meta length, keyword use.

Report first. Do not start fixing.

---

## Step 2: Rankings and cannibalization

Pull from Ahrefs:

- Current ranking position for the target keyword, US organic. If Ahrefs returns nothing because the page sits past position 20 or is untracked, note it and move on. Do not guess a position.
- The full SERP for the keyword, top 15, with DR, referring domains, and traffic per result.
- Volume, difficulty, and CPC for the primary keyword and 8 to 10 variants.

Then the **cannibalization check**, before any competitor work. Search salesforge.ai/blog and the mailforge, primeforge, warmforge, and leadsforge blogs for the primary keyword and its closest variants.

If a competing article already exists, decide which of two things this is, and write the decision into the brief:

- **Refresh.** It replaces the existing article. The brief carries the redirect plan and what the new version does better.
- **Complement.** It targets a different sub-intent. The brief names the specific intent split and the internal links between the two.

If there is no honest intent split, do not write a new article. Refresh the old one instead.

---

## Step 3: Competitor teardown

Fetch the top 3 ranking pages. For each: what sections and angles they cover that we do not, what their title and meta look like, and where the real quality gap is.

Then a plain diagnosis: why each one outranks us, and what would beat it. Separate what we control, which is content, from what we do not, which is links. Say which is which. A link gap is not a content problem and pretending otherwise wastes a rewrite.

---

## Step 4: Evidence pull

This step exists because `rules/writing.md` bans invented complaints and requires real ratings, and nothing else in the process gathers that material. Skip it and the writer either fabricates or goes vague.

For every tool the article covers, collect into the brief:

- **Pricing from the vendor's live pricing page only.** Both billing cycles where the page exposes both. Record the URL and the date. Never take a price from G2, Capterra, TrustRadius, a listicle, Reddit, an AI summary, or one of our own older articles. Check the JavaScript price constants if the toggle is client-side, because the rendered page shows only one cycle.
- **Rating and review count**, verified live, per platform.
- **Two or three real complaint themes**, drawn from G2 reviews at 3 stars and below, Trustpilot or Capterra where the score diverges from G2, and Reddit threads. A theme counts only when several users raise it. One angry review is not a theme.
- **Quotes**, if the article uses them. Verbatim, with the reviewer name, role, star rating, date, and a link to the individual review. A quote missing any of those is unusable, so do not carry it into the brief.

Also re-check the Forge figures in `rules/positioning.md` against the live pages if the last verification date there is more than 30 days old. Stale internal facts have caused more errors than anything else.

---

## Step 5: Keyword gap

Build the gap list from the Ahrefs variants and the competitor teardown: covered, partly covered, missing. Flag the missing terms that appear in top-3 pages and carry real volume.

No third-party term tool is in this process. The Ahrefs variants plus the competitor teardown give you the gap list, and that is enough. Chasing a term-frequency score means writing to the same template as the pages already ranking, which is the opposite of what we want.

---

## Step 6: Outline approval, hard stop

**Do not draft a single section before the outline is approved.**

Present:

1. **Type and routed product.** Listicle, alternatives, VS, or review. Which Forge product, and why. If routing could honestly go two ways, say so and recommend one.
2. **JTBD.** One statement: "When [situation], I want to [motivation], so I can [outcome]." One per article. The intro angle maps to the situation and the outcome.
3. **SERP context.** Primary keyword with volume and difficulty, current rank, the top 3 to beat, and the angle they are all missing.
4. **Section flow** as a numbered list, with a line of rationale each.
5. **Three titles** under 55 characters, three different angles. Include the character count on each.
6. **Meta description** under 155 characters, with the count.
7. **What I actually tested.** Two or three real observations Jaimin can stand behind: timings, costs, what broke, what surprised him. `rules/writing.md` requires first-hand moments and forbids inventing them, so this is where the real ones come from. **If there are none for this article, say so in the outline.** The draft then uses hedged category-general framing instead of first-person specifics, and nobody has to invent a Tuesday afternoon that never happened.
8. **Chunk plan.** Which sections get drafted in which turn.
9. **Flagged decisions.** Anything ambiguous: routing, tool inclusion, structure changes, unresolved facts from `rules/positioning.md`.

A single word approves and advances. Any structural edit resets: apply it, re-present the affected part, wait again.

Mid-draft, three things send you back here: a fact that changes the routing, a competitor structure that is clearly better than the approved flow, or an intro angle that will not land. Stop and ask. Do not quietly rewrite the plan.

---

## Step 7: Draft

One section per turn, in a fresh context, reading `research/<slug>.md` plus the two rules files. Follow the approved chunk plan.

Transitions between chunks are practitioner voice. The last thought in one tool section threads into the next one by contrast or by a shared theme. Never "Next up" or "In the following section", which read as machine-written and are banned narrator framings.

Any figure you do not have goes in as `[[FIGURE: what it is]]`. Do not estimate, and do not quietly drop the sentence.

---

## Step 8: Lint and repair

Run the linter. It checks everything tagged `[LINT]` in `rules/writing.md` and blocks on failure.

Then repair in a loop: the linter names the violation and its location, you fix that specific thing, run it again. Repeat until clean. This works because fixing a named violation at a named location is easy and finding your own violations is not.

Do not hand-check anything the linter covers. Read for the `[JUDGE]` items instead, which is voice, real first-hand moments, competitor fairness, and whether every product section says who it is not for.

---

## Step 9: Publish gate

Jaimin's checks, and none of them are delegable:

- Every `[[FIGURE:` placeholder replaced with a real number
- Every competitor price re-checked against the live vendor page today
- Every rating and review count re-checked live
- Every quote confirmed to exist at its permalink, said by that person
- Any legal or comparative claim about a named vendor reviewed
- Byline set to Frank Sondors

Then paste into Webflow, confirm the comparison table CSS survived the paste, and publish.

---

## After publishing

Update the verification date on any figure in `rules/positioning.md` that was re-checked.

At 30 and 60 days, check position movement for the primary keyword and two or three variants. If the article has not moved into the top 10 despite passing everything, the diagnosis is one of four things: content depth, a link gap, a freshness signal, or SERP volatility. Name which one before acting.

Freshness upkeep: refresh the year in the title within the first two weeks of January, keep a visible "Updated" date, re-verify pricing and ratings at 6 months, and refresh immediately when a competitor changes pricing or ships or kills a feature the article describes.

---

## What is deliberately not in this process

- **A 13-pass self-review.** The mechanical passes are the linter. The judgment passes are step 8's read. Asking a model to audit its own draft against a long checklist in the same context does not work, and explicit self-verification instructions make current models over-verify without improving quality.
- **A NOTES companion file.** It existed to hand work to a second person. Only Jaimin operates this, so the pre-publish list lives in step 9.
- **A separate project-state file.** Article state lives in git. Facts live in `rules/positioning.md` with verification dates.
- **Rule changes as a response to one bad article.** One bad article is a bug in that article. A pattern across five is a rule change, and a rule change means adding, editing, or deleting a tagged rule and saying why in the commit.
