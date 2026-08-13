"""Editorial linter. Masks non-prose, then checks each rule tagged [LINT] in rules/writing.md."""
import re, sys, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
def load(n):
    p = os.path.join(HERE, 'data', n)
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]

BANNED_WORDS = load('banned-words.txt')
PRODUCT_NAMES = load('product-names.txt')
BANNED_PHRASES = load('banned-phrases.txt')
FIG_VERBS = load('figurative-verbs.txt')
def _fact(line):
    """`needle|why`, or `re:pattern|label|why` when the rule needs a regex.
    A regex rule carries its own label because the pattern itself reads badly in a
    finding. Neither the pattern nor the label nor the reason may contain a pipe."""
    p = [f.strip() for f in line.split('|')]
    if p[0].startswith('re:') and len(p) == 3: return (p[0], p[1], p[2])
    return (p[0], p[0], p[1])

FACTS = [_fact(l) for l in load('fact-conflicts.txt')]
LOWERCASE_BRANDS = load('lowercase-brands.txt')
SPELLINGS = [tuple(f.strip() for f in l.split('|', 1)) for l in load('spellings.txt')]

def _protected_spans(text):
    """Character ranges covered by a product name. Banned-word hits inside these are exempt."""
    spans = []
    for name in PRODUCT_NAMES:
        for m in re.finditer(re.escape(name), text, re.I):
            spans.append((m.start(), m.end()))
    return spans

def _in_spans(i, spans):
    return any(a <= i < b for a, b in spans)

def _mask_paired_quotes(t, minlen=25):
    """Mask review quotes by pairing quote marks in order, so a sentence-final
    quoted word cannot swallow the text up to the next real quote."""
    pos = [m.start() for m in re.finditer(r'"', t)]
    out = list(t)
    for a, b in zip(pos[0::2], pos[1::2]):
        if b - a - 1 >= minlen:
            for i in range(a, b + 1):
                if out[i] != '\n': out[i] = ' '
    return ''.join(out)

def word_pattern(w):
    """Match a banned word with either a hyphen or a space between its parts."""
    parts = re.split(r'[-\s]', w)
    return r'\b' + r'[-\s]'.join(re.escape(p) for p in parts) + r'\b'

# ---------- masking: rules apply to body prose, not to these ----------
def mask(text):
    """Blank out regions where the rules do not apply, preserving offsets."""
    def blank(m): return ' ' * len(m.group(0))
    t = text
    t = re.sub(r'```.*?```', blank, t, flags=re.S)      # code fences
    t = re.sub(r'`[^`\n]*`', blank, t)                   # inline code
    t = re.sub(r'^\s*>.*$', blank, t, flags=re.M)        # blockquotes (verbatim quotes)
    t = _mask_paired_quotes(t)                           # review quotes, properly paired
    t = re.sub(r'^\s*\|.*$', blank, t, flags=re.M)       # markdown tables
    t = re.sub(r'^.*(?:\s\|\s).*(?:\s\|\s).*$', blank, t, flags=re.M)   # extracted table rows
    t = re.sub(r'^.*\s{6,}.*$', blank, t, flags=re.M)     # padded table remnants
    t = re.sub(r'\]\([^)\s]*\)', blank, t)               # link targets
    t = re.sub(r'https?://\S+', blank, t)                # bare urls
    t = re.sub(r'(?is)<style\b.*?</style>', blank, t)     # css blocks in the comparison table
    t = re.sub(r'<[^>]+>', blank, t)                     # html tag markup, cell text survives
    return t

# A sentence can also open with a markdown link, a quote, a price, a digit, or a
# lowercase-branded competitor. Missing those glued two sentences into one and hid
# real over-25-word findings.
_SENT_START = ('(?=[A-Z(\\[“"$0-9]'
               + ''.join('|' + re.escape(b) + r'\b' for b in LOWERCASE_BRANDS) + ')')

def sentences(prose_lines):
    out = []
    for l in prose_lines:
        l = re.sub(r'^\s*[-*]\s*', '', l)
        # a bolded label followed by a colon is a label, not part of the sentence.
        # TL;DR entries and key-feature bullets are required to carry one, and
        # counting it would charge the same words twice against the 25-word ceiling.
        l = re.sub(r'^\*\*(.+?)(?:\*\*\s*:|\s*:\*\*)\s*', '', l)
        l = l.replace('**', '')
        l = re.sub(r'\b([A-Z])\.', r'\1', l)              # initials
        for s in re.split(r'(?<=[.!?])\s+' + _SENT_START, l):
            s = s.strip()
            if len(s.split()) > 2: out.append(s)
    return out

def _sections(text, head_re):
    """Bodies of every section whose heading matches, each stopping at the next heading."""
    out = []
    for m in re.finditer(head_re, text, re.I | re.M):
        rest = text[m.end():]
        nxt = re.search(r'^#{1,6}\s', rest, re.M)
        out.append(rest[:nxt.start()] if nxt else rest)
    return out

# A tool name followed by a colon, then "Best for". Accepts the colon inside or
# outside the bold, since both render the same.
_TLDR_SHAPE = re.compile(r'^-\s+\*\*.+?(?:\*\*\s*:|\s*:\*\*)\s*Best for\b')
_FEATURE_SHAPE = re.compile(r'^-\s+\*\*.+?(?:\*\*\s*:|\s*:\*\*)')
_G2_SHAPE = re.compile(r'G2 puts .+ at [\d.]+ from [\d,]+ reviews', re.I)


def structure(text, add):
    """Rules about the shape of a section rather than the words in it."""
    # per-tool disqualifier lines. Removed from the guidelines 2026-08-13 by Jaimin
    for m in re.finditer(r'\*\*Not for:?\*\*', text, re.I):
        add('ERROR', 'not-for-line', ctx(text, m.start()))

    # TL;DR entries read "Tool: Best for ..."
    for sec in _sections(text, r'^#{2,3}\s*TL;DR.*$'):
        for line in sec.splitlines():
            if line.lstrip().startswith('- ') and not _TLDR_SHAPE.match(line.strip()):
                add('ERROR', 'tldr-shape', line.strip()[:88])

    # key feature bullets carry a colon after the feature name
    for sec in _sections(text, r'^#{3,4}\s*Key features.*$'):
        for line in sec.splitlines():
            s = line.strip()
            if s.startswith('- **') and not _FEATURE_SHAPE.match(s):
                add('ERROR', 'feature-bullet-colon', s[:88])

    # the ratings line is one sentence and nothing else. Screenshots go in by hand
    for sec in _sections(text, r'^#{3,4}\s*(?:What real users say|G2 [Rr]ating).*$'):
        live = [l.strip() for l in sec.splitlines() if l.strip()]
        if len(live) > 1:
            add('ERROR', 'ratings-section-long(%d lines)' % len(live), live[0][:88])
        elif live and not _G2_SHAPE.search(live[0]):
            add('WARN', 'ratings-line-shape', live[0][:88])

    # "why people leave X" subsections stay short
    for head in re.finditer(r'^##\s*Why [Pp]eople (?:[Ll]eave|[Ll]ook).*$', text, re.M):
        rest = text[head.end():]
        nxt = re.search(r'^##\s', rest, re.M)
        block = rest[:nxt.start()] if nxt else rest
        for sub in _sections(block, r'^###\s.*$'):
            paras = [p for p in re.split(r'\n\s*\n', sub) if p.strip()]
            if len(paras) > 2:
                add('WARN', 'why-leave-subsection(%d paras)' % len(paras),
                    paras[0].strip()[:88])


def check(title, meta, text, label):
    body = mask(text)
    lines = body.splitlines()
    prose = [l for l in lines if l.strip() and not l.lstrip().startswith(('#', '|'))]
    findings = []
    def add(sev, rule, detail): findings.append((sev, rule, detail))

    structure(text, add)

    # words and phrases
    prot = _protected_spans(body)
    for w in BANNED_WORDS:
        for m in re.finditer(word_pattern(w), body, re.I):
            if _in_spans(m.start(), prot): continue
            add('ERROR', 'banned-word:' + w, ctx(body, m.start()))
    for p in BANNED_PHRASES:
        for m in re.finditer(re.escape(p), body, re.I):
            add('ERROR', 'banned-phrase:' + p, ctx(body, m.start()))

    # first person plural. 'us' case-sensitive lowercase only, to spare "US"
    for m in re.finditer(r'\b(?:we|We|our|Our)\b|(?<![A-Z])\bus\b(?![A-Z])', body):
        w = m.group(0)
        if w.lower() == 'us' and re.search(r'\b(US|U\.S\.)\b', body[max(0, m.start()-3):m.start()+3]): continue
        add('ERROR', 'first-person-plural:' + w, ctx(body, m.start()))

    # figurative verbs where the subject looks like a product
    for v in FIG_VERBS:
        for m in re.finditer(r'\b(?:The|the|It|it)\s+\w*\s?\b' + v + r'\b', body):
            add('WARN', 'figurative-verb:' + v, ctx(body, m.start()))

    # punctuation
    for m in re.finditer(r';', body):
        if 'TL;DR' in ctx(body, m.start(), 8): continue
        add('ERROR', 'semicolon', ctx(body, m.start()))
    for m in re.finditer(r'!', body):
        add('WARN', 'exclamation', ctx(body, m.start()))

    # sentence + paragraph shape
    ss = sentences(prose)
    over = [s for s in ss if len(s.split()) > 25]
    for s in over[:40]:
        add('WARN', 'sentence>25w(%dw)' % len(s.split()), s[:100])
    paras = [p for p in re.split(r'\n\s*\n', body)
             if p.strip() and not p.lstrip().startswith(('#', '-', '*', '|'))]
    pcounts = [len(sentences([p])) for p in paras]
    for p, c in zip(paras, pcounts):
        if c > 3: add('WARN', 'paragraph>3sent(%d)' % c, p.strip()[:100])

    # seo
    if title and len(title) > 55: add('WARN', 'title>55(%d)' % len(title), title)
    if meta and len(meta) > 155: add('WARN', 'meta>155(%d)' % len(meta), meta[:80])
    if not meta: add('WARN', 'meta-missing', 'no meta description on page')

    # facts. a needle prefixed `re:` is a regex, so a rule can require a wrong
    # figure near a phrase instead of banning the phrase outright.
    for needle, label, why in FACTS:
        pat = needle[3:] if needle.startswith('re:') else re.escape(needle)
        n = len(re.findall(pat, text, re.I))
        if n: add('ERROR', 'fact:' + label, '%dx  %s' % (n, why))

    # case-sensitive spellings. the fact and banned-phrase checks are both case-
    # insensitive, so neither can tell Co-pilot from Co-Pilot. this one can.
    for wrong, fix in SPELLINGS:
        for m in re.finditer(r'(?<![\w-])' + re.escape(wrong) + r'(?![\w-])', text):
            add('ERROR', 'spelling:' + wrong, 'write ' + fix + '  ' + ctx(text, m.start()))

    # lowercase-branded competitor names, capitalised only to open a heading or sentence
    for brand in LOWERCASE_BRANDS:
        cap = brand[0].upper() + brand[1:]
        for m in re.finditer(r'\b' + re.escape(cap) + r'\b', text):
            before = text[:m.start()]
            # opens a heading, a line, a list item, a table cell, or a new sentence.
            # the HTML clause covers the comparison table, where the name opens a
            # <th> or <td> and there is no markdown pipe to recognise it by.
            opens = (not before.strip()
                     or re.search(r'(?:^|\n)[#>|\s*_\-\d.)]*$', before) is not None
                     or re.search(r'<[^<>]*>\s*$', before) is not None
                     or re.search(r'[.?!:]["\')\]]?\s+$', before) is not None)
            if not opens:
                add('ERROR', 'brand-casing:' + brand,
                    'write "%s" mid-sentence. %s' % (brand, ctx(text, m.start())))

    # placeholders. WARN here so a marker can live in a draft, which is the whole
    # point of it. publish-check.py escalates it to blocking.
    for m in re.finditer(r'\[\[FIGURE:', text):
        add('WARN', 'unresolved-placeholder', ctx(text, m.start()))

    return findings, {'sentences': len(ss), 'over25': len(over),
                      'paras': len(paras), 'over3': sum(1 for c in pcounts if c > 3),
                      'avg_para': round(sum(pcounts)/max(1, len(pcounts)), 1),
                      'chars': len(text)}

def ctx(t, i, w=42):
    return ('...' + t[max(0, i-w):i+w].replace('\n', ' ').strip() + '...')

def interlinks(text):
    urls = re.findall(r'\]\((https?://[^)\s]+)\)', text)
    return sum(1 for u in urls if '/blog/' in u), len(urls)

def opening_frames(text):
    """Repetition across per-tool section openers. Returns (pattern, hits, total)."""
    bf = re.findall(r'\*\*Best (?:For|for):\*\*\s*(\S+\s+\S+\s+\S+)', text)
    if len(bf) < 3: return None
    heads = {}
    for b in bf:
        key = ' '.join(b.split()[1:3]).lower()
        heads[key] = heads.get(key, 0) + 1
    top = max(heads.items(), key=lambda kv: kv[1])
    return top[0], top[1], len(bf)
