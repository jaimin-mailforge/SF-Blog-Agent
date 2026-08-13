# Linter calibration log

## Fixed

1. **Product names tripping banned words.** `Seamless.AI` matched the banned word
   `seamless`. Fixed with span-based exemption: product names in
   `data/product-names.txt` mark protected character ranges, and a banned-word hit
   inside one is skipped. First attempt blanked the names instead, which distorted
   sentence splitting and inflated the over-25-word count. Spans, not blanking.
2. **Quote masking paired the wrong quote marks.** The old regex started at a
   sentence-final `"planned."` and ran to the next opening quote, leaving the real
   review quote unmasked. Replaced with `_mask_paired_quotes`, which pairs quote
   marks in document order and masks any pair over 25 characters. Verified against
   the GoHighLevel review, where `us` inside a reviewer quote no longer fires.
3. **Hyphen variants missed.** `game-changer` on the list did not match
   `game changer` in prose. `word_pattern()` now matches either form.
4. **Table rows read as long sentences.** Extracted HTML flattens table cells onto
   one line. Now masked three ways: markdown pipe rows, lines with two or more
   ` | ` separators, and lines carrying runs of six or more spaces. Re-running after
   the fix moved the over-25-word counts by roughly one percent, which confirms
   those long sentences are genuine and not artifacts.

5. **A fact rule fired on a correct competitor fact.** `billed quarterly` was written
   to catch the Agent Frank price error and blocked a HeyReach pricing table whose
   quarterly column is accurate. Quarterly billing is not a Forge-only cycle, so
   banning the phrase was never the right shape. Fact needles can now be regexes
   (prefix `re:`, with an explicit label since a raw pattern reads badly in a
   finding), and the two Forge billing traps are expressed as "wrong figure in the
   same sentence as the product" instead. Fact rules still run against raw text
   rather than masked text, deliberately: a wrong price inside a table is still
   wrong. Verified against 13 cases including both traps written correctly, written
   backwards, and split across sentences.

## Open

- **Bare `Seamless` in a slash list.** `Apollo/Seamless/HeyReach` is clearly the
  product, but adding bare `Seamless` to the exemption list would let real uses of
  the banned word through. Leaving it to fire and be dismissed by a human. One
  false positive per article is an acceptable price for not opening that hole.
- **A sentence ending on a single capital letter does not split.** The initials rule
  strips the period from `\b[A-Z]\.` so "Frank S. Sondors" stays one sentence, and
  that also eats the period in "LinkedIn, email and X. It is cheaper", gluing two
  sentences together. X is a real brand in this category, so this will recur. Every
  narrower rule tried also matches "J. Smith", so it needs a real fix rather than a
  tweak. Worked around in the Expandi draft by not ending a sentence on X.
- **`meta-missing` on every published page.** Either Webflow sets the description
  somewhere the extractor does not read, or the articles genuinely ship without
  one. Needs a look in Webflow before it can be treated as a real defect.

- **`PreToolUse` only sees Write and Edit.** A file written through Bash, such as a
  Python heredoc doing a bulk find-and-replace across a draft, never reaches the
  gate. The `Stop` hook still lints the tree and holds the turn open, so a violation
  cannot survive a turn, but `CLAUDE.md`'s stronger claim that it "cannot reach
  disk" is only true for Write and Edit. Either widen the matcher to Bash or soften
  the claim. Found during the judge pass on the Expandi draft, where the whole
  contraction rewrite went in through Bash.

## Rule promotion status

`PreToolUse` and `Stop` hooks are live and blocking on `drafts/` and `articles/`.
The rules files are out of scope, since they carry the banned lists in prose and
would flag themselves. Warnings report and do not block.
