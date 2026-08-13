"""Pre-publish gate. Run against the FINAL copy as it sits in Webflow, or against
the live URL after publishing.

    python3 lint/publish-check.py https://www.salesforge.ai/blog/slug
    python3 lint/publish-check.py path/to/final.md

Exists because first-person-plural leaks enter during editing and CMS assembly,
not in the draft. Every published article checked so far had we/our/us in it while
the draft it came from had none. The draft-time hook cannot see that.
"""
import sys, os, re, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C
from extract import extract

def load(target):
    if target.startswith('http'):
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as fh:
            tmp = fh.name
        ua = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/120 Safari/537.36')
        subprocess.run(['curl', '-sS', '-A', ua, target, '-o', tmp], check=True)
        d = extract(tmp)
        os.unlink(tmp)
        return d['title'], d['meta'], d['text']
    text = open(target, encoding='utf-8').read()
    title = text.splitlines()[0].lstrip('# ').strip() if text.strip() else ''
    m = re.search(r'\*\*Meta:\*\*\s*(.+)', text)
    return title, (m.group(1).strip() if m else ''), text

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 1
    target = sys.argv[1]
    title, meta, text = load(target)
    findings, st = C.check(title, meta, text, target)
    # a [[FIGURE:]] marker is allowed in a draft and never in published copy
    findings = [(('ERROR' if f[1] == 'unresolved-placeholder' else f[0]), f[1], f[2])
                for f in findings]
    err = [f for f in findings if f[0] == 'ERROR']
    warn = [f for f in findings if f[0] == 'WARN']
    bl, al = C.interlinks(text)

    print('PUBLISH CHECK  %s' % target)
    print('  title %d chars   meta %s   blog interlinks %d (min 5)'
          % (len(title), len(meta) if meta else 'MISSING', bl))
    print('  sentences %d, over 25 words %d   paragraphs %d, over 3 sentences %d'
          % (st['sentences'], st['over25'], st['paras'], st['over3']))

    # the leak this file exists for
    fp = [f for f in err if f[1].startswith('first-person-plural')]
    print('\n  first-person-plural: %d %s'
          % (len(fp), 'CLEAN' if not fp else 'MUST FIX BEFORE PUBLISH'))
    for _, r, d in fp:
        print('     %-28s %s' % (r, d[:80]))

    other = [f for f in err if not f[1].startswith('first-person-plural')]
    print('\n  other errors: %d' % len(other))
    for _, r, d in other[:20]:
        print('     %-28s %s' % (r[:28], d[:80]))
    print('  warnings: %d' % len(warn))

    if err:
        print('\nDO NOT PUBLISH. %d error(s) open.' % len(err))
        return 1
    print('\nClear to publish.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
