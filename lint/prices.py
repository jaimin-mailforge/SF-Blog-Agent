"""Re-verify every price a research brief claims, against the vendor's live page.

    python3 lint/prices.py research/expandi-alternatives.md
    python3 lint/prices.py --url https://expandi.io/pricing
    python3 lint/prices.py research/x.md --stale 30

This exists because the price step is the one most likely to get skipped and the
most expensive when it is wrong, and because two specific things went wrong on the
Expandi article:

  Waalaxy served EUR at 19/49/69 on seven different URL forms while the brief
  carried USD at 16/32/55 from a screenshot. No dollar sign appeared anywhere in
  1.4 MB of served HTML.

  lemlist's 100,000-email tier read $80 on the pricing page and $71 in the help
  centre, and the two were never reconciled.

So this tool deliberately does NOT pick a number. It reports what the page serves,
which currency it serves it in, and whether the figures the brief claims still
appear. A disagreement is handed to a human, because a bot cannot settle a vendor
contradiction and should not pretend to.

Exit code is the number of vendors needing a human look.
"""
import sys, os, re, subprocess, tempfile, datetime, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120 Safari/537.36')
TODAY = datetime.date.today()

# "**Pricing**, expandi.io/pricing, read 2026-08-13. Business **$99 ... $79 ...**"
# The read date is optional on purpose. Requiring it made this tool skip Waalaxy,
# whose line is "**Pricing**, waalaxy.com/pricing." with no date, and Waalaxy is the
# single least-verified price in the whole brief. A verifier that silently ignores its
# hardest case is worse than no verifier, so an undated source is picked up and flagged.
PROV = re.compile(
    r'\*\*Pricing\*\*[^,\n]*,\s*([a-z0-9.\-]+\.[a-z]{2,}[^\s,.]*)'
    r'(?:[^\n]{0,40}?read\s*(\d{4}-\d{2}-\d{2}))?',
    re.I)
# "## Evidence: Waalaxy" -> a vendor the brief covers
EVIDENCE = re.compile(r'^##\s+Evidence:\s*(.+?)\s*$', re.M)
MONEY = re.compile(r'[$\u20ac\u00a3]\s?\d[\d,]*(?:\.\d{1,2})?(?<![,.])')
CURRENCY = {'$': 'USD', '€': 'EUR', '£': 'GBP'}


def fetch(url):
    if not url.startswith('http'):
        url = 'https://' + url
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as fh:
        tmp = fh.name
    r = subprocess.run(['curl', '-sSL', '-A', UA, '-w', '%{http_code}',
                        '-o', tmp, url], capture_output=True, text=True)
    code = (r.stdout or '').strip()[-3:]
    body = open(tmp, encoding='utf-8', errors='replace').read()
    os.unlink(tmp)
    return url, code, body


def probe(url):
    url, code, body = fetch(url)
    text = re.sub(r'(?is)<(script|style)\b.*?</\1>', ' ', body)
    text = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', text))
    served = sorted({CURRENCY[c] for c in CURRENCY if c in text})
    figures = MONEY.findall(text)
    seen, uniq = set(), []
    for f in figures:
        k = f.replace(' ', '')
        if k not in seen:
            seen.add(k)
            uniq.append(k)
    toggle = bool(re.search(r'\b(annual|yearly|monthly|per month|per year|/mo|/yr)\b',
                            text, re.I))
    return {'url': url, 'code': code, 'bytes': len(body), 'currencies': served,
            'figures': uniq, 'has_toggle': toggle, 'text': text}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    stale_days = 14
    if '--stale' in sys.argv:
        stale_days = int(sys.argv[sys.argv.index('--stale') + 1])

    if '--url' in sys.argv:
        target = sys.argv[sys.argv.index('--url') + 1]
        p = probe(target)
        print('PROBE  %s' % p['url'])
        print('  http %s   %d bytes   currencies served: %s   billing words: %s'
              % (p['code'], p['bytes'], ', '.join(p['currencies']) or 'NONE FOUND',
                 'yes' if p['has_toggle'] else 'no'))
        print('  figures on the page: %s' % (', '.join(p['figures'][:30]) or 'none'))
        if len(p['currencies']) > 1:
            print('  MORE THAN ONE CURRENCY SERVED. Record which one you read.')
        if not p['figures']:
            print('  No figures found. The page may be JS-rendered, so read it in a')
            print('  browser and record a screenshot rather than trusting this.')
        return 0

    if not args:
        print(__doc__)
        return 1
    brief = args[0]
    text = open(brief, encoding='utf-8').read()
    rows = PROV.findall(text)
    if not rows:
        print('No pricing provenance lines found in %s.' % brief)
        print('Expected the brief format: **Pricing**, vendor.com/pricing, read YYYY-MM-DD.')
        return 1

    print('PRICE VERIFY  %s' % os.path.relpath(os.path.abspath(brief), ROOT))
    print('  %d recorded source(s), stale threshold %d days\n' % (len(rows), stale_days))
    needs_human = 0

    for url, read_on in rows:
        try:
            age = (TODAY - datetime.date.fromisoformat(read_on)).days
        except ValueError:
            age = None
        p = probe(url)
        # every money figure the brief states in the sentences around this source
        window = text[max(0, text.find(url) - 200):text.find(url) + 900]
        claimed = sorted({m.replace(' ', '') for m in MONEY.findall(window)})
        still_there = [c for c in claimed if c.replace('$', '').replace(',', '')
                       in p['text'].replace(',', '')]
        gone = [c for c in claimed if c not in still_there]

        flags = []
        if p['code'] != '200':
            flags.append('http %s' % p['code'])
        if not read_on:
            flags.append('no read date recorded, so staleness is unknowable')
        elif age is not None and age > stale_days:
            flags.append('read %d days ago' % age)
        if len(p['currencies']) > 1:
            flags.append('serves %s' % '/'.join(p['currencies']))
        if claimed and 'USD' not in p['currencies'] and any('$' in c for c in claimed):
            flags.append('brief says USD, page serves %s'
                         % ('/'.join(p['currencies']) or 'no currency symbol'))
        # A claimed figure missing from the served HTML is only strong evidence when
        # the page has no billing toggle and no currency switcher. Otherwise curl is
        # simply looking at the wrong tab, and flagging it trains people to ignore
        # this tool, which puts us back to unverified prices.
        weak = p['has_toggle'] or len(p['currencies']) > 1
        if gone and not weak:
            flags.append('%d claimed figure(s) not on the page' % len(gone))
        if not p['figures']:
            flags.append('no figures found, likely JS-rendered')

        status = 'LOOK' if flags else 'ok'
        if flags:
            needs_human += 1
        print('  [%s] %s' % (status, p['url']))
        print('        read %s%s, http %s, serves %s'
              % (read_on or 'DATE NOT RECORDED',
                 '' if age is None else ' (%d days ago)' % age,
                 p['code'], ', '.join(p['currencies']) or 'no currency symbol'))
        if claimed:
            print('        brief claims: %s' % ', '.join(claimed))
            if gone:
                print('        not in the served HTML: %s' % ', '.join(gone[:8]))
                if p['has_toggle'] or len(p['currencies']) > 1:
                    print('        (weak signal: the page has a billing toggle or a')
                    print('        currency switcher, so curl sees only one tab)')
        if flags:
            for f in flags:
                print('        ! %s' % f)
        print()

    # Only treat an Evidence section as a vendor if its title names a known product.
    # "Evidence: access limits that shape the article" is a real section and not a
    # vendor, and flagging it as an unsourced price is noise.
    known = set()
    names = os.path.join(ROOT, 'lint', 'data', 'product-names.txt')
    if os.path.exists(names):
        known = {l.strip().lower() for l in open(names, encoding='utf-8') if l.strip()}
    vendors = [v for v in EVIDENCE.findall(text)
               if v.strip().lower() in known
               or any(v.strip().lower() == k.split('.')[0] for k in known)]
    hosts = ' '.join(u for u, _ in rows).lower()
    unsourced = [v for v in vendors
                 if not any(tok in hosts for tok in
                            re.findall(r'[a-z]{4,}', v.lower()))]
    if unsourced:
        print('  Evidence sections with no **Pricing**, vendor.com line at all:')
        for v in unsourced:
            print('     ! %s' % v)
        print('  Either the price is unverified or the provenance was never written')
        print('  down. Both are blockers.\n')
        needs_human += len(unsourced)

    print('%d source(s) need a human look.' % needs_human)
    if needs_human:
        print('Do not resolve a disagreement by picking. Read the page in a browser,')
        print('screenshot it, and record the URL, the date and the currency you saw.')
    return needs_human


if __name__ == '__main__':
    sys.exit(main())
