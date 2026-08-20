"""The linter. Checks every [LINT] rule and blocks on errors.

    python3 lint/run.py                          every draft and article in the tree
    python3 lint/run.py drafts/expandi.md        one file
    python3 lint/run.py https://.../blog/slug    a live page
    python3 lint/run.py --quiet                  one line per file, errors only

Exit code is the number of files with errors, capped at 125, so it works in a
shell conditional and in CI.

A [[FIGURE:]] marker is a legal placeholder in drafts/ and an error anywhere else,
because an unresolved figure must never reach a published page.
"""
import sys, os, re, glob, subprocess, tempfile, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C
from extract import extract

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCOPES = ('drafts', 'articles')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120 Safari/537.36')


def load(target):
    """Return (label, title, meta, text, is_draft) for a path or a URL."""
    if target.startswith('http'):
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as fh:
            tmp = fh.name
        subprocess.run(['curl', '-sS', '-A', UA, target, '-o', tmp], check=True)
        d = extract(tmp)
        os.unlink(tmp)
        return target, d['title'], d['meta'], d['text'], False
    text = open(target, encoding='utf-8').read()
    title = text.splitlines()[0].lstrip('# ').strip() if text.strip() else ''
    m = re.search(r'\*\*Meta:\*\*\s*(.+)', text)
    label = os.path.relpath(os.path.abspath(target), ROOT)
    return label, title, (m.group(1).strip() if m else ''), text, '/drafts/' in ('/' + label)


def tree():
    out = []
    for scope in SCOPES:
        for f in sorted(glob.glob(os.path.join(ROOT, scope, '**', '*.md'),
                                  recursive=True)):
            if os.path.basename(f) == 'README.md':
                continue
            out.append(f)
    return out


def report(target, quiet=False):
    label, title, meta, text, is_draft = load(target)
    findings, st = C.check(title, meta, text, label)
    if not is_draft:
        findings = [(('ERROR' if r == 'unresolved-placeholder' else sev), r, d)
                    for sev, r, d in findings]
    err = [f for f in findings if f[0] == 'ERROR']
    warn = [f for f in findings if f[0] == 'WARN']
    bl, al = C.interlinks(text)

    floors = []
    if st['stdev'] < C.STDEV_FLOOR:
        floors.append('stdev %.2f' % st['stdev'])
    if st['short_pct'] < C.SHORT_FLOOR:
        floors.append('short %.1f%%' % st['short_pct'])
    if st['long_pct'] < C.LONG_FLOOR:
        floors.append('long %.1f%%' % st['long_pct'])

    if quiet:
        print('%-44s %2d err  %2d warn%s' % (label[-44:], len(err), len(warn),
                                             '  rhythm: ' + ', '.join(floors) if floors else ''))
        return len(err)

    print('=' * 78)
    print('%s' % label)
    print('  %s' % (title[:70] or '(no title)'))
    print('  title %d chars   meta %s   blog interlinks %d (min 5)'
          % (len(title), len(meta) if meta else 'MISSING', bl))
    print('  rhythm  stdev %.2f (%.1f+)   <=6w %.1f%% (%d+)   >25w %.1f%% (%d+)%s'
          % (st['stdev'], C.STDEV_FLOOR, st['short_pct'], C.SHORT_FLOOR,
             st['long_pct'], C.LONG_FLOOR, '   FLOOR MISS' if floors else ''))
    print('  sentences %d, over 25 words %d   paragraphs %d, over %dw %d'
          % (st['sentences'], st['over25'], st['paras'], C.PARA_WORD_CAP,
             st['over_para_cap']))
    print('  ERRORS %d   WARNINGS %d' % (len(err), len(warn)))
    counts = collections.Counter(r.split('(')[0] for _, r, _ in findings)
    for rule, n in counts.most_common(20):
        print('     %-34s %d' % (rule, n))
    for sev, rule, det in err:
        print('     ! %-28s %s' % (rule[:28], det[:86]))
    for sev, rule, det in warn:
        print('     ~ %-28s %s' % (rule[:28], det[:86]))
    print('  %s' % ('CLEAN' if not err else 'BLOCKED, %d error(s)' % len(err)))
    return len(err)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    quiet = '--quiet' in sys.argv
    targets = args or tree()
    if not targets:
        print('nothing to lint under %s' % ' or '.join(SCOPES))
        return 0
    bad = sum(1 for t in targets if report(t, quiet) > 0)
    print('\n%d file(s) checked, %d with errors.' % (len(targets), bad))
    return min(bad, 125)


if __name__ == '__main__':
    sys.exit(main())
