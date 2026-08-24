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

**Pricing**, dux-soup.com/pricing, read 2026-08-24. USD, billing words present, but only
a single figure served, $175. The per-tier rates are not in the served HTML.

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

**Recommendation, flagged not decided: cut to eight and drop PhantomBuster and Dux-Soup.**
That matches the Expandi article's count, removes both unpriceable vendors, and keeps
every tool that is a genuine Dripify replacement. If the ten stays, both need screenshots.

**Sections to keep.** The rhythm is already good and the interlink count is 16, so the
structural bones are sound. Keep the comparison table, the use-case router, and the FAQ
shape.

**Sections to rewrite.** All ten TL;DR bullets, the Salesforge section (to pull the three
elsewhere-only must-covers into it), and every paragraph over 60 words.

**Sections to cut.** Whatever covers the two dropped tools, if the cut is approved.

**A Forge product does not keep the top slot because it had it.** Salesforge currently
leads. On this article's dimension, LinkedIn plus email in one sequence without per-seat
pricing, it has a real claim, and Dripify's per-seat model is the exact contrast. But
HeyReach's agency structure is a genuine rival on a different dimension, so the decision
belongs in the outline rather than being inherited.

## Open, blocking

1. **The prioritisation decision** at the top of this brief. Full rewrite, mechanical-only
   pass, or defer in favour of `outreach-alternatives`.
2. **The tool list.** Ten or eight, and whether PhantomBuster and Dux-Soup go.
3. **PhantomBuster pricing.** No figures in the served HTML. Needs a screenshot showing the
   billing toggle and the currency in the same frame, or the tool gets cut.
4. **Dux-Soup pricing.** Only $175 served. Needs a screenshot of the per-tier rates.
5. **We-Connect pricing.** Monthly rates and annual totals are both present in the HTML and
   need separating. A screenshot settles it.
6. **Every rating on the page.** G2 and Capterra both 403, so run
   `python3 lint/evidence.py research/dripify-alternatives.md` and capture what it names.
7. **First-person claims.** `rules/observations.md` has OBS-001 for mailbox scaling and
   nothing else usable for a LinkedIn article. The same shortfall the Expandi piece hit.
   A screening count for this article would need its own entry, and it must say
   **screened** rather than tested unless a hands-on test actually ran.

## Not blocking, worth knowing

- **A linter bug surfaced from this page and is now fixed.** `We-Connect` was reported as a
  first-person-plural ERROR 12 times, because `\b` treats the hyphen as a word boundary.
  The first-person check now honours the same product-name span exemption the banned-word
  check uses, and `We-Connect`, `Dux-Soup`, `PhantomBuster` and `Skylead` were added to
  `lint/data/product-names.txt`. Three selftest cases lock it, including one confirming a
  real "we" is still caught. The raw audit was 55 errors; 48 is the true count.
- HeyReach's Dripify review outranks every dedicated alternatives page here, which is
  worth reading before writing the Dripify evaluation section.
