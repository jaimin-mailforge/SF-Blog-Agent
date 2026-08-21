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

10. **Figurative verbs only fired when the subject was "the" or "it".** Fixed 2026-08-13.
   The pattern was `\b(?:The|the|It|it)\s+\w*\s?VERB`, which misses the two commonest
   forms: a named product as the actor ("Waalaxy sits at 0.5%") and a relative clause in
   the mandated explainer sentence ("a LinkedIn automation tool that puts email steps
   inside"). Four clear violations in the Expandi draft, all reported clean. The subject
   list now includes every name in `product-names.txt` plus this/that/which/who. "G2 puts
   X at 4.6" is the wording section 9b mandates and G2 is deliberately not a subject, so
   it needs no exemption. Verified: catches all four, does not fire on the mandated line.

11. **The banned-verb data file was two verbs short of the rule.** Fixed 2026-08-13.
   `writing.md` section 5 bans nine figurative verbs. `figurative-verbs.txt` carried seven,
   missing **lives** and **flows**, so those two were unenforceable no matter what the
   subject pattern did. Both added, third-person-singular only. Bare "live" and "living"
   are deliberately not banned: the subject pattern would flag "the live pricing page",
   which is correct usage and appears in the draft's own methodology line.

12. **A four-sentence paragraph reported as three.** Fixed 2026-08-13. Paragraph shape
   reused `sentences()`, which drops fragments under three words so that table debris and
   bare labels do not get charged against the 25-word ceiling. That filter also ate real
   short sentences, so the Skylead FAQ paragraph's "Two caveats." vanished and a
   four-sentence paragraph counted as three. `sentences()` now takes `min_words`, still 3
   by default for the word-count check, and paragraph counting passes 1.

13. **Four rules had no checker at all.** Added 2026-08-13, all WARN, since they are
   judgment calls on prose and the repo convention is that warnings report and do not
   block. Each one reproduced a finding an independent editorial read had made by hand,
   which is how they were calibrated.

   - `proscons-4x4` and `proscons-symmetry` for section 5's named ban on "perfectly
     balanced pros and cons, four against four". The Expandi draft ran 4v4 in seven of
     seven competitor sections.
   - `entry-frame-repeat` and `entry-superlative` for section 21's requirement that tool
     section entry angles vary. Five sections opened on a superlative.
   - `define-by-negation` for section 6. Counts "rather than", "instead of" and bare
     ", not". The draft ran 28.
   - `unscoped-comparison` for section 17. Counts "of the nine", "on this list" and scoped
     "here", none of which survive being quoted off the page by an LLM or a snippet. The
     draft ran 32.

   Thresholds are constants at the top of `check.py`, not magic numbers inline.

14. **Two rules for prose continuity, and one of them had been unenforced for a cycle.** Added
   2026-08-20 after Jaimin read the Expandi draft as disconnected and lacking a practitioner
   narrator. Both WARN.

   Worth recording how they were calibrated, because the first four instruments I built all said
   the draft was *better* than the editor-approved article and all four were measuring the wrong
   thing. Connective openers: draft 27.7%, approved 12.1%. Back-reference: draft 31.5%, approved
   20.6%. Subordination: draft 11.4%, approved 7.4%. Runs of short parallel sentences: draft
   17.4%, approved 28.6%. On every count the draft won, and the draft was the one that read
   broken. The defect was one level up, at the paragraph and section, and it does not show in any
   sentence statistic.

   - `trailing-superlative-i`. A superlative followed by an "I"-clause in the same sentence, which
     parks the narrator in a trailing position to license the claim. Section 20 has capped this at
     two per article since 2026-08-19 and never had a checker, so fifteen shipped. Approved
     article: 1. Draft: 15.
   - `frame-restart`. Topic announcements: "is what matters", "matters most", "worth
     understanding", "Two things", "There are N reasons", "X is the thing/part", "is the Nth
     gate", "What differs". Approved article: 0. Draft: 7. "is the real reason" was tried and
     dropped: it reads as a paragraph closing line as often as a restart and cost half the
     precision.

   Both counted rather than located, on the same reasoning as the four checks in item 13: one
   instance is a signpost, eight is a prose habit.

15. **`sentence-fragment` false-positived on clean prose.** Fixed 2026-08-20. The continuity pass
   produced "You source the other end with Leadsforge.", which has a subject and a finite verb and
   was reported as verbless. `_FINITE` is an allowlist of verbs, not a parser, so any legitimate
   verb missing from it reads as a fragment. Added the fourteen the new prose needed: source, hear,
   govern, split, chain, earn, lift, drop, check, scale, track, trade and their -s forms. Regression
   checked against the five fragments the rule exists to catch, and the two it already documented
   as misses ("In fragments.", "Connected or not.") are still misses, unchanged. The lesson is that
   the allowlist grows with the prose, so expect to add to it after any pass that changes the verbs
   in use.

16. **The documented linter command crashed on a fresh clone.** Fixed 2026-08-20.
   `CLAUDE.md` told every session to run `python3 lint/run.py` as the linter. That file
   was a calibration harness that opened `/tmp/bench.md` and three `/tmp/*.html` pages,
   none of them in git, so on any fresh clone the documented command died with
   FileNotFoundError. It survived this long only because one container persisted.

   Split in two rather than patched. `lint/run.py` is now the linter and takes nothing
   from `/tmp`: no args lints the tree, a path lints one file, a URL fetches and extracts
   a live page, `--quiet` gives one line each, and the exit code is the number of files
   with errors. `lint/calibrate.py` keeps the threshold work, skips missing corpus files
   with a warning instead of crashing, and grows a `--fetch` mode to rebuild them.

   Worth noting why it mattered beyond tidiness: the URL mode is what makes a rewrite
   auditable in one command, and that was already sitting in `publish-check.py` unused
   by anything the docs pointed at.

17. **Two rules had no checker because they were counting jobs, not prose jobs.** Added
   2026-08-20 as standalone tools rather than `check.py` rules, because both need a
   second file to compare against.

   - `lint/coverage.py`. The guidelines say every must-cover feature of a featured
     product must appear, "Not most. All." I got that wrong by hand twice on one draft,
     first bundling three must-covers into a single bullet and then shipping 11 bullets
     against 12. It parses the guidelines, resolves the section from the playbook table,
     and reports in-section / elsewhere-only / uncertain / missing plus a bullet-count
     check. The elsewhere-only bucket is the important one: a must-cover matching only a
     comparison-table row is the bundling failure wearing a pass.
   - `lint/prices.py`. Re-verifies every price a brief claims against the vendor's live
     page. Deliberately does not pick a number. It reproduces both known traps on
     demand: Waalaxy serves EUR only, and the brief's USD figures appear nowhere in the
     HTML. Two calibration lessons went into it. Requiring a read date made it skip
     Waalaxy entirely, the least-verified price in the brief, so the date is optional
     and its absence is the flag. And flagging every figure missing from the served HTML
     produced 40-odd false alarms from billing toggles curl cannot flip, so that signal
     is labelled weak when a toggle or a currency switcher is present. A verifier that
     cries wolf gets ignored, and then prices are unverified again.

18. **AI framings: one index, and the measurement that said not to build a checker.**
   Added 2026-08-21 on Jaimin's instruction to strictly avoid typical AI framings.

   Twenty-five candidate framings counted across the approved article, the Expandi draft
   and three published articles first. Almost nothing hit. Structural tells scored zero:
   no punchline paragraphs anywhere, no negation-then-correction pairs in the Expandi
   draft against one in the approved article, colon-explainers level at two each,
   pronoun-subject openers 9.5% against the approved article's 6.9%. The earlier passes
   had already removed them, so section 5a is written as a preventive index rather than
   a repair list, and it says so at the top. No new checker: section 6 had just finished
   recording that four metrics in a row said our prose was fine when a human said
   otherwise, and adding a fifth on the same day would have been the trap.

   Three calibration decisions worth keeping:

   - `at scale` was a candidate and is **allowed**. The approved article uses it three
     times. Banning it would flag the benchmark, the same error an intro paragraph-count
     check made earlier the same day.
   - `whether you're X or Y` stays a judgment call. Slop as an audience hedge, precise as
     a plan comparison, same construction. A hard ban is an ERROR that blocks a write, so
     anything with a legitimate twin cannot have one.
   - `source of truth` was banned and unbanned within the hour. It caught two genuine
     instances and both were correct usage, because single source of truth is how CRM
     vendors describe themselves. Section 6 had removed the layman-language rule that
     same day to stop us stripping this reader's own vocabulary, and banning this would
     have been that deleted rule returning through a different file. The lesson is that a
     phrase can be corporate jargon and still be the plain word for the person reading.

   Net: `leverage` and its forms plus `landscape` to banned-words, nineteen phrases to
   banned-phrases, all verified to fire zero times on the approved article before landing.
   The two genuine catches in the corpus were `that said` once and, before the reversal,
   `source of truth` twice.

## Open

- **`sentence-fragment` cannot see a verbless FAQ opener.** Surfaced 2026-08-20 by a reading pass,
  not by the linter. `_is_fragment` returns early on anything matching `^(?:Yes|No)\b`, because
  section 16 mandates the "Yes." plus support shape and the article's own approved phrasing includes
  "Yes, with a specific caveat.", which is verbless and correct. That exemption also passed
  "Yes, but not as a channel.", a real regression from a finite-verb original. Narrowing the
  exemption to a bare "Yes." would flag the mandated caveat form, so the gap stays open and the
  FAQ openers are a read-for item. Caught here by an adversarial reviewer, which is what `[JUDGE]`
  is for.

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
