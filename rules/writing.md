# Forge Blog Writing Rules

How we write. Product facts, pricing, and positioning live in `rules/positioning.md`. The production process lives in `rules/process.md`.

Every rule below carries an enforcement tag:

- `[LINT]` a script checks it. You do not need to hold it in your head, but do not fight it either.
- `[JUDGE]` a reviewer with fresh eyes checks it. Write toward it deliberately.
- `[HUMAN]` Jaimin checks it before publishing. Flag anything uncertain.

A rule with no tag does not exist. If you want a new rule, it needs a tag first.

This file is written under its own rules. If you find an em dash, a banned word, or a 30-word sentence in here, that is a bug worth reporting.

---

## 1. Who is writing

Every piece is written by Frank Sondors, co-founder and CEO of Salesforge. He is the default and only byline.

Frank runs cold email and LinkedIn outreach for a living. He has:

- Set up domains, mailboxes, and DNS records with his own hands
- Burned domains and learned from it
- Tested most tools in this market, not just read about them
- Real opinions, real numbers, and real complaints

The reader should think: this is advice from someone who actually does this work.

Never write as a brand. Never write as a marketing team. Never write in an anonymous corporate voice.

The founder byline and the practitioner voice fit together. Frank can credibly claim broad hands-on experience across this category. That widens what the truth rules in section 7 allow, but it does not remove them.

---

## 2. Voice `[LINT]` `[JUDGE]`

**The hard rule, and it governs every other rule in this file.** Fixed by Jaimin on 2026-08-13.

> Active voice, first person point of view wherever it makes sense, authentic human voice. Absolutely no AI slop, no fluff, simple sentences and simple English. Content is factual and accurate, based on research.

Six words of that carry the weight, so read them as tests you can fail:

- **Active voice.** Name the doer. "Expandi charges per seat", not "a per-seat charge is applied".
- **First person where it makes sense.** "I" for what Frank did or saw. Not forced into a sentence that has no person in it.
- **Authentic human voice.** A practitioner talking, not a brand announcing.
- **No AI slop, no fluff.** Every sentence carries a fact, a number, an opinion, or a decision. If cutting a sentence loses the reader nothing, it was slop. Sentences that describe the article, the data, or the reviewers instead of presenting the content are the most common form of it. See the banned narrator framings in section 5.
- **Simple sentences, simple English.** One idea per sentence, everyday words. See sections 3 and 6.
- **Factual and accurate, based on research.** Every claim traces to the brief, to `rules/positioning.md`, or to `rules/observations.md`. Nothing traces to a plausible-sounding guess. See section 7.

The numbered rules:

1. First person "I" only. Never "we", "our", or "us". `[LINT]`
2. Active voice. Passive is acceptable only when the actor genuinely does not matter. If you can name the doer, name them. `[JUDGE]`
3. Write like you talk. If you would not say the sentence out loud to a colleague, rewrite it. `[JUDGE]`
4. Contractions are good: I've, it's, don't, that's, you'll. `[JUDGE]`
5. Starting a sentence with And, But, or So is fine. People do it. `[JUDGE]`
6. Talk to the reader with "you". "You'll need about 10 mailboxes for this volume." `[JUDGE]`

---

## 3. Sentences and paragraphs `[LINT]`

- Ideal sentence length: 12 to 20 words.
- Hard ceiling: 25 words. Go over only when there is a reason, and never twice in a row.
- A bolded label followed by a colon does not count toward the 25. "**Bounce Shield:**" is a label, not part of the sentence, and the linter strips it before measuring.
- One idea per sentence. If an "and" joins two full thoughts, split it.
- Vary the rhythm. Follow a medium sentence with a short one. Like this.
- Paragraphs: 1 to 3 sentences. New idea means new paragraph.
- Skim test: if a section cannot be skimmed in 5 seconds, rewrite it.

**Section length.** Fixed by Jaimin on 2026-08-13. Diagnosis sections stay short and to the point. That covers "Why people leave [Competitor]", "Why people look for [Competitor] alternatives", and any H2 whose job is to name a problem rather than review a product.

- **Two short paragraphs per subsection is enough.** The linter warns past two.
- One point per subsection. The H3 says what the problem is, the two paragraphs say what it costs the reader, and the section ends.
- No third paragraph adding a comparison, a caveat, and a scaled-up example. Pick the strongest one.
- The arithmetic goes in the paragraph that needs it, not in a paragraph of its own.

---

## 4. Punctuation `[LINT]`

- No em dashes. Not once. Use a comma, a period, or a colon.
- No semicolons. Split into two sentences.
- No en dashes in prose. Use "to" in ranges: "$3 to $2 per mailbox".
- No exclamation marks in body copy. One in an intro or a CTA is the maximum, and it is rarely needed.
- Rhetorical questions: one or two per article.
- Normal quotes, normal commas. No emojis.

---

## 5. Banned words and phrases `[LINT]`

**Banned words**

seamless, seamlessly, robust, leverage (as a verb), empower, streamline, unlock, elevate, ensure, ensures, moreover, furthermore, additionally, cutting-edge, next-generation, game-changer, hassle-free, guesswork, delve, landscape (figurative), realm, harness, supercharge, revolutionize, effortlessly, comprehensive, holistic, innovative, state-of-the-art, utilize (say "use")

**Banned figurative verbs**

Do not give a product or a feature a body. When the subject of the sentence is a tool, a feature, or a plan, do not use: sits, puts, pulls, lives, rests, boasts, weaves, flows, houses.

- Wrong: "The warmup tool sits inside the dashboard."
- Right: "You find the warmup tool inside the dashboard."
- Wrong: "The extension pulls data from LinkedIn."
- Right: "The extension gets emails from LinkedIn profiles."

A person can still pull a list or put a domain into a workspace. The ban applies when the product is the actor.

**Banned phrases**

- "in today's world" and "in today's fast-paced environment"
- "all-in-one solution"
- "best-in-class"
- "take your outreach to the next level"
- "look no further"
- "it's worth noting that"
- "whether you're a X or Y", in any version
- "dive into" and "let's dive in"
- "at the end of the day", once per article maximum, only if it reads naturally
- "This feature allows you to..."
- "what makes", "the answer is", "what separates", "here's the thing"

**Banned narrator framings**

These are shapes, not words, so read for them separately.

- Literary metaphor: "a tale of two X", "the story of X is", "two versions of the same product"
- Journalist wrap-up: "tells the real story", "speaks volumes", "says it all"
- Narrator preamble: "the honest read is", "the real question is", "what the patterns add up to"
- Writing about the article: "the most useful signal in this review", "the rest of this post covers", "below I will walk through"

If a sentence describes the article, the data, or the reviewers rather than presenting the content, cut it.

**Banned patterns** `[JUDGE]`

- Formal transitions between paragraphs. Just start the next thought.
- Perfectly balanced pros and cons, four against four, all the same length. Real reviews are lopsided.
- Three-item lists in every sentence. "Fast, reliable, and scalable" is a tell.
- Repeating the product name at the start of consecutive sentences.
- Every paragraph the same length.

---

## 6. Preferred language `[JUDGE]`

Small everyday verbs and concrete nouns: set up, run, send, check, connect, fix, break, cost, save, switch, land in the inbox, burn a domain.

- "it took me 10 minutes" beats "the setup process is quick"
- "you pay $48 a month" beats "affordable pricing options"
- "my reply rate went from 2% to 9%" beats "significantly improved results"

Numbers make writing believable. Use exact prices, times, counts, and ratings with review counts.

**Layman language only.** Plain everyday words a non-marketer would say. If a word would slow down a reader who sees it once, replace it.

**No trailing add-on clauses.** Do not write a main clause, then a comma, then a tail. That shape reads as machine-written.

- Wrong: "Full setup takes under five minutes, and the guided flow calculates how many domains you need based on your target volume."
- Right: "Full setup takes under five minutes. The guided flow works out how many domains you need for your target volume."
- Wrong: "Domain forwarding: Visitors to your secondary domains land on your main site, set up inside the platform."
- Right: "Domain forwarding: Point your secondary domains at your main site."

Start with the action. Keep one thought. End the sentence. Feature bullets follow the same rule.

---

## 7. Truth rules `[LINT]` `[HUMAN]`

This is the most important section in the file. Absolute claims destroy trust, and invented specifics are worse.

1. **Every product claim must be verifiable against `rules/positioning.md`.** If the positioning file does not support it, do not write it. Ask.
2. **No absolute guarantees.** Never write "the bill never moved", "always lands in the inbox", "guaranteed replies", "zero spam", "100% placement".
3. **Two claim types, handled differently.**
   - **Product facts** (pricing, features, limits, plan contents): state them plainly and exactly, from the positioning file.
   - **Outcomes** (reply rates, deliverability, meetings, savings): frame as observed experience. "Has come down." "Has been steady." "Climbed noticeably." "Stayed predictable as we grew."
4. **Mark every placeholder number.** When you need a figure you do not have, write it as `[[FIGURE: reply rate for the 40-mailbox setup]]` so Jaimin replaces it before publishing. `[LINT]` blocks publishing while any `[[FIGURE:` marker remains.
5. **When unsure, say less.** "Deliverability has been steady for us" is safe. "100% inbox placement" is not.
6. **Competitor pricing comes from the vendor's live pricing page only.** Never from G2, Capterra, TrustRadius, a listicle, Reddit, an AI summary, or one of our own older articles. Re-check on every rewrite. Record the URL you used.

The fix pattern:

- Risky: "We scaled to 20 mailboxes and the bill never moved."
- Safe: "I scaled to 20 mailboxes and paid nothing extra for them, because Salesforge does not price per mailbox or per sender. That kept costs predictable as the team grew."

---

## 8. How to sound human `[JUDGE]`

1. **First-hand moments**, two to three per article. "I uploaded a 5,000-contact list on a Tuesday and the enrichment finished before my coffee did."
2. **Small real complaints**, including about our own products. "The dashboard felt cluttered in my first week." One real flaw earns more trust than ten compliments.
3. **Opinions.** "I think the Growth plan is the only one worth buying past 5,000 contacts."
4. **Conditional honesty.** "If you send under 500 emails a month, you do not need this yet."
5. **Light asides**, once or twice per article. "(No, I counted.)"
6. **Admissions of limits.** "I have not tested their enterprise plan, so I cannot speak to it."
7. **Constructive framing for negatives.** Name the issue, its impact, and a fix. Mild, specific, professional.

Human does not mean fake typos, deliberate grammar mistakes, lowercase "i", or manufactured flaws. Human means specific, honest, and conversational.

---

## 9. Structure: listicle, "Best X tools"

1. **Intro**, 3 to 6 short paragraphs. Open on the problem or a personal moment. Never "in this article we will". Say how many tools you tested and why most did not make it.
2. **How I chose.** Your criteria as a short list. Be specific: what you tested, for how long, what you measured.
3. **TL;DR.** One bullet per tool, in the article's running order. See section 9a for the fixed shape.
4. **Comparison table.** The HTML template in `assets/comparison-table.html`. See section 14.
5. **Tool sections.** The routed Forge product first and deepest. See section 9b for the fixed skeleton.
6. **"Which one should you pick?"** Answer by use case, not by hype.
7. **FAQs.** Minimum 5, direct answer in the first sentence of each.

---

## 9a. The TL;DR block `[LINT]`

Fixed by Jaimin on 2026-08-13. The linter blocks any TL;DR bullet that misses the shape.

**Tool name, colon, then "Best for".** Every bullet, no exceptions.

    - **[Salesforge](#salesforge):** Best for GTM teams and Agencies running LinkedIn plus
      email plus AI in one platform, with unlimited mailboxes and unlimited LinkedIn senders
      on Growth. Primebox™ unifies replies across every channel, and Warmforge warm up is
      bundled at no extra cost.

Rules for the bullet:

- The tool name is a jumplink to its section, and it carries the colon.
- "Best for" is the first thing after the colon. Not "runs", not "charges", not "is the cheapest".
- Then who it is for, in the words a buyer would use about themselves.
- Then one or two sentences on the mechanics that earn that fit. Named features, real numbers.
- Then the annual price where the article is price-led. See section 9c.
- No "Not for" clause. See section 13.

The point of the fixed shape is that this block is what AI Overviews and Perplexity lift. A bullet that opens on the buyer is quotable as a recommendation. A bullet that opens on a feature is not.

---

## 9b. The tool section skeleton `[LINT]`

Every product section in a listicle, an alternatives post, or a category page uses this order.

1. **H2:** "N. [Tool Name]"
2. **Best for:** one line, the buyer in their own words, never "everyone". For Salesforge this line always opens "Best for GTM teams and Agencies". See `rules/positioning.md`.
3. **G2 Rating:** "X out of 5 (N reviews)".
4. **A plain explainer sentence, and it opens the prose.** "[Tool] is a [what kind of tool] that [what it does]." Say what the thing is before you say what is interesting about it. A reader who has never heard of the tool must be able to follow the second paragraph.
5. **2 to 4 more paragraphs.** The mechanics, the billing unit, the trade-off, one specific first-hand moment where `rules/observations.md` funds one.
6. **H3 "Key features".** 5 to 8 bullets for a competitor. For the routed Forge product, **one bullet per must-cover feature in that product's section of `rules/forge-positioning-guidelines.md`, and the same number of bullets as that section lists.** Colon after the feature name. See below.
7. **H3 "Pros and cons".** A two-column table, lopsided and honest. For Salesforge the cons column carries exactly one point. See `rules/positioning.md`.
8. **H3 "Pricing".** Annual rates only. See section 9c.
9. **H3 "What real users say".** One line, and only one. See below.

**The plain explainer, rule 4, is the one that gets skipped.** Opening on the most interesting fact reads well to someone who already knows the category and loses everyone else. Explain, then argue.

- Wrong: "Every other tool on this list runs email and LinkedIn as two campaigns you keep in step by hand."
- Right: "Salesforge is a multichannel outreach tool that runs cold email and LinkedIn as two channels of one sequence." Then the contrast.

**Key features bullets carry a colon after the feature name.** `[LINT]`

- Right: "Flat per-sender pricing with free unlimited users: The vendor FAQ is explicit that teammates, VAs and clients are not charged for."
- Wrong: "Flat per-sender pricing with free unlimited users. The vendor FAQ is explicit..."

The feature name is the bolded part and it is a name, not a sentence. Then the colon, then what it does in one or two sentences.

**The bullet count is not yours to choose. It is the length of the must-cover list.** Fixed by Jaimin on 2026-08-13.

Work out which list governs before writing the section:

- **The routed product's own section in `rules/forge-positioning-guidelines.md` is the checklist.** For a LinkedIn-focused article that is "Salesforge: LinkedIn", which lists 12 must-cover features, so the key features carry 12 bullets. For a cold email article it is "Salesforge: Cold Email". For a multichannel piece it is "Salesforge: Multichannel", and that one also requires the Category A and Leaning B framing.
- **One bullet per feature, using the doc's feature name.** Reword for cadence, never for meaning.
- **Shuffle the order between articles.** The doc says so directly. Lead with whatever the article is about, so a LinkedIn piece opens on the six native LinkedIn actions rather than on unlimited mailboxes.
- **Supporting products are not entries on that list.** Warmforge, the Leadsforge Company Followers search and the infrastructure products belong in the prose, the pricing paragraph, or the Final Verdict. The playbook names them separately for exactly this reason.

**Never bundle must-covers behind one label.** Two failures on the Expandi draft, both caused by it. The first pass hid A/B testing, the API and MCP inside an Agent Frank bullet, and campaign analytics and the followers search were never written at all. The second pass still merged the API, Integrations and MCP CLI into one bullet, which read as complete and was three features short. Count the bullets against the doc, then check each name.

**The ratings section is one line.** `[LINT]` Fixed by Jaimin on 2026-08-13.

    ### What real users say

    G2 puts Salesforge at 4.6 from 137 reviews.

Nothing else goes in that section. No con-tag breakdown, no one-star arithmetic, no reading of what the reviews cluster on. Jaimin adds review screenshots by hand directly below that line, and prose underneath it gets in the way. The linter blocks a second line.

Complaint themes still belong in the article. Put them where they are load-bearing: in the cons column, in the pricing paragraph when the complaint is about price, or in the "Best for" line when the complaint decides who should walk away.

---

## 9c. Pricing in prose and tables `[LINT]`

**Annual rates only, everywhere, for every tool.** Fixed by Jaimin on 2026-08-13. The full rule and its edge cases are in `rules/positioning.md` under "Annual format only". The short version:

- Pricing tables carry one price column and it is the annual one. The linter blocks a "Billed monthly" or "Billed quarterly" column header.
- Prose says "$39 per user per month billed annually". Never "$59 monthly, $39 annually".
- Cost-at-scale math runs on annual rates end to end.

---

## 10. Structure: alternatives post, "X alternatives"

1. **Intro.** Acknowledge the competitor is a good tool. Then give the true reasons people look elsewhere: price jumps, seat limits, missing channels, deliverability trouble.
2. **"Why people leave [Competitor]".** 3 to 5 specific reasons drawn from real public complaints, never invented. One H3 per reason, two short paragraphs each. See the section-length rule in section 3.
3. **TL;DR and comparison table**, same rules as the listicle. See sections 9a and 14.
4. **The Forge product first and deepest.** Frame it as "why I moved" or "what I found", not "why it is better".
5. **Other alternatives**, same skeleton as section 9b, each matched to a reader type.
6. **"When [Competitor] is still the better choice".** Always include this. It is the highest-trust section in the post, and it is not optional.
7. **FAQs.** Minimum 5.

---

## 11. Structure: VS post, "X vs Y"

1. **TL;DR near the top**, 3 to 5 sentences. Give the verdict by use case immediately.
2. **Comparison table.** Mandatory. See section 14.
3. **Section by section, by job:** deliverability, pricing, sending limits, LinkedIn, reply management, support. Say which tool wins each one and why.
4. **Pricing math.** "For 10,000 contacts, X costs $Y a month and Z costs $W a month."
5. **Final verdict by reader type.** Commit. Never "both are great".
6. **FAQs.** Minimum 5.

---

## 12. Structure: review or product post

1. What the tool is, in two plain sentences.
2. How I tested it: duration, volume, what I measured.
3. Feature walkthrough in the order a user meets them. Steps and before-and-after examples where they help.
4. Pricing with real numbers.
5. Pros and cons, lopsided and honest.
6. Who should use it. The reader who should walk away is routed in the verdict, never in a "Not for" label. See section 13.
7. Verdict and one CTA.
8. FAQs. Minimum 5.

---

## 13. Who it's for `[LINT]` `[JUDGE]`

**No per-tool "Not for:" line. Ever.** Fixed by Jaimin on 2026-08-13, reversing the rule that stood here earlier the same day. The linter blocks the line on sight.

The line was required in every product section, then made optional, and is now banned outright. Three shapes are gone with it:

- `**Not for:** anyone who wants LinkedIn on its own.`
- `**Not for:** anyone sending real email volume.`
- Any bolded disqualifier label under a tool's H2, whatever it is called.

**Disqualification still has to happen.** It moves to the three places where it reads as advice instead of a warning label:

1. **The Best for line.** Naming the buyer precisely already excludes everyone else. "Best for solo operators and two-person teams who want native email at the lowest price" tells a fifteen-person team to keep reading.
2. **The cons column.** A real limitation stated plainly does the disqualifying work. "One mailbox per account, capped at 200 emails a day" is the disqualifier for anyone sending volume.
3. **The Final Verdict, and "When [Competitor] is still the better choice".** These route by reader type across the whole article, including the reader who should not buy anything on the list.

An article that never tells a reader to walk away still fails this rule. What changed is the mechanism, not the obligation.

Why it matters, unchanged: readers trust a writer who tells them to walk away, and LLM recommendations are personalised to the person asking, so their prompt carries company size, budget, and deal size. Content that names the fit precisely can be matched to the right person. Honest disqualification is how we get recommended. It just belongs in prose a reader can act on, not in a label under every heading.

---

## 14. Comparison table `[LINT]`

Almost every article needs one. Use the HTML template in `assets/comparison-table.html` exactly. Do not retype the CSS and do not substitute a markdown table.

- The routed Forge product column carries `class="highlight-col"` on its `<th>` and on every `<td>`, plus the "Best Overall" badge.
- The Forge product header links to its signup URL.
- The purple highlight stays whichever Forge product is routed. Only the label and the link change.
- **Ship the full CSS block every time.** Fixed by Jaimin on 2026-08-13. The `<style>` block in the template goes into the article verbatim, every article, no trimming and no "the site already has these styles". Copy the file, do not retype it.
- Up to 6 tool columns plus the Feature column, so 7 in total. An alternatives post includes the incumbent as one of the 6, because a reader comparing alternatives needs the thing they are leaving in the table.
- Every tool name in the table is a jumplink to its section. The routed Forge product links to its signup URL instead.
- Cells state what the tool actually is, in one to three lines. "No, email only" beats an X mark. "Yes, native. 6 LinkedIn actions with conditional branching" beats a check mark.
- **No semicolons in cells.** Section 4 applies inside the table. Use a comma or a period.
- Pricing cells carry the annual rate only, phrased "$40/month (billed annually)". See section 9c.

**Canonical row set for LinkedIn, cold email, and multichannel articles.** Fixed by Jaimin on 2026-08-13. Cover all fourteen. Do not invent new categories per article and do not quietly drop a row because a competitor looks bad in it.

1. Best for
2. Mailboxes and LinkedIn senders
3. AI personalization
4. LinkedIn actions
5. Multichannel (LinkedIn + email)
6. LinkedIn account safety
7. Unified reply inbox
8. Native integrations
9. Free Chrome Extension
10. AI SDR
11. MCP + CLI
12. Agency support
13. Free trial
14. Starting price

Two things that row set does deliberately. It opens on "Best for" rather than price, so the table reads as a routing aid instead of a price list. And rows 9 through 11 are where the Forge stack is structurally ahead, so they stay in even when a competitor column is a wall of "No".

Row swaps by routed product: for Leadsforge, replace rows 4 through 7 with "Database size", "Chat-based lead finder", "Company Lookalikes and Company Followers", and "Waterfall enrichment". For Warmforge, replace rows 4 through 7 with "Warmup pool quality", "Heat Score™ tracking", "Inbox placement tests", and "Health checks". For Mailforge, Infraforge, or Primeforge, replace rows 3 through 7 with "IP model", "Pre-warmed mailboxes", "DNS setup (SPF, DKIM, DMARC)", "Domain forwarding", and "Deliverability monitoring".

Check that the CSS block survived the paste into Webflow. Rich-text editors sometimes strip an inline `<style>`, and the table looks broken without it.

---

## 15. Headings `[LINT]`

- H2s are plain and searchable. "Salesforge pricing", not "What's the damage?"
- Match H2s to what people search or ask an LLM. A question as an H2 is fine when it reads naturally.
- One H1, the title. H2 for main sections. H3 for pricing and reviews inside a tool section. Never skip a level.
- No emojis, no drama colons.

---

## 16. SEO `[LINT]`

- Primary keyword in the title, the URL, the first 100 words, and at least one H2. Natural placement only.
- Title under 55 characters. Meta description under 155 characters, with the primary keyword and a clear hook.
- Minimum 5 internal links. TOFU posts link down to MOFU and BOFU. BOFU posts link to landing pages.
- Anchor text must already exist word for word in the draft. The destination must genuinely cover the anchor's topic. No "click here". No repeated anchor text.
- Comparison tables carry jumplinks to each tool's section.
- Answer the exact searched question early and directly.
- Article schema on every post. No FAQ schema: Google deprecated FAQ rich results in May 2026, so it earns nothing and adds markup risk.

---

## 17. LLM visibility `[JUDGE]`

LLMs search the web and quote what they find. The goal is to be the source they quote.

1. **BOFU first.** Listicles, alternatives, and VS posts are what LLMs pull from when someone asks for the best tool in a category.
2. **Write value props as quotable lines.** LLMs lift exact wording, so every key claim should be one clear, self-contained sentence with a real number. "Unlimited mailboxes and LinkedIn senders with no seat-based pricing." "Mailboxes ready in 30 minutes."
3. **State who it's for and who it's not for.** See section 13.
4. **Cover use cases in detail.** An agency with 40 clients. A founder's first outbound campaign. An SDR team at 50,000 emails a month. Each scenario you describe is another conversation where an LLM can recommend us.
5. **Topic depth beats prompt-chasing.** Build coverage across the whole topic instead of one page per exact query.
6. **Snippet-ready blocks.** TL;DRs, tables, and direct-answer FAQs are what AI Overviews and Perplexity summarise. Front-load the answer.
7. **On-page tricks are the cherry, not the cake.** Skip llms.txt-style tactics. The honest, specific content does the work.

---

## 18. CTAs `[JUDGE]`

- CTAs enable action. They never push.
- Primary: free trial or signup. Say "no credit card required" when it is true.
- Secondary: book a demo, watch a demo, use the calculator.
- Placement: after pricing, after value is shown, and near the final verdict. Never in every section.
- No "best", "#1", or "guaranteed" inside CTA copy. No fake urgency.
- Working examples: "Start a free 14-day trial, no credit card needed." "Book a demo to see Agent Frank work a real lead list."

---

## 19. Competitors `[JUDGE]` `[HUMAN]`

- Neutral-positive, never dismissive. Trust converts better than bias.
- Every competitor mentioned gets at least one real strength.
- Match each competitor to the reader it suits.
- Only verifiable public limitations: pricing tiers, feature gaps, seat limits. Never invent a flaw.
- Our framing is "better fit for this specific reader", never "the best tool ever".
- **A Forge product does not get the #1 slot automatically.** It earns the top spot when it genuinely leads on the dimension the article is about, and the section says why. If a competitor honestly wins that dimension, put the competitor first and use the Forge product's section to name the reader who should still choose it.
- Legal and comparative claims about a named vendor are `[HUMAN]`. Flag them.

---

## 20. Naming `[LINT]`

Correct, always: Salesforge, Mailforge, Primeforge, Leadsforge, Infraforge, Warmforge, Agent Frank, Primebox™, Heat Score™, Bounce Shield, Megaforge, Auto-Pilot, Co-Pilot.

Never: SalesForge, Sales Forge, Frank AI, the Agent, AgentFrank, Autopilot, Copilot, Prime Inbox, bounce protection, or any invented abbreviation.

Collective term: "Forge stack".

**Fixed feature names live in `rules/forge-positioning-guidelines.md`.** That file's do-not-paraphrase list is the authority: Bounce Shield, Primebox™, Heat Score™, "AI personalization across 21+ languages", waterfall enrichment, ESP matching. Always 21+, never 20+.

**One open conflict, flagged 2026-08-13.** The guidelines write "Autopilot and Co-pilot modes". This section and the linter require "Auto-Pilot" and "Co-Pilot" and ban "Autopilot". Autopilot is not in the guidelines' own fixed-names list, so drafts keep Auto-Pilot and Co-Pilot until Jaimin picks one. Do not flip it on your own.

Agent Frank is he/him. You hire Agent Frank. You never buy him or activate him. He is an AI SDR, never a bot, an automation, or a workflow.

Competitors are spelled exactly as they spell themselves on their own site.

**Lowercase-branded names.** Some vendors style their name lowercase. Use their spelling in body prose, and capitalise only where the name opens a heading or a sentence. So "Lemlist charges per seat" at the start of a sentence, and "the thing lemlist does best" mid-sentence. Current lowercase brands: lemlist. The linter enforces this.

---

## 21. Before publishing

The linter runs items marked `[LINT]` and blocks on failure. Do not hand-check those. Read for the rest.

`[JUDGE]`

- [ ] At least 2 first-hand moments with specifics
- [ ] At least 1 real limitation of our own product
- [ ] Every competitor has a real strength
- [ ] A "Best for" line on every product section, and the reader who should walk away routed in the Final Verdict. No "Not for" labels anywhere. See section 13
- [ ] Every tool section opens on a plain explainer sentence saying what the tool is. See section 9b
- [ ] Every must-cover feature for the routed product appears somewhere. See `rules/forge-positioning-guidelines.md`
- [ ] Cross-product stories present: under one roof, and two ways to run it, three with partners
- [ ] Outcomes hedged as experience, product facts stated exactly
- [ ] Tool section openings vary after the explainer sentence. No two use the same entry angle
- [ ] "When [Competitor] is still the better choice" present in alternatives posts
- [ ] Paragraph rhythm mixes lengths

`[HUMAN]`

- [ ] Every `[[FIGURE:` placeholder replaced with a real number
- [ ] Every competitor price re-checked against the vendor's live pricing page today
- [ ] Every rating and review count re-checked live
- [ ] Any legal or comparative claim about a named vendor reviewed
- [ ] Byline set to Frank Sondors
