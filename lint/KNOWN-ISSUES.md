# Linter calibration log

Findings from the first baseline run against four articles. Fix these before any
rule is promoted to blocking.

## Confirmed linter bugs

1. **Product names trigger banned-word hits.** `Seamless.AI` matches the banned
   word `seamless`. The rules already exempt product names, so the linter needs a
   `data/product-names.txt` exemption applied before the banned-word scan.
2. **Quote masking pairs the wrong quote marks.** The regex `"[^"\n]{25,}"` starts
   matching at a sentence-final `"planned."` and consumes the text up to the *next*
   opening quote, so the real review quote after it is left unmasked. Observed on
   the GoHighLevel review, where `us` inside a verbatim reviewer quote was flagged.
   Needs a proper paired-quote pass, or extraction that emits blockquote markers.
3. **Hyphen variants are missed.** `game-changer` is on the banned list but the
   article writes `game changer`, which does not match. Word entries need to match
   both hyphenated and spaced forms.
4. **Table rows become pseudo-sentences.** HTML extraction flattens TL;DR table
   rows into single lines, which then read as 30-word sentences. Roughly 15 to 20
   percent of the `sentence>25w` findings on extracted articles are this artifact.
   Markdown sources are unaffected. Table regions need masking before the
   sentence pass.

## Not bugs, real findings

- `first-person-plural` fires on all three published articles and never on the
  markdown draft. High confidence, see the baseline report.
- Fact conflicts fire consistently and are all genuine.
- `meta-missing` on all three published pages is real, not an extraction gap.

## Rule promotion status

Everything runs at report level. Nothing blocks yet. Per the GitLab discipline in
`rules/writing.md`, a rule becomes blocking only once the existing corpus passes
it clean.
