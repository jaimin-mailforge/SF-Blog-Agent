# Forge Stack Positioning and Product Facts

What we say. Voice and structure live in `rules/writing.md`.

**Read `rules/forge-positioning-guidelines.md` first.** It is the locked positioning reference and it wins on feature names, feature descriptions, must-cover checklists, positioning statements, and the article-type playbooks. This file is the evidence layer and it wins on live-verified prices, the pricing traps, and the resolved-decision log. Its reconciliation section lists the nine conflicts between the two files and how each one resolves.

Every figure below was read from the vendor's own page on **2026-08-13**. The source column is the page to re-check. Re-verify pricing on every rewrite, because these pages change without notice.

If a fact is not in this file, do not write it. Ask.

---

## How to use this file

**Feature names are fixed.** Do not paraphrase them. Bounce Shield is always Bounce Shield, never "bounce protection". Primebox™ and Heat Score™ always carry the trademark. Waterfall enrichment is never "cascade enrichment". ESP matching is never "provider matching".

**The must-cover lists are coverage checklists, not article prose.** They say which facts have to appear somewhere in a piece. They are not sentences to copy. If your prose starts sounding like these bullets, you have drifted into marketing register. Rewrite against `rules/writing.md`.

**Every must-cover feature appears somewhere in the piece when that product is featured.** All of them, not most. But tie each one to a specific gap, advantage, or use case, and never paste the list as a wall of bullets.

---

## Pricing

### Annual format only `[LINT]`

**Every price in every article is the annual-billing rate, phrased as "$X/month billed annually".** Added 2026-08-13 by Jaimin. This applies to Forge products and to every competitor.

- Pricing tables carry one price column, the annual one. No "Billed monthly" column, no "Billed quarterly" column. The linter blocks both headers.
- Prose quotes the annual rate and nothing else. "Dripify Basic is $39 per user per month billed annually", not "$59 monthly, $39 annually".
- Where a vendor's cheaper cycle is the only rate published, say so plainly and name the cycle.
- Where a vendor's page opens on a different cycle, still quote annual, and tell the reader which tab the page opens on if it is not annual.
- Cost-at-scale math uses annual rates throughout. Never mix cycles inside one calculation.

The tables further down this file keep both cycles on purpose. They are the evidence layer, not article copy. Read the annual column.

### The four traps

These caused real errors in both of the previous rule sets. Read them before quoting any price.

1. **The Salesforge pricing page loads on annual billing.** Anyone reading it casually gets $40 and $80 and calls them "the price". They are the annual-billing rates.
2. **Infraforge's short billing cycle is quarterly, not monthly.** Mailforge and Primeforge are monthly. Never write "Infraforge $4 per mailbox per month, billed monthly".
3. **The infrastructure pages' headline "Mailbox cost of $X /month" is the short-cycle unit price**, shown directly above a separate "Billed yearly" figure. The annual effective rate is always lower.
4. **Agent Frank has two different $499s.** The headline card is $499 per month billed annually. A separate add-on slider shows $499 per month billed quarterly for 1,000 active contacts. They are not the same thing.

### Salesforge

| Plan | Billed monthly | Billed annually | Source |
|---|---|---|---|
| Pro | $48/month | **$40/month** | salesforge.ai/pricing |
| Growth | $96/month | **$80/month** | salesforge.ai/pricing |

Preferred phrasing: "Salesforge Pro from $40/month billed annually, or $48/month billed monthly."

**Pro includes:** 1,000 active contacts in sequence, 5,000 emails/month, 300 email validation credits/month, 300 personalization credits/month, 300 social action credits/month, 1 LinkedIn sender, 1 user, unlimited contact storage, unlimited mailboxes, unlimited premium warm up via Warmforge, unlimited workspaces, Primebox™, sentiment analysis, smart mailbox rotation, dynamic IPs, knowledge base, live chat support.

**Growth includes** everything in Pro plus: 10,000 active contacts, 50,000 emails/month, 1,000 of each credit type per month, unlimited LinkedIn senders, unlimited users.

**Growth-only features**, exactly as the page lists them under "Exclusive Growth Plan Features": Salesforge MCP and CLI, multi-language sequences, A/B testing, personal onboarding, advanced settings, priority support, Salesforge API, Primebox AI, ESP matching, integrations.

**Do not list mailboxes as a Growth differentiator.** Both plans connect unlimited mailboxes, and both include unlimited premium warm up. The only sender difference is LinkedIn: 1 on Pro, unlimited on Growth.

**Trial:** 14-day free trial, no credit card required. The trial allows 50 contacts, 100 emails, 50 email validation credits, 50 personalization credits, 100 social action credits, plus warm up and unlimited mailboxes.

Overage is slider-priced on the same page. Quote it only when the article does pricing math, and read the live slider when you do.

### Agent Frank

| Item | Billed quarterly | Billed annually | Source |
|---|---|---|---|
| Agent Frank | $599/month | **$499/month** | salesforge.ai/pricing |

Base plan covers up to 1,000 active contacts. Beyond 2,000 contacts per month the page quotes $0.25 per contact. Access requires booking a demo first, so the CTA for Agent Frank is a demo, not a trial.

Includes: 24/7 automated prospecting, Auto-Pilot and Co-Pilot modes, fully customizable agent, 500M+ contact search engine, 21+ languages, dedicated account manager, shared Slack channel.

### Leadsforge

| Plan | Price | Credits | Source |
|---|---|---|---|
| Essential, monthly | $49/month | 2,000 credits/month, unused credits roll over | leadsforge.ai/pricing |
| Essential, annual | $588/year | 28,000 credits, granted upfront | leadsforge.ai/pricing |

**$588 is exactly 12 times $49.** The annual plan is not a dollar discount. The "2 months free" arrives as extra credits, 28,000 against 24,000. Never write that annual Leadsforge costs less per month, because it does not. The accurate framing is "same monthly cost, roughly 17% more credits, granted upfront."

100 free credits on signup, no credit card required. Credits do not expire. Searching and refining a list is free. Credits are charged when you enrich and export.

**Credit costs:** 1 email = 1 credit. 1 LinkedIn profile URL = 1 credit. 1 mobile number = 10 credits. 1 company follower plus their LinkedIn URL = 1 credit. 1 company lookalike = 1 credit, charged per company and not per lead.

### Mailforge

Shared email infrastructure. Short cycle is monthly.

| Volume | Billed monthly | Billed annually (effective) |
|---|---|---|
| 1 to 100 slots | $3.00/mailbox/month | $2.50/mailbox/month |
| 501 to 600 | $2.50 | $2.08 |
| 1,001+ | $2.00 | $1.67 |

Honest range: **$3.00 down to $2.00 per mailbox per month on monthly billing, or $2.50 down to $1.67 on annual.** Price drops at volume across eleven tiers. Minimum 10 mailbox slots, charged whether or not you create the mailboxes. Domains are separate at $14/year for .com, charged once. SSL and domain masking is an add-on at $2 per domain per month, or $6 per domain per year. No free trial.

### Infraforge

Dedicated IP infrastructure. **Short cycle is quarterly.**

| Volume | Billed quarterly | Billed annually (effective) |
|---|---|---|
| 1 to 100 slots | $4.00/mailbox/month | $3.33/mailbox/month |
| 501 to 600 | $3.50 | $2.92 |
| 1,001+ | $3.00 | $2.50 |

Honest range: **$4.00 down to $3.00 per mailbox per month on quarterly billing, or $3.33 down to $2.50 on annual.** Minimum 10 mailbox slots. Domains $14/year. Add-ons: dedicated IP addresses at $99 per IP per month billed quarterly, Masterbox at $7 per workspace per month billed annually or $9 billed quarterly, SSL and domain masking at $2 per domain per month or $6 per year. No free trial. Custom pricing for enterprise volume.

### Primeforge

Google Workspace and Microsoft 365 mailboxes. Short cycle is monthly.

| Volume | Billed monthly | Billed annually (effective) |
|---|---|---|
| 1 to 100 slots | $4.50/mailbox/month | $3.75/mailbox/month |
| 501 to 600 | $4.00 | $3.33 |
| 1,001+ | $3.50 | $2.92 |

Honest range: **$4.50 down to $3.50 per mailbox per month on monthly billing, or $3.75 down to $2.92 on annual.** Minimum 10 mailbox slots. Domains $14/year.

**No free trial**, and the reason is worth stating plainly: Primeforge is infrastructure, so you have to buy domains and mailboxes to use it. You can explore the app after signing up without buying anything.

### Warmforge

Per warm-up slot. The toggle is three-state and defaults to quarterly.

| Volume | Monthly | Quarterly | Annually |
|---|---|---|---|
| 1 to 10 slots | $12/slot/month | $10/slot/month | **$9/slot/month** |
| 51 to 100 | $10 | $8 | $5.25 |
| 1,001+ | $6 | $4 | $2.25 |

1 free warming slot on signup, plus 1 free placement test that renews monthly. Each paid slot includes AI warm up, DNS, MX and blacklist health checks, and 1 free placement test per month.

**Placement tests**, priced separately from slots:

| Plan | Allowance | Billed monthly | Billed annually |
|---|---|---|---|
| Pro | 100 tests/month, 50 mailboxes per test | $39/month | $32.50/month |
| Growth | Unlimited tests, 250 mailboxes per test | $169/month | $140.80/month |

No standalone free trial, since you need to buy slots to warm anything.

**Included free with Salesforge**, and this is the sharpest pricing point in the stack: a Salesforge subscription gets unlimited Warmforge mailbox slots at no extra cost, and covers any mailbox type rather than only Gmail and Outlook.

### Pre-warmed mailboxes

**Never publish a price for these.** Pre-warmed mailboxes on Infraforge and Primeforge are sold separately from the standard mailbox slots, and pricing is quoted in-app. No vendor marketing page carries a figure, and the two help-desk articles that do describe incompatible structures, so any number we print is a coin flip.

What you can say: pre-warmed mailboxes are available separately on both Infraforge and Primeforge, they ship ready to send on day one, and they save the standard two to four week warm up wait. Primeforge pre-warmed mailboxes have been warming for at least three months before you get them. For cost, point the reader to the app.

This also means pricing-math sections must not silently assume pre-warmed. If an article works out cost at scale, use the standard slot rates and say pre-warmed is extra.

---

## Subscription structure

Confirmed on salesforge.ai/stack: **each product is a separate subscription, and they share one login.** The vendor's own FAQ says "you need to have a separate subscription for each product" and separately that you can switch between products after logging in once.

Correct framings: "one login", "shared login", "no export or re-upload friction", "everything under one roof".

Banned framings: "one subscription", "no second subscription", "everything in a single plan", "data and outreach in one subscription".

The canonical stack URL is **salesforge.ai/stack**. The path /forge-stack returns a 404.

---

## Product facts

### Salesforge

Multichannel outreach platform running cold email and LinkedIn as coordinated channels inside one sequence and one inbox.

**Must-cover features**

- **Unlimited mailboxes, users, and workspaces.** No per-seat or per-mailbox pricing. Unlimited mailboxes on both plans. 1 LinkedIn sender on Pro, unlimited on Growth.
- **Multichannel with conditional sequences.** LinkedIn and email steps in one sequence with real if/then branching. If a connection request is accepted, send a LinkedIn message. If not, fall back to email. Not two parallel campaigns stitched together.
- **Six native LinkedIn actions:** connection requests, messages, InMails, post likes, follows, and withdraw requests. Each action type is capped at 30 per 24 hours per profile to stay inside LinkedIn's safe range. Each action uses 1 social action credit. A profile at full capacity needs roughly 400 to 500 social actions per month. Withdraw requests let a sequence clean up stale invites, which is how an actual SDR works the channel.
- **AI personalization across 21+ languages.** AI variables pull prospect-specific details like company news, LinkedIn activity, and industry context. Always "21+", never "20+".
- **LinkedIn account safety.** Actions route through high-quality shared proxies with optional custom proxy support. Authentication is session-token only, so the LinkedIn password is never stored. No Chrome extension injection, no DOM manipulation.
- **Primebox™ with Auto-Pilot and Co-Pilot modes.** Every email and LinkedIn reply lands in one inbox. Auto-Pilot handles replies end to end. Co-Pilot drafts them for a human to approve.
- **Free unlimited warm up via Warmforge.** Included with the subscription, unlimited slots, any mailbox type.
- **ESP matching** (Growth only). Sender and recipient matched by provider, Google to Google, Microsoft to Microsoft, for better inbox placement.
- **Sender rotation.** Volume spread across mailboxes and domains so no single mailbox burns its reputation.
- **Text-only content.** No heavy HTML, tracking pixels, or attachments by default.
- **Bounce Shield.** Blocks sends to addresses likely to bounce before reputation takes damage.
- **Built-in email validation.** Every contact validated before send.
- **A/B testing** (Growth only) plus campaign analytics on open, reply, positive reply, and meeting rates.
- **Agent Frank support.** Agent Frank can run the whole workflow autonomously.
- **Integrations and API.** 27 integrations listed on salesforge.ai/integrations, each with its own page. Growth plan only, along with API access. The native and mediated split is in the integrations subsection below, and the two are different claims that must never be blurred.
- **Salesforge MCP and CLI** (Growth only). Agent-native access from Claude, Cursor, or a custom agent.

**Two-layer framing, required in every multichannel article.** Anchor the piece in the category buyers actually search, then use the stack as the reason we win it.

- **The category: multichannel outreach platform.** This is what buyers compare inside. Direct competitors are Outreach, Salesloft, Reply.io, Lemlist, and LaGrowthMachine, plus stitched stacks like Instantly with Expandi bolted on.
- **The wedge: a deliverability-first outbound operating system.** Competitors sell the outreach layer alone. Salesforge comes with the deliverability layer (Warmforge), the infrastructure layer (Mailforge, Infraforge, Primeforge), the lead layer (Leadsforge), and the autonomous execution layer (Agent Frank).

Position Salesforge as the answer in the category, and pull wedge evidence to justify why.

**Which must-cover list governs.** The list above is the whole product. `rules/forge-positioning-guidelines.md` splits Salesforge into three sections, and the article type picks one of them as the checklist for the key features.

| Article type | Checklist section | Bullets |
|---|---|---|
| LinkedIn outreach alternatives | Salesforge: LinkedIn | 12 |
| Cold email tool alternatives | Salesforge: Cold Email | 16 |
| Multichannel, VS posts, category pages | Salesforge: Multichannel | 9 Category A, 8 Leaning B |

The key features carry one bullet per feature on the governing list, and the same number of bullets. Features on the other two lists are still true, and they go in the table, the prose, or the pricing paragraph when they earn a place. They do not pad the bullet list.

**How the Salesforge section is written.** Fixed by Jaimin on 2026-08-13. These are not suggestions.

- **The Best for line always opens "Best for GTM teams and Agencies".** Then continue with what the article is about. "Best for GTM teams and Agencies running LinkedIn and email in one platform, with unlimited mailboxes and unlimited LinkedIn senders on Growth."
- **The cons column carries exactly one point: "No free plan. A 14-day free trial is available."** One point, not four. Do not add a learning-curve con, a credit-cap con, or a plan-gating con, and do not pad the column to match the pros. Plan gating belongs in the pricing paragraph, where it reads as a fact rather than a complaint.
- **Every must-cover feature above appears somewhere in the section.** All of them. The comparison table rows carry a good share, and the key-features list carries the rest.
- **Cross-product stories are required in every comparison piece.** Under one roof, and two ways to run it, three with partners. See the cross-product section below.

### Integrations

Verified against salesforge.ai/integrations on 2026-08-13. The site carries 27 integration cards, each with a child page, and it labels every one **Native** or **Custom** through its own "Integration type" field. That split is the vendor's, not ours, so use it.

Of the 27, five are other Forge products, so **22 are genuinely third-party.**

**Native, OAuth straight from Salesforge:** HubSpot, Salesforce, GoHighLevel, Attio, Slack, Sendspark.

**Native, set up partner-side with a Salesforge API key:** Clay, folk, Databar.ai, Persana AI.

**Native, other shapes:** RB2B by first-party webhook, Breakcold as a marketplace app, Weezly in-sequence.

**Custom or mediated:** Zapier, Make, Bitscale, OutboundSync, plain webhooks, SMTP, and Pipedrive.

**Pipedrive is mediated, not native.** Its own page carries a Native label and mentions OAuth, then its How To Use It section opens by saying the integration is supported through Zapier or webhooks, and both routes described are a Zap or a webhook build. There is no Salesforge app in the Pipedrive Marketplace. Never call Pipedrive a native integration.

**Make** is labelled Custom while its body calls it "our native integration with Make". Sidestep the contradiction and call it an official Make app, which the Make directory confirms.

**Gating.** Integrations and API access are Growth-only. The Pro plan lists neither. One carve-out: connecting Google Workspace, Microsoft 365, and SMTP mailboxes, plus Warmforge warm up, is ungated, because Pro includes unlimited mailboxes and unlimited premium warm up. No individual third-party integration is available on Pro.

**n8n** has 10 templates at salesforge.ai/directory/n8n-templates but no card on the integrations page. Safe to mention as templates, not as a listed integration.

**Never write "1000+ integrations".** That is hero copy on the hub page. The documented count is 27.

### Leadsforge

AI-native lead finder. Plain-English chat instead of filter stacking.

**Must-cover features**

- **500M+ B2B contact database.** Returns verified emails, LinkedIn URLs, and mobile numbers.
- **Chat-based lead discovery.** Describe the ICP in a sentence and get a matching list. No boolean queries.
- **Company Lookalikes.** Feed it accounts you already close and it returns similar companies. Charged per company.
- **Company Followers search.** Give it a company domain and get the people following that page. The vendor calls these "company followers", so do not write "competitor followers".
- **Waterfall enrichment.** Each lookup cascades across multiple verified providers until it finds a match. Never name the underlying providers, because the site does not.
- **Signals, event-based sourcing.** Five signal types: **job change, acquisition, funding, investor, and hiring.** The workflow: pick Signals as the sourcing path, pick a signal type, set the provider-specific filters, see the estimated number of matching companies or contacts, extract with credits, review the per-match evidence in the Details view, then enrich and move the leads into the Enriched table. For company-based signals, Leadsforge finds matching companies, matches them against its database, then surfaces the relevant employees. Hiring signals carry company name, job title, department, seniority, date posted, open-until date, and the job posting URL. **Hiring signals are currently US-only.** Credits are charged at extraction based on how many companies or contacts you select, and enrichment costs more on top. Do not invent a fixed per-signal price.
- **API, MCP, and CLI** for programmatic access. The API key is generated in app settings.
- **Chrome extension** for enrichment while browsing LinkedIn or the web. Salesforge-branded and shared across the stack, not Leadsforge-only. **Free to install, and lookups consume Leadsforge credits** at the rates above, 1 per email and 10 per mobile number. New users get 100 free credits on Leadsforge signup.
- **Integrations.** Hands lists straight to Salesforge under the shared login with no export step, or exports to CSV in one click. HubSpot and Salesforce both have direct OAuth integrations with field mapping. Sourcing matters here: leadsforge.ai/integrations does not exist, and the marketing site answers the integrations question without naming a single partner. Both integrations are documented only in the help centre, so attribute them there and never say the site advertises them.

**Accuracy guardrail, confirmed against the live site:** Signals are event-based, and they are not topic intent. The words "researching" and "topic" appear nowhere on leadsforge.ai. Never describe Leadsforge as surfacing "accounts actively researching your category", and never imply it licenses a topic-intent feed. The nearest thing to category-level interest is the company followers feature, which is follower-based.

### Mailforge

Distributed shared email infrastructure for cold outreach. Setup in under five minutes with automated DNS and no server maintenance.

**Must-cover features:** shared IP pool built for cold email rather than everyday business mail, distributed across a pool used by 10,000+ businesses. Bulk domain and mailbox creation in minutes, with guided setup that works out how many you need for your target volume. Automated SPF, DKIM, DMARC, and custom domain tracking, with bulk DNS updates. Domain forwarding, so you can point secondary domains at your main site or a landing page from inside the platform, with no external registrar. Domain flexibility with no lock-in, in or out. Workspaces per project or client, with free movement between them. SSL and domain masking as an add-on. Works with any sending software, and natively with Salesforge under a shared login. MCP and CLI for agent-native provisioning.

### Infraforge

Private email infrastructure with dedicated IPs. Built for agencies and high-volume senders who want full control.

**Must-cover features:** dedicated IP per mailbox on dedicated servers, so reputation is yours alone and not shared with strangers in a pool. Pre-warmed mailboxes available separately for day-one sending, otherwise expect the standard two to four week warm up. Multi-IP provisioning, each IP with its own independent reputation, so one campaign's deliverability cannot drag down another. Unlimited domains and mailboxes with automated DNS. Bulk domain and mailbox generators. Domain forwarding from inside the platform. Real-time deliverability monitoring with live alerts. Masterbox for viewing every reply across a workspace in one place. SSL and domain masking. Workspaces. White-label for agencies and resellers. Infraforge API, MCP, and CLI. Native Salesforge integration.

### Primeforge

Real Google Workspace and Microsoft 365 mailboxes. The right pick when you want to match the provider your prospects already use.

**Must-cover features:** legitimate, properly configured Google Workspace and Microsoft 365 mailboxes, not repurposed accounts or EDU workarounds that break when a provider changes policy. Pre-warmed mailboxes available separately for day-one sending. ESP matching to land in the primary tab instead of promotions. Mail goes out through Google's and Microsoft's own sending infrastructure rather than a third-party SMTP relay, so you inherit the sender reputation of the two providers your prospects already trust. Automated SPF, DKIM, and DMARC. Domain forwarding from inside the platform. Mailbox profile branding out of the box, including profile pictures. Workspaces for organising across projects and clients. Works with any sending software, natively with Salesforge. Primeforge API, MCP, and CLI.

**Positioning tip for every infrastructure article:** Primeforge pairs with Mailforge or Infraforge for diversification. The teams that do best run two or more providers so they always have a matching mailbox for the prospect's inbox provider.

### Warmforge

Deliverability tool with premium warm up and inbox placement testing. Free and unlimited inside Salesforge, also sold standalone.

**Must-cover features:** one-click AI warm up, where AI-written emails mimic real conversation. Heat Score™ tracking per mailbox, so you know when a mailbox is safe to scale. Inbox placement tests across Google, Outlook, and others, showing whether mail lands in primary, promotions, or spam. Health checks on DNS, MX, and blacklist status with alerts. Multilingual warm up traffic. Works with Google Workspace, Microsoft 365, and IMAP or SMTP mailboxes from Mailforge and Infraforge. Included free with unlimited slots on any Salesforge plan.

**Accuracy guardrail on the pool.** The site claims the pool is made up **exclusively of aged accounts** and is **dominated by real Google Workspace and Microsoft 365 mailboxes**. Use that wording. Do not write "only Google Workspace and Microsoft 365", because "dominated by" is not "only". Do not describe the pool as containing IMAP or SMTP mailboxes either, because the site does not say that. There is one pool and it is premium by default, with no tiers and no paid upgrade.

### Agent Frank

Fully autonomous AI SDR that runs the whole outbound workflow using the Forge stack as its operating environment.

**Must-cover capabilities:** prospects continuously from the Leadsforge 500M+ database, enriches contact and company data before outreach, writes personalized email and LinkedIn messages, runs multichannel sequences and follow-ups, manages replies through Primebox™, books meetings on the rep's calendar, runs 24/7 without manual intervention. Base plan covers up to 1,000 active contacts. Available in 21+ languages. The pricing-page card reads 20+, and the fixed count across the stack is 21+, so write 21+. Comes with a dedicated account manager and a shared Slack channel.

Agent Frank is he/him. You hire him. He is an AI SDR, never a bot, an automation, or a workflow.

---

## Cross-product stories

Every comparison piece includes the first two. Use the others where they fit.

- **Under one roof.** No competitor offers infrastructure (Mailforge, Infraforge, Primeforge), deliverability (Warmforge), lead finding (Leadsforge), multichannel outreach (Salesforge), and an autonomous AI SDR (Agent Frank) as one connected stack under one login.
- **Warmforge is free with Salesforge.** Unlimited slots, any mailbox type. Every competitor that charges per warm-up slot on top of a sending tool is more expensive at the same functionality.
- **Three infrastructure options, one login.** Start on Mailforge for cost, move to Infraforge for dedicated control, add Primeforge for ESP matching, and never migrate off your Salesforge account.
- **Leadsforge feeds Salesforge directly.** Lists go from discovery to campaign in the same environment, with no CSV export.
- **Primebox™ unifies every reply.** One inbox for LinkedIn and email across the stack.
- **MCP-native across the stack.** Agent Frank, or your own agents, can operate every product through one protocol.
- **Two ways to run it, three with partners.** Your team operates it, Agent Frank operates it, or a Forge Expert agency operates it.

---

## Article-type playbooks

| Article type | Product to position | Lead with |
|---|---|---|
| Cold email tool alternatives | Salesforge | Warmforge free, Primebox™, three infrastructure options |
| LinkedIn outreach alternatives | Salesforge | Six native LinkedIn actions plus email in one sequence |
| B2B lead finder alternatives | Leadsforge | Chat-based finding plus direct Salesforge activation |
| Cold email infrastructure | Mailforge, Infraforge, or Primeforge | Three options under one login, move without migrating |
| Email warm-up alternatives | Warmforge | Aged-account pool, plus free and unlimited with Salesforge |
| AI SDR alternatives | Agent Frank | Runs on the whole stack, not a point tool |
| Best-of listicles | Whichever fits the category | Under one roof, as the closing argument and not the opener |
| Head-to-head comparisons | The Forge product in the URL | Ecosystem breadth against point-tool depth |

**Cold email angle.** Sending is a solved problem. The fight is deliverability and reply management. Competitors handle sending and leave you to bolt on infrastructure, warm up, lead data, and reply management from other vendors.

**LinkedIn angle.** Most LinkedIn tools stop at connection requests and messages. Few combine every native action with email in the same sequence, and none unify replies from both channels in one inbox.

**Lead finder angle.** Most tools give you filters and hope the intersection produces something useful. Leadsforge takes a sentence. And because the same company owns the outreach layer, lists get activated instead of sitting in a spreadsheet.

**Infrastructure angle.** Infrastructure is not one-size-fits-all. Shared, dedicated, and provider-native mailboxes each have a right moment. Owning all three means never migrating as you scale.

**Warm-up angle.** Every warm-up tool claims better deliverability. Warmforge adds Heat Score™, placement tests, and health checks, which makes it a deliverability console rather than only a warm-up tool. Then the cost story: free and unlimited with Salesforge, against per-slot pricing everywhere else.

**Best-of listicles.** These are not a place to pitch. They are a place to be the most useful reference on the internet for the category. Cover the obvious competitors, including Instantly, Smartlead, Apollo, and HubSpot Sales Hub. Skipping them makes the piece read as agenda-driven.

**Head-to-head.** The reader has already narrowed to two. Help them pick correctly instead of trashing the competitor. Name the parts where the competitor is genuinely better.

### First-party data and statistics posts

A separate article type, and the highest-authority thing this blog can publish, because the underlying data is ours and no competitor sitting outside the stack can reproduce it. Saleshandy's cold email statistics post is built on an analysis of 53.1 million cold emails sent through their platform, and it carries organic authority for their whole blog. We have equivalent or larger data across Warmforge, Mailforge, Infraforge, and Salesforge.

Article ideas that fit: reply-rate benchmarks by industry, team size, or sequence length from Salesforge send data. Deliverability benchmarks on bounce rate, spam rate, and primary placement from Warmforge placement tests plus infrastructure send logs. LinkedIn connection-accept and message-reply benchmarks. Heat Score™ progression and time-to-healthy from Warmforge. Agent Frank meetings booked per active contact. Cost per mailbox at scale across Mailforge, Infraforge, and Primeforge.

Required in every one of these:

- **A data methodology block right after the intro.** Name the dataset, the number of emails or sequences or accounts, the date range, and the filters applied. Pattern: "This analysis covers X million cold emails sent through Salesforge between [month] and [month], across N connected accounts and M sequences. Warm-up traffic and internal team emails were excluded."
- **First-party charts** built from the raw data by our own team, never lifted from a third-party market report. Make the underlying numbers available to readers who want to cite them.
- **A named data steward.** The person accountable for the dataset and reachable for methodology questions. With Frank as the byline this is usually Frank, but name whoever actually owns the numbers.
- **A comparison against public industry benchmarks** where they exist, with an honest explanation of why ours differ. Better warm up, tighter targeting, and a different sender profile are all legitimate reasons. Say which one applies.
- **An action per benchmark.** "Average reply rate is X percent" is a statistic. "The top decile hit Y percent and shared these three habits" is a benchmark. Close every benchmark section by telling the reader what to do about it.

Aim for four to six of these a year, roughly quarterly. Version the dataset and note what changed at each refresh. These get refreshed quarterly rather than annually, and they deserve distribution beyond the blog: a LinkedIn post from Frank carrying the two or three strongest charts, a drop to the Slack community, and at least one podcast or guest pitch built around the dataset.

---

## Open verification items

None currently open. Add one here the moment a fact looks uncertain, rather than shipping it and hoping.

## Resolved, do not re-open

**Auto-Pilot and Co-Pilot spelling.** Decided by Jaimin on 2026-08-13 in favour of the hyphenated, capitalised form, against the spelling in the positioning guidelines doc. The guidelines have been corrected in all nine places, and `lint/data/spellings.txt` now blocks `Autopilot`, `autopilot`, `AutoPilot`, `Auto-pilot`, `Copilot`, `copilot`, `CoPilot` and `Co-pilot` case-sensitively. This is the one case where `rules/writing.md` overturned a locked feature name, and it went that way because the guidelines' own do-not-paraphrase list never contained Autopilot.

**Waalaxy has no free plan, and Pro is $16 per user per month billed annually.** Decided by Jaimin on 2026-08-13 in favour of the live page over the comparison-table template, which shows a free plan at 80 invites a month and roughly EUR 9.50. Read on waalaxy.com/pricing on 2026-08-13: the rendered page carries no "free plan", "freemium" or "free forever" anywhere, only a 14-day trial on all three tiers. Two further traps came out of the same check. Waalaxy is serving more than one version of that page, one with a Monthly, Quarterly -20%, Yearly -50% toggle and one with Monthly, Yearly -20%, which is where the stray euro figures came from. So screenshot the toggle rather than quoting a discount percentage, and treat the yearly tab as the default view. Pro is capped at 300 invitations a month and the 800 ceiling starts at Advanced.

**Integrations.** Verified against salesforge.ai/integrations on 2026-08-13. Every one of the 18 names carried by the old positioning doc turned out to be real and vendor-documented, so the list was accurate and the earlier decision to cut it back to three was wrong. Two things had gone wrong in the other direction: the claim that salesforge.ai/pricing confirms HubSpot and Pipedrive came from a false positive, since those strings live inside a HubSpot booking-tracker script in the page head and the pricing page names no partner at all. And Pipedrive is mediated rather than native, on the evidence of its own page. Details in the integrations subsection above.

**AI personalization language count.** Use **"21+ languages"**, never "20+". Reversed by Jaimin on 2026-08-13 when the Forge Stack Positioning Guidelines landed, which fix 21+ in their own do-not-paraphrase list. The earlier entry in this slot had chosen "20+" as the vendor's own site phrasing. The guidelines are the prescriptive layer, so they win. The linter now bans "20+ languages".

**Pre-warmed mailbox pricing.** Decided by Jaimin on 2026-08-13: never print a figure. See the pre-warmed section above.

**LinkedIn actions.** Six: connection requests, messages, InMails, post likes, follows, **withdraw requests**. Reversed by Jaimin on 2026-08-13. The earlier entry in this slot named profile views as the sixth and said withdraw requests must not be added back. Two independent signals overturned it on the same day: the Forge Stack Positioning Guidelines list withdraw requests, and Jaimin's own comparison-table template lists "Connection, message, InMail, like, follow, withdraw". Profile views is now the banned one, and the linter flags it next to Salesforge.

**Chrome extension credit consumption.** Verified by Jaimin directly in-app on 2026-08-13: the extension is free to install and lookups do consume Leadsforge credits, 1 per email and 10 per mobile. Recorded here because the Chrome Web Store listing says "Free Unlimited contact lookups", which contradicts it. That listing is marketing copy, and in-app behaviour wins. Do not "correct" this back off the store page.
