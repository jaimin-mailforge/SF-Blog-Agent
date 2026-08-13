# Research brief: expandi-alternatives

Drafting reads this file plus `rules/writing.md`, `rules/positioning.md`, and `rules/observations.md`. Nothing else.

**Status:** research in progress. Sections marked TBD are waiting on the three research pulls.

---

## Article

- **Type:** Alternatives listicle
- **Primary keyword:** expandi alternatives (US)
- **Working title:** 8 Best Expandi Alternatives for LinkedIn + Email (2026) — 54 chars
- **Target URL:** salesforge.ai/blog/expandi-alternatives — refresh of the existing page, pending the cannibalization check
- **Byline:** Frank Sondors

## Routing

Expandi is a LinkedIn automation tool, so this routes to **Salesforge**, positioned on the LinkedIn and multichannel angle per `rules/positioning.md`. Lead with multichannel conditional sequences and the six native LinkedIn actions, then the unified inbox, then the deliverability layer as the wedge. The competitors here are LinkedIn-first tools, so the strongest contrast is email and LinkedIn inside one branching sequence with replies from both channels landing in one place.

Salesforge does not get the top slot automatically. It earns it on this article's dimension, which is running both channels in one sequence without per-seat pricing. If the evidence says a competitor genuinely wins that, the competitor goes first.

## JTBD

TBD, to be written once the SERP and complaint evidence lands. Draft direction: "When my LinkedIn outreach is capped by seat pricing and my email lives in a separate tool, I want one platform that runs both channels in a single sequence, so I can scale outreach without doubling my bill or my tabs."

## Baseline: the current published article

Measured with `lint/publish-check.py` on 2026-08-13. This is the number the rewrite has to beat.

| Metric | Current |
|---|---|
| Errors | 8 |
| First-person-plural | 3, including the heading "How **We** Evaluated Each LinkedIn Automation Tool" |
| Banned words | seamlessly, robust x2, streamline |
| Fact conflicts | "withdraw requests" listed as a LinkedIn action |
| Warnings | 19 |
| Sentences over 25 words | 13 of 349 |
| Paragraphs over 3 sentences | 5 of 120 |
| Title / meta | 52 chars / **missing** |
| Blog interlinks | 6 |

Meta description is missing on the live page. Confirm in Webflow whether that is real or something the extractor cannot see.

## Approved structure

Approved 2026-08-13, with four amendments agreed the same day.

1. Introduction
2. TL;DR: 8 Expandi Alternatives
3. Why People Leave Expandi
   1. Per-Seat Pricing That Doubles With Add-Ons
   2. Account Restrictions Even Inside "Safe" Limits
   3. LinkedIn-First, Email Bolted On
   4. Billing Disputes and Refund Refusals
4. How I Evaluated These Expandi Alternatives
5. Feature Comparison: Top 5 Expandi Alternatives (HTML template, 6 columns: Salesforge plus 4)
6. Salesforge
7. HeyReach
8. Dripify
9. Meet Alfred
10. Waalaxy
11. La Growth Machine
12. lemlist
13. Snov.io
14. **When Expandi Is Still the Better Choice** (added)
15. Final Verdict: Which Expandi Alternative is Best?
16. FAQs

### Per-tool section shape

Every tool section runs in this order:

1. `**Best for:** [specific buyer] [specific use case] [specific constraint]` (added)
2. `**G2 Rating:** X.X out of 5 (N,NNN reviews)` (added)
3. Narrative intro, 2 to 4 paragraphs, distinct opening angle per tool
4. Key features, bold-label bullets
5. Pros and cons, table, rows reflect reality and are not padded to match
6. Pricing, table, both billing cycles
7. What real users say

**Who it's not for is optional per tool** as of the rule change on 2026-08-13. It is carried at article level by the Final Verdict and by section 14. Write the per-tool line only where a tool has a sharp disqualifier worth naming.

### Opening angles, one per tool

No two tool sections may open the same way. Assigned entry points, to be confirmed against the evidence:

| Tool | Entry angle |
|---|---|
| Salesforge | Feature architecture, two channels in one branching sequence |
| HeyReach | Who it is built for, agencies running many LinkedIn seats |
| Dripify | Pricing math |
| Meet Alfred | Community sentiment |
| Waalaxy | Positioning observation, the freemium on-ramp |
| La Growth Machine | A specific workflow it does that others cannot |
| lemlist | What its reply rate depends on |
| Snov.io | Cost at low volume |

## Chunk plan

Approved: 7 chunks, two tools per chunk.

| Chunk | Sections |
|---|---|
| 1 | Introduction, TL;DR, Why People Leave Expandi (4 sub-sections) |
| 2 | How I Evaluated, Feature Comparison table |
| 3 | Salesforge, HeyReach |
| 4 | Dripify, Meet Alfred |
| 5 | Waalaxy, La Growth Machine |
| 6 | lemlist, Snov.io |
| 7 | When Expandi Is Still the Better Choice, Final Verdict, FAQs |

## Observations available

From `rules/observations.md`. These are the only first-person specifics with numbers that may appear in this draft.

- **OBS-001** Connected 22 mailboxes to one Salesforge account, bill did not change for adding them. Directly usable, since per-seat pricing is this article's core argument.
- **OBS-004** Eight tools tested over 90 days with matched lists, sequences and mailboxes. The methodology basis, but it belongs to the cold email test and covers a different tool set. **Do not attach the 90 days or the eight tools to this article.** The How I Evaluated section needs its own criteria, written as criteria rather than as a claimed test period.

Nothing in the log covers LinkedIn accept rates, message reply rates, or any of these eight tools by name. So per-tool first-person specifics are not available. Use category-general framing, cited sources, or broad tenure claims in those sections.

## SERP context

TBD.

## Competitor teardown, top 3

TBD.

## Keyword gap

TBD.

## Evidence per tool

TBD. Pricing on both cycles with source URL and date, ratings with counts, two or three recurring complaint themes with a count of how many users raised each, genuine strengths, and channel architecture.

## Why People Leave Expandi: claim status

Each of the four sub-sections needs real support or it gets cut. Ratings pending.

| Claim | Support | Decision |
|---|---|---|
| Per-seat pricing doubles with add-ons | TBD | |
| Account restrictions inside safe limits | TBD | |
| LinkedIn-first, email bolted on | TBD | |
| Billing disputes and refund refusals | TBD | |

A thinly supported ban or refund claim about a named competitor is the riskiest sentence in this article. Cut rather than soften.

## Internal links

TBD. Target 5 or more blog-to-blog links, anchors that already exist word for word in the draft, no duplicate anchor text.
