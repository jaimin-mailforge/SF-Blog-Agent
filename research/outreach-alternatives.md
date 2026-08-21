# Research brief: outreach-alternatives

**Status: partial.** Keyword data, SERP and the Outreach pricing check are done and dated.
Everything under "Open, blocking" is unresolved and the article cannot be drafted past the
introduction until it is. Started 2026-08-21.

## Article

Target primary keyword: **outreach alternatives**. Competitor is Outreach.io, a sales
engagement platform.

**This is a rewrite, not a new article.** `salesforge.ai/blog/outreach-alternatives`
already sits in the position-1 block for the primary keyword. Current title tag is
"10 Best Outreach Alternatives in 2026 (Tested & Ranked)". Jaimin's new intro copy
shortlists **eight** tools against the live page's ten, so the tool list is changing and
the title has to change with it.

Handle accordingly. Rewriting a page that already ranks first is a different risk profile
from writing a new one, and nothing here should drop a term the page already earns.

## Keyword data

Ahrefs pulled 2026-08-21, US.

| Keyword | US volume | KD | CPC |
|---|---|---|---|
| outreach alternatives (primary) | 600 | 1 | $30.00 |

Global volume 800. Parent topic is the keyword itself.

**Four times the Expandi keyword's volume at a $30 CPC.** Difficulty 1. This is a
higher-value page than the Expandi one and it is already won, so the rewrite is
defending a position rather than chasing one.

## SERP context

`serp-overview` pulled 2026-08-21, US, top 15.

| Position | Who | DR | Traffic |
|---|---|---|---|
| 1 block | **salesforge.ai/blog/outreach-alternatives**, salesforce.com, klenty.com | | |
| 2 | reddit.com/r/sales, "Looking for Outreach.io alternatives" | 95 | 389 |
| 3 | g2.com Outreach alternatives | 91 | 178 |
| 4 | People Also Ask block | | |
| 5 | salesforce.com/compare/outreach-competitors | 92 | 19 |
| 6 | amplemarket.com/competitors/outreach | 65 | 83 |
| 7 | artisan.co/blog/outreach-io-alternatives | 75 | 109 |
| 8 | **crono.one, "5 Outreach Alternatives Under $100"** | 48 | 63 |
| 9 | listkit.io, "We Reviewed 8 Outreach.io Alternatives" | 55 | 126 |
| 10 | fundraiseinsider.com | 32 | 52 |
| 11 | gartner.com Outreach Agentic AI Platform alternatives | 92 | 44 |
| 12 | revenue.io | 72 | 42 |
| 13 | emailtooltester.com, "7 Best Email Outreach Tools" | 79 | 3,784 |
| 14 | expandi.io/blog/outreach-competitors | 72 | 13 |
| 15 | youtube.com, "Outreach.io Review: Are There Better Alternatives?" | 99 | 9 |

**Three things the SERP says about intent.**

1. **Price sensitivity is explicit.** Crono ranks eighth with a title that is literally a
   price ceiling, "5 Outreach Alternatives Under $100". Jaimin's intro instinct to contrast
   Outreach's hidden quote against published prices is reading the SERP correctly.
2. **Partly a review query, like the Expandi keyword.** A YouTube review ranks 15th and
   Gartner's alternatives page ranks 11th, so the page has to evaluate Outreach and not
   only list replacements.
3. **Slot compression.** Reddit at 2 with 389 traffic, G2 at 3, a PAA block at 4 and
   Gartner at 11 are all unwinnable with content. Realistic contest is the position-1
   block plus 5 to 9.

**The four live PAA questions**, which the FAQ should answer directly:
What are the top 5 email marketing platforms? Is outreach better than SalesLoft?
Is outreach considered a CRM? What is the best outreach method?

Note the second and third. "Is Outreach a CRM" is a real confusion in this audience and
worth a direct answer.

## Evidence: Outreach

**Pricing**, outreach.io/pricing, read 2026-08-21. **Outreach publishes no figure.** The
served page carries zero dollar amounts, says "custom pricing" three times, "request a
demo" twice, and "per user" once. Verified by fetch, 243,665 bytes, http 200. No currency
symbol appears anywhere on it.

This is the strongest verified fact available for the intro and it needs no screenshot,
because the absence of a number is the finding.

**Audit of the current published page**, `python3 lint/run.py <url>`, 2026-08-21:
40 errors, 18 warnings against the current rulebook. Worst clusters are brand-casing on
lemlist (10), en dashes (8), sentence fragments (8), em dashes (5), paragraphs over 60
words (5), TL;DR shape (4), and "best-in-class" (4). Also one `fact:Billed quarterly`,
which is the annual-format rule, and `too-few-long`, so the prose is compressed into the
middle. Rhythm reads stdev 7.34 with 42.1% of sentences at six words or fewer, which is
the opposite failure from the Expandi draft: this page is choppy, not flat.

## Open, blocking

Nothing below can be resolved from a public page and each one blocks a specific sentence.

1. **The screening count.** Jaimin's copy says "I tested 15+ outreach alternatives".
   `rules/observations.md` has no entry for an Outreach test, so section 7 blocks the
   claim. Also note the verb: the Expandi article uses "screened" rather than "tested"
   because no 90-day test was run, and OBS-005 records that constraint. Needs the real
   number, and needs deciding whether a hands-on test actually happened.
2. **The entry-price range.** The copy says tools start "between $32.50 and $63 a month
   (billed annually)". No vendor page has been read for this article and the eight tools
   are not chosen yet, so there is no provenance for either end of that range. Both
   figures need a live pricing page and a read date before they can appear.
3. **The Capterra support score.** The copy says "Support gets the lowest score on
   Outreach's Capterra page". Capterra returns 403 to automated access, same as G2, so
   this needs Jaimin's screenshot with the dimension scores visible.
4. **The contract terms.** The copy says you "sign a twelve-month contract that renews on
   its own". Neither "12-month" nor "annual" appears anywhere on outreach.io/pricing, so
   this needs a source, most likely the MSA or order form rather than the marketing site.
5. **The three product absences.** "No warm-up underneath, no placement testing, LinkedIn
   as a manual task list." Consistent with what Outreach is, and asserted by Jaimin who
   knows the product, but not yet sourced to an Outreach page or doc. Confirm before the
   draft states them.
6. **The tool list.** Eight tools, not chosen. Playbook routing needs deciding too: this
   is a sales-engagement competitor rather than a pure cold email tool, so whether it
   takes Playbook 1 (cold email alternatives, Salesforge Cold Email, 16 must-covers) or
   the multichannel section (17 must-covers) is a real decision, not a default.

## Not blocking, worth knowing

- Klenty ranks in the position-1 block with its own Outreach alternatives page, and
  Klenty is already in `lint/data/product-names.txt`, so it has appeared in our content
  before.
- `emailtooltester.com` at 13 pulls 3,784 traffic against everyone else's double digits.
  It ranks for 118 keywords on that URL, so it is winning a much broader head term and is
  not really competing for this one.
