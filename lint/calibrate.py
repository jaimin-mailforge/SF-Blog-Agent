"""Calibration harness. Checks our thresholds against a reference corpus.

NOT the linter. `lint/run.py` is the linter. This file answers a different question:
"would this threshold fire on the editor-approved article?" That is how every numeric
constant in check.py was set, and it is the only guard against a rule that reads
plausible and flags good prose.

It needs a local corpus that is deliberately NOT in git, because the files are
published pages belonging to other people:

    /tmp/bench.md          our cold-email draft, markdown, supplied by hand
    /tmp/<slug>.html       saved page source, one per slug in SLUGS

Rebuild the HTML half with:

    python3 lint/calibrate.py --fetch

Missing files are skipped with a warning instead of crashing, so a partial corpus
still works. This used to be lint/run.py, which meant the linter command documented
in CLAUDE.md crashed on any fresh clone.
"""
import sys, os, re, collections, subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C
from extract import extract

SLUGS = ('gohighlevel-review', 'email-sequence-software', 'linkedin-ai-tools',
         'rocketreach-alternatives')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120 Safari/537.36')


def fetch():
    for slug in SLUGS:
        url = 'https://www.salesforge.ai/blog/%s' % slug
        print('fetching %s' % url)
        subprocess.run(['curl', '-sS', '-A', UA, url, '-o', '/tmp/%s.html' % slug],
                       check=True)
    print('done. /tmp/bench.md is a draft, not a page, so supply it by hand.')


def corpus():
    arts = []
    if os.path.exists('/tmp/bench.md'):
        md = open('/tmp/bench.md', encoding='utf-8').read()
        m = re.search(r'\*\*Meta:\*\*\s*(.+)', md)
        arts.append(('cold-email-software (md)',
                     md.splitlines()[0].lstrip('# ').strip(),
                     m.group(1).strip() if m else '', md))
    else:
        sys.stderr.write('skip: /tmp/bench.md absent\n')
    for slug in SLUGS:
        path = '/tmp/%s.html' % slug
        if not os.path.exists(path):
            sys.stderr.write('skip: %s absent, run --fetch\n' % path)
            continue
        d = extract(path)
        arts.append((slug, d['title'], d['meta'], d['text']))
    return arts


def main():
    if '--fetch' in sys.argv:
        fetch()
        return 0
    arts = corpus()
    if not arts:
        sys.stderr.write('no corpus. run: python3 lint/calibrate.py --fetch\n')
        return 1

    summary = []
    for label, title, meta, text in arts:
        f, st = C.check(title, meta, text, label)
        err = [x for x in f if x[0] == 'ERROR']
        warn = [x for x in f if x[0] == 'WARN']
        bl, al = C.interlinks(text)
        of = C.opening_frames(text)
        print('=' * 78)
        print('%s' % label.upper())
        print('  %s' % title[:70])
        print('  chars %-6d sentences %-4d over-25w %-3d paras %-4d over-%dw %-3d avg-para %s'
              % (st['chars'], st['sentences'], st['over25'], st['paras'],
                 C.PARA_WORD_CAP, st['over_para_cap'], st['avg_para']))
        print('  rhythm  stdev %-5.2f (%.1f+)  <=6w %-5.1f%% (%d+)  >25w %-5.1f%% (%d+)'
              % (st['stdev'], C.STDEV_FLOOR, st['short_pct'], C.SHORT_FLOOR,
                 st['long_pct'], C.LONG_FLOOR))
        print('  blog interlinks %-3d (min 5)   all links %-3d   title %d   meta %s'
              % (bl, al, len(title), len(meta) if meta else 'MISSING'))
        if of:
            print('  per-tool opener "%s": %d of %d sections' % (of[0], of[1], of[2]))
        print('  ERRORS %d   WARNINGS %d' % (len(err), len(warn)))
        counts = collections.Counter(r.split('(')[0] for _, r, _ in f)
        for rule, n in counts.most_common(14):
            print('     %-34s %d' % (rule, n))
        for sev, rule, det in err[:12]:
            print('     ! %-26s %s' % (rule[:26], det[:88]))
        summary.append((label, len(err), len(warn), bl, st['over25'], st['over_para_cap']))

    print('=' * 78)
    print('%-26s %6s %6s %6s %8s %8s'
          % ('ARTICLE', 'ERR', 'WARN', 'ILINK', '>25w', '  >60w'))
    for s in summary:
        print('%-26s %6d %6d %6d %8d %8d' % s)
    return 0


if __name__ == '__main__':
    sys.exit(main())
