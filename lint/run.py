import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C
from extract import extract

ARTS = []
# benchmark markdown
md = open('/tmp/bench.md', encoding='utf-8').read()
ARTS.append(('cold-email-software (md)',
             md.splitlines()[0].lstrip('# ').strip(),
             re.search(r'\*\*Meta:\*\*\s*(.+)', md).group(1).strip(), md))
for slug in ('gohighlevel-review', 'email-sequence-software', 'linkedin-ai-tools'):
    d = extract('/tmp/%s.html' % slug)
    ARTS.append((slug, d['title'], d['meta'], d['text']))

summary = []
for label, title, meta, text in ARTS:
    f, st = C.check(title, meta, text, label)
    err = [x for x in f if x[0] == 'ERROR']; warn = [x for x in f if x[0] == 'WARN']
    bl, al = C.interlinks(text)
    of = C.opening_frames(text)
    print('=' * 78)
    print('%s' % label.upper())
    print('  %s' % title[:70])
    print('  chars %-6d sentences %-4d over-25w %-3d paras %-4d over-3-sent %-3d avg-para %s'
          % (st['chars'], st['sentences'], st['over25'], st['paras'], st['over3'], st['avg_para']))
    print('  blog interlinks %-3d (min 5)   all links %-3d   title %d   meta %s'
          % (bl, al, len(title), len(meta) if meta else 'MISSING'))
    if of: print('  per-tool opener "%s": %d of %d sections' % (of[0], of[1], of[2]))
    print('  ERRORS %d   WARNINGS %d' % (len(err), len(warn)))
    counts = collections.Counter(r.split('(')[0] for _, r, _ in f)
    for rule, n in counts.most_common(14):
        print('     %-34s %d' % (rule, n))
    for sev, rule, det in err[:12]:
        print('     ! %-26s %s' % (rule[:26], det[:88]))
    summary.append((label, len(err), len(warn), bl, st['over25'], st['over3']))

print('=' * 78)
print('%-26s %6s %6s %6s %8s %8s' % ('ARTICLE', 'ERR', 'WARN', 'ILINK', '>25w', '>3sent'))
for s in summary:
    print('%-26s %6d %6d %6d %8d %8d' % s)
