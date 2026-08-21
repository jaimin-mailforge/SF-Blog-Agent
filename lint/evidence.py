"""Evidence intake gate. Ties every unverifiable claim in a brief to a file on disk.

    python3 lint/evidence.py research/<slug>.md          audit a brief, offline
    python3 lint/evidence.py research/<slug>.md --probe   also fetch each vendor page
    python3 lint/evidence.py --list                       show the evidence tree

Exit code is the number of gaps, so it works in a shell conditional.

## Why this exists

`prices.py` catches the symptom of an unverified price. It cannot catch the cause, which
is that a screenshot arrives in chat, gets transcribed into a brief by hand, and from then
on nothing connects the claim to the image it came from. That is exactly how Waalaxy's
price went wrong: the brief said USD 16/32/55, every automated route served EUR 19/49/69,
and the only thing standing behind the USD figures was a screenshot nobody could re-open.

Two classes of claim can never be machine-verified, and both need a file:

  **Ratings.** G2 and Capterra both return 403 to automated access. Every rating in every
  brief is therefore hand-captured by definition, and `rules/writing.md` section 9b says
  so. A rating with no screenshot is a number with no source.

  **Prices on pages a fetch cannot read.** A JS-rendered page, a geolocated one, or one
  behind a currency switcher. `--probe` finds these; the rest of the time the recorded
  read date plus a successful fetch is enough and no screenshot is needed. This gate is
  deliberately targeted: demanding a screenshot for every price would make the ones that
  matter invisible in the noise.

## The convention

    assets/evidence/<slug>/<vendor>-<what>-<YYYY-MM-DD>.png

Reference it from the brief, anywhere in the vendor's Evidence section:

    **Pricing**, waalaxy.com/pricing, read 2026-08-13, evidence: waalaxy-pricing-2026-08-13.png

The filename carries the date so a stale screenshot is visible without opening it, and so
two captures of the same page do not overwrite each other.

**What a screenshot has to show.** The two things that went wrong on the Expandi article
were both invisible in the crop: which billing tab was selected, and which currency was
being served. Capture the toggle and the currency symbol in the same frame as the price,
or the screenshot settles nothing.
"""
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prices import PROV, MONEY, probe
import check as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_ROOT = os.path.join(ROOT, 'assets', 'evidence')

SECTION = re.compile(r'^##\s+Evidence:\s*(.+?)\s*$', re.M)
REF = re.compile(r'evidence:\s*([A-Za-z0-9._\-/]+\.(?:png|jpg|jpeg|webp|pdf))', re.I)
# "Capterra **4.4 from 31 reviews**" and "G2 4.2 from 112 reviews"
RATING = re.compile(r'\b(G2|Capterra)\b[^.\n]{0,40}?(\d\.\d)\s*(?:from|out of|/)', re.I)


def slug_of(path):
    return os.path.splitext(os.path.basename(path))[0]


def sections(text):
    """[(vendor, body)] for each '## Evidence: X' block, plus ('(preamble)', head)."""
    marks = [(m.start(), m.group(1)) for m in SECTION.finditer(text)]
    out = []
    if marks:
        out.append(('(outside any Evidence section)', text[:marks[0][0]]))
    else:
        return [('(whole brief)', text)]
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((name, text[pos:end]))
    return out


def main():
    if '--list' in sys.argv:
        if not os.path.isdir(EVIDENCE_ROOT):
            print('No evidence tree yet. Expected at %s'
                  % os.path.relpath(EVIDENCE_ROOT, ROOT))
            return 0
        for d in sorted(os.listdir(EVIDENCE_ROOT)):
            full = os.path.join(EVIDENCE_ROOT, d)
            if not os.path.isdir(full):
                continue
            files = sorted(f for f in os.listdir(full) if not f.startswith('.')
                           and f != 'README.md')
            print('%-34s %d file(s)' % (d, len(files)))
            for f in files:
                print('    %s' % f)
        return 0

    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 1
    brief = args[0]
    do_probe = '--probe' in sys.argv
    text = open(brief, encoding='utf-8').read()
    slug = slug_of(brief)
    ev_dir = os.path.join(EVIDENCE_ROOT, slug)

    print('EVIDENCE  %s' % os.path.relpath(os.path.abspath(brief), ROOT))
    print('  evidence dir: %s%s' % (os.path.relpath(ev_dir, ROOT),
                                    '' if os.path.isdir(ev_dir) else '   (does not exist)'))
    on_disk = set()
    if os.path.isdir(ev_dir):
        on_disk = {f for f in os.listdir(ev_dir)
                   if not f.startswith('.') and f != 'README.md'}
    print()

    gaps, referenced = [], set()

    for vendor, body in sections(text):
        refs = [r for r in REF.findall(body)]
        referenced.update(os.path.basename(r) for r in refs)
        # Mask paired quotes first. The Expandi brief quotes a competitor's unsourced
        # claim in order to debunk it, "Expandi G2 4.2 from 112 reviews", and we are not
        # the ones asserting it. check.py already has this masking and it is tested.
        ratings = [(p, s) for p, s in RATING.findall(C._mask_paired_quotes(body))]
        prices = PROV.findall(body)

        missing_files = [r for r in refs if os.path.basename(r) not in on_disk]
        needs = []
        if ratings and not refs:
            plats = sorted({p.title() for p, _ in ratings})
            needs.append('%d rating claim(s) from %s, no screenshot referenced. '
                         'Both platforms 403, so a rating with no file has no source.'
                         % (len(ratings), ' and '.join(plats)))
        for r in missing_files:
            needs.append('referenced but not on disk: %s' % r)

        if do_probe:
            for url, read_on in prices:
                p = probe(url)
                unreadable = (not p['figures']) or len(p['currencies']) > 1
                if unreadable and not refs:
                    why = ('no figures in the served HTML' if not p['figures']
                           else 'serves %s' % '/'.join(p['currencies']))
                    needs.append('%s cannot be machine-read (%s) and has no screenshot'
                                 % (url, why))

        if needs or refs or ratings or prices:
            status = 'GAP ' if needs else 'ok  '
            print('  [%s] %s' % (status, vendor))
            if refs:
                for r in refs:
                    mark = 'on disk' if os.path.basename(r) in on_disk else 'MISSING'
                    print('        evidence: %-44s %s' % (r, mark))
            if ratings and not needs:
                print('        %d rating claim(s), covered' % len(ratings))
            for n in needs:
                print('        ! %s' % n)
                gaps.append('%s: %s' % (vendor, n))
            print()

    orphans = sorted(on_disk - referenced)
    if orphans:
        print('  Files on disk that no brief line references:')
        for o in orphans:
            print('        ? %s' % o)
        print('        Either wire each one into a provenance line or delete it. An')
        print('        unreferenced screenshot is evidence nobody can find.\n')

    print('%d gap(s).' % len(gaps))
    if gaps:
        print('A gap is not a lint error, it is a missing fact. Capture the screenshot,')
        print('drop it in %s, and add "evidence: <file>" to the'
              % os.path.relpath(ev_dir, ROOT))
        print('provenance line it backs. Show the billing toggle and the currency in')
        print('the same frame, because those are the two things the crop usually loses.')
    return min(len(gaps), 125)


if __name__ == '__main__':
    sys.exit(main())
