# Research brief: dripify-alternatives

**Status: complete through step 5. Stopped for outline approval.** Audit, coverage diff,
keyword and SERP data, and the price pass are all done and dated 2026-08-24. Two vendor
prices need a human look and are listed under "Open, blocking".

## Read this first: the prioritisation flag

This is the lowest-value keyword of the three articles now in flight, by a wide margin,
and the page currently earns nothing.

| Keyword | US volume | KD | CPC | Our position |
|---|---|---|---|---|
| outreach alternatives | 600 | 1 | **$30.00** | **position-1 block** |
| expandi alternatives | 150 | 0 | not pulled | 9 |
| **dripify alternatives** | **40** | **0** | **$3.50** | **absent from the top 12** |

One fifteenth the volume of the Outreach keyword and roughly a ninth the CPC. Ahrefs
attributes no ranking keyword and no traffic to this URL, and it does not appear in the
top 12 for its own primary term.

**So there is a real decision before the outline: is this the right article to spend a
rewrite on, when `outreach-alternatives` is 600 volume at $30 CPC, already holds the
position-1 block, and has a partial brief waiting on four items?** Flagged rather than
decided, because it is Jaimin's call. Two honest arguments for doing it anyway are below.

**Argument for doing it regardless.** The page states nine instances of wrong facts about
our own products, and that is a correctness problem independent of traffic. A page nobody
finds is still a page that says Salesforge does 20+ languages and integrates natively with
Pipedrive. Both are wrong.

**Argument for doing it cheaply.** A mechanical-only pass would clear 48 errors and all
nine fact errors in one sitting, with no research, no new tools, and no outline. If the
answer to the prioritisation question is "not now", that is the version to run.

## Decisions resolved 2026-08-24 by Jaimin

1. **Full rewrite**, not a mechanical pass, and not deferred behind Outreach. The
   40-volume prioritisation flag above was read and overridden deliberately.
2. **Skylead keeps a full tool section**, overriding the 2026-08-13 resolution that made
   it FAQ-only on the Expandi article, on condition that it gets verified. What that
   verification actually returned is below, and it is only partly good news.
3. **Nine tools. PhantomBuster is cut** on category grounds: it is a scraper rather than a
   LinkedIn sequencer, and it ranks seventh for this term with its own competitor page.
   Dux-Soup stays. The title changes from "10 Best" to nine.
4. **Salesforge keeps the top slot**, earned on this article's dimension, which is escaping
   Dripify's per-seat model with both channels in one sequence.

### What the Skylead verification returned, and what it did not

Re-probed skylead.io/pricing on 2026-08-24, 387,011 bytes, USD, http 200. Figures served:
$100, $999, $1,999. **Identical to the 2026-08-13 read. Nothing has changed in 11 days.**

**Still not published: the annual rate.** The Annual plan card reads "For sales teams &
agencies with a steady seat count", then **"Let's talk"**, then "Pay 10 months & get 2
months free". So Skylead publishes a monthly seat rate and an annual *structure*, and no
annual number.

**This is writable, and section 9c already says how.** Its "when a vendor publishes no
price" clause, added 2026-08-19, permits saying plainly that the vendor does not publish
the figure. So the Skylead pricing block states: All-in-one at $100 per seat per month,
Agency at $999 for 50 seats or $1,999 for unlimited, both talk-to-sales, and the annual
plan unpriced with the ten-for-twelve structure named as the vendor names it.

**Do not compute $83.33.** Ten months over twelve is arithmetic Skylead has not published,
and the Waalaxy precedent in the Expandi brief is explicit: do not derive a rate from a
stated discount, because the rounding is unknown.

**Two things remain blocked and they gate the section, not the article.**

- **The rating.** G2 and Capterra both 403. Needs a screenshot or the section carries no
  rating line, which would make it the only one of nine without one.
- **The LinkedIn action list.** The pricing page verifies "LinkedIn automation" as a
  feature but publishes no granular action list. On a LinkedIn-focused article the action
  count is a comparison-table row, so either a source is found for it or that cell reads
  "Not published" and the article says so.

**If the rating screenshot does not arrive, the honest fallback is the 2026-08-13
resolution:** Skylead returns to FAQ-only. Flagging that now rather than discovering it
at draft time.

## Article

Target primary keyword: **dripify alternatives**. Competitor is Dripify, a LinkedIn
automation tool with email steps inside the drip campaign.

**Playbook routing: Playbook 2, LinkedIn outreach tool alternatives.** Product section is
**Salesforge: LinkedIn**, 12 must-covers, same as the Expandi article. Key differentiator
to lead with, per the playbook table: multichannel with 6 native LinkedIn actions plus
email in one sequence.

Current live title tag: "10 Best Dripify Alternatives in 2026 (Ranked)", 45 chars.
Meta 139 chars. 16 blog interlinks, well over the minimum of 5.

## Keyword and SERP

Ahrefs pulled 2026-08-24, US. `dripify alternatives`: volume 40, difficulty 0, CPC $3.50.

**Note on the tool.** `keywords-explorer-overview` returned an empty set for a
multi-keyword query and worked for a single keyword. The same thing happened on the
Outreach brief. Treat multi-keyword pulls as unreliable and query one at a time.

`serp-overview`, top 12, 2026-08-24:

| Position | Who | DR | Traffic |
|---|---|---|---|
| 1 | SERP feature, no URL attributed | | |
| 2 | sbl.so/linkedin/dripify-alternatives | 29 | 86 |
| 3 | Reddit cluster, r/Botdog and r/SaaS, 3 results plus a "more results" link | 95 | 23 |
| 4 | **heyreach.io/blog/dripify-review** | 72 | 105 |
| 5 | hyperclapper.com, "We Tried Dripify Alternatives" | 17 | 49 |
| 6 | meetalfred.com/alternates/dripify-alternative | 53 | 17 |
| 7 | phantombuster.com/blog/dripify-competitors-alternatives | 72 | 14 |
| 8 | alexberman.com/dripify-alternative | 29 | 6 |
| 9 | snov.io/dripify-alternative | 81 | 1 |
| 10 | People Also Ask block | | |
| 11 | youtube.com, "Looking for Dripify alternatives?" | 99 | 1 |

**We are not in it.** `site-explorer-organic-keywords` in exact mode for this URL returns
zero rows, so Ahrefs attributes no ranking keyword and no traffic to the page. Both
endpoints agree, unlike the Expandi URL where they disagreed.

**Three things the SERP says about intent.**

1. **Competitor-owned and thin.** The strongest result is HeyReach's *review* of Dripify
   at position 4, and four of the top nine are vendors writing about a rival
   (HeyReach, Meet Alfred, PhantomBuster, Snov.io). DR is low across the board: 29, 17,
   53, 29. Nothing here is hard to beat on quality.
2. **Partly a review query, again.** HeyReach ranks with a review, a YouTube review ranks
   11th, and the PAA block asks "Is Dripify worth it?" So the page has to evaluate Dripify
   itself and not only list replacements. Same pattern as both other keywords.
3. **Slot compression is severe for a 40-volume term.** Position 1 is an unattributed
   SERP feature, position 3 is a Reddit cluster of three results plus a "more results"
   link, and position 10 is PAA. Content can win 2 and 4 through 9, no more.

**The four live PAA questions**, which the FAQ should answer directly: Is Dripify worth
it? What is the best LinkedIn automation tool? How much is Dripify monthly? What is
Dripify?

Note the third. "How much is Dripify monthly" wants a monthly figure, and
`rules/writing.md` section 9c mandates annual rates. The FAQ answer names the annual rate
and may use the one permitted saving line to reference monthly. Do not add a monthly
column to satisfy the query.

## Baseline: the current published article

`python3 lint/run.py <url>`, 2026-08-24: **48 errors, 21 warnings.**

Rhythm is fine and needs no work: stdev 7.56, 26.9% at six words or fewer, 8.1% over 25.
All three floors clear. 308 sentences, 89 paragraphs.

**Mechanical, fix in one pass. 45 of the 48.**

| Finding | Count |
|---|---|
| em-dash | 13 |
| sentence-fragment | 13 |
| semicolon | 9 |
| brand-casing: lemlist | 6 |
| brand-casing: lemwarm | 2 |
| banned-phrase "what makes" | 1 |
| sentence over 45 words | 1 |

**Structural.**

- **TL;DR is wrong in every bullet.** All 10 fail `tldr-shape`: none opens with one of the
  four permitted openers. Two also carry a price figure, which section 9a bans.
- **7 paragraphs over the 60-word cap.**
- `entry-frame-repeat` ×1: two tool sections open on the same frame.
- **Check the TL;DR anchors in Webflow.** Every bullet's link extracts as an absolute URL
  back to this same page rather than an in-page anchor. That may be Webflow rewriting
  `#anchor` hrefs on render, so verify in the CMS before treating it as a defect.

**Fact errors about our own products. Nine instances, four rules. This is the strongest
reason the rewrite exists.**

| Rule | Instances | What is wrong |
|---|---|---|
| `fact:20+ languages` | 4 | Canonical is **21+ languages**. Locked in the positioning guidelines. |
| `fact:Pipedrive called native` | 2 | Pipedrive is mediated through Zapier or webhooks. Never a native Salesforge integration. |
| `fact:Billed quarterly` | 2 | Pricing is annual-only. The page carries a quarterly mention. |
| `fact:Agent Frank $499 quarterly` | 1 | Verify against `rules/positioning.md` before changing. The page reads "$599/mo commitment, billed quarterly", and the rule says quarterly is $599 and $499 is the annual rate, so the figure may be right while the quarterly framing is not. |

The first two are unambiguously wrong and appear six times between them. Fix at every
occurrence in the same pass, per `CLAUDE.md`.

## Coverage diff

`python3 lint/coverage.py` against **Salesforge: LinkedIn**, 12 must-covers. Bullet count
matches at 12, so nothing is missing outright, but three are in the wrong place:

- **In the product section: 8.**
- **Elsewhere only, 3:** Account safety as standard, LinkedIn email and phone finder
  Chrome Extension, Testing and analytics. Each matches somewhere on the page but not
  inside the Salesforge section, which is the bundling failure rather than coverage.
- **Uncertain, 1:** MCP CLI at 50% token match. Read it.

## Prices

Probed 2026-08-24. Every figure below is what the vendor's live page served to a fetch.

**Pricing**, dripify.io/pricing, read 2026-08-24. USD, billing toggle present. Figures
served: $29, $39, $49, $59, $69, $79, $99. The Expandi brief's recorded Dripify annual
rates of Basic $39, Pro $59, Advanced $79 all appear, so **Dripify's own pricing is
unchanged** and can be carried across.

The live page currently says only "Dripify starts around $39-79/mo per seat with
seat-based scaling". That is a range where the article should carry the per-tier annual
rates, and it omits the quota-per-tier point that made the Expandi article's Dripify
section work.

**Pricing**, we-connect.io/pricing, read 2026-08-24. USD. Figures served: $49, $59, $79,
$16, plus $240, $588, $708, $948 which look like annual totals rather than monthly rates.
Separate the two before quoting either.

**Pricing**, dux-soup.com/pricing, read 2026-08-24. USD, billing toggle present, and
**fully readable**: $11.25, $14.99, $41.25, $55.00, $74.17, $99.00, $371.00 across its
Pro, Turbo, Cloud and Team tiers. Separate monthly from annual before quoting, because a
Monthly and a Yearly tab are both present.

**Corrected 2026-08-24.** An earlier pass of this brief reported only "$175" here and
recommended cutting the tool on the grounds that it could not be priced. Both were wrong,
and the cause was two bugs in `lint/prices.py`. Its `probe()` never collapsed whitespace,
so the page's "$  11.25" with two spaces did not match a regex allowing one, and every
tier price was invisible. And the "$175" it did report was not a price at all, it came
from a case study reading "3 closed deals worth $175k". Both fixed, both locked by eight
new selftest cases. Recorded here because a tool cut for a tooling failure is the worst
kind of editorial decision.

**Pricing**, phantombuster.com/pricing, read 2026-08-24. **3,676 bytes, no figures, no
currency symbol.** The page is JS-rendered or blocking the fetch.

Carried over from the Expandi brief and still valid for the shared tools: Expandi,
HeyReach, Waalaxy, Meet Alfred, lemlist, Skylead. Re-verify each with
`python3 lint/prices.py research/dripify-alternatives.md` before drafting, because those
reads are dated 2026-08-13 and the staleness threshold is 14 days.

## Decide what survives

**The tool list is the biggest open question.** The page currently runs ten: Salesforge,
HeyReach, Expandi, Skylead, Waalaxy, Meet Alfred, lemlist, Dux-Soup, We-Connect,
PhantomBuster.

- **Seven are already researched** in `research/expandi-alternatives.md`, with verified
  prices, ratings and complaint themes: Salesforge, HeyReach, Expandi, Skylead, Waalaxy,
  Meet Alfred, lemlist. Those transfer at near-zero research cost.
- **Three are new and two of the three cannot be priced by fetch:** Dux-Soup, We-Connect,
  PhantomBuster.
- **PhantomBuster is arguably off-category.** It is a scraper and multi-platform
  automation tool, not a LinkedIn sequencer, and it ranks at 7 for this term with its own
  competitor page. Including it invites the comparison it wants.

**RESOLVED 2026-08-24: cut to nine, drop PhantomBuster only.** Reasoning kept below.

**Revised 2026-08-24.** The earlier recommendation also dropped Dux-Soup, and the reason
given was that it could not be priced by fetch. That was a bug in our own prober, not a
fact about the tool. Dux-Soup is a LinkedIn automation tool running drip campaigns, which
makes it a direct Dripify substitute and one of the longest-established ones. It stays.
"My script could not read the page" is never an editorial reason to cut a tool.

PhantomBuster is a different case and the argument against it does not rest on tooling.
It is a scraper and multi-platform automation product rather than a LinkedIn sequencer, so
it answers a different question than the rest of the list. It also ranks seventh for this
term with its own competitor page, so including it hands a rival the comparison it wants.
Its pricing page separately serves 3,676 bytes with no figures and no currency symbol,
confirmed after the prober was fixed, so it would need a screenshot on top of that.

**Sections to keep.** The rhythm is already good and the interlink count is 16, so the
structural bones are sound. Keep the comparison table, the use-case router, and the FAQ
shape.

**Sections to rewrite.** All ten TL;DR bullets, the Salesforge section (to pull the three
elsewhere-only must-covers into it), and every paragraph over 60 words.

**Sections to cut.** The PhantomBuster section, if the cut is approved.

**A Forge product does not keep the top slot because it had it.** Salesforge currently
leads. On this article's dimension, LinkedIn plus email in one sequence without per-seat
pricing, it has a real claim, and Dripify's per-seat model is the exact contrast. But
HeyReach's agency structure is a genuine rival on a different dimension, so the decision
belongs in the outline rather than being inherited.

## Open, blocking

1. **The prioritisation decision** at the top of this brief. Full rewrite, mechanical-only
   pass, or defer in favour of `outreach-alternatives`.
2. **The tool list.** Ten or eight, and whether PhantomBuster and Dux-Soup go.
3. **PhantomBuster pricing.** No figures in the served HTML, re-confirmed after the prober
   was fixed. Needs a screenshot showing the billing toggle and the currency in the same
   frame, or the tool gets cut. Cutting it is the recommendation anyway, on category
   grounds.
4. **We-Connect pricing.** Monthly rates and annual totals are both present in the HTML and
   need separating. A screenshot settles it.
5. **Dux-Soup monthly against annual.** No longer blocking. All seven tier prices are
   readable, but a Monthly and a Yearly tab are both on the page and only one is served to
   a fetch, so confirm which figures are the annual rates before quoting them.
6. **Every rating on the page.** G2 and Capterra both 403, so run
   `python3 lint/evidence.py research/dripify-alternatives.md` and capture what it names.
7. **First-person claims.** `rules/observations.md` has OBS-001 for mailbox scaling and
   nothing else usable for a LinkedIn article. The same shortfall the Expandi piece hit.
   A screening count for this article would need its own entry, and it must say
   **screened** rather than tested unless a hands-on test actually ran.

## Not blocking, worth knowing

- **Two tooling bugs surfaced from this page and both are now fixed.** The price prober
  missed every tier price on dux-soup.com and reported a case study figure as the only
  price. Details in the Prices section above, eight selftest cases lock it.
- **A linter bug surfaced from this page and is now fixed.** `We-Connect` was reported as a
  first-person-plural ERROR 12 times, because `\b` treats the hyphen as a word boundary.
  The first-person check now honours the same product-name span exemption the banned-word
  check uses, and `We-Connect`, `Dux-Soup`, `PhantomBuster` and `Skylead` were added to
  `lint/data/product-names.txt`. Three selftest cases lock it, including one confirming a
  real "we" is still caught. The raw audit was 55 errors; 48 is the true count.
- HeyReach's Dripify review outranks every dedicated alternatives page here, which is
  worth reading before writing the Dripify evaluation section.
