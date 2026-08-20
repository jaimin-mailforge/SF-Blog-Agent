"""Must-cover coverage check against rules/forge-positioning-guidelines.md.

    python3 lint/coverage.py drafts/expandi-alternatives.md
    python3 lint/coverage.py drafts/x.md --section "Salesforge: LinkedIn"
    python3 lint/coverage.py --list

The guidelines say every must-cover feature in a featured product's section must
appear in the piece: "Not most. All." That is a counting job and I got it wrong by
hand twice on the Expandi draft, first hiding three must-covers inside one bullet
and then shipping 11 bullets against 12. Hence this file.

Reports three buckets and never pretends to certainty it does not have:

    COVERED     enough distinctive tokens matched
    UNCERTAIN   partial match, a human has to look
    MISSING     nothing matched

Exit code is the number of MISSING items, so it works in a conditional.
"""
import sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDE = os.path.join(ROOT, 'rules', 'forge-positioning-guidelines.md')

STOP = set('''a an the and or of to in on for with without at by from as is are be
that this those these it its their our your you we not no any all every each one two
into inside across per via plus over under more most than then so if when where which
who what how can could will would may might must let does do did has have had'''.split())

# Where the guidelines phrase a feature differently from how prose naturally says it.
# Keys are guideline feature names, values are extra token sets that also count.
ALIAS = {
    'mcp cli': {'mcp', 'cli'},
    'api': {'api'},
    'integrations': {'integrations', 'hubspot', 'salesforce'},
    'testing and analytics': {'test', 'testing', 'analytics'},
    'native linkedin actions': {'linkedin', 'actions'},
}


def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower())
            if w not in STOP and len(w) > 2}


def sections():
    """Return {section title: [(feature name, full bullet), ...]}."""
    text = open(GUIDE, encoding='utf-8').read()
    out, cur, collecting = {}, None, False
    for line in text.splitlines():
        h2 = re.match(r'^##\s+(?!#)(.+?)\s*$', line)
        h3 = re.match(r'^###\s+(.+?)\s*$', line)
        if h2:
            cur = h2.group(1).strip()
            out.setdefault(cur, [])
            collecting = False
            continue
        if h3:
            collecting = 'must-cover' in h3.group(1).lower() or 'must cover' in h3.group(1).lower()
            continue
        if collecting and cur and line.startswith('- '):
            body = line[2:].strip()
            name = body.split(':', 1)[0].strip() if ':' in body else body
            out[cur].append((name, body))
    return {k: v for k, v in out.items() if v}


def playbook_map():
    """article-type phrase -> guidelines section, from the quick reference table."""
    text = open(GUIDE, encoding='utf-8').read()
    block = text.split('## Playbook quick reference table', 1)
    if len(block) < 2:
        return {}
    out = {}
    for row in block[1].splitlines():
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        if len(cells) < 2 or cells[0].lower().startswith(('article type', '---')):
            continue
        atype, product = cells[0], cells[1]
        m = re.match(r'([A-Za-z ]+?)\s*\(([^)]+)\)', product)
        out[atype.lower()] = ('%s: %s' % (m.group(1).strip(), m.group(2).strip())
                              if m else product)
    return out


def guess_section(path, secs):
    """Pick the guidelines section from the draft filename and its H1."""
    name = os.path.basename(path).lower()
    head = ''
    try:
        head = open(path, encoding='utf-8').readline().lower()
    except OSError:
        pass
    hay = name + ' ' + head
    for atype, section in playbook_map().items():
        key = atype.split()[0]
        if 'linkedin' in atype and 'linkedin' in hay:
            return section
        if 'cold email' in atype and 'cold email' in hay:
            return section
        if 'lead finder' in atype and ('lead' in hay or 'finder' in hay):
            return section
        if 'infrastructure' in atype and 'infrastructure' in hay:
            return section
        if 'warmup' in atype and ('warmup' in hay or 'warm up' in hay):
            return section
    return None


def forge_block(text):
    """The Salesforge (or first Forge) product section of the draft, where the
    key-feature bullets that answer the checklist live."""
    m = re.search(r'^##\s+\d+[.)\-]\s*(Salesforge|Leadsforge|Mailforge|Infraforge|'
                  r'Primeforge|Warmforge)\b.*$', text, re.M)
    if not m:
        return text, 0
    rest = text[m.start():]
    nxt = re.search(r'^##\s+\d+[.)\-]\s', rest[10:], re.M)
    block = rest[:nxt.start() + 10] if nxt else rest
    bullets = len(re.findall(r'^-\s+\*\*', block, re.M))
    return block, bullets


def main():
    secs = sections()
    if '--list' in sys.argv:
        for k, v in sorted(secs.items()):
            print('%-38s %2d must-covers' % (k, len(v)))
        return 0

    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 1
    path = args[0]
    text = open(path, encoding='utf-8').read()

    want = None
    if '--section' in sys.argv:
        want = sys.argv[sys.argv.index('--section') + 1]
    else:
        want = guess_section(path, secs)
    if not want or want not in secs:
        print('Could not resolve a guidelines section for %s.' % path)
        print('Pass one explicitly. Available:')
        for k, v in sorted(secs.items()):
            print('   --section "%s"   (%d must-covers)' % (k, len(v)))
        return 1

    block, bullets = forge_block(text)
    want_list = secs[want]
    hay_all = tokens(text)
    hay_block = tokens(block)

    # Scope matters as much as presence. A must-cover whose tokens appear only in a
    # comparison-table row or in a competitor's section is not covered in any useful
    # sense, and that is precisely how three of them got hidden inside one bullet on
    # the first pass of the Expandi draft.
    in_section, elsewhere, uncertain, missing = [], [], [], []
    for name, body in want_list:
        need = tokens(name) or tokens(body)
        extra = ALIAS.get(name.lower(), set())
        blk = len(need & hay_block) / max(1, len(need))
        doc = len(need & hay_all) / max(1, len(need))
        if (bool(extra) and extra <= hay_block) or blk >= 0.6:
            in_section.append(name)
        elif doc >= 0.6 or (bool(extra) and extra <= hay_all):
            elsewhere.append(name)
        elif max(blk, doc) >= 0.3:
            uncertain.append((name, round(max(blk, doc), 2)))
        else:
            missing.append(name)

    print('COVERAGE  %s' % os.path.relpath(os.path.abspath(path), ROOT))
    print('  guidelines section : %s' % want)
    print('  must-covers        : %d' % len(want_list))
    print('  key-feature bullets in the Forge section : %d%s'
          % (bullets, '' if bullets == len(want_list)
             else '   <-- COUNT MISMATCH, guidelines want one bullet per must-cover'))
    print('  in the product section %d   elsewhere only %d   uncertain %d   missing %d'
          % (len(in_section), len(elsewhere), len(uncertain), len(missing)))
    if missing:
        print('\n  MISSING from the whole piece. Every one of these has to appear:')
        for n in missing:
            print('     - %s' % n)
    if elsewhere:
        print('\n  ELSEWHERE ONLY. Matched on the page but not in the Forge product')
        print('  section, so check it is a real feature bullet and not a table row:')
        for n in elsewhere:
            print('     ? %s' % n)
    if uncertain:
        print('\n  UNCERTAIN, partial match, read these yourself:')
        for n, s in uncertain:
            print('     ~ %-52s %.0f%% of tokens' % (n, s * 100))
    if not (missing or elsewhere or uncertain) and bullets == len(want_list):
        print('\n  All must-covers present in the product section, counts match.')
    return len(missing) + len(elsewhere)


if __name__ == '__main__':
    sys.exit(main())
