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

# Subjects that can be given a figurative body: pronouns, relative pronouns, and every
# product name. Longest-first so "Snov.io" wins over a shorter prefix.
_FIG_SUBJ = r'\b(?:The|the|It|it|This|this|That|that|Which|which|Who|who|' + '|'.join(
    re.escape(n) for n in sorted(PRODUCT_NAMES, key=len, reverse=True)) + r')'

# Thresholds for the four style checks added 2026-08-13. All WARN: they are judgment
# calls on prose, and the repo convention is that warnings report and do not block.
NEGATION_CAP = 10        # "rather than" alone
NEGATION_TOTAL_CAP = 15  # plus "instead of" and bare ", not"
SCOPED_CAP = 12          # "here" / "of the nine" / "on this list" as comparison anchors
SUPERLATIVE_ENTRY_CAP = 3  # tool sections allowed to open on a superlative

# Rhythm, calibrated 2026-08-19 against the editor-approved RocketReach article
# (stdev 8.55, 28.0% at <=6 words, 10.3% over 25) and our flat Expandi draft
# (5.82, 13.9%, 0.0%). Floors matter as much as the ceiling.
HARD_SENTENCE_CAP = 45   # ERROR. nothing in a body paragraph needs 45 words
STDEV_FLOOR = 7.0        # spread of sentence length
SHORT_FLOOR = 18.0       # min share of sentences at six words or fewer
LONG_FLOOR = 5.0         # min share over 25 words
PARA_WORD_CAP = 60       # replaces the 3-sentence cap

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

def punct_text(text):
    """Text for the punctuation checks. Unlike mask(), this KEEPS table cells, because
    section 14 says section 4 applies inside the table. It drops only the places a
    semicolon or a dash is legitimate: css blocks, code, link targets and bare urls."""
    def blank(m): return ' ' * len(m.group(0))
    t = re.sub(r'(?is)<style\b.*?</style>', blank, text)
    t = re.sub(r'```.*?```', blank, t, flags=re.S)
    t = re.sub(r'`[^`\n]*`', blank, t)
    t = re.sub(r'\]\([^)\s]*\)', blank, t)
    t = re.sub(r'https?://\S+', blank, t)
    return t

# A sentence can also open with a markdown link, a quote, a price, a digit, or a
# lowercase-branded competitor. Missing those glued two sentences into one and hid
# real over-25-word findings.
_SENT_START = ('(?=[A-Z(\\[“"$0-9]'
               + ''.join('|' + re.escape(b) + r'\b' for b in LOWERCASE_BRANDS) + ')')

def sentences(prose_lines, min_words=3):
    """min_words drops fragments that are not sentences. It defaults to 3 because the
    25-word check does not want table debris or a bare label counted as prose.
    Paragraph-shape counting passes min_words=1: a two-word sentence like "Two caveats."
    is a real sentence, and dropping it undercounted a four-sentence paragraph as three."""
    out = []
    for l in prose_lines:
        # Strip a list marker, but never the first * of a bold **label**. The old
        # `[-*]` ate it, which defeated the label pattern below, so every
        # **Best for:** line at paragraph start was measured with its label counted.
        l = re.sub(r'^\s*(?:-|\*(?!\*)|\d+\.)\s+', '', l)
        # a bolded label followed by a colon is a label, not part of the sentence.
        # TL;DR entries and key-feature bullets are required to carry one, and
        # counting it would charge the same words twice against the 25-word ceiling.
        l = re.sub(r'^\*\*(.+?)(?:\*\*\s*:|\s*:\*\*)\s*', '', l)
        l = l.replace('**', '')
        # No initials rule. It used to strip the period from `\b[A-Z]\.` so that
        # "Frank S. Sondors" stayed one sentence, but it also ate the period in
        # "LinkedIn, email and X. Every other tool" and glued two sentences into a
        # false long one. Across every draft and article in the repo, that pattern
        # matched only the bug and never a real initial, and the byline is fixed as
        # "Frank Sondors" with no middle initial, so there is nothing to protect.
        # If an initial ever does appear, it splits into a fragment under three
        # words, which the filter below drops. That under-reports rather than
        # inventing an error, which is the safer direction to fail in.
        for s in re.split(r'(?<=[.!?])\s+' + _SENT_START, l):
            s = s.strip()
            if len(s.split()) >= min_words: out.append(s)
    return out

def _tool_sections(text):
    """(name, body) for every numbered tool H2, each stopping at the next H2."""
    out = []
    for m in re.finditer(r'^##\s+\d+\s*[.)\-–]\s*(.+?)\s*(?:\{#[^}]*\})?\s*$', text, re.M):
        rest = text[m.end():]
        nxt = re.search(r'^##\s', rest, re.M)
        out.append((m.group(1).strip(), rest[:nxt.start()] if nxt else rest))
    return out

def _proscons(sec):
    """(pros, cons) cell counts from a section's Pros/Cons table only.

    Two bugs fixed 2026-08-13. It scanned every two-column table in the section, so a
    per-volume pricing table inflated the count. And it dropped rows whose pros cell was
    empty, which made an asymmetric table invisible whenever cons was the longer column,
    the exact shape the rule wants writers to reach for."""
    m = re.search(r'###\s+Pros and cons\s*\n(.*?)(?=\n###|\Z)', sec, re.S)
    if not m: return 0, 0
    rows = re.findall(r'^\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$', m.group(1), re.M)
    rows = [r for r in rows if r[0].strip() != 'Pros' and '---' not in r[0]]
    return sum(1 for r in rows if r[0].strip()), sum(1 for r in rows if r[1].strip())

def _entry_sentence(sec):
    """First sentence of the paragraph after the mandated explainer, which is the entry
    angle section 21 requires to vary. Skips the Best for and G2 Rating lines."""
    paras = [p.strip() for p in re.split(r'\n\s*\n', sec)
             if p.strip() and not p.lstrip().startswith(('#', '-', '*', '|', '<'))
             and not p.lstrip().startswith('**Best for')
             and not p.lstrip().startswith('**G2 Rating')
             and not p.lstrip().startswith('**Not for')]
    if len(paras) < 2: return ''
    return re.split(r'(?<=[.!?])\s+', paras[1])[0]

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
    # Figurative verbs, meaning a product or feature given a body. The subject list has to
    # include product names and relative pronouns, not just the/it: the commonest form of
    # this is a named product as the actor ("Waalaxy sits at 0.5%") or a relative clause
    # inside the mandated explainer sentence ("a tool that puts email steps inside"), and
    # both walked straight through the old the/it-only pattern.
    # "G2 puts X at 4.6" is the wording section 9b mandates, and G2 is deliberately not a
    # subject here, so it does not match and needs no exemption.
    for v in FIG_VERBS:
        for m in re.finditer(_FIG_SUBJ + r"(?:'s|’s)?\s+(?:\w+\s+){0,2}?\b" + v + r'\b', body):
            add('WARN', 'figurative-verb:' + v, ctx(body, m.start()))

    # punctuation
    # Punctuation runs on cell-inclusive text. mask() blanks table rows, so six of the
    # seven semicolons in the approved RocketReach article were invisible to this check
    # while section 14 explicitly extends section 4 into cells.
    ptext = punct_text(text)
    for m in re.finditer(r';', ptext):
        if 'TL;DR' in ctx(ptext, m.start(), 8): continue
        add('ERROR', 'semicolon', ctx(ptext, m.start()))
    # Section 4 bans em and en dashes and was tagged [LINT] with no implementation at all.
    for ch, label in (('\u2014', 'em-dash'), ('\u2013', 'en-dash')):
        for m in re.finditer(ch, ptext):
            add('ERROR', label, ctx(ptext, m.start()))
    for m in re.finditer(r'!', body):
        add('WARN', 'exclamation', ctx(body, m.start()))

    # sentence + paragraph shape
    ss = sentences(prose)
    L = [len(s.split()) for s in ss]

    # Hard stop only. The old rule warned on every sentence over 25 words, and clearing
    # those warnings is what flattened the Expandi draft: measured against the
    # editor-approved RocketReach article, both sit at a 13-word mean, but the approved
    # article has stdev 8.55 against our 5.82, 28% of sentences at six words or fewer
    # against our 14%, and 10.3% over 25 words against our 0%. A ceiling with no floor
    # makes writers converge on the middle, which is the one thing section 3 asks them
    # not to do. So the ceiling is a soft target in prose and the linter checks spread.
    for s in ss:
        if len(s.split()) >= HARD_SENTENCE_CAP:
            add('ERROR', 'sentence>=%dw(%dw)' % (HARD_SENTENCE_CAP, len(s.split())), s[:100])
    if len(L) >= 80:
        import statistics as _st
        sd = _st.pstdev(L)
        short = 100.0 * sum(1 for x in L if x <= 6) / len(L)
        long_ = 100.0 * sum(1 for x in L if x > 25) / len(L)
        if sd < STDEV_FLOOR:
            add('WARN', 'rhythm-flat(stdev %.1f)' % sd,
                'needs %.1f+. same mean, less spread. add very short and very long sentences' % STDEV_FLOOR)
        if short < SHORT_FLOOR:
            add('WARN', 'too-few-short(%.0f%%)' % short,
                'needs %.0f%%+ of sentences at six words or fewer' % SHORT_FLOOR)
        if long_ < LONG_FLOOR:
            add('WARN', 'too-few-long(%.0f%%)' % long_,
                'needs %.0f%%+ over 25 words. a coordinate series may run long' % LONG_FLOOR)
    paras = [p for p in re.split(r'\n\s*\n', body)
             if p.strip() and not p.lstrip().startswith(('#', '-', '*', '|'))]
    # Cap words, not sentences. Section 3's stated purpose is the five-second skim test,
    # which is word density. The sentence cap inverted it: a 74-word three-sentence
    # paragraph passed while a 28-word four-sentence pricing paragraph failed, and it
    # capped the approved article's best tonal paragraph, which runs six short sentences.
    for p in paras:
        w = len(p.split())
        if w > PARA_WORD_CAP:
            add('WARN', 'paragraph>%dw(%dw)' % (PARA_WORD_CAP, w), p.strip()[:100])

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
    # Forge-scoped. The Primebox mode spellings must not fire on a competitor's real
    # product name: ZoomInfo ships "Copilot AI", and section 20 says competitors are
    # spelled the way they spell themselves. Unscoped, this rule produced 9 of the 26
    # errors on the approved RocketReach article, all of them false positives.
    _FORGE = re.compile(r'\b(?:Salesforge|Primebox|Agent Frank|Warmforge|Leadsforge|'
                        r'Mailforge|Infraforge|Primeforge|Forge)\b')
    for wrong, fix in SPELLINGS:
        for m in re.finditer(r'(?<![\w-])' + re.escape(wrong) + r'(?![\w-])', text):
            # Scope to the containing sentence, not a character window: a Forge mention
            # in an adjacent paragraph must not license a hit on a competitor's product.
            lo = max((text.rfind(c, 0, m.start()) for c in '.!?\n'), default=-1) + 1
            hi = min((x for x in (text.find(c, m.end()) for c in '.!?\n') if x != -1),
                     default=len(text))
            if not _FORGE.search(text[lo:hi]): continue
            add('ERROR', 'spelling:' + wrong, 'write ' + fix + '  ' + ctx(text, m.start()))

    # --- style checks added 2026-08-13, all for rules that were already written down ---

    # Section 5 bans "perfectly balanced pros and cons, four against four, all the same
    # length. Real reviews are lopsided." Nothing checked it, and the Expandi draft ran
    # 4-against-4 in seven of seven competitor sections.
    tool_secs = _tool_sections(text)
    sym = []
    for name, sec in tool_secs:
        pros, cons = _proscons(sec)
        if pros and pros == cons:
            sym.append('%s %dv%d' % (name, pros, cons))
            if pros == 4:
                add('WARN', 'proscons-4x4:' + name, 'four against four, the shape section 5 bans by name')
    if len(sym) >= 3:
        add('WARN', 'proscons-symmetry(%d)' % len(sym), ', '.join(sym))

    # Section 21 requires tool-section entry angles to vary. Two checks: a repeated opening
    # signature, and too many sections entering on a superlative.
    frames, supers = {}, []
    for name, sec in tool_secs:
        opener = _entry_sentence(sec)
        if not opener: continue
        key = ' '.join(opener.lower().split()[:3])
        frames.setdefault(key, []).append(name)
        if re.search(r'\b(?:cheapest|widest|largest|best-rated|most granular|nothing else|'
                     r'no other tool|only tool|unmatched)\b', opener, re.I):
            supers.append(name)
    for key, names in frames.items():
        if len(names) > 1:
            add('WARN', 'entry-frame-repeat', '"%s..." opens %s' % (key, ' and '.join(names)))
    if len(supers) > SUPERLATIVE_ENTRY_CAP:
        add('WARN', 'entry-superlative(%d)' % len(supers), 'sections opening on a superlative: ' + ', '.join(supers))

    # Section 6 bans trailing add-on clauses, and defining a thing by what it is not is the
    # same reflex. Counted rather than located: one instance is fine, thirty is a tic.
    n_rt = len(re.findall(r'\brather than\b', body, re.I))
    n_io = len(re.findall(r'\binstead of\b', body, re.I))
    n_bare = len(re.findall(r',\s+not\s+\w', body))
    if n_rt > NEGATION_CAP or (n_rt + n_io + n_bare) > NEGATION_TOTAL_CAP:
        add('WARN', 'define-by-negation(%d)' % (n_rt + n_io + n_bare),
            '"rather than" %d, "instead of" %d, bare ", not" %d' % (n_rt, n_io, n_bare))

    # Section 17 wants claims that survive being quoted off the page. "the widest here" and
    # "the only one of the nine" mean nothing in an LLM answer or a snippet.
    scoped = []
    for pat, label in ((r'\bof the (?:nine|eight|seven|ten|six|five)\b', 'of the N'),
                       (r'\bon this list\b', 'on this list'),
                       (r'\bin this comparison\b', 'in this comparison'),
                       (r'(?:est|widest|only|nothing|no other|more|fewer|better|worse|first|last)'
                        r'\b[^.]{0,40}?\bhere\b', 'scoped "here"')):
        n = len(re.findall(pat, body, re.I))
        if n: scoped.append('%s %d' % (label, n))
    total_scoped = sum(int(s.rsplit(' ', 1)[1]) for s in scoped)
    if total_scoped > SCOPED_CAP:
        add('WARN', 'unscoped-comparison(%d)' % total_scoped,
            'name the comparison set: ' + ', '.join(scoped))

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

    import statistics as _st
    pw = [len(p.split()) for p in paras] or [0]
    return findings, {'sentences': len(ss), 'over25': sum(1 for x in L if x > 25),
                      'paras': len(paras), 'over_para_cap': sum(1 for x in pw if x > PARA_WORD_CAP),
                      'stdev': round(_st.pstdev(L), 2) if len(L) > 1 else 0.0,
                      'short_pct': round(100.0 * sum(1 for x in L if x <= 6) / max(1, len(L)), 1),
                      'long_pct': round(100.0 * sum(1 for x in L if x > 25) / max(1, len(L)), 1),
                      'avg_para': round(sum(pw)/max(1, len(pw)), 1),
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
