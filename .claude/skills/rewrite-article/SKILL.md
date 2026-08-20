---
name: rewrite-article
description: Rewrite an existing published article from its URL. Audits the live page against every current rule, diffs its coverage against the positioning must-covers, re-verifies every price it states, then writes a rewrite brief and stops for outline approval. Use when the user gives a blog URL to rewrite or refresh.
---

# Rewrite an existing article from its URL

Argument: the live URL. Everything starts from what the page actually says today,
not from what we remember writing.

Read `rules/process.md`. This skill replaces steps 1 to 6 for an article that
already exists. Do not draft prose here.

## 1. Audit the live page

One command gives the full style audit, because the linter already takes a URL:

    python3 lint/run.py <url>

Expect a lot on any older page, and expect most of it to be real. The rules tightened
after those pages shipped: semicolons, em dashes, en dashes and verbless fragments are
all banned now and were not linted then. Even the editor-approved RocketReach article
returns 27 errors against the current rulebook.

Sort the findings into three buckets before writing anything:

- **Mechanical.** Punctuation, we/our/us, brand casing, banned words. Fix in a pass.
- **Structural.** Missing TL;DR shape, no "Best for" line, missing comparison table,
  ratings sections too long, interlinks under five.
- **Judgment.** Frame restarts, trailing-superlative "I", flat rhythm, sections with
  no argument. These need the `polish-draft` skill after the rewrite, not before.

## 2. Diff the coverage

Save the extracted text and check it against the positioning must-covers:

    python3 lint/run.py <url> > /tmp/audit.txt
    python3 lint/coverage.py <path-to-local-copy>.md --section "<Product: Variant>"

`python3 lint/coverage.py --list` gives the section names and counts. An "ELSEWHERE
ONLY" result means the feature appears on the page but not in the Forge product
section, which is the bundling failure, not coverage.

## 3. Re-verify every price the page states

This is the step that matters most on a rewrite, because a published price goes stale
silently and the page keeps ranking while it is wrong.

Pull every figure the live page states, then probe each vendor's current page:

    python3 lint/prices.py --url https://<vendor>/pricing

For each one, decide and record: unchanged, changed, or unverifiable. A changed price
is the strongest reason the rewrite exists and belongs in the brief's angle.

**Stop and ask** on a multi-currency page, a JS-rendered page with no figures, or a
disagreement between the vendor's pricing page and its help centre. lemlist's
100,000-email tier reads $80 on one and $71 on the other, and that is not a bot's
call to make.

Every price becomes the annual rate, phrased "$X/month billed annually", even if the
old page carried monthly or quarterly columns.

## 4. Check what changed in the market

The rewrite has to earn its refresh. Use Ahrefs `serp-overview` on the primary
keyword and compare against who ranked when the page was written. Note new entrants,
tools that shut down, and tools that changed their billing unit. Then
`gsc-page-history` or `site-explorer-organic-keywords` for what the page currently
ranks for, so the rewrite does not drop a term that is already earning.

## 5. Decide what survives

List explicitly, in the brief:

- Sections to keep as-is
- Sections to rewrite
- Sections to cut, with the reason
- Tools to add or drop from the list, with the reason
- Interlinks to add, minimum five to other blog posts

A Forge product does not keep the top slot because it had it. It earns it on the
dimension this article is about, or a competitor goes first.

## 6. Write the rewrite brief

Write to `research/<slug>.md`. Same shape as a new-article brief, plus two sections
a rewrite needs and a new article does not:

- **Baseline: the current published article.** The audit buckets, with counts.
- **What changed since it published.** Prices, tools, SERP, and the ranking data.

Then check the brief's own provenance:

    python3 lint/prices.py research/<slug>.md

## 7. Hard stop

Present the outline plus the survive/rewrite/cut list and the flagged decisions.

**Do not draft a section before the outline is approved.** After approval, draft one
section per turn from the brief plus the rules files. When the draft is complete, run
the `polish-draft` skill for the continuity and voice pass, then
`python3 lint/run.py drafts/<slug>.md` must be clean before it goes anywhere.
