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

6. **The colon rule double-charged the 25-word ceiling.** Jaimin's 2026-08-13 format
   change put a colon after the feature name in TL;DR entries and key-feature
   bullets, where a period used to be. That merged a label and its description into
   one sentence for the splitter, and 7 of the 17 over-25-word findings on the
   Expandi draft were bullets whose prose had not changed at all. `sentences()` now
   strips a leading bolded label plus colon before splitting, so the label is not
   charged against the sentence budget. The remaining 10 findings were real and were
   split by hand.
7. **Lowercase brands could not open an HTML table cell.** The `opens` check claimed
   in its own comment to allow a table cell, but the regex only recognised a markdown
   pipe, so `<th><a href="#lemlist">Lemlist</a></th>` failed while `| Lemlist |`
   passed. Now an HTML tag immediately before the name also counts as opening. This
   matters because the mandated comparison table is HTML, not markdown.

8. **A sentence ending on a single capital letter now splits.** Fixed 2026-08-13 by
   deleting the initials rule rather than narrowing it. It stripped the period from
   `\b[A-Z]\.` to keep "Frank S. Sondors" whole, and that ate the period in
   "LinkedIn, email and X. Every other tool", counting two sentences as one long
   one. Every narrower rule tried broke on either "J. Smith" or "Category A. Category
   B". What settled it was checking the corpus: across every draft and article, that
   pattern matched the bug twice and a real initial zero times, and the byline is
   fixed as "Frank Sondors" with no middle initial. So the rule was protecting
   nothing. If an initial ever appears it splits into a sub-three-word fragment the
   filter drops, which under-reports instead of inventing an error. The Expandi draft
   went from 393 sentences to 394, still 0 errors.

9. **`PreToolUse` only sees Write and Edit.** Closed 2026-08-13 by correcting the
   claim rather than widening the matcher. A file written through Bash, such as a
   heredoc doing a bulk find-and-replace, never reaches the gate, so `CLAUDE.md`'s
   claim that a violation "cannot reach disk" was only true for Write and Edit.
   Widening to Bash would fire the linter on every unrelated shell command, so
   `CLAUDE.md` now states the guarantee that actually holds, which is the `Stop`
   hook: a violation cannot survive a turn. It also tells you to run the linter
   yourself after a Bash write. Found during the judge pass on the Expandi draft,
   where the whole contraction rewrite went in through Bash.

## Open

- **Bare `Seamless` in a slash list.** `Apollo/Seamless/HeyReach` is clearly the
  product, but adding bare `Seamless` to the exemption list would let real uses of
  the banned word through. Leaving it to fire and be dismissed by a human. One
  false positive per article is an acceptable price for not opening that hole.
- **`meta-missing` on every published page.** Either Webflow sets the description
  somewhere the extractor does not read, or the articles genuinely ship without
  one. Needs a look in Webflow before it can be treated as a real defect.

## Rule promotion status

`PreToolUse` and `Stop` hooks are live and blocking on `drafts/` and `articles/`.
The rules files are out of scope, since they carry the banned lists in prose and
would flag themselves. Warnings report and do not block.
