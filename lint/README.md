# lint

Deterministic checks for every rule tagged `[LINT]` in `rules/writing.md`.

    python3 lint/run.py                 # baseline across the corpus
    python3 lint/extract.py page.html   # pull article text out of a Webflow page

- `data/*.txt` hold the word, phrase and fact lists. Edit these, not the code.
- `check.py` masks non-prose regions first, then runs each check.
- `KNOWN-ISSUES.md` tracks calibration bugs found against real articles.

Masking matters more than the checks. Rules apply to body prose, never to code,
tables, link targets, or verbatim review quotes. Most false positives come from
masking gaps, not from bad rules.
