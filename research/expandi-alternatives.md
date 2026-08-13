# Research brief: expandi-alternatives

Drafting reads this file plus `rules/writing.md`, `rules/positioning.md`, and `rules/observations.md`. Nothing else.

**Status:** SERP, teardown and cannibalization complete. Per-tool evidence still pending.

---

## Article

- **Type:** Alternatives listicle
- **Primary keyword:** expandi alternatives (US)
- **Working title:** 8 Best Expandi Alternatives for LinkedIn + Email (2026), 54 chars
- **Target URL:** salesforge.ai/blog/expandi-alternatives. Refresh of the existing page, pending the cannibalization check
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
| Banned words | `seamlessly`, `robust` x2, `streamline` |
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

Ahrefs pulled 2026-08-13. SERP snapshot dated 2026-08-06.

| Keyword | US volume | KD |
|---|---|---|
| expandi alternatives (primary) | 150 | 0 |
| expandi pricing | 150 | 3 |
| expandi alternative | 100 | no data |
| expandi vs heyreach | 100 | no data |
| expandi io | 90 | 4 |
| expandi vs dripify | 70 | no data |
| expandi review | 60 | no data |

Addressable set is roughly 500 searches a month. **Noise, do not build sections for these:** expandi competitors (0 US volume), expandi alternatives 2026 (10), expandi vs lemlist (10). Ahrefs holds no record at all for "best expandi alternatives", "alternatives to expandi", or "expandi io alternatives".

**Honest ceiling.** This is a low-volume, high-intent, brand-modified SERP. The number one result is credited with 16 estimated monthly visits. Win it for conversion, not for traffic. Do not let anyone judge this rewrite on sessions.

**Current rank.** Two Ahrefs endpoints disagree and both are recorded rather than reconciled by assumption. `serp-overview` puts the page at **position 9** with URL rating 4, 12 referring domains, 276 backlinks. `site-explorer-organic-keywords` in exact mode returned zero rows across four attempts, so Ahrefs attributes no ranking keyword and no traffic to the URL. Position 9 is the only figure that exists. Current title tag is "7 Best Expandi Alternatives I Actually Tested (2026)".

**No link gap. This is winnable on content.** Keyword difficulty is 0. The number one page has **one referring domain** and a URL rating of 4. Positions 5, 8, 10, 11, 12, 14, 17, 18 and 19 have **zero** referring domains. Our page already carries more page-level link equity than both number one and number three. Domain rating is not the sort key either: DR 32 ranks tenth, DR 4 ranks twelfth, while DR 78 sits at eighteen. No link campaign is required.

**Two real constraints, both content-side.**

1. **Slot compression.** A Reddit cluster occupies position 4 with three sitelinks, and a People Also Ask block takes position 7. Content cannot win those. Realistically this page competes for positions 1 to 3 and 5 to 6.
2. **Intent blending.** HeyReach ranks third with an Expandi *review* page, and expandi.io's own blog ranks thirteenth. Google reads this keyword as partly a review query. **So the winning page has to carry a real evaluation of Expandi itself, not only a list of eight other tools.** That is why the Why People Leave section and the When Expandi Is Still the Better Choice section carry more weight here than they would on a normal listicle.

**The four live PAA questions**, which the FAQ section should answer directly: How much does Expandi cost? What is the difference between Skylead and Expandi? What is the difference between Meet Alfred and Expandi? Is expandi.io good?

## Competitor teardown, top 3

| | artisan.co (#1) | salesrobot.co (#2) | heyreach.io (#3) |
|---|---|---|---|
| Words | ~1,940 | ~5,160 | ~2,330 |
| Tools | 7, padded with ZoomInfo and Apollo, which are not LinkedIn automation tools | 4 | 1 real, 7 named in a bare list |
| Type | Alternatives | Alternatives | **Review** |
| First-party screenshots | No, vendor homepage grabs | Yes, around 40 | Yes, 12 genuine Expandi UI captures, **all with empty alt text** |
| Named-reviewer quotes | No, aggregate only | One | No, aggregate only |
| Both billing cycles | No | For the alternatives, not for Expandi | No |
| Stated methodology | No | Yes, a named 6-factor rubric | No |
| Last modified | **2025-05-23, 15 months stale** | 2026-04-23 | 2026-06-25 |

**What all three share.** Expandi priced at exactly one number, $99 a month, with no annual cycle anywhere. A self-serving top slot in every case, so no page lets a competitor win on merit. The same three complaints about Expandi, which are account bans, price, and complexity, every one sourced from aggregate ratings rather than a named user. And not one of them states who a tool is **not** for.

Number two also gets a fact wrong that we can correct: it calls Expandi "a single-tier pricing plan, one plan only", which the live pricing page contradicts.

## The angle: price what people actually buy, at the seat count they buy it at

Verified on live vendor pages 2026-08-13. Nobody in the top 20 has done this arithmetic.

- **Expandi Business:** $99 per seat per month on monthly billing, **$79 per seat per month on annual**, marketed as two months free. The pricing page carries a Monthly and Annually toggle at 20% off.
- **Image and GIF personalization**, the feature all three top pages cite as Expandi's selling point, **is not included.** It runs through Hyperise, whose cheapest paid tier is **$69 per seat per month** for 5,000 image views and up to 5 active images. Video personalization needs Hyperise's $149 tier or a separate Senspark integration.
- **So the configuration people are actually comparing against costs $168 per seat per month** on monthly billing, or $148 with Expandi annual and Hyperise monthly.
- **Scaled to five seats:** $495 a month for Expandi alone on monthly billing, $395 on annual, and $840 with Hyperise on all five seats. Still below the 10-seat threshold where Expandi's Agency tier and its unpublished volume discount begin.
- The Agency tier starts at "+10 Seats" behind a Talk To Sales wall. **The three-to-five-seat agency, the most common buyer in this category, has no published price anywhere on this SERP.**

Secondary lever: the number one result was last modified 2025-05-23 and pads its list with two data platforms that do not do LinkedIn automation. A page that is correct, current, and priced beats it without a single new backlink.

## Keyword gap

Covered by the current page: the tool list, per-tool features, Expandi at both billing cycles, a methodology section.

Missing and worth adding: the add-on arithmetic above, a three-to-five-seat cost table, who each tool is not for, direct answers to the four PAA questions, and first-party Expandi UI screenshots with real alt text.

**Do not chase:** linkedin automation tools (1300), linkedin automation software (300), linkedin outreach tools (200). See the boundary note below.

## Cannibalization

**Straight refresh of the existing URL.** No sibling page targets "expandi alternatives" or a close variant. Mailforge, Primeforge, Warmforge and Leadsforge have zero Expandi pages between them.

Three things to carry forward:

1. **A hard boundary with `/blog/linkedin-automation-tools`.** That page ranks **number one in the US** for linkedin automation tools (1300), linkedin automation tool (500), linkedin automation (900), best linkedin automation tools (250) and linkedin automation platform (150). This rewrite stays on brand-modified intent and **internal-links up to that page.** Chasing category head terms from here would put two Salesforge URLs into a SERP the site already owns.
2. **Real duplication elsewhere in the Expandi cluster**, though not on this keyword: `/blog/heyreach-vs-expandi` against `/comparison/heyreach-vs-expandi`, and `/blog/expandi-vs-dripify` against `/comparison/expandi-vs-dripify`. Two URLs each chasing one head-to-head query, which is why expandi vs heyreach (100) and expandi vs dripify (70) earn nothing. Separate consolidation job, not a blocker here.
3. **Two technical defects on the target URL**, worth fixing in the same pass. The page emits **two conflicting canonical tags**, one www and one non-www, so Google picks arbitrarily. And its JSON-LD dates are invalid: `"datePublished": "May 20, 2026T00:00:00Z"` is not ISO-8601 and will not parse, which means the page has never signalled an update.

## Tool list change from the current page

The live page covers seven tools: Salesforge, HeyReach, Skylead, La Growth Machine, lemlist, Dripify, Meet Alfred. The approved outline covers eight. **Skylead is dropped, Waalaxy and Snov.io are added.** Note that one of the four live PAA questions asks about the difference between Skylead and Expandi, so dropping Skylead entirely leaves that question unanswered. Options: answer it in the FAQ without giving Skylead a section, or reinstate Skylead. Flagged for a decision.

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
