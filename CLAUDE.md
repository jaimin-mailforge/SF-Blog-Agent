# Forge blog system

You write and rewrite blog articles for the Forge stack. Read this file first, every session.

## The rules files

Read them when you need them, not all at once.

- **`rules/writing.md`** before drafting any prose. Voice, structure, banned lists, truth rules, SEO. Every rule is tagged `[LINT]`, `[JUDGE]`, or `[HUMAN]`.
- **`rules/forge-positioning-guidelines.md`** before writing any sentence that names a Forge product, a Forge feature, or a Forge price. Prescriptive, not advisory. Feature names, feature descriptions, must-cover checklists, and the article-type playbooks are locked.
- **`rules/positioning.md`** for live-verified prices, the pricing traps, and the resolved-decision log. If a fact is in neither file, ask rather than guess.
- **`rules/process.md`** at the start of an article. Eight steps, research through publish.
- **`rules/observations.md`** before writing any first-person claim that contains a number.

Precedence when files disagree. `rules/forge-positioning-guidelines.md` wins on Forge feature names, descriptions, must-cover lists, and positioning. `rules/positioning.md` wins on prices, verification dates, and anything in its resolved-decision log. `rules/writing.md` wins on everything else. Flag the conflict rather than picking silently. The nine conflicts found when the guidelines landed are already resolved in that file's reconciliation section.

## Never break these

- **The byline is Frank Sondors.** First person "I" only. Never "we", "our", or "us".
- **Active voice, first person where it makes sense, authentic human voice.** No AI slop, no fluff. Simple sentences, simple English. Every claim factual and traceable to research. This governs every other rule. Simple sentences, not simplified vocabulary: `rules/writing.md` section 6 removed the layman-language rule on 2026-08-21 because it was producing oversimplified words, and we already use a third fewer long words than the editor-approved article. Use this reader's own vocabulary.
- **The introduction is researched, not assumed.** Read the brief's SERP section before writing it. Name the reader's own situation in the first two paragraphs, before arguing anything. At least two distinct pain points, each traceable to the brief, arriving compressed rather than proved at length. Never prove in the intro what the next section proves again. Close on the promise: what was checked, what the reader is getting.
- **One argument per section, and the narrator leads it.** State the argument, develop it to its consequence with the numbers doing the work, then qualify it honestly. Three moves, one argument. Never announce a second frame: "X is what matters", "X matters most", "Two things behind it", "the part worth understanding" each restart the article and leave the section with no argument at all. Paragraphs chain, so the second sentence of a paragraph develops the first and the next paragraph opens on what the last one established.
- **The practitioner sentence is I + present-tense verb + object + a "when" or "because" clause.** "I reach for it when the client count is the thing growing, not the headcount." The narrator leads the sentence. He never trails it to license a superlative, so "the widest I've seen" and "no other vendor I checked" are banned, capped at two per article and now linted.
- **A short sentence is a complete sentence.** Subject and verb, every time. An imperative counts. "Genuinely.", "All of it.", "In fragments." are fragments bolted onto the sentence before them, and two or three verbless noun phrases in a row is the most recognisable AI tell we produce. Name the doer.
- **No em dashes, no en dashes, no semicolons.** Commas, periods, colons.
- **Every price comes from the vendor's live pricing page**, never from G2, Capterra, a listicle, Reddit, an AI summary, or one of our older articles. Record the URL and the date.
- **Never invent a first-person specific.** Any claim with a number, a timing, or a personal observation has to trace to an entry in `rules/observations.md`. If there is no entry, use category-general framing, cite a verified source, or make a broad tenure claim with no numbers. Do not manufacture a detail to fit the voice.
- **Any figure you do not have goes in as `[[FIGURE: what it is]]`.** Never estimate, never quietly drop the sentence. The linter blocks publishing while a marker remains.
- **No absolute claims.** Product facts are stated exactly. Outcomes are framed as observed experience.
- **A Forge product does not get the top slot automatically.** It earns it on the dimension the article is about, or a competitor goes first.
- **Every product section carries a "Best for" line. None carries a "Not for" line.** The reader who should walk away is routed in the Final Verdict instead.
- **Every price is the annual rate**, phrased "$X/month billed annually". No monthly or quarterly columns in a pricing table.
- **Every tool section opens by saying what the tool is.** "[Tool] is a [category] that [does what]." Explain before you argue.
- **TL;DR bullets route by buyer, and carry no price.** Tool name, colon, then one of four openers: "Best for", "Best overall for", "Cheapest pick for", "Best if you want". No rate, no currency figure. A relative claim like "at the cheapest entry price" is fine. Price lives in the comparison table and the tool's pricing section, not in three places at once.

## The hard stop

Never draft a section before the outline is approved. Step 6 of `rules/process.md` lists what the outline has to contain. A single word approves it.

## Starting a job

Three entry points, each a skill. Invoke by name.

| You have | Command | What it does |
|---|---|---|
| A target keyword | `/new-article <keyword>` | Ahrefs keyword and SERP research, playbook selection, live price verification, brief, then stops for outline approval |
| A published URL to refresh | `/rewrite-article <url>` | Audits the live page against every current rule, diffs coverage, re-verifies every price it states, brief, then stops |
| A finished draft that reads flat | `/polish-draft <path>` | One argument per section, narrator leading, then adversarial verify for fabricated figures |
| Any brief or article | `/verify-prices <path-or-url>` | Re-checks every recorded price against the vendor's live page |

A first draft you already have is raw material for the brief, nothing more. Its prose
has passed no rule in this repo, so it does not shortcut the outline stop.

## The tools

    python3 lint/run.py                     lint every draft and article
    python3 lint/run.py <path>              one file
    python3 lint/run.py <url>               a live page, fetched and extracted
    python3 lint/run.py --quiet             one line per file

    python3 lint/coverage.py <path>         must-cover coverage vs the guidelines
    python3 lint/coverage.py --list         every product section and its count

    python3 lint/prices.py <brief>          re-verify every recorded price
    python3 lint/prices.py --url <url>      probe one vendor pricing page

    python3 lint/calibrate.py               thresholds vs the reference corpus
    python3 lint/calibrate.py --fetch       rebuild that corpus

`coverage.py` exists because the must-cover count is binding and I got it wrong by
hand twice on the same draft. `prices.py` exists because a bot cannot settle a vendor
contradiction and must hand it to a human instead of picking.

## The linter

    python3 lint/run.py

It checks every `[LINT]` rule and it blocks. A `PreToolUse` hook runs it on every Write and Edit into `drafts/` or `articles/`, so a violation cannot reach disk that way. A file written through Bash skips that gate, a heredoc doing a bulk find-and-replace being the usual case, so the guarantee that actually holds is the `Stop` hook: it lints the tree and refuses to end the turn while errors remain. A violation cannot survive a turn. Run the linter yourself after any Bash write rather than waiting for the Stop hook to catch it.

When it fires, fix the named violation at the named location and run it again. Do not argue with it and do not hand-check what it covers. Read for the `[JUDGE]` items instead: voice, real first-hand moments, competitor fairness, opening-frame variety across tool sections.

If a rule is genuinely wrong, say so and we change the rule. Do not work around it.

## Drafting shape

Research writes a brief to `research/<slug>.md`. Drafting reads only that brief plus the rules files, one section per turn, fresh context each time. If the brief is missing something, fix the brief rather than pasting extra context into the drafting turn.

## Working style

- Single-word approvals advance. Do not restate the decision or summarise what you are about to do. Just do it.
- Do not ask clarifying questions unless genuinely blocked. Ambiguities go into the outline as flagged decisions.
- Flag conflicts before applying them: research against a rule, one rule file against another, a cascading change. Name the conflict, name the options, wait.
- Corrections apply everywhere at once. If a word slips through in five places, fix all five in the same pass.
- Show the changed section, not the whole file.
- Say what changed, not what you are about to do.
- When something breaks, own it plainly and give the fix.
