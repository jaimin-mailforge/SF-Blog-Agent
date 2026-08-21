"""Score a draft section by section, so a polish pass targets only what needs it.

    python3 lint/sections.py drafts/<slug>.md            ranked table
    python3 lint/sections.py drafts/<slug>.md --targets   just the sections to polish
    python3 lint/sections.py drafts/<slug>.md --all       show clean sections too

Exit code is the number of sections needing a polish pass.

## Why this exists

The continuity pass on the Expandi draft rewrote all eleven prose units, spent 1.1M
subagent tokens across 22 agents, and hit the org's monthly spend limit mid-run. Seventeen
agents died and the run had to be resumed.

**And then this tool proved that pass was justified,** which was not the answer I expected
when I built it. Run against the pre-polish draft it scores 13 of 16 sections above the
threshold, 81%, and ranks Salesforge first on 4 frame restarts, which is the same section
a human read as the worst offender. I had told Jaimin the fan-out was mostly waste and
the linter could have named three or four sections. That was wrong, and the measurement
is what says so.

The value is forward-looking, not a retroactive indictment. The same draft after the pass
scores 2 of 16, so the next pass over it is a 12% job rather than a 100% one. Re-polishing
a finished article, or polishing one written section by section under the current rules,
is where a full fan-out genuinely burns the budget on prose that is already right.

`trailing-superlative-i` and `frame-restart` already localise the defect. Nothing read
that localisation back out. This reads it out: rank the sections, polish the top few,
leave the rest alone.

## Why it recomputes instead of reading findings

`trailing-superlative-i` and `frame-restart` are counted rules with article-level caps of
two. A section carrying one instance is invisible in the article-level output, and a
section carrying four is reported as part of one number. For targeting you need the raw
per-section count, so this recomputes the same patterns check.py uses, imported from it
rather than copied, so the two cannot drift apart.

## What the score means

It is a triage order, not a verdict. A section at the top of the list is where the polish
pass should start, and a human still decides when to stop. The weights say a narrator
parked behind a superlative and a restarted frame are what a polish pass actually fixes,
while a long paragraph is a trim somebody can do by hand in a minute.
"""
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# What a polish pass is for, weighted by how much of one it takes to fix.
W_TRAILING_I = 3     # narrator used as a citation. a rewrite of the sentence
W_FRAME = 3          # a restarted frame. a rewrite of the section's argument
W_FRAGMENT = 2       # verbless sentence. a rewrite of the sentence
W_LONG_PARA = 1      # over the 60-word cap. a trim

# Below this, leave the section alone. Calibrated so the Expandi draft after its polish
# pass reports zero targets and the same draft before it reports the sections that were
# actually broken.
POLISH_THRESHOLD = 3


def split_sections(text):
    """[(heading, body)] on H2 boundaries, preamble first."""
    marks = [(m.start(), m.group(0).strip()) for m in re.finditer(r'^##\s+(?!#).*$', text, re.M)]
    if not marks:
        return [('(whole file)', text)]
    out = [('(intro, before the first H2)', text[:marks[0][0]])]
    for i, (pos, head) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((head.lstrip('# ').strip(), text[pos:end]))
    return out


def score_section(body):
    prose_lines = [l for l in C.mask(body).splitlines()
                   if l.strip() and not l.lstrip().startswith(('#', '|'))]
    sents = C.sentences(prose_lines)
    n = len(sents)

    trailing = 0
    for s in sents:
        m = re.search(C._ICITE, s)
        if m and re.search(C._SUPER, s[:m.start()], re.I):
            trailing += 1

    frames = 0
    for s in sents:
        for pat, _ in C._FRAME:
            if re.search(pat, s, re.I):
                frames += 1
                break

    # Mirror check.py's own iteration exactly: paragraph prose only, skipping any
    # paragraph that opens a list, a table, a heading, HTML, or a bold label. Filtering
    # by LINE instead reported the Final Verdict's six mandated routing labels
    # ("**Running LinkedIn and email as one motion:** Salesforge.") as fragments, while
    # the article-level check correctly said zero. A scorer that disagrees with the
    # tested checker is worse than no scorer, because it sends a polish pass at prose
    # that is already right.
    frags = 0
    for para in re.split(r'\n\s*\n', C.mask(body)):
        if para.lstrip().startswith(('-', '*', '|', '#', '<')):
            continue
        for sent in C.sentences([para], min_words=1):
            if C._is_fragment(sent):
                frags += 1

    long_paras = 0
    for p in re.split(r'\n\s*\n', C.mask(body)):
        p = p.strip()
        if not p or p.startswith(('#', '|', '<', '-')):
            continue
        if len(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p).split()) > C.PARA_WORD_CAP:
            long_paras += 1

    # No per-section rhythm score, deliberately. The three floors were calibrated on
    # whole articles of 300 to 440 sentences. A 21-sentence section has no meaningful
    # distribution, and scoring one flagged the intro and the Waalaxy section as "flat"
    # when the article clears every floor. That is the same wrong-instrument mistake
    # writing.md section 6 records four times over. Rhythm is an article-level property.
    score = (W_TRAILING_I * trailing + W_FRAME * frames + W_FRAGMENT * frags
             + W_LONG_PARA * long_paras)
    return {'sentences': n, 'trailing': trailing, 'frames': frames, 'frags': frags,
            'long_paras': long_paras, 'score': score}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 1
    path = args[0]
    targets_only = '--targets' in sys.argv
    show_all = '--all' in sys.argv
    text = open(path, encoding='utf-8').read()

    rows = []
    for head, body in split_sections(text):
        st = score_section(body)
        if st['sentences'] == 0:
            continue
        rows.append((head, st))
    rows.sort(key=lambda r: -r[1]['score'])
    targets = [r for r in rows if r[1]['score'] >= POLISH_THRESHOLD]

    if targets_only:
        for head, _ in targets:
            print(head)
        return len(targets)

    print('SECTION SCORES  %s' % os.path.relpath(os.path.abspath(path), ROOT))
    print('  polish threshold %d. weights: trailing-I %d, frame %d, fragment %d, '
          'long para %d\n'
          % (POLISH_THRESHOLD, W_TRAILING_I, W_FRAME, W_FRAGMENT, W_LONG_PARA))
    print('  %-5s %-46s %5s %6s %6s %5s %5s'
          % ('score', 'section', 'sents', 'trailI', 'frame', 'frag', 'para'))
    print('  ' + '-' * 92)
    for head, st in rows:
        if not show_all and st['score'] < POLISH_THRESHOLD:
            continue
        print('  %-5d %-46s %5d %6d %6d %5d %5d'
              % (st['score'], head[:46], st['sentences'], st['trailing'], st['frames'],
                 st['frags'], st['long_paras']))

    if not targets:
        print('\n  Nothing at or above the threshold. No polish pass needed.')
        print('  Every section is clean on the four things a polish pass fixes.')
        return 0

    total = len(rows)
    print('\n  %d of %d sections need a pass. That is %d%% of the draft, so a full-file '
          'fan-out\n  would spend roughly %d%% of its budget on prose that is already right.'
          % (len(targets), total, round(100 * len(targets) / total),
             round(100 * (total - len(targets)) / total)))
    print('\n  Polish these, in this order:')
    for head, st in targets:
        why = []
        if st['trailing']:
            why.append('%d trailing-I' % st['trailing'])
        if st['frames']:
            why.append('%d frame restart%s' % (st['frames'], '' if st['frames'] == 1 else 's'))
        if st['frags']:
            why.append('%d fragment%s' % (st['frags'], '' if st['frags'] == 1 else 's'))
        if st['long_paras']:
            why.append('%d long para%s' % (st['long_paras'], '' if st['long_paras'] == 1 else 's'))
        print('     %-44s %s' % (head[:44], ', '.join(why)))
    return len(targets)


if __name__ == '__main__':
    sys.exit(main())
