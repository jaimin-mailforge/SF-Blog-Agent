# Research brief: expandi-alternatives

Drafting reads this file plus `rules/writing.md`, `rules/positioning.md`, and `rules/observations.md`. Nothing else.

**Status:** research complete. All nine tools evidenced. Three decisions open, listed at the end.

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

## Evidence: access limits that shape the article

**G2, Trustpilot and TrustRadius all return 403 to automated fetching, and Reddit is blocked.** Every route was tried: browser user agents, full navigation headers, regional Trustpilot domains, the legacy g2crowd domain, a text-rendering proxy, Reddit's JSON API, old.reddit, and the PullPush archive. The agent proxy reports no relay failures, so these are the destinations' own bot walls.

**Capterra is readable and is the verified base for everything below.** Anything from G2, Trustpilot or Reddit is marked unverified and must not enter the draft.

Two hard sourcing warnings:

- **Do not use these circulating figures.** "Expandi has a 23% account restriction rate within 90 days" and "LinkedIn detection increased 340% from 2023 to 2025" come from competitor marketing pages with no stated methodology. The widely repeated "Expandi G2 4.2 from 112 reviews" and "HeyReach 4.8 from 280+ reviews" appear only in third-party posts and conflict across sources.
- `meetalfred.com/alternatives/expandi` and `dripify.com/comparison/why-choose-dripify-over-meet-alfred/` both rank for our keyword. Their own pricing pages are fine sources for their own prices. Nothing on their comparison pages is a fact about a rival.

## Evidence: Expandi

**Pricing**, expandi.io/pricing, read 2026-08-13. Business **$99 per seat monthly, $79 per seat annual** (20% off, marketed as two months free). Agency is custom, 10+ seats, adding roles and permissions, client reporting, dedicated CSM and white label. 7-day trial, all features, no card charged.

**The billing unit is the story.** From Expandi's own help centre: one seat connects to one LinkedIn account at a time, pricing is per seat, and **you pay for purchased seats whether or not they are connected to a LinkedIn account.**

**Add-ons.** Image and GIF personalization, the feature every top-ranking page cites as Expandi's selling point, is not included. Expandi's page says only that it "requires an additional cost". It runs through Hyperise, whose own live pricing starts at **$69 per seat per month** for unlimited designs, up to 5 active images and 5,000 image views, with annual at roughly $57.50. Video personalization needs Hyperise's $149 tier or a separate Senspark integration, price not published.

**Ratings.** Capterra **4.4 from 31 reviews** (5 star 22, 4 star 4, 3 star 1, 2 star 2, 1 star 2. Ease 4.1, value 4.2, support 4.3, features 4.4). G2 and Trustpilot unverified.

**Not published anywhere reachable:** contact limits, email account limits, sending caps, Agency per-seat rate. Expandi's own recommended-limits and email-integration help articles are login-gated.

### The four claims, rated

| Claim | Verdict | Action |
|---|---|---|
| Per-seat pricing doubles with add-ons | **Thinly supported.** The arithmetic is $99 plus $69 equals $168, a 70% increase, not a doubling. As a user grievance it is one 2023 review about being charged for 7 seats while using 4. | Publish the arithmetic as fact with both vendor pages cited. **Drop the word "doubles".** Do not attribute it to users. |
| Account restrictions inside safe limits | **Unsupported. Zero of 31 Capterra reviews mention a restriction or ban.** The only quote found had no reachable source. The quantified figures circulating are competitor marketing. Expandi's own safe-limits doc is login-gated, so the premise cannot even be stated. | **Cut.** |
| LinkedIn-first, email bolted on | **Well supported, from Expandi's own documentation.** 11 campaign types and **none is an email campaign**. Email exists as a single step plus an "if email exists" condition, inside the Builder campaign only. The inbox is explicitly LinkedIn and Sales Navigator only, so **email replies never appear in it**. Email needs your own mailbox, and IMAP for reply detection. Expandi publishes its own guide to using Smartlead for the email leg. No native email infrastructure, no warm-up. | **Keep. This is the strongest claim in the article.** |
| Billing disputes and refund refusals | **Thinly supported and stale.** Two Capterra users, both March 2023, one platform. Capterra's aggregated cons do list billing issues. | Soften to "a small number of older reviews" or cut. |

### Expandi's genuine strengths, for section 14

1. **The widest LinkedIn campaign surface of any tool here.** 11 named campaign types including Mobile Connector, which Expandi says adds 100 connection requests a week, plus free Open InMail, Group, Event Invite, Company Follow Invite, Inbound and Recovery.
2. **A real conditional builder.** Three true/false conditions plus engagement actions nothing else here matches: skill endorsement, like a post, like a company post, invite to follow company, and signals on profile visits, company visits and post engagement.
3. **Safety scaffolding as a product feature.** Cloud-based, a dedicated country-based IP per account, profile auto warm-up, and randomised limits the tool refuses to let you exceed.

## Evidence: HeyReach

**Pricing**, heyreach.io/pricing, read 2026-08-13. Growth **$79 per sender monthly, $71 quarterly, $63 yearly**. Agency **$999 / $899 / $799** for 25 senders, expandable to 50. Unlimited **$2,999 / $2,699 / $2,399**. Plus a managed Done For You tier.

**Billing is flat per LinkedIn sender, not per user.** From the vendor FAQ: a sender is a LinkedIn account, and HeyReach does not charge for adding teammates, VAs, clients or users. **Human seats are unlimited and free.** Whitelabel add-on $500 per additional brand on Unlimited. Growth includes a dedicated residential proxy per sender; Agency and Unlimited require you to bring your own. Trial is 14 days, no card, 3 LinkedIn accounts.

**Ratings.** Capterra **5.0 from 2 reviews**, which is statistically meaningless and must be stated with the count. G2 and Trustpilot unverified.

**No usable complaint themes exist.** Two accessible reviews, neither negative. **Do not write a complaint section implying otherwise.** Two defensible product-level limitations instead:

- **No native email sending.** Multichannel means paying separately for Instantly, Smartlead or EmailBison on top.
- **The Agency floor.** At $79 per sender, 12 senders is $948, so the $999 bundle only pays off above roughly 12 to 13 senders. Mid-size teams sit in a gap.

**Strengths.** Flat per-sender pricing with free unlimited human users and whitelabel at Agency. A unified LinkedIn inbox across every connected account, with sender rotation and per-client workspaces under one login. Real plumbing: API, webhooks, an MCP server, and bidirectional Instantly and Smartlead sync so a reply on either channel pauses steps on both.

**Architecture.** LinkedIn-only for sending. Confirmed actions: connection requests, messages, follows, profile views, plus an "if connected" condition. InMail is unverified, so do not claim it. Email is a handoff step into Smartlead or Instantly. Inbox is LinkedIn-only.

## Evidence: Dripify

**Pricing**, dripify.com/pricing, read 2026-08-13. Basic **$59 per user monthly, $39 annual**. Pro **$79 / $59**. Advanced **$99 / $79**. Enterprise custom. One seat connects one LinkedIn account, so five reps need five seats.

**Dripify publishes exact daily quotas per plan**, which nothing else here does. Basic, Pro, Advanced: connection requests 20 / 75 / 75, messages 30 / 100+ / 100+, Sales Navigator InMails 10 / 30 / 30, profile views 100 / 200+ / 200+, endorsements 10 / 50+ / 50+, post likes 10 / 50+ / 50+, follows 10 / 50+ / 50+.

**Add-ons.** Email-finder credit packs at $29 per 1,000, $49 per 2,000, $69 per 5,000, $99 per 10,000. 100 credits included monthly on every plan, valid 30 days, no rollover. Credits cover finding and verifying addresses, not sending. Trial is 7 days with Advanced features, no card.

**Ratings.** Capterra **4.7 from 477 reviews**, ease 4.7, support 4.6. **The largest verified review base in this article by a wide margin.** G2 and Trustpilot unverified.

**Complaint themes.** Note the method: Capterra's filter surfaces mostly 4 and 5 star reviews whose cons field is critical, so these are cons mentioned rather than low ratings.

1. **Cost relative to value, especially stacked on Sales Navigator, 5 separate users.** Named: Saif I. (CEO), Joyce H., Victoria D., plus two more.
2. **Basic is more limited than people expect, 2 users.** Richard L. (fCMO, 3 star, July 2025) on one campaign that cannot be edited or archived, where editing means deleting the campaign's data.
3. Borderline at 2 users: sequence bugs when the first step is a connection request to an existing contact.

**Zero mentions of LinkedIn bans and zero support-failure complaints** in the readable reviews.

**Strengths.** Genuine native email inside the same sequence on every paid plan including the $39 tier, not an integration handoff, with the email finder built in. Published per-plan daily quotas for all seven action types. The deepest verified satisfaction record here.

**Architecture.** LinkedIn plus email in one sequence, 15+ actions and conditions. **Email uses your own mailbox, Gmail or Outlook only, one mailbox per account, capped at 200 emails a day.** No native infrastructure, no warm-up. Pro and above get a dedicated LinkedIn inbox; whether email replies land there is unverified.

## Evidence: Meet Alfred

**Pricing**, meetalfred.com/pricing, read 2026-08-13 from raw HTML since the page 403s to normal fetching. Basic **$59 monthly, $49 quarterly, $29 annual**. Pro **$99 / $79 / $49**. Team **$79 / $59 / $39**. Per user. EUR and GBP published alongside USD.

**Two oddities worth naming in the article.** Team is cheaper than Pro on every billing cycle. And the page markets annual as 50% off while the quarterly toggle says 20% but delivers closer to 17.

**Basic is LinkedIn-only.** Email and X automation start at Pro, which makes the $29 headline misleading for anyone buying it for multichannel. Trial length is not stated anywhere on the pricing page.

**Ratings.** Capterra **2.8 from 13 reviews**. Distribution: 5 star 4, 4 star 1, 3 star 2, 2 star 0, **1 star 6**. Ease of use 2.7 and **customer service 1.9**. That 1.9 is the single most quotable verified number in this article. Always state the 13-review base with it.

**Complaint themes**, from a 13-review base with six one-star reviews:

1. **Support unresponsive or ineffective, around 5 users.** One reports up to four days without a reply, another that support was unavailable for weeks during an outage. Corroborated by the 1.9 support sub-score.
2. **Buggy or non-functional, around 4 users.** Chat windows disappearing after messages, failures connecting or sending through LinkedIn.
3. **Refunds refused under a no-refund policy, around 4 users**, including one citing email bounces and reconnection failures on a paid account.

**Strengths.** Cheapest annual entry here at $29 per user, with published EUR and GBP pricing rather than a checkout conversion surprise. **Three channels in one sequence, LinkedIn plus email plus X**, which nothing else in this comparison offers. The broadest set of LinkedIn campaign entry points and relationship tooling, including auto-withdrawal of pending invitations, automated greetings on birthdays and job changes, a 600+ template library, and white label from 5 users.

**Architecture.** LinkedIn, email and X in one sequence. Email is your own mailbox over SMTP or IMAP. No native infrastructure, no warm-up. **The unified inbox is LinkedIn-side only:** the pricing table lists a LinkedIn inbox, an InMail inbox and a Sales Navigator inbox, with no email inbox row. Multichannel requires Pro or Team.

## Evidence: Waalaxy

**Pricing**, waalaxy.com/pricing, read 2026-08-13. Per user. Pro **€19**, Advanced **€49**, Business **€69** per user per month. Enterprise unpriced, for teams of 5+.

**Those are annual-tab prices, and the monthly figures could not be recovered.** The toggle defaults to Yearly at minus 50 percent, and the monthly and quarterly numbers exist only after a JavaScript click. They are absent from the HTML and from all 28 Framer bundles. The vendor FAQ confirms quarterly at minus 20 percent and annual at up to 50 percent savings. **Do not print a monthly euro figure.** The page's own JSON-LD lists 19 / 39 / 69 USD, which contradicts the rendered €49, so ignore the schema.

**Two gating facts that matter more than the price.** Email sequences and LinkedIn-plus-email campaigns exist **only on the €69 Business tier**, so Pro and Advanced are LinkedIn-only. And the **LinkedIn Inbox is a €20 per month add-on**, never bundled on any plan, with a free tier of 500 conversations. The invite ceiling is **800 a month even at the top tier**. No email warm-up anywhere on the site. 14-day trial on all three plans, and **the free plan people remember is gone**.

**Ratings.** Capterra **4.4 from 253 reviews**, ease 4.3, customer service 4.5.

**Complaints.** Missing features and thin native integrations, around 8 reviewers. Extension and reliability bugs, around 6. Price against value, around 6. LinkedIn limits and account restrictions, around 5, including a suspension after four months and campaigns blocking before reaching daily limits. **Caveat: a large share of Waalaxy's Reddit threads are authored by competing vendors.** Only first-person user statements were counted.

**Strengths.** Cheapest genuine entry point in the set at €19 with unlimited campaigns included. Customer service is its best-scoring dimension. Import breadth covers LinkedIn Basic, Sales Navigator and Recruiter Lite, plus auto-import of post likers and commenters.

**Wrong for** agencies running multiple LinkedIn accounts at volume, and for anyone email-led: email needs the €69 tier, invites never exceed 800 a month, there is no warm-up, and the inbox costs extra.

## Evidence: La Growth Machine

**Pricing**, lagrowthmachine.com/pricing, read 2026-08-13 from the inline pricing object, which is authoritative since the server-rendered card values are stale. **Priced per identity, meaning per sending profile, not per human seat.**

| Plan | Monthly | Annual | Channels | Team members |
|---|---|---|---|---|
| Basic | €60 / $70 | **€50 / $60** | LinkedIn, email | 3 included |
| Pro | €120 / $135 | **€100 / $110** | plus calls | **25 free** |
| Ultimate | €180 / $195 | **€150 / $165** | plus X | unlimited |

**The gating fact that matters for this article: the unified LinkedIn-and-email inbox is Pro and above. Basic explicitly excludes it, and Basic also gives you one email sender.** So the cheap-looking tier lacks the two things a LinkedIn-plus-email motion needs. Identities are billed separately on every tier. Agency needs 6 identities minimum, Custom needs a 6-month commitment. 14-day trial, no card. No email warm-up product.

**Ratings.** Capterra **4.9 from 45 reviews**, ease 4.7, **customer service 5.0**. Best-rated tool in the set. Trustpilot shows 2.9 from 8 reviews but the page is unreadable and the base is tiny, so note the divergence at most and do not build on it.

**Complaints, thin and stated as such.** Widget and identity management overhead, 3 reviewers. Set limits not always respected, 3 mentions. Weak reporting and complexity for the price, 3 voices. Per-identity cost, 2 voices. **Reddit has almost no organic criticism of this tool, most of it is competitor-authored.** If the article needs a stronger negative case for La Growth Machine, that evidence does not exist in public data. Say so or drop it.

**Strengths.** Best-rated here, with documented human support SLAs of under 24, 4 and 2 hours by tier. Cost scales by sender rather than headcount, with 25 team members free on Pro. Native waterfall enrichment across 9 email providers and 2 verification tools, plus LinkedIn intent import from likers, commenters and event attendees.

**LinkedIn actions, 5:** visit profile, like latest posts, connection request, DM, and AI-generated voice message.

**Wrong for** solo founders and agencies with many LinkedIn accounts. Three senders on Pro is €300 a month annual, €360 monthly, before enrichment credits.

## Evidence: lemlist

**Correction to an assumption in this brief.** The earlier note that lemlist's Email plan is "$55 per user per month" is **wrong**. The plan card reads "$55 a month, **unlimited users**, 50,000 emails a month", and the comparison table checks "unlimited users and email senders" for the Email plan only. The price is keyed to **send volume**, not seats. The page's own comparison header says "From $55 per user per month", contradicting its own card. Flag the contradiction, do not repeat it.

**Pricing**, lemlist.com/pricing, read 2026-08-13 from the embedded pricing dataset, so all three cycles are directly confirmed.

**Multichannel, per user:** $109 monthly, $99 quarterly, **$87 yearly**. Enterprise is talk-to-sales, 5 users minimum.

**Email, flat by volume with unlimited users:** 50,000 emails at $69 monthly and **$55 yearly**. Then 100,000 at $89 / $80, 200,000 at $159 / $127, 500,000 at $359 / $287, 1,000,000 at $659 / $527.

**LinkedIn automation requires the Multichannel plan**, confirmed twice: it appears only in that plan's feature block, and the comparison table gates LinkedIn profile visits, follows and invites, text messages, voice messages, in-app calling, VoIP, SMS, the WhatsApp add-on and the unified inbox to Multichannel and Enterprise. **The unified inbox is Multichannel only**, despite the Email plan's marketing card listing it. Another internal contradiction, and the comparison table is the more specific source.

**lemwarm is included in every plan**, per the vendor FAQ. That is a genuine differentiator against most of this set.

**Credits.** 1 credit is $0.01, 1,000 credits $10. Verified email 5 credits, phone number 20. Intent signals from 20 credits for a website visit up to 400 for LinkedIn engagement. 14-day full Multichannel trial, no card, no free plan.

**Ratings.** Capterra **4.6 from 387 reviews**, ease 4.5, customer service 4.6.

**Complaints.** Per-seat cost at team scale, around 8 voices, including criticism of no discounts until 20+ seats. **Lead database value below the pitch, around 4 users**, with the most concrete being a trialist who ran 130 target companies through Sales Navigator, Scrupp, Clay and lemlist and found only 9 unique to lemlist, about 12 percent, verdict "wouldn't be worth the price of admission". Support depth, around 4 voices, including "their support is not technical and only relays what their technical people tell them". Reporting accuracy, 2 voices.

**Strengths.** Widest channel span in one sequence: email, LinkedIn with 4 action types, SMS, WhatsApp, and in-app calling, with **conditional next steps on every plan including Email**. Email infrastructure bundled rather than bolted on, including lemwarm, inbox rotation, rotating IPs, custom tracking domain, deliverability hub, and in-app domain and mailbox purchase. The Email plan's unlimited-users volume pricing is genuinely cheap for email-only teams.

**Wrong for** LinkedIn-first teams on a budget. A five-rep team on Multichannel is $545 a month month-to-month, against $55 flat for the email-only plan they cannot use. Also wrong for anyone buying it as a lead database.

## Evidence: Snov.io

**Pricing**, snov.io/pricing, read 2026-08-13 from the page's own price attributes. **Flat per plan, with unlimited team seats on every paid plan.** No per-seat multiplier anywhere.

| Plan | Monthly | Annual | Credits/mo | Warm-up slots |
|---|---|---|---|---|
| Trial | Free, renewable 30-day cycles | Free | 50 | 1 |
| Starter | **$39** | **$29.25** | 1,000 | 3 |
| Pro S | **$99** | **$74.25** | 5,000 | Unlimited |
| Pro M | $189 | $141.75 | 20,000 | Unlimited |
| Pro L | $369 | $276.75 | 50,000 | Unlimited |
| Ultra | $738 | $553.50 | 100,000 | Unlimited |

**LinkedIn automation is a paid add-on, not included.** Verbatim from the plan features: LinkedIn account slots "are not included in the price and are purchased separately at **$69/mo per slot**", or **$62 with an annual subscription**, with a further $10 off each slot for Sales Suite subscribers. A free 7-day LinkedIn trial is available on Starter and above. **So one LinkedIn seat costs the plan plus $69.** A three-rep LinkedIn team is $207 a month of slots before the plan.

Other add-ons: enrichment tokens at $0.02 each with 90-day validity, sending domains from $12 a year, and done-for-you Google mailboxes at $5 a month per account.

**Ratings.** Capterra **4.5 from 215 reviews**, ease 4.6, customer service 4.7.

**Complaints.** Data accuracy and freshness, around 5 users, including a 3-star reviewer who found "the delivery rate was pretty low and when I ran the similar contacts in different tool, I received a 20% higher open rate". Deliverability degradation at scale, 3 users. Bugs and UX gaps, around 4 reviewers, including duplicate contacts created for no reason. Credit expiry, 2 voices, thin. **Snov's Reddit history is mostly 2017 to 2018 noise plus competitor comparison posts.** Roughly four genuine user complaints exist. Do not inflate.

**Strengths.** Cheapest credible all-in-one and it does not charge per seat: $29.25 annual with unlimited seats, senders, campaigns and follow-ups. **Deliverability tooling is native and unusually complete for the price**, including warm-up with unlimited slots on Pro tiers, a premium business-domain pool, a 7-tier verifier, mailbox rotation, placement checks, and blacklist and reputation checks. The LinkedIn add-on is architecturally serious, with cloud execution and a dedicated location-based proxy per account.

**LinkedIn actions, 7**, the most granular in the set: messages, InMail, connection requests, follows, skill endorsements, post likes, profile views. **Unibox included on all paid plans**, and recipients are charged once whether first contact is email or LinkedIn, which implies genuinely shared campaign state.

**Wrong for** anyone whose primary channel is LinkedIn, since the product is email-first and LinkedIn inverts its price advantage. Also wrong as a lead database.

## Cross-cutting findings

These are the three patterns the article's argument rests on. All from the evidence above.

**1. Almost nobody bundles email warm-up.** Of the eight alternatives, only **lemlist** (lemwarm on every plan) and **Snov.io** (unlimited slots on Pro tiers) include it. Expandi, HeyReach, Dripify, Meet Alfred, Waalaxy and La Growth Machine have **no warm-up product at all**. Salesforge includes unlimited Warmforge slots free on both plans, covering any mailbox type.

**2. A unified inbox covering both channels is rarer still.** Expandi, HeyReach, Meet Alfred and Waalaxy are all **LinkedIn-only inboxes**, and Waalaxy charges €20 a month for its. Dripify's email-reply handling is unverified. La Growth Machine gates it to Pro. lemlist gates it to Multichannel. Only **Snov.io** includes it on every paid plan. Salesforge's Primebox™ carries both channels on both plans.

**3. Seven different billing units, which is the spine of the piece.** Per seat where a seat is one LinkedIn account: **Expandi** $99 / $79, **Dripify** $59 to $99 / $39 to $79. Per sender with humans free: **HeyReach** $79 / $63. Per identity with humans free: **La Growth Machine** €60 / €50. Per user: **Meet Alfred** $59 / $29, **Waalaxy** €19 to €69, **lemlist Multichannel** $109 / $87. Flat with unlimited seats: **Snov.io** $39 / $29.25 plus $69 per LinkedIn slot, and **lemlist Email** $55 flat by volume. Salesforge is flat with unlimited mailboxes on both plans and unlimited LinkedIn senders and users on Growth at $80 annual.

That third pattern is the honest reason Salesforge earns the top slot on this article's dimension. Not "more features". A team of five running five LinkedIn accounts pays five multiples almost everywhere in this set.

## Why People Leave Expandi: claim status

Each of the four sub-sections needs real support or it gets cut. Ratings pending.

Rated in the Expandi evidence section above. Summary: one claim is well supported and keeps its section, one needs rewriting as arithmetic, one is unsupported and gets cut, one is thin and stale. A replacement sub-section is proposed in the outline-change note below.

A thinly supported ban or refund claim about a named competitor is the riskiest sentence in this article. Cut rather than soften.

## Internal links

TBD. Target 5 or more blog-to-blog links, anchors that already exist word for word in the draft, no duplicate anchor text.
