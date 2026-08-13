# Forge Stack Product Positioning Guidelines

Handed down by Jaimin on 2026-08-13 as a locked reference. Read it before writing any sentence that names a Forge product, a Forge feature, or a Forge price.

## Precedence, and how this file sits next to `rules/positioning.md`

Two files now carry Forge facts. They do different jobs and the split is deliberate.

- **This file wins on** feature names, feature descriptions, must-cover checklists, positioning statements, cross-product stories, and the article-type playbooks. It is prescriptive.
- **`rules/positioning.md` wins on** live-verified prices, verification dates, the pricing traps, and the resolved-decision log. It is the evidence layer, re-checked against vendor pages.

Where they disagree on anything else, flag it rather than picking silently.

## Reconciliation log, 2026-08-13

Nine conflicts surfaced when this file landed. Each one is resolved below. Do not re-litigate them without changing this section.

**Resolved in favour of this file, reversing an earlier decision.**

1. **AI personalization language count.** This file fixes `21+ languages`, never `20+`. That reverses Jaimin's 2026-08-13 entry in `rules/positioning.md`, which had chosen `20+` as the vendor's own phrasing. The linter now bans `20+ languages`.
2. **The six native LinkedIn actions.** Connection requests, messages, InMails, post likes, follows, and **withdraw requests**. That reverses the 2026-08-13 entry which named profile views as the sixth and said withdraw requests must not be added back. Jaimin's comparison-table template corroborates withdraw, so two independent signals agree. The linter now flags profile views as a Salesforge action.

**Resolved in favour of `rules/positioning.md`, because the live page is more specific.**

3. **Agent Frank pricing.** This file says "from $499/month, billed quarterly". The live page has two different $499s: $499/month billed annually on the headline card, and a separate 1,000-contact add-on slider. Quarterly is $599/month. Use $499/month billed annually.
4. **Pipedrive.** Jaimin's comparison-table template lists Pipedrive under native integrations. Its own vendor page describes a Zapier or webhook build, and there is no Salesforge app in the Pipedrive marketplace. Pipedrive stays mediated, never native.
5. **Delivery models.** This file's Delivery models section lists two ways to run the stack and then calls it a three-way model. The third is a Forge Expert agency, named in the cross-product section. Write it as "two ways to run it, three with partners".
6. **Salesforge plan prices.** This file lists Pro $48 and Growth $96, which are the monthly-billing rates. Articles quote annual only, so Pro is $40/month and Growth is $80/month, both billed annually.

**Open, awaiting Jaimin.**

7. **Autopilot spelling.** This file writes "Autopilot and Co-pilot modes". `rules/writing.md` section 20 and the linter require "Auto-Pilot" and "Co-Pilot" and explicitly ban "Autopilot". Autopilot is not in this file's own fixed-names list, so the drafts keep Auto-Pilot and Co-Pilot until Jaimin picks one.
8. **Localized Greeting variable.** Jaimin's comparison-table template pairs it with the 21+ languages claim. No Forge page and neither positioning file documents it, so it is left out of drafts until it can be verified.
9. **Waalaxy pricing and free plan.** Jaimin's comparison-table template shows a free plan at 80 invites a month and Pro at roughly EUR 9.50 billed annually. The live page read on 2026-08-13 showed USD 16 per user annually and no free tier, and Waalaxy is serving more than one version of that page. The verified live figure stands in drafts and the free-plan claim is cut until it can be confirmed.

## Purpose
This document is the positioning reference for the full Forge Stack.
It is prescriptive, not advisory. Every feature name, feature description, product positioning statement, and cross-product story in this document is locked in. Writers don't copy word-for-word but reword as per sentence cadence and never for meaning.
If a writer wants to change how a feature is described, that requires a review and update to this document first, not a one-off variation inside an article.
## How to use this document
Feature names are fixed. Do not paraphrase.
- "Bounce Shield" is always "Bounce Shield," never "bounce protection" or "bounce filter"
- "Primebox™" always carries the trademark, never "Prime Inbox" or "unified inbox tool"
- "Heat Score™" always carries the trademark
- "AI personalization across 21+ languages" always uses 21+, never 20+ or "many languages"
- "Waterfall enrichment" is always "waterfall enrichment," never "cascade enrichment" or "sequential enrichment"
- "ESP matching" is always "ESP matching," never "provider matching" or "inbox provider pairing"
Feature descriptions are fixed. The 1-3 sentence descriptions in each product section are the canonical narrative. Minor cadence tweaks are fine. Rewriting the substance is not.
Every product section is a must-cover checklist. When a product is featured in an article, every must-cover feature in that product's section must appear somewhere in the piece. Not most. All.
Cross-product stories must be included. Every comparison piece must include the "under one roof" story and the two-way delivery model. See the Cross-product advantages section.
Style rules that override everything:
- No em dashes anywhere
- No AI filler phrases
- Titles under 55 characters
- TL;DR after every intro
- Final Verdict before FAQ
- First-person practitioner voice
Applying this document to article types. See the "Positioning playbooks by article type" section at the end for exactly which product to position, which features to highlight for each of these article types:
- Cold email tool alternatives
- LinkedIn outreach tool alternatives
- B2B lead finder tool alternatives
- Cold email infrastructure alternatives
- Email warmup tool alternatives
- Best-of listicles and category pages
- Head-to-head comparisons (Salesforge vs X)
## Overview
Forge Stack is a multi-product outbound sales platform. This document covers positioning for:
- Salesforge (LinkedIn and Cold Email channels)
- Leadsforge (AI lead finder)
- Mailforge (shared email infrastructure)
- Infraforge (private email infrastructure with pre-warmed mailboxes)
- Primeforge (Google Workspace and Microsoft 365 mailboxes with option for prewarmed)
- Warmforge (premium email warmup, included with Salesforge)
- Agent Frank (autonomous AI SDR)
- Pricing and delivery models
- Positioning playbooks by article type
## Salesforge: LinkedIn
Positioning statement (paraphrase, do not copy verbatim): Salesforge is a multichannel outreach platform that runs cold email and LinkedIn as coordinated channels inside one sequence and one unified inbox. This section covers the LinkedIn side: native LinkedIn actions, account safety infrastructure, and how LinkedIn touches plug into the same sequence as cold email.
### Must-cover features
- Unlimited senders and mailboxes: No per-seat or per-mailbox caps on senders. Teams can plug in 1 LinkedIn account (on Pro plan) and unlimited LinkedIn accounts and connected mailboxes (on Growth plan) they own without paying more as headcount grows.
- Multichannel with conditional sequences: LinkedIn steps branch based on prospect behavior (accepted, replied, viewed profile, and so on) and combine with email touches inside the same sequence. Actual if/then logic, not linear "email then LinkedIn" chains. Example: if a connection request gets accepted, trigger a LinkedIn message. If it does not, fall back to email.
- AI personalization across 21+ languages: Every message can be personalized at scale with AI. AI variables pull prospect-specific details like company news, LinkedIn activity, and industry context. Native support for 21+ languages so localized campaigns run without a separate copywriter per region.
- Native LinkedIn actions: Six native LinkedIn actions available inside a sequence, which are connection requests, messages, InMails, post likes, follows, and withdraw requests. This lets sequences mimic how an actual SDR works on LinkedIn: warm up the profile, engage before pitching, and clean up stale invites. Each action type is capped at 30 per day per profile to stay within LinkedIn's safe usage thresholds.
- Account safety as standard: All LinkedIn actions route through high-quality shared proxies, with optional custom proxy support. Authentication is session-token-only, so the user's LinkedIn password is never stored. Daily action limits are conservative and mimic human behavior patterns. No Chrome extension injection, no DOM manipulation. LinkedIn accounts stay safe long-term.
- Primebox™ with Autopilot and Co-pilot modes: All LinkedIn and email replies land in one inbox. Autopilot lets AI handle replies end-to-end. Co-pilot drafts replies for a human to approve before sending.
- LinkedIn email & phone finder Chrome Extension: Extracts verified emails from LinkedIn profiles and searches. Powered by Leadsforge: connects to the user's Leadsforge account and pulls from the 500M+ contact database. New users get 100 free credits on signup, additional lookups use Leadsforge credits.
- Testing and analytics: A/B testing on messaging variants (Growth plan only), plus campaign-level analytics covering send volume, connect rate, reply rate, and meeting conversion.
- Agent Frank support: Agent Frank can operate the entire email and LinkedIn workflow autonomously: prospecting, sequencing, replying, and booking meetings 24/7.
- API: Open API access (Growth plan) for programmatic control over sequences, contacts, and campaigns.
- Integrations: Native integrations across CRMs (HubSpot, Salesforce, Pipedrive, HighLevel, Breakcold, Attio, Folk), data providers (Clay, Bitscale, RB2B, Databar AI, Persana AI, Sendspark, Weezly), and automation platforms (Slack, Zapier, Make, Webhooks).
- MCP CLI: Agent-native access via Claude, Cursor, or custom agents. Create sequences, manage contacts, and trigger actions directly from AI workflows with scripted campaign operations.
## Salesforge: Cold Email
Positioning statement (paraphrase, do not copy verbatim): Salesforge is a multichannel outreach platform that runs cold email and LinkedIn as coordinated channels inside one sequence and one inbox. This section covers the Cold Email side: sender scale, premium deliverability, contact enrichment, and how email touches plug into the same sequence as LinkedIn.
### Must-cover features
- Unlimited mailboxes, users, and workspaces: Teams and agencies can run any number of clients, sending accounts, and operators without hitting seat limits.
- Multichannel with conditional sequences: Cold email steps combine with LinkedIn touches in a single logic-driven sequence.
- AI personalization across 21+ languages: Every email can be AI-personalized at scale using AI variables that pull prospect-specific details like company news, LinkedIn activity, and industry context.
- Unlimited warmup via Warmforge: Every connected mailbox is warmed for free using the native Forge Stack warmup product. Warmup and sending live in the same environment.
- ESP matching: Sender and recipient mailboxes are matched by email service provider to improve inbox placement (Google to Google, Microsoft to Microsoft).
- Text-only content: Emails ship without heavy HTML, tracking pixels, or attachments by default. Cleaner payload, better inboxing.
- Sender rotation: Volume is distributed across multiple sending mailboxes and domains automatically so no single mailbox burns through reputation.
- Bounce Shield: Blocks sends to addresses likely to bounce, protecting sender reputation before it gets damaged.
- Built-in email validation: Every contact is validated before send to keep bounce rates low.
- Primebox™ with Autopilot and Co-pilot modes: All replies across mailboxes and channels flow into one inbox. Autopilot handles replies fully. Co-pilot drafts responses for human approval.
- LinkedIn email & phone finder Chrome Extension: Finds verified email addresses directly from LinkedIn. Powered by Leadsforge: connects to the user's Leadsforge account and pulls from the 500M+ contact database. New users get 100 free credits on signup, additional lookups use Leadsforge credits.
- Testing and analytics: A/B testing on subject lines and body variants, plus campaign performance tracking on open, reply, positive reply, and meeting rates.
- Agent Frank support: Agent Frank runs the full cold email workflow autonomously: prospecting, sequencing, replying, and booking meetings 24/7.
- API: Open API access (Growth plan) for programmatic control over sequences, contacts, and campaigns.
- Integrations: Native integrations across CRMs (HubSpot, Salesforce, Pipedrive, HighLevel, Breakcold, Attio, Folk), data providers (Clay, Bitscale, RB2B, Databar AI, Persana AI, Sendspark, Weezly), and automation platforms (Slack, Zapier, Make, Webhooks).
- MCP CLI: Agent-native access via Claude, Cursor, or custom agents. Create sequences, manage contacts, and trigger actions directly from AI workflows with scripted campaign operations.
## Salesforge: Multichannel
Positioning statement (paraphrase, do not copy verbatim): Salesforge sells as a multichannel outreach platform where cold email and LinkedIn are two channels of one workflow, not two products stitched together. What separates it from other multichannel platforms is the wider Forge Stack behind it: infrastructure (Mailforge, Infraforge, Primeforge), warmup (Warmforge), lead finder (Leadsforge), and an autonomous SDR (Agent Frank) all sit under one login (separate subscriptions).
### Category A / Leaning B framing (must anchor every multichannel article)
- Category A: Multichannel outreach platform. This is the category buyers search for and compare inside. Direct competitors: Outreach, Salesloft, Reply.io, Lemlist, LaGrowthMachine, plus stitched-together stacks like Instantly + Expandi.
- Leaning B: Deliverability-first outbound operating system. This is where Salesforge differentiates. Competitors sell the outreach layer only. Salesforge bundles the deliverability layer (Warmforge), the infrastructure layer (Mailforge, Infraforge, Primeforge), the lead finder layer (Leadsforge), and the autonomous execution layer (Agent Frank) with the outreach product.
Every multichannel article positions Salesforge as the answer in Category A while pulling Leaning B evidence to justify why it wins the category.
### Category A must-cover features (the multichannel platform)
- Multichannel with conditional sequences: LinkedIn and cold email steps run inside a single sequence with actual if/then logic. Example: if a connection request gets accepted, trigger a LinkedIn message. If it does not, fall back to email. Not two parallel campaigns manually stitched together, one sequence with branching logic.
- Six native LinkedIn actions plus email in one flow: Connection requests, messages, InMails, post likes, follows, withdraw requests, and cold email touches all executable within the same sequence.
- AI personalization across 21+ languages: Same AI variables work for both LinkedIn messages and cold email copy. Company news, LinkedIn activity, industry context. 21+ languages so localized campaigns run without a separate copywriter per region.
- Primebox™ with Autopilot and Co-pilot modes: All LinkedIn and email replies land in one inbox. Autopilot handles routine replies end-to-end. Co-pilot drafts responses for a human to approve. One place instead of switching between LinkedIn tabs and email clients.
- A/B testing and cross-channel analytics: A/B test messaging variants across both channels (Growth plan). Analytics cover open rate, reply rate, connection acceptance rate, and meeting conversion in one dashboard.
- LinkedIn email & phone finder Chrome Extension: Powered by Leadsforge. Bridges LinkedIn prospecting into email outreach without leaving the workflow.
- Unified pricing: One subscription covers both channels. No separate LinkedIn tool license, no separate email tool license.
- API: Open API access (Growth plan) for programmatic control over sequences, contacts, and campaigns.
- Integrations: Native integrations across CRMs (HubSpot, Salesforce, Pipedrive, HighLevel, Breakcold, Attio, Folk), data providers (Clay, Bitscale, RB2B, Databar AI, Persana AI, Sendspark, Weezly), and automation platforms (Slack, Zapier, Make, Webhooks).
### Leaning B must-cover features (the outbound operating system)
- Warmforge included free: Every mailbox is warmed continuously using the Warmforge premium pool (aged Google Workspace and Microsoft 365 mailboxes only). Unlimited warmup slots on both Pro and Growth. No competitor bundles a premium warmup product for free.
- Three infrastructure options under one login: Mailforge (shared), Infraforge (dedicated with pre-warmed mailboxes), Primeforge (Google Workspace and Microsoft 365 with ESP matching). Move between them as scale and budget shift without switching platforms or migrating.
- Leadsforge integration: Chat-based B2B lead discovery with 500M+ contacts, waterfall enrichment, and intent signals feeds directly into Salesforge sequences. No CSV exports.
- Agent Frank: Autonomous AI SDR that runs the entire multichannel workflow end-to-end. Prospecting, sequencing, replying, meeting booking, 24/7.
- MCP-native across the stack: Every Forge product exposes an MCP server, so Claude, Cursor, or custom agents can operate Salesforge, Warmforge, Leadsforge, and the infrastructure products through a single protocol.
- Three-way delivery model: Same product runs three ways: team operates it, Agent Frank operates it, or a Forge Expert agency operates it. No competitor matches this.
- API: Open API access (Growth plan) for programmatic control over sequences, contacts, and campaigns.
- Integrations: Native integrations across CRMs (HubSpot, Salesforce, Pipedrive, HighLevel, Breakcold, Attio, Folk), data providers (Clay, Bitscale, RB2B, Databar AI, Persana AI, Sendspark, Weezly), and automation platforms (Slack, Zapier, Make, Webhooks).
## Leadsforge
Positioning statement (paraphrase, do not copy verbatim): An AI-native lead finder platform that turns natural language into targeted B2B lists, backed by a 500M+ contact database, waterfall enrichment, and intent signals.
### Must-cover features
- 500M+ B2B contact database: Contact and company data at a scale competitive with the largest incumbents.
- Chat-based lead discovery: Users describe their ICP in plain English and Leadsforge returns a matching list. No filter stacking, no boolean queries.
- Company Lookalikes: Feed Leadsforge a set of accounts you already close and it surfaces similar companies based on firmographic and behavioral signals.
- Competitor Followers Search: Pull the list of people following your competitors so you can target their exact audience.
- Waterfall enrichment: For every contact, Leadsforge queries multiple data providers in sequence to fill in emails, phone numbers, and other fields at maximum coverage and confidence.
- Intent signals: Build lead lists from real buying signals like funding rounds, acquisitions, job changes, new investments, and tech stack shifts. Filter each signal by location, industry, company size, and role to narrow down to accounts that are actually in-market. Every match comes with proof from public sources (company pages, news, posts) so outreach lands in the buying window instead of guessing.
- API, MCP, and CLI: for programmatic access
- Chrome Extension: for on-the-fly enrichment during LinkedIn or web browsing. Extension is free to install; enrichment uses Leadsforge credits. New users get 100 free credits on signup
- Integrations: across the Forge Stack (Salesforge, Warmforge, Agent Frank) and third-party CRMs and tools
## Mailforge
Positioning statement (paraphrase, do not copy verbatim): Distributed shared email infrastructure for cold outreach. Ideal when starting out, scaling fast, or expecting higher complaint volume. Full setup in under five minutes with automated DNS and zero server maintenance.
### Must-cover features
- Shared IPs made for cold outreach: Shared infrastructure model similar to Gmail or Outlook, but designed specifically for cold outreach rather than everyday business email. Mailbox accounts distributed across a pool used by 10,000+ businesses.
- Bulk domain and mailbox creation: Create hundreds or thousands of domains and mailboxes in minutes. Guided setup calculates how many domains and mailboxes are needed based on target sending volume.
- Automated DNS and email authentication: Every domain gets automated setup of SPF, DKIM, DMARC, and custom domain tracking following industry best practices. Bulk DNS updates in a few clicks.
- Domain forwarding: Redirect secondary domains to your primary website or a designated landing page. Handled inside the platform alongside DNS setup, no external registrar or third-party tools required.
- Domain flexibility: Add domains to Mailforge or transfer them to and from other providers. No lock-in.
- Workspaces: Separate workspaces per project or client. Move domains and mailboxes between workspaces freely.
- SSL and Domain Masking (add-on): Display branded websites without revealing the primary domain. SSL and domain masking available as an add-on for full security and privacy at scale.
- Tool integration: Works with any sending software. Native integration with Salesforge (shared login, domains flow directly into sequences with no export step).
- MCP CLI: for agent-native provisioning from Claude, Cursor, and other AI clients with scripted management
### Pricing
- $3 to $2 per mailbox per month, billed annually (price drops at volume)
- Minimum 10 mailbox slots
- Domains priced separately by TLD
- SSL and Domain Masking: $2 per domain per month, or $6 per domain per year
## Infraforge
Positioning statement (paraphrase, do not copy verbatim): Private email infrastructure with dedicated IPs and pre-warmed mailboxes (sold separately). Built for agencies and pros who want total control, performance at scale, and immediate sending without a two-to-four week warmup wait when they buy prewarmed mailboxes. Otherwise, they need to perform a 2-4 week email warmup.
### Must-cover features
- Dedicated IP infrastructure: Every mailbox runs on dedicated servers with its own IP address. Sender reputation is fully under the customer's control, not shared with other senders.
- Pre-warmed mailboxes: Ready-to-send mailboxes and domains available on day one. Skip the standard two-to-four week warmup wait before running live campaigns.
- Multi-IP provisioning: Assign multiple dedicated IPs per account, each with its own independent reputation. High-volume senders can segment campaigns or client workloads across separate IPs so one campaign's deliverability does not affect another.
- Unlimited domains and mailboxes: Set up unlimited domains and mailboxes with automated DNS and email authentication (DMARC, SPF, DKIM).
- Bulk generators: Bulk domain generator creates multiple domains in one click. Mailbox auto-generator builds multiple inboxes at once for high-volume outreach setups.
- Domain forwarding: Redirect secondary domains to your primary website or a designated landing page. Handled inside the platform alongside DNS setup, no external registrar or third-party tools required.
- Real-time deliverability monitoring: Live alerts and monitoring on every mailbox so issues are caught before they burn a domain.
- Masterbox: See all emails across all your accounts within a workspace in one simple view. No more checking individual mailboxes to keep up with replies at scale.
- SSL and domain masking: Secure redirection and domain masking to protect the primary brand domain.
- Workspaces: Project-level organization with easy movement of domains and mailboxes between workspaces.
- White-label option: Full rebranding available for agencies and resellers who want to run Infraforge under their own brand.
- Infraforge API: Full programmatic control over mailboxes, domains, and IPs
- Forge MCP CLI: Agent-native provisioning with scripted management
- Direct native integration: with Salesforge and any other sending tool
### Pricing
- $4 to $3 per mailbox per month, billed annually (price drops at volume)
- First domain and mailbox live in about 5 minutes
- Custom pricing available for enterprise volume
## Primeforge
Positioning statement (paraphrase, do not copy verbatim): Google Workspace and Microsoft 365 mailboxes with an option to buy prewarmed inboxes to skip warmup waiting period. The gold standard for cold outreach when the goal is to match the mailbox provider your prospects already use.
### Must-cover features
- Real Google Workspace and Microsoft 365 mailboxes: Legitimate, properly configured mailboxes on the two providers most prospects use. Not repurposed accounts, EDU workarounds, or shady loopholes that break the moment a provider updates its policies.
- Pre-warmed mailboxes: Mailboxes are ready to send from day one. No manual warmup required to start outreach. Sold separately.
- ESP Matching: Send from the same provider your recipient uses (Google to Google, Microsoft to Microsoft) to boost primary inbox placement and avoid the promotions tab.
- Automated DNS setup: SPF, DKIM, and DMARC configured automatically on every domain. No manual DNS work.
- Mailbox profile branding: Profile pictures, GIFs, and profile setup handled out of the box to add legitimacy to the sender identity.
- Domain forwarding: Redirect secondary domains to your primary website or a designated landing page. Handled inside the platform alongside DNS setup, no external registrar or third-party tools required.
- Workspaces: Multi-workspace support for organizing mailboxes across projects and clients.
- Tool integration: Works with any sending software. Native Salesforge integration means shared login and no export step.
- Primeforge API: for automated mailbox provisioning
- Forge MCP CLI: for agent-native access with scripted management
### Pricing
- $4.50 to $3.50 per mailbox per month, billed annually (price drops at volume)
- First mailbox live in about 30 minutes
- No free trial (mailboxes must be purchased) but the app is free to explore before buying
### Positioning tip (must include into infrastructure content)
Primeforge is best paired with Mailforge or Infraforge for diversification. The most successful teams run two or more ESPs so they always have a matching mailbox for their prospect's inbox provider. This is a key upsell angle in every infrastructure comparison piece.
## Warmforge
Positioning statement (paraphrase, do not copy verbatim): Email deliverability tool with premium warmup with inbox placement. Included free with every Salesforge plan (unlimited warmup slots). Also available standalone for teams warming mailboxes outside the stack.
### Must-cover features
- One-click AI email warmup: Connect a mailbox, click once, warmup starts automatically. AI-written emails mimic real human conversation to signal legitimacy to inbox providers.
- Premium warmup pool: The warmup pool contains a mix of SMTP, Google Workspace and Microsoft 365 mailboxes.
- Multilingual warmup activity: Warmup emails generated across multiple languages so activity looks natural to inbox providers worldwide, not just English-heavy patterns.
- Heat Score™ tracking: Every mailbox has a Heat Score that indicates reputation strength over time. Clear signal for when a mailbox is safe to scale sending volume on.
- Inbox Placement Tests: Run placement tests across major ESPs (Google, Outlook, and others) to see exactly where emails are landing (primary, promotions, or spam) before campaigns go live.
- Health Checks: Automated monitoring of DNS records, MX records, and blacklist status for every mailbox. Alerts on any potential spam risks.
- Mailbox compatibility: Works with Google Workspace and Microsoft 365 mailboxes and even IMAP/SMTP mailboxes from Mailforge and Infraforge.
- Included with Salesforge: Salesforge subscribers get unlimited warmup slots at no additional cost. This is a key positioning point against every competitor that charges per warmup slot on top of a sending tool.
### Pricing (standalone)
- Warmup: $9 per mailbox slot per month, billed annually. 1 free slot on signup. Each slot includes AI warmup, DNS/MX/blacklist checks, and 1 free placement test per month
- Placement Test Pro: $32.50 per month, billed annually (100 tests, up to 50 mailboxes per test)
- Placement Test Growth: $140.80 per month, billed annually (unlimited tests, up to 250 mailboxes per test)
- Included with Salesforge: unlimited warmup slots at no additional cost
## Salesforge Pricing (must reflect current pricing on every article)
- Pro: $48/month, 1,000 contacts, 5,000 emails/month, 1 user, unlimited mailboxes
- Growth: $96/month, 10,000 contacts, 50,000 emails/month, unlimited users, multiple LinkedIn accounts and senders
- Agent Frank: from $499/month, billed quarterly
- All paid plans include: unlimited warmup (via Warmforge), mailbox rotation, dynamic IPs, email validation, Primebox
- Included on both Pro and Growth: unlimited premium warmup via Warmforge, smart mailbox rotation, Primebox™, 14-day free trial with no credit card required.
- Growth-only features (must call out in comparison content): A/B testing, multi-language sequences, ESP matching, API access, unlimited LinkedIn senders, unlimited users.
- 14-day free trial, no credit card required
Infrastructure product pricing (Mailforge, Infraforge, Primeforge) and standalone Warmforge pricing appear in each product section above.
## Delivery models (must call out in top-of-funnel content)
Every top-of-funnel article should surface that customers can run the Forge Stack two ways:
- Their own team operates it. DIY, standard SaaS.
- Agent Frank operates it. Autonomous AI SDR runs the workflow end-to-end.
This three-way delivery model is a positioning differentiator no direct competitor matches.
## Cross-product advantages (must cover into every comparison piece)
- Leadsforge feeds Salesforge directly: Lists move from discovery to campaign in the same environment. No CSV export required.
- Warmforge warms every mailbox for free with Salesforge: Deliverability infrastructure is included, not a paid add-on.
- Three infrastructure options under one login: Primeforge, Mailforge, and Infraforge run from a single Salesforge account. Move between them as scale and budget shift without switching tools or migrating.
- Primebox™ unifies every reply: One inbox for LinkedIn and email replies across the stack.
- MCP-native across every product: Agent Frank, or the customer's own agents, can operate the entire platform through a single protocol.
- Three-way delivery model: Team-run, agent-run, or agency-run. No direct competitor matches this.
- The "under one roof" story: No competitor offers infrastructure (Primeforge, Mailforge, Infraforge), deliverability (Warmforge), lead finder (Leadsforge), multichannel outreach (Salesforge), and an autonomous AI SDR (Agent Frank) as one integrated stack. That is the core Forge Stack positioning story.
## Agent Frank
Positioning statement (paraphrase, do not copy verbatim): A fully autonomous AI SDR that runs the entire outbound workflow end-to-end, using the full Forge Stack as its operating environment.
### Must-cover capabilities
- Prospects continuously from the Leadsforge 500M+ database
- Enriches contact and company data before outreach
- Writes personalized email and LinkedIn messages using AI
- Runs multichannel sequences and handles follow-ups
- Manages replies through Primebox
- Books meetings directly on the rep's calendar
- Runs 24/7 without manual intervention
- Base plan handles up to 1,000 active contacts
## Positioning playbooks by article type
#### NOTE - This is just for reference, don't copy paste, and shuffle the features in every article.
Each playbook below defines exactly which product to position, which features to cover, what narrative to use, and how the intro and verdict should sound.
Sample paragraphs are illustrative patterns showing the shape to hit; feature checklists and narrative angles are fixed.
## Playbook 1: Cold email tool alternatives
Examples of this article type: "Instantly alternatives," "Smartlead alternatives," "Lemlist alternatives," "Apollo alternatives," "Woodpecker alternatives," "Mailshake alternatives," "Reply.io alternatives," "Outreach.io alternatives," "Salesloft alternatives"
Product to position: Salesforge (Cold Email)
Supporting products/features to cover in throughout the piece:
- Warmforge (included free with Salesforge, unlimited warmup slots)
- Leadsforge (waterfall enrichment, LinkedIn email & phone finder Chrome Extension)
- Mailforge, Infraforge, Primeforge (three infrastructure options under one login)
- Agent Frank (autonomous AI SDR)
- Primebox™ (unified inbox for LinkedIn and email)
Fixed features to cover:
- Unlimited mailboxes, users, and workspaces
- AI personalization across 21+ languages
- Unlimited warmup via Warmforge
- ESP matching
- Text-only content
- Sender rotation
- Bounce Shield
- Built-in email validation
- Domain reputation and inbox placement monitoring
- Waterfall enrichment
- Primebox™ with Autopilot and Co-pilot modes
- Multichannel with conditional sequences
- LinkedIn email & phone finder Chrome Extension (powered by Leadsforge)
- A/B testing and campaign analytics
- Agent Frank support
- CRM integrations (HubSpot, Pipedrive, API), MCP, CLI
Narrative angle:
Most cold email tools handle sending. That is where they stop. The writer's job is to show that competitor X handles part of the workflow well but leaves the customer to bolt on infrastructure, warmup, lead finder, and reply management from other vendors. Salesforge, running on the full Forge Stack, handles all of that in one product with one login. However, the narrative angle will depend on the specific tool alternative article we're writing.
The core positioning story: sending is a solved problem. The fight in 2026 is deliverability and reply management. Salesforge wins on deliverability (Warmforge included free, ESP matching, Bounce Shield, sender rotation, text-only, domain monitoring) and reply management (Primebox with Autopilot and Co-pilot).
Common competitor weak points to compare against:
- Warmup as a paid add-on or third-party bolt-on
- No native LinkedIn support in the same sequence
- No first-party infrastructure product (customers bring their own mailboxes)
- Reply inbox that only covers email, not LinkedIn
- No autonomous SDR option
- Seat limits on higher plans (users, workspaces, or mailboxes)
## Playbook 2: LinkedIn outreach tool alternatives
Examples of this article type: "Expandi alternatives," "Dux-Soup alternatives," "Waalaxy alternatives," "HeyReach alternatives," "Dripify alternatives," "MeetAlfred alternatives," "Lemlist alternatives (LinkedIn side)," "LaGrowthMachine alternatives"
Product to position: Salesforge (LinkedIn)
Supporting products to cover in:
- Leadsforge (LinkedIn email & phone finder Chrome Extension, Competitor Followers Search)
- Warmforge (for the email side of multichannel sequences)
- Agent Frank (autonomous LinkedIn + email SDR)
- Primebox™ (unified LinkedIn and email replies)
Fixed features to cover:
- Unlimited senders and mailboxes
- Multichannel with conditional sequences (LinkedIn + email in one flow)
- AI personalization across 21+ languages
- Six native LinkedIn actions (connection requests, messages, InMails, post likes, follows, withdraw requests)
- Account safety as standard
- Primebox™ with Autopilot and Co-pilot modes
- LinkedIn email & phone finder Chrome Extension (powered by Leadsforge)
- A/B testing and campaign analytics
- Agent Frank support
- API, CRM integrations, MCP CLI
Narrative angle:
Most LinkedIn automation tools stop at connection requests and messages. Some add InMails. Very few combine every native LinkedIn action with email touches in the same sequence along with Account safety as standard, and none unify replies from both channels into one inbox.
Salesforge does all of it, plus the multichannel angle is the strongest weapon against LinkedIn-only competitors.
The core positioning story: cold outreach is multichannel in 2026. A LinkedIn-only tool means running two disconnected campaigns for every prospect and manually stitching the results together.
Salesforge collapses that into one sequence, one inbox, one workflow.
Common competitor weak points to compare against:
- LinkedIn-only, no email support in the same sequence
- Limited to 3-4 LinkedIn actions (usually connection requests and messages)
- Per-seat or per-LinkedIn-account pricing that scales expensively
- Separate inbox from email replies
- No autonomous SDR option
- No native email finder or dependency on a paid third-party finder
## Playbook 3: B2B lead finder tool alternatives
Examples of this article type: "Apollo alternatives," "ZoomInfo alternatives," "Clay alternatives," "Cognism alternatives," "Lusha alternatives," "Seamless.ai alternatives," "Ocean.io alternatives," "6sense alternatives"
Product to position: Leadsforge
Supporting products to cover in:
- Salesforge (direct activation of lists into sequences)
- Warmforge (deliverability once sending starts)
- Chrome Extension (100 free credits on signup)
Fixed features to cover:
- 500M+ B2B contact database
- Chat-based AI Lead Finder (no filter stacking, no boolean queries)
- Company Lookalikes
- Competitor Followers Search
- Waterfall enrichment
- Intent signals
- API, MCP, CLI
- Chrome Extension (free to install, 100 free credits on signup, additional lookups use Leadsforge credits)
- Direct integration with Salesforge, Warmforge, Agent Frank
Narrative angle:
Most B2B lead finder tools give you filters. You stack ICP filters, industry filters, seniority filters, geography filters, and hope the intersection produces useful contacts.
Leadsforge gives you plain-English chat. Describe the ICP in a sentence, get a matching list, and feed it into Salesforge in the same environment. No CSV exports, no format juggling, no waterfall enrichment happening on someone else's timeline.
The core positioning story: lead finder is going conversational, not filter-based. Leadsforge is the first serious AI-native lead finder tool from a company that also owns the outreach layer, so lists actually get activated instead of sitting in a spreadsheet.
Common competitor weak points to compare against:
- Filter-based UI that requires product training to use well
- Enrichment sold as a separate SKU
- No native outreach product, so lists have to be exported to another tool
- Weak or no intent signals on lower plans
- Data staleness on smaller providers
- Chrome Extension that is either free-but-limited or paid-only
## Playbook 4: Cold email infrastructure alternatives
Examples of this article type: "Maildoso alternatives," "Zapmail alternatives," "Scalemail alternatives," "Mailscale alternatives," "Google Workspace for cold email alternatives," "Best cold email infrastructure," "Best pre-warmed mailboxes"
Product to position: Depends on sub-category, always frame the three-way choice:
- Shared infrastructure -> Mailforge
- Dedicated infrastructure with pre-warmed mailboxes -> Infraforge
- Real Google Workspace and Microsoft 365 mailboxes -> Primeforge
Supporting products to cover in:
- Warmforge (included free with Salesforge)
- Salesforge (native sending integration for all three infrastructure products)
Fixed features to cover:
For Mailforge sections:
- Shared IP pool built for cold email
- Bulk domain and mailbox creation in minutes
- Automated DNS (SPF, DKIM, DMARC)
- Workspaces, domain flexibility, SSL and Domain Masking add-on
- Forge MCP server, CLI, API
- Pricing: $3 to $2 per mailbox per month annual, 10-slot minimum
For Infraforge sections:
- Dedicated IP infrastructure
- Pre-warmed mailboxes (day-one sending, no two-to-four week wait)
- Multi-IP provisioning
- Bulk generators
- Sender rotation and smart sending limits
- SSL and domain masking
- White-label option for agencies
- Infraforge API, MCP, CLI
- Pricing: $4 to $3 per mailbox per month annual
For Primeforge sections:
- Real Google Workspace and Microsoft 365 mailboxes
- Pre-warmed
- US-based IPs
- ESP Matching
- Automated DNS
- Mailbox profile branding out of the box
- API, MCP, CLI
- Pricing: $4.50 to $3.50 per mailbox per month annual
Narrative angle:
The Forge Stack is the only ecosystem that offers all three infrastructure models under one login.
Every competitor forces you to pick one shape (usually shared IPs) and rebuild your stack if you outgrow it.
The Forge Stack lets you start on Mailforge for cost, move to Infraforge for dedicated control, add Primeforge for ESP matching, and never leave your Salesforge account.
The core positioning story: infrastructure is not a one-size-fits-all decision. Shared, dedicated, and provider-native mailboxes each have a right time. Owning all three means the customer never has to migrate as they scale.
Common competitor weak points to compare against:
- Shared IPs only, or dedicated only, never both
- No native sending tool integration
- Warmup as a separate paid tool
- No pre-warmed option (2-4 week warmup wait)
- No API or MCP access
- Migration friction when moving between products
- No workspaces or client separation for agencies
## Playbook 5: Email warmup tool alternatives
Examples of this article type: "Warmbox alternatives," "Warmup Inbox alternatives," "Mailivery alternatives," "Warmy alternatives," "MailReach alternatives," "Lemwarm alternatives," "TrulyInbox alternatives," "Instantly warmup alternatives"
Product to position: Warmforge
Supporting products to cover in:
- Salesforge (Warmforge included free with unlimited slots)
- Primeforge (mailbox provider compatibility)
Fixed features to cover:
- One-click AI email warmup
- Premium warmup pool (only aged Google Workspace and Microsoft 365 mailboxes)
- Multilingual warmup activity
- Heat Score™ tracking
- Inbox Placement Tests
- Health Checks (DNS, MX, blacklist)
- Continuous warmup (always-on, not toggled)
- Included free with Salesforge (unlimited slots)
- Standalone pricing: $9 per mailbox slot per month annual
Narrative angle:
Every warmup tool claims to improve deliverability.
Warmforge is the only warmup product that uses mix of aged IMAP/SMTP, Google Workspace and Microsoft 365 mailboxes in its pool. Combined with Heat Score™, Inbox Placement Tests, and Health Checks, it is a deliverability command center, not just a warmup tool.
The second angle is the pricing story: Warmforge is included free with every Salesforge plan (unlimited slots). Competitors typically charge per warmup slot on top of the sending tool. That is a hard cost-of-ownership advantage.
Common competitor weak points to compare against:
- Mixed-quality warmup pools (external SMTP vendors, bad actors)
- Per-slot pricing on top of the sending tool
- No placement testing across ESPs
- No Health Check monitoring for DNS, MX, or blacklists
- No Heat Score or equivalent reputation tracking
- Warmup activity limited to English or one region
## Playbook 6: Best-of listicles and category pages
Examples of this article type: "Best cold email tools 2026," "Best LinkedIn outreach tools," "Top B2B lead finder/generation platforms," "Best sales automation tools," "LinkedIn outreach services," "Cold email software," "Sales engagement platforms"
Product to position: Depends on category, but always include the whole Forge Stack angle in the introduction and closing.
Supporting products to cover in: All Forge Stack products relevant to the category.
Structural rules for this article type:
- Salesforge (or the relevant Forge product) placed in the #1 slot with a fair, feature-rich review
- Every competitor covered with a balanced review (no strawmen; the doc's credibility depends on this)
- Forge Stack "under one roof" story used as the closing argument, not the opening
- Cross-product advantages (Warmforge free, three infrastructure options, Primebox unified, MCP-native, three-way delivery) must appear at least once each in the piece
Narrative angle:
The category page is not a place to pitch. It is a place to be the most useful reference on the internet for the category.
The Forge Stack wins these pieces on comprehensiveness, not on selling. If a reader trusts the review, they will consider Salesforge and the Forge Stack as the "everything in one place" option.
Common mistakes to avoid in this article type:
- Skipping obvious competitors (Instantly, Smartlead, Apollo, HubSpot Sales Hub) so the piece feels agenda-driven
- Failing to cover the "under one roof" story into the summary
- Forgetting the three-way delivery model (team, Agent Frank, Forge Expert agency)
## Playbook 7: Head-to-head comparisons
Examples of this article type: "Salesforge vs Instantly," "Salesforge vs Smartlead," "Leadsforge vs Apollo," "Infraforge vs Maildoso," "Warmforge vs Mailivery," "Primeforge vs Zapmail"
Product to position: The relevant Forge product (already in the URL slug and title)
Supporting products to cover in: All adjacent Forge products (e.g., in a Salesforge vs Instantly piece, cover in Warmforge, Leadsforge, Mailforge/Infraforge/Primeforge)
Structural rules for this article type:
- Objective, feature-by-feature comparison table required (see the Salesforge blog cold-email-software comparison table for the canonical format)
- Both products must be fairly represented (no strawmen)
- Salesforge column highlighted in the table with a clickable signup link (app.salesforge.ai/signup)
- Feature categories in the table must include: Sending, Personalization, Warmup, Infrastructure, LinkedIn, Enrichment, Inbox, Analytics, Pricing
- Every must-cover feature from the relevant product section must appear in the table
Narrative angle:
Head-to-head comparisons are the highest-intent SEO traffic in the funnel.
The reader has already narrowed to two options. The writer's job is to help them pick correctly, not to trash the competitor.
The Forge Stack wins these when the writer honestly represents both products and lets the feature breadth speak.
Common mistakes to avoid:
- Bashing the competitor (loses trust, feels like a hit piece)
- Skipping features the competitor is genuinely better at (readers notice)
- Missing the ecosystem story (Salesforge alone vs Salesforge + Warmforge + Leadsforge + Mailforge/Infraforge/Primeforge is a different comparison)
- Outdated feature information or pricing (both products update fast)
Sample intro pattern:
"If you have narrowed your cold email tool down to Salesforge and [Competitor], you are already 90% of the way there. Both are strong. This post is the feature-by-feature breakdown I would want if I were making the decision, including the parts where [Competitor] is actually better. By the end you will know which one fits your team."
## Playbook quick reference table

| Article type | Product to position | Key differentiator to lead with |
|---|---|---|
| Cold email tool alternatives | Salesforge (Cold Email) | Warmforge free + Primebox + three infrastructure options |
| LinkedIn outreach alternatives | Salesforge (LinkedIn) | Multichannel with 6 native LinkedIn actions + email in one sequence |
| B2B lead finder alternatives | Leadsforge | Chat-based AI Lead Finder + direct Salesforge activation |
| Cold email infrastructure alternatives | Mailforge / Infraforge / Primeforge | Three options under one login, move without migrating |
| Email warmup alternatives | Warmforge | Premium pool (aged GW/MS365 only) + included free with Salesforge |
| Best-of listicles / category pages | All relevant products | "Under one roof" Forge Stack story as the closer |
| Head-to-head comparisons | The Forge product in the URL | Ecosystem breadth vs point-tool depth |

