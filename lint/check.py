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

# Continuity and narrator position, calibrated 2026-08-20 against the approved RocketReach
# article. Both discriminate cleanly: approved scores 1 and 0, the Expandi draft scored 15
# and 8. Section 9b has capped trailing-superlative "I" at two per article since 2026-08-19
# and had no checker, which is how fifteen of them survived a full review cycle.
TRAILING_I_CAP = 2       # "the widest I've seen", "no other vendor I checked"
INTRO_SHARED_FIGURES = 2  # money figures the intro and the next section may share
FRAME_RESTART_CAP = 2    # "X is what matters", "Two things...", "matters most"

# A superlative, then an "I"-clause after it in the same sentence. The narrator is being used
# as a citation to license the claim instead of leading the sentence.
_SUPER = (r"\b(?:widest|lowest|highest|cheapest|deepest|best|worst|largest|biggest|smallest|"
          r"fewest|broadest|tightest|cleanest|strongest|weakest|only|first|most\s+\w+|"
          r"least\s+\w+|no\s+other|nobody\s+else|nothing\s+else|any\s+other|"
          r"more\s+than\s+(?:any|most))\b")
_ICITE = (r"\bI(?:'ve|\s+have)?\s+(?:found|checked|compared|recorded|priced|saw|seen|tested|"
          r"looked|read|counted|scored|reviewed|measured|encountered)\b")

# Topic announcements. Each one opens a new frame instead of developing the previous one, and
# a section carrying four of them has no argument at all. "is the real reason" is deliberately
# not here: it reads as a paragraph closing line as often as a restart, and cost 50% precision.
_FRAME = (
    (r"\b(?:is|are)\s+what\s+matters\b",                     'is what matters'),
    (r"\bmatters\s+most\b",                                   'matters most'),
    (r"\bworth\s+understanding\b",                            'worth understanding'),
    (r"^\s*(?:Two|Three|Four)\s+things\b",                     'Two/Three things'),
    (r"^\s*There\s+are\s+(?:two|three|four)\s+reasons\b",     'There are N reasons'),
    (r"^\s*(?:The|This|That)\s+\w+(?:\s+\w+){0,2}\s+is\s+the\s+(?:thing|point|part)\b",
                                                              'X is the thing/part'),
    (r"\bis\s+the\s+(?:second|third)\s+gate\b",              'is the Nth gate'),
    (r"^\s*What\s+(?:differs|matters)\b",                      'What differs/matters'),
)

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

# Finite verbs, for the sentence-fragment check. Not a parser, a heuristic: a short
# stretch of prose with none of these is almost always a fragment.
_FINITE = re.compile(
    r"\b(?:is|are|was|were|be|been|being|am|has|have|had|do|does|did|can|could|will|would|"
    r"shall|should|may|might|must|let|"
    r"run|runs|ran|get|gets|got|go|goes|went|come|comes|came|make|makes|made|take|takes|took|"
    r"give|gives|gave|put|puts|pay|pays|paid|cost|costs|charge|charges|bill|bills|add|adds|"
    r"send|sends|sit|sits|mean|means|need|needs|want|wants|work|works|use|uses|keep|keeps|kept|"
    r"land|lands|leave|leaves|left|start|starts|stop|stops|include|includes|carry|carries|"
    r"cover|covers|read|reads|show|shows|tell|tells|say|says|find|finds|found|reach|reaches|"
    r"point|points|recommend|recommends|pick|picks|stay|stays|count|counts|move|moves|know|knows|"
    r"treat|treats|ask|asks|spread|clear|clears|route|routes|branch|branches|combine|combines|"
    r"handle|handles|draft|drafts|score|scores|rate|rates|hold|holds|publish|publishes|"
    r"connect|connects|expect|expects|explain|explains|decide|decides|cap|caps|exist|exists|"
    r"arrive|arrives|invert|inverts|matter|matters|depend|depends|turn|turns|deserve|deserves|"
    r"sell|sells|buy|buys|help|helps|beat|beats|stand|stands|fit|fits|fail|fails|grow|grows|"
    r"drift|drifts|apply|applies|price|prices|quote|quotes|list|lists|name|names|"
    r"burn|burns|roll|rolls|refund|refunds|verify|verifies|enrich|enriches|warm|warms|"
    # added 2026-08-20: false-positived on clean prose from the continuity pass
    r"source|sources|hear|hears|govern|governs|split|splits|chain|chains|earn|earns|"
    r"lift|lifts|drop|drops|check|checks|scale|scales|track|tracks|trade|trades|"
    r"bundle|bundles|diverge|diverges|settle|settles|route|branch|serve|serves)\b"
    r"|\b\w+(?:'s|'re|'ve|'ll|'d|n't)\b", re.I)

def _is_fragment(s):
    """True when a short stretch of prose carries no finite verb.

    A heuristic, so it is deliberately conservative: a missed fragment costs a reader
    nothing, while a wrongly flagged one would block a publish. Hence the exemptions.
    Any -ed word counts as a verb, and an FAQ direct answer opening "Yes," or "No," is
    exempt because section 16 mandates that shape."""
    s = s.strip().strip('()')
    if not s or len(s.split()) > 8: return False
    if re.match(r'^(?:Yes|No)\b', s): return False        # mandated FAQ answer shape
    # Any inflected word counts as a possible verb. This makes the check miss fragments
    # like "Two caveats." and "In fragments.", and that is the deliberate trade: without
    # a parser, the alternative is flagging "Pro grants 300." and "lemlist bundles the
    # first half everywhere." as verbless, which would block a publish over good prose.
    # The check catches the blatant cases only. The rest is section 2's job, and a read.
    if re.search(r'\b\w{3,}(?:s|ed|ing)\b', s): return False
    return not _FINITE.search(s)

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

_FORGE_TOOL = re.compile(r'\b(?:Salesforge|Leadsforge|Mailforge|Infraforge|Primeforge|'
                         r'Warmforge|Megaforge|Agent Frank)\b', re.I)

# A con cell earns its imbalance by citing something checkable.
_CITED_CON = re.compile(r'\b\d[\d,.]*\s*(?:mentions|reviews)\b'
                        r'|\bcon tag\b'
                        r'|\b(?:scores?|rated|rating|holds)\b[^|]{0,30}\b\d[\d.]*\b'
                        r'|\b\d[\d.]*\s*(?:out of|/)\s*5\b'
                        r'|\b\d[\d.]*%', re.I)

def _proscons_text(sec):
    """Raw text of the Pros and cons table, for citation checks."""
    m = re.search(r'###\s+Pros and cons\s*\n(.*?)(?=\n###|\Z)', sec, re.S)
    return m.group(1) if m else ''

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
# Closed set of TL;DR openers. Decided by Jaimin on 2026-08-19, widened from the
# single mandatory "Best for" after the editor-approved RocketReach article used four
# variants. The set stays closed so AI Overviews still lift a predictable shape, but a
# tool whose whole case is price can say so: "Cheapest pick for email-only lookups".
TLDR_OPENERS = ('Best for', 'Best overall for', 'Cheapest pick for', 'Best if you want')
# A currency symbol followed by a digit. Deliberately narrow: a bare number plus
# "a month" would flag "caps you at 300 invitations a month", which is not a price.
_TLDR_PRICE = re.compile(r'[$\u20ac\u00a3]\s?\d')
_TLDR_SHAPE = re.compile(r'^-\s+\*\*.+?(?:\*\*\s*:|\s*:\*\*)\s*(?:'
                         + '|'.join(re.escape(o) for o in TLDR_OPENERS) + r')\b')
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
            if not line.lstrip().startswith('- '): continue
            if not _TLDR_SHAPE.match(line.strip()):
                add('ERROR', 'tldr-shape', 'open with one of ' + ', '.join(TLDR_OPENERS)
                    + '  ' + line.strip()[:70])
            # No price figures in the TL;DR. Decided by Jaimin on 2026-08-19. Relative
            # claims like "at the cheapest entry price" are fine; a currency figure is not.
            m = _TLDR_PRICE.search(line)
            if m:
                add('ERROR', 'tldr-price', 'no price figures in the TL;DR, it routes by buyer  '
                    + line.strip()[max(0, m.start() - 40):m.start() + 30])

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
    #
    # Product names are exempt by span, the same way banned words are. Found 2026-08-24 on
    # the live Dripify alternatives page, which reviews a tool called We-Connect: \b treats
    # the hyphen as a word boundary, so every one of its 12 mentions was reported as a
    # first-person-plural ERROR. The rule that matters most in this repo was firing on a
    # competitor's name.
    for m in re.finditer(r'\b(?:we|We|our|Our)\b|(?<![A-Z])\bus\b(?![A-Z])', body):
        w = m.group(0)
        if _in_spans(m.start(), prot): continue
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

    # Sentence fragments. Added 2026-08-19 after the short-sentence floor was gamed with
    # them: chasing "18% of sentences at six words or fewer" produced "Genuinely.",
    # "All of it.", "Connected or not.", "In fragments.", "At that price." and ten more.
    # A short sentence and a fragment are not the same thing, and the fragment pile-up is
    # the AI-slop staccato the voice rule exists to prevent. The floor wants short
    # COMPLETE sentences, so this check keeps the two apart.
    # Paragraph prose only: a bullet may legitimately end on a list.
    for para in paras:
        if para.lstrip().startswith(('-', '*', '|', '#', '<')): continue
        for s in sentences([para], min_words=1):
            if _is_fragment(s):
                add('WARN', 'sentence-fragment', 'no verb: "%s"' % s.strip()[:60])

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
    # Competitor pros/cons balance. Decided by Jaimin on 2026-08-19, replacing the old
    # "four against four is banned" check. The editor-approved RocketReach article runs
    # every competitor within one of balanced and puts all its imbalance in the house
    # product, on the reasoning that bias in the Forge cons cell is discounted by every
    # reader while bias in a rival's table is where trust actually leaks. So a competitor
    # may run net-negative only when a con cell cites evidence: a con-tag mention count,
    # a review score, a sub-score, or a share.
    tool_secs = _tool_sections(text)
    for name, sec in tool_secs:
        pros, cons = _proscons(sec)
        if not pros and not cons: continue
        if _FORGE_TOOL.search(name): continue          # house product is exempt by design
        if cons - pros >= 2 and not _CITED_CON.search(_proscons_text(sec)):
            add('WARN', 'proscons-uncited:' + name,
                '%d cons against %d pros with nothing cited. balance it or cite a con tag, '
                'a score or a share' % (cons, pros))

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

    # Section 9b, the narrator as citation. A superlative followed by an "I"-clause in the same
    # sentence parks the narrator in a trailing position to license the claim. The rule has
    # existed since 2026-08-19 with a cap of two and no checker. Fix is one of two things: make
    # the narrator lead the sentence, or scope the claim inside it and drop the "I" entirely.
    trailing = []
    for sent in sentences(prose):
        m = re.search(_ICITE, sent)
        if m and re.search(_SUPER, sent[:m.start()], re.I):
            trailing.append(sent.strip())
    if len(trailing) > TRAILING_I_CAP:
        add('WARN', 'trailing-superlative-i(%d)' % len(trailing),
            'narrator used as a citation, cap %d: %s' % (TRAILING_I_CAP, trailing[0][:70]))

    # Section 3, the through-line. Counted rather than located, because one topic announcement
    # in an article is a signpost and eight is a prose habit that leaves every section without
    # an argument.
    restarts = []
    for sent in sentences(prose):
        for pat, name in _FRAME:
            if re.search(pat, sent, re.I):
                restarts.append((name, sent.strip())); break
    if len(restarts) > FRAME_RESTART_CAP:
        add('WARN', 'frame-restart(%d)' % len(restarts),
            'develop the argument, do not restart it: ' +
            ', '.join('"%s"' % n for n, _ in restarts[:4]))

    # Section 9d, the introduction. Two things here are mechanical. Whether the intro
    # names plural pain points is not, so it stays a [JUDGE] read and this code does
    # not pretend otherwise.
    #
    # The duplication check is the one that matters. The Expandi intro ran the $79 to
    # $136.50 arithmetic across three paragraphs and "Why People Leave Expandi" ran the
    # identical arithmetic immediately after, with the sources. An intro that proves
    # what the next section proves has no reason to exist.
    parts = re.split(r'^##\s+(?!#)', body, flags=re.M)
    if len(parts) >= 3:
        intro, first_sec = parts[0], parts[1]
        money = re.compile(r'[$\u20ac\u00a3]\s?\d[\d,]*(?:\.\d{1,2})?(?<![,.])')
        a = {m.group(0).replace(' ', '') for m in money.finditer(intro)}
        b = {m.group(0).replace(' ', '') for m in money.finditer(first_sec)}
        shared = a & b
        if len(shared) > INTRO_SHARED_FIGURES:
            add('WARN', 'intro-duplicates-next(%d)' % len(shared),
                'intro and the next section both prove %s. Name it once in the intro.'
                % ', '.join(sorted(shared)[:5]))
        # No intro paragraph-count check. Section 9 asks for "3 to 6 short paragraphs"
        # and the editor-approved article runs 9, so a count check would flag the
        # benchmark. That conflict belongs in the rules file, not in a warning nobody
        # can act on. Flagged to Jaimin 2026-08-21.

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
