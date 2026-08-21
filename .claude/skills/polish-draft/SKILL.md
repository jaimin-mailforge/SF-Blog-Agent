---
name: polish-draft
description: Continuity and practitioner-voice pass on a finished draft. Rewrites each prose block for one argument per section with the narrator leading, then adversarially verifies every rewrite for fabricated figures and lost figures. Use on a draft that is already lint-clean but reads disconnected, or reads like a bibliography rather than a practitioner.
---

# Continuity and voice pass

Argument: a path under `drafts/`. Run this on a draft that already passes
`python3 lint/run.py`. A lint-clean draft can still fail the two defects this skill
exists for, which is how it got written.

## Why this exists, and what not to measure

The Expandi draft was lint-clean and read disconnected. Four instruments all said it
beat the editor-approved article and all four were measuring the wrong level:

| | Approved | The draft that read broken |
|---|---|---|
| Connective openers | 12.1% | 27.7% |
| Back-reference | 20.6% | 31.5% |
| Subordination | 7.4% | 11.4% |
| Runs of short parallel sentences | 28.6% | 17.4% |

Do not re-derive those. The defect is at the paragraph and the section, and no
sentence statistic reaches it. Read `rules/writing.md` sections 2 and 3 for the two
rules that do catch it.

## 1. Scope the pass before you spend anything on it

    python3 lint/sections.py <path>              ranked, with the reason per section
    python3 lint/sections.py <path> --targets    just the section headings to polish

**Polish only the sections it names.** The first continuity pass on the Expandi draft
fanned out over all eleven prose units, spent 1.1M subagent tokens across 22 agents, and
hit the org's monthly spend limit mid-run. On that draft the spend was justified, 13 of 16
sections scored above the threshold. On the same draft after the pass it is 2 of 16. A
re-polish, or a draft written section by section under the current rules, is where a
full-file fan-out burns most of its budget on prose that is already right.

The scorer counts raw per-section instances, not the capped article-level findings, because
`trailing-superlative-i` and `frame-restart` both cap at two per article and a section
carrying one is invisible in the article-level output. So a clean `lint/run.py` does not
mean there is nothing to polish, and `sections.py` reporting a target does not mean the
linter is failing.

## 2. Measure the two things that do discriminate

    python3 lint/run.py <path>

`trailing-superlative-i` and `frame-restart` are the two checks for this. The approved
article scores 1 and 0. A draft with 15 and 7 has both defects.

Then read the draft yourself, section by section, and for each one write down the
single argument it runs. If you cannot state it in one sentence, or if you find
yourself writing two, that section has no argument and needs this pass.

## 3. Split the prose into units and rewrite each one

Work per section, not per file, and do not touch tables, key-feature bullets or
`**Best for:**` lines unless they carry a defect.

For each unit the shape is three moves and one argument:

1. **State it**, with the narrator leading. `I point most buyers at it first because
   it turns two invoices into one.`
2. **Develop it to its consequence**, with the numbers doing the work.
3. **Qualify it honestly.**

Banned, because each one restarts the article: `X is what matters`, `X matters most`,
`the part worth understanding`, `Two things behind it`, `There are three reasons`,
`X is the second gate`, `What differs is`.

The practitioner sentence is **I + present-tense verb + object + a "when" or
"because" clause**. Never park "I" in a trailing clause after a superlative. Test it
by deleting the "I" clause: if the sentence still says everything it said, the
narrator was decoration.

Paragraphs chain. The second sentence develops the first. The next paragraph opens on
what the previous one established, named rather than pointed at with a bare "that".
A discourse marker in front of a sentence that does not follow is worse than no marker.

If the work is large enough to fan out, one subagent per section with the brief above,
each writing its replacement to a scratch file rather than editing the draft, so
parallel writes cannot collide.

## 4. Adversarially verify every rewrite

This is not optional and it is where the value is. On the Expandi pass the verify
stage found 82 defects the linter could not see, including:

- A fabricated cost claim no source supported
- An invented frequency ranking in a first-person sentence
- Arithmetic no source performed, in three places
- Four absolutes where the original had a scoped claim
- A fabricated count
- An inference that contradicted the sentence two lines above it
- Three false connectives, where `So` asserted logic the previous paragraph did not carry

Check each rewrite for: fabricated figures, lost figures, invented first-person
experience, banned punctuation, fragments, passive drift, surviving frame restarts,
surviving trailing-superlative "I", real continuity versus connective-deep, length
drift, and meaning drift toward an absolute.

Default to reporting a defect when unsure. Reject a finding only with a reason.

## 5. Deterministic fact check, not a judgment call

Before and after, diff every figure and URL across the whole file:

    python3 - <<'PY'
    import re, collections
    NUM = re.compile(r'(?<![\w.])(?:\$\s?[\d,]+(?:\.\d+)?|[\d,]+(?:\.\d+)?%|[\d,]+(?:\.\d+)?\+?)(?![\w])')
    URL = re.compile(r'https?://[^\s)\]]+')
    old = open('BEFORE.md', encoding='utf-8').read()
    new = open('AFTER.md', encoding='utf-8').read()
    def t(s): return collections.Counter(m.group(0).replace(' ','') for m in NUM.finditer(s)), collections.Counter(URL.findall(s))
    o, ou = t(old); n, nu = t(new)
    print('LOST :', sorted(k for k in o if k not in n) or 'none')
    print('ADDED:', sorted(k for k in n if k not in o) or 'none')
    print('URLS lost/added:', sorted(k for k in ou if k not in nu) or 'none',
          sorted(k for k in nu if k not in ou) or 'none')
    PY

A figure appearing more often is fine. A figure that appears nowhere in the original
is a fabrication and has to come out.

## 6. Rhythm follows, it does not lead

Do not chase the distribution floors directly. Real chaining produces variance on its
own: the Expandi pass cleared a standing `rhythm-flat` warning as a side effect,
stdev 6.97 to 7.07, with no sentence written for the metric.

If a floor is still short afterwards, split a sentence where both halves stand alone
and keep the left half short. Never bolt on a fragment or an extra clause. Bolting on
produced 14 fragments and roughly 10 redundancies on earlier passes, both of which had
to be undone.

## 7. Read it yourself last

The linter and the verifiers both miss things a read catches. On the Expandi pass a
final read found a verdict sentence sitting before the evidence its "because" clause
pointed at, two more verdicts wedged mid-argument, a product name used twice in one
sentence, and the same phrase opening two adjacent paragraphs. None of that is
machine-detectable.

Finish with `python3 lint/run.py <path>` clean, then report what changed with the
before-and-after counts for `trailing-superlative-i` and `frame-restart`.
