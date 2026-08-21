---
name: verify-prices
description: Re-verify every price a research brief or a live article claims, against the vendor's current pricing page. Use before drafting, before publishing, and on any article older than a month. Also use when a price looks wrong or a vendor has changed its plans.
---

# Price verification

Argument: a brief under `research/`, a draft under `drafts/`, a live URL, or a single
vendor pricing URL.

This is a standalone skill because it is the step most likely to get skipped and the
most expensive when it is wrong. Two specific failures are why:

- Waalaxy served EUR at 19/49/69 across seven URL forms, including `?currency=USD`
  and the `/us/` route, while our brief carried USD at 16/32/55 from a screenshot.
  No dollar sign appeared anywhere in 1.4 MB of served HTML.
- lemlist's 100,000-email tier reads $80 on the pricing page and $71 in the help
  centre. The two were never reconciled and the draft had to pick one and say so.

## Run it

    python3 lint/prices.py research/<slug>.md          every source in a brief
    python3 lint/prices.py --url https://x.com/pricing  one vendor page
    python3 lint/prices.py research/<slug>.md --stale 7 tighter staleness threshold

Then close the loop on everything a fetch cannot settle:

    python3 lint/evidence.py research/<slug>.md         every claim needs a file
    python3 lint/evidence.py research/<slug>.md --probe  also fetch each vendor page
    python3 lint/evidence.py --list                      what is on disk

`prices.py` finds the symptom. `evidence.py` finds the cause, which is a screenshot that
arrived in chat, got transcribed by hand, and left nothing on disk connecting the claim to
the image. Every rating needs a file, because G2 and Capterra both 403. A price needs one
only when `--probe` says the page cannot be machine-read.

## What the output means

- `serves EUR/GBP/USD` — the page has a currency switcher. Which one you read is now
  part of the fact. Record it.
- `not in the served HTML` with the weak-signal note — curl saw one tab of a billing
  toggle. This is not evidence the price changed.
- `no figures found, likely JS-rendered` — the tool cannot see this page. A human has
  to open it.
- `no read date recorded` — the provenance line is incomplete, so staleness is
  unknowable. Fix the brief.
- `Evidence sections with no **Pricing**, vendor.com line at all` — a vendor is
  covered in the brief with no recorded source for its price. Blocker.

## The rules this enforces

From `CLAUDE.md` and `rules/writing.md`:

- Every price comes from the vendor's live pricing page. Never from G2, Capterra, a
  listicle, Reddit, an AI summary, or one of our older articles.
- Record the URL and the date. The brief format the verifier reads is
  `**Pricing**, vendor.com/pricing, read YYYY-MM-DD.`
- Every price is the annual rate, phrased "$X/month billed annually". No monthly or
  quarterly columns in a pricing table.
- `rules/positioning.md` wins on Forge prices and on anything in its resolved-decision
  log. Check there before changing a Forge figure.

## Where you must stop and ask

Do not resolve any of these by picking a number:

- The page serves a currency the brief does not claim
- More than one currency is served and the brief does not say which was read
- The vendor's pricing page and its help centre disagree
- No figure appears in the HTML, so the page is JS-rendered or geolocated
- A figure moved and you cannot tell whether the plan changed or the toggle did

In every one of those cases, ask for a screenshot of the rendered page and record the
URL, the date and the currency seen. A screenshot of a rendered page beats any
extraction of it. That sentence is in the Expandi brief because it was learned the
hard way.

## Any figure you cannot verify

It goes in as `[[FIGURE: what it is]]`. Never estimate, never quietly drop the
sentence. The linter blocks publishing while a marker remains in `articles/`, and
allows it in `drafts/`.
