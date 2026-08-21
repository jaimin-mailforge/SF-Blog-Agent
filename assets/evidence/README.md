# Evidence

Hand-captured proof for claims no fetch can verify. One directory per article slug.

    assets/evidence/<slug>/<vendor>-<what>-<YYYY-MM-DD>.png

Reference it from the brief, on the provenance line it backs:

    **Pricing**, waalaxy.com/pricing, read 2026-08-13, evidence: waalaxy-pricing-2026-08-13.png

`python3 lint/evidence.py research/<slug>.md` checks that every referenced file exists,
that every rating claim has a file behind it, and that no file sits here unreferenced.

## What needs a file

**Every rating.** G2 and Capterra both return 403 to automated access, so every rating in
every brief is hand-captured by definition. A rating with no screenshot is a number with
no source.

**Prices on pages a fetch cannot read.** JS-rendered, geolocated, or behind a currency
switcher. `lint/evidence.py --probe` finds them. Everything else is covered by a recorded
read date plus a successful fetch, and does not need a screenshot. The gate is targeted on
purpose: demanding an image for every price would bury the ones that matter.

## What the capture has to show

The two things that went wrong on the Expandi article were both cropped out of the shot:

- **Which billing tab is selected.** Waalaxy's toggle reads Monthly, Quarterly -20%,
  Yearly -50%, and the brief recorded a 50% discount against an actual 20%.
- **Which currency is being served.** Every automated route served Waalaxy at EUR
  19/49/69 while the screenshot showed USD 16/32/55. That one is still unresolved.

Capture the toggle and the currency symbol in the same frame as the price. A crop that
loses either settles nothing, and a screenshot that settles nothing is worse than none,
because it looks like verification.
