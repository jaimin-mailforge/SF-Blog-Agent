---
name: new-article
description: Start a new Forge blog article from a target keyword. Runs keyword and SERP research, picks the article-type playbook, verifies every competitor price on the live vendor page, writes the research brief, then stops for outline approval. Use when the user gives a target keyword, or a keyword plus an existing first draft.
---

# New article from a target keyword

Argument: the target primary keyword. Optionally a path to an existing first draft,
in which case treat that draft as raw material for step 5 and nothing more. Its
prose has not passed any rule in this repo.

Read `rules/process.md` first. This skill is steps 1 to 6 of it. Do not draft
prose in this skill. The hard stop at the end is the point.

## 1. Fix the slug and check for cannibalization

Slug is the keyword, hyphenated. Check `drafts/` and `articles/` for anything close,
and search the live blog before assuming the page is new:

    python3 lint/run.py --quiet
    curl -sS "https://www.salesforge.ai/blog/<slug>" -o /dev/null -w '%{http_code}\n'

A 200 means this is a rewrite, not a new article. Switch to the `rewrite-article`
skill and say so.

## 2. Keyword data

Use the Ahrefs MCP tools, not a guess:

- `keywords-explorer-overview` for volume and difficulty on the primary
- `keywords-explorer-related-terms` and `keywords-explorer-search-suggestions` for
  the secondary set and the PAA questions
- `serp-overview` for who ranks and what the SERP shape is

Record the numbers with the date. If Ahrefs is unavailable, say so in the brief
rather than substituting an estimate.

## 3. Read the SERP, do not skim it

Fetch the top 10 and lint them, which tells you what the competition actually is
and what our own rules would say about it:

    python3 lint/run.py <competitor-url>

For each of the top 5, record: what it covers, what every one of them covers (table
stakes), and what none of them do (the angle). The angle is the thing none of them
did. Do not claim our research beats what ranks without having looked.

## 4. Pick the playbook and the must-covers

`rules/forge-positioning-guidelines.md` has the routing table under
"Playbook quick reference table". Match the article type to it, then note the exact
must-cover count for the product section it names:

    python3 lint/coverage.py --list

The count is binding. The guidelines say "Not most. All." One key-feature bullet per
must-cover, and the count has to match. This is where the Expandi draft went wrong
twice, first bundling three must-covers into one bullet and then shipping 11 against 12.

## 5. Verify every price on the live vendor page

Never from G2, Capterra, a listicle, Reddit, an AI summary, or one of our own older
articles. For each vendor, probe the live page and record what it serves:

    python3 lint/prices.py --url https://<vendor>/pricing

Write the provenance into the brief in the format the verifier reads:

    **Pricing**, vendor.com/pricing, read YYYY-MM-DD. Plan **$X per seat annual**.

Always include the read date. Omitting it is how Waalaxy's price went unverified.

**Stop and ask when the page and your reading disagree, when more than one currency
is served, or when no figure appears in the HTML at all.** A JS-rendered or
geolocated pricing page needs a human screenshot. Do not pick a number to move on,
and do not convert between currencies.

Every price is the annual rate, phrased "$X/month billed annually".

## 6. First-person claims

Read `rules/observations.md`. Every first-person claim carrying a number, a timing
or a personal measurement must trace to a logged entry. Count what the log can
actually fund before promising two or three first-hand moments in the outline.

If the log cannot fund them, say so in the brief as a known shortfall with the
category-general fallback named. Do not manufacture a detail to fit the voice.

## 7. Write the brief

Write to `research/<slug>.md`. Model it on `research/expandi-alternatives.md`, which
has the section shape that worked. It must carry: the keyword data with dates, the
SERP teardown, the angle, the playbook and its must-cover count, per-vendor evidence
with price provenance and read dates, the observation-log inventory, the approved
structure, and every open question as a flagged decision rather than a silent choice.

Then verify the brief against itself:

    python3 lint/prices.py research/<slug>.md

## 8. Hard stop

Present the outline: H2 and H3 list, the tool order with the reason a competitor
goes first if one does, the angle, the must-cover count, and the flagged decisions.

**Do not draft a section before the outline is approved.** A single word approves it.
Then drafting happens one section per turn, reading only the brief plus the rules
files, per `rules/process.md`.
