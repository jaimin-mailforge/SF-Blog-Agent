"""Regression test for the rules. Run it after ANY change to check.py or lint/data/.

    python3 lint/selftest.py           run everything
    python3 lint/selftest.py -v        also print the passing cases
    python3 lint/selftest.py --rules   CASES and BENCHMARK only, no draft invariants

Exit code is the number of failures, so it works in a shell conditional.

## Why this exists

On 2026-08-21 I broke the linter three times in one session and caught all three by
hand, which is luck rather than process. The repo is now 2,030 lines of rules and 1,445
lines of checker with no test at all, and `calibrate.py` prints numbers for a human to
read, which is not the same thing.

Two of the three bugs would have been caught here instantly:

  A new local variable named `paras` shadowed the one check() builds for the paragraph
  stat, and the Expandi draft's paragraph count silently fell from 119 to 9. Nothing
  errored. See INVARIANTS below.

  An intro paragraph-count check flagged the editor-approved article, because section 9
  asks for "3 to 6 short paragraphs" and the approved article runs 9. A rule that fires
  on the benchmark is mis-calibrated by definition. See BENCHMARK below.

The third was a rule contradicting another rule: `source of truth` was added to
banned-phrases while section 6 had just been rewritten to stop stripping this reader's
own vocabulary. That one is a judgment call and no test catches it, but the MUST NOT FIRE
table below is where a known-good phrase goes once someone has argued for it, so the
argument does not have to be had twice.

## The three layers

1. CASES: micro-fixtures. A rule must fire on the violation it was written for, and must
   not fire on prose that merely looks like it. Every entry in the must-not-fire half is
   a real false positive that shipped once.
2. INVARIANTS: sanity bounds on the live draft. Not exact values, because the draft
   changes legitimately. A 400-sentence document cannot have 9 paragraphs.
3. BENCHMARK: the editor-approved article, vendored at fixtures/approved-rocketreach.txt.
   Its error count may not rise. If a new rule pushes it up, either the rule is wrong or
   the ceiling needs raising deliberately, with a note saying why.
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'fixtures', 'approved-rocketreach.txt')
DRAFT = os.path.join(ROOT, 'drafts', 'expandi-alternatives.md')

# The approved article's error count on 2026-08-21. It is allowed to fall, never to rise.
# Raise this only with a comment explaining which rule changed and why the benchmark
# genuinely violates it.
BENCHMARK_ERROR_CEILING = 27

# (label, text, rule substring, must_fire)
CASES = [
    # ---- punctuation and person, the hard bans -------------------------------
    ('em dash',            'Pricing is simple — until you add a seat.', 'em-dash', True),
    ('en dash',            'Expect 60–90 days before you are productive.', 'en-dash', True),
    ('semicolon',          'Pro grants 300; Growth grants 1,000.', 'semicolon', True),
    ('first person we',    'We tested every tool on the list.', 'first-person-plural', True),
    ('first person our',   'Our roundup covers nine tools.', 'first-person-plural', True),
    ('US not us',          'Coverage is thin outside US tech.', 'first-person-plural', False),
    # found live on the Dripify page 2026-08-24: \b splits on the hyphen, so the product
    # name We-Connect was reported as first-person plural 12 times.
    ('We-Connect spared',  'We-Connect offers LinkedIn smart sequences.', 'first-person-plural', False),
    ('Dux-Soup spared',    'Dux-Soup runs repeatable drip campaigns.', 'first-person-plural', False),
    ('real we still caught',
     'We-Connect is fine but we tested it ourselves.', 'first-person-plural', True),

    # ---- fragments. every false positive below shipped once -------------------
    ('fragment adverb',    'Expandi is a good one. Genuinely.', 'sentence-fragment', True),
    ('fragment phrase',    "They're unhappy with the bill. All of it.", 'sentence-fragment', True),
    ('fragment drumbeat',  'One sequence. One set of exit rules.', 'sentence-fragment', True),
    ('verb source',        'You source the other end with Leadsforge.', 'sentence-fragment', False),
    ('verb bundle',        'Only Salesforge and lemlist bundle it.', 'sentence-fragment', False),
    ('verb govern',        'One set of exit rules governs them.', 'sentence-fragment', False),
    ('verb split',         'I split the sentence where both halves stand alone.', 'sentence-fragment', False),
    ('imperative',         'Stay put.', 'sentence-fragment', False),
    ('mandated FAQ yes',   'Yes, with a specific caveat.', 'sentence-fragment', False),

    # ---- banned words and phrases --------------------------------------------
    ('banned seamless',    'The handoff is seamless across both channels.', 'banned-word:seamless', True),
    ('banned leverage',    'You can leverage the same sequence twice.', 'banned-word:leverage', True),
    ('banned landscape',   'The outreach landscape changed last year.', 'banned-word:landscape', True),
    ('banned that said',   'That said, Expandi is LinkedIn-only.', 'banned-phrase:that said', True),
    ('product name spared',
     'Apollo and Seamless.AI both sell contact data.', 'banned-word:seamless', False),
    # argued for and allowed on 2026-08-21, see writing.md section 5a
    ('allowed at scale',   'It holds up at scale on the Growth plan.', 'banned-', False),
    ('allowed source of truth',
     'I use it when the CRM is the source of truth.', 'banned-', False),
    ('allowed whether youre',
     "Whether you're on Pro or Growth, mailboxes are unlimited.", 'banned-', False),
    ('allowed navigate',   'Navigating the dashboard takes a minute.', 'banned-', False),

    # ---- figurative verbs ----------------------------------------------------
    ('fig verb sits',      'Waalaxy sits at 0.5% of one-star reviews.', 'figurative-verb', True),
    ('fig verb lives',     'The unified inbox lives inside the sequence.', 'figurative-verb', True),
    ('mandated G2 puts',   'G2 puts Salesforge at 4.6 from 137 reviews.', 'figurative-verb', False),

    # ---- spellings, case sensitive ------------------------------------------
    # rule name carries the wrong spelling verbatim, so match on the prefix and stay
    # case-agnostic. Writing 'spelling:autopilot' here failed on first run: the finding
    # is 'spelling:Autopilot'. The test found a bug in the test, which still counts.
    ('spelling autopilot', 'Autopilot handles the replies for you in Salesforge.',
     'spelling:', True),
    ('spelling copilot',   'Copilot drafts the reply for Salesforge to send.',
     'spelling:', True),
    ('correct Auto-Pilot', 'Auto-Pilot handles the replies for you in Salesforge.',
     'spelling:', False),
    ('correct Co-Pilot',   'Co-Pilot drafts the reply for Salesforge to send.',
     'spelling:', False),
    # scoping: a Forge mention must not license a hit on a competitor in another sentence
    ('spelling scoped out',
     'Outreach ships Autopilot. Salesforge is a different product.', 'spelling:', False),

    # ---- counted rules. each fires only above its cap, so the case must exceed it
    ('frame restart x3',
     'The branching is what matters. The billing unit matters most. '
     'Two things behind it come from the stack.', 'frame-restart', True),
    ('frame restart x1 under cap',
     'The branching is what matters.', 'frame-restart', False),
    ('trailing superlative I x3',
     "It is the widest I have seen. No other vendor I checked publishes them. "
     "It is the cleanest structure I found.", 'trailing-superlative-i', True),
    ('trailing superlative I x1 under cap',
     'It is the widest I have seen.', 'trailing-superlative-i', False),

    # ---- placeholders: legal in a draft, never in an article -----------------
    ('placeholder warns',  'The rate is [[FIGURE: annual price]] a month.',
     'unresolved-placeholder', True),
]


def fires(text, rule_sub):
    findings, _ = C.check('Title that is a reasonable length here', 'm' * 140, text, 'selftest')
    return [f for f in findings if rule_sub in f[1]]


def run_cases(verbose):
    fails = []
    for label, text, rule, must in CASES:
        hits = fires(text, rule)
        ok = bool(hits) == must
        if not ok:
            fails.append('CASE  %-34s expected %s on "%s", got %s'
                         % (label, 'a hit' if must else 'no hit', rule,
                            [h[1] for h in hits] or 'nothing'))
        elif verbose:
            print('  ok    %-34s %s' % (label, rule))
    return fails


def _sections_agree(text, findings):
    """sections.py recomputes rules for targeting. It must not disagree with check.py."""
    try:
        import sections as S
    except Exception:
        return True, 'sections.py not importable, skipped'
    per_section = sum(S.score_section(body)['frags']
                      for _, body in S.split_sections(text))
    article = sum(1 for f in findings if f[1] == 'sentence-fragment')
    return per_section == article, 'per-section %d, article-level %d' % (per_section, article)


def run_invariants(verbose):
    """Sanity bounds on the live draft. These catch a stat that silently collapses."""
    fails = []
    if not os.path.exists(DRAFT):
        return ['INVARIANT  draft missing at %s' % DRAFT]
    text = open(DRAFT, encoding='utf-8').read()
    title = text.splitlines()[0].lstrip('# ').strip()
    findings, st = C.check(title, 'm' * 141, text, 'draft')
    err = [f for f in findings if f[0] == 'ERROR']
    warn = [f for f in findings if f[0] == 'WARN']

    checks = [
        ('draft has no errors',        len(err) == 0,           '%d errors' % len(err)),
        ('draft has no warnings',      len(warn) == 0,          '%d warnings' % len(warn)),
        # the paras-shadowing bug dropped this from 119 to 9 with no error raised
        ('paragraph count is sane',    st['paras'] > 50,        'paras=%d' % st['paras']),
        ('sentence count is sane',     st['sentences'] > 300,   'sentences=%d' % st['sentences']),
        ('paras fewer than sentences', st['paras'] < st['sentences'],
         'paras=%d sentences=%d' % (st['paras'], st['sentences'])),
        # sections.py must agree with the article-level fragment count. It did not on
        # first run: filtering by line instead of by paragraph reported the Final
        # Verdict's six mandated routing labels as fragments while check.py said zero.
        ('sections.py agrees on fragments', _sections_agree(text, findings)[0],
         _sections_agree(text, findings)[1]),
        ('rhythm floors hold',
         st['stdev'] >= C.STDEV_FLOOR and st['short_pct'] >= C.SHORT_FLOOR
         and st['long_pct'] >= C.LONG_FLOOR,
         'stdev=%.2f short=%.1f long=%.1f' % (st['stdev'], st['short_pct'], st['long_pct'])),
    ]
    for label, ok, detail in checks:
        if not ok:
            fails.append('INVARIANT  %-30s %s' % (label, detail))
        elif verbose:
            print('  ok    %-34s %s' % (label, detail))
    return fails


def run_benchmark(verbose):
    """A rule that fires on the editor-approved article is mis-calibrated."""
    if not os.path.exists(FIXTURE):
        return ['BENCHMARK  fixture missing at %s' % FIXTURE]
    text = open(FIXTURE, encoding='utf-8').read()
    findings, st = C.check('9 RocketReach Alternatives With Better Data Accuracy 2026',
                           'm' * 131, text, 'benchmark')
    err = [f for f in findings if f[0] == 'ERROR']
    fails = []
    if len(err) > BENCHMARK_ERROR_CEILING:
        new = sorted({f[1].split('(')[0] for f in err})
        fails.append('BENCHMARK  errors rose to %d, ceiling is %d. Rules present: %s'
                     % (len(err), BENCHMARK_ERROR_CEILING, ', '.join(new)))
        fails.append('           A new rule is flagging the approved article. Fix the rule,')
        fails.append('           or raise the ceiling with a comment saying why.')
    elif verbose:
        print('  ok    %-34s %d errors, ceiling %d'
              % ('benchmark within ceiling', len(err), BENCHMARK_ERROR_CEILING))

    # the benchmark must keep passing the rhythm floors it was used to calibrate
    if st['stdev'] < C.STDEV_FLOOR or st['short_pct'] < C.SHORT_FLOOR \
            or st['long_pct'] < C.LONG_FLOOR:
        fails.append('BENCHMARK  the approved article now fails a rhythm floor: '
                     'stdev=%.2f short=%.1f long=%.1f. The floors were calibrated ON it, '
                     'so a floor it fails is wrong.'
                     % (st['stdev'], st['short_pct'], st['long_pct']))
    elif verbose:
        print('  ok    %-34s stdev=%.2f short=%.1f long=%.1f'
              % ('benchmark clears rhythm floors', st['stdev'], st['short_pct'],
                 st['long_pct']))
    return fails


def main():
    verbose = '-v' in sys.argv
    # --rules skips the draft invariants. Those assert the live draft is at 0 errors and
    # 0 warnings, which is true between jobs and false in the middle of one, so the Stop
    # hook runs this mode: rule integrity cannot be tripped by ordinary draft editing.
    rules_only = '--rules' in sys.argv
    print('RULE SELFTEST' + (' (rules only)' if rules_only else ''))
    fails = run_cases(verbose) + run_benchmark(verbose)
    if not rules_only:
        fails += run_invariants(verbose)
    print('  %d micro-cases, %s invariants, benchmark ceiling %d'
          % (len(CASES), 'skipped' if rules_only else '7', BENCHMARK_ERROR_CEILING))
    if not fails:
        print('\nPASS. Safe to commit a rule change.')
        return 0
    print('\n%d FAILURE(S):\n' % len(fails))
    for f in fails:
        print('  ' + f)
    print('\nDo not commit until these are green or deliberately re-baselined.')
    return min(len(fails), 125)


if __name__ == '__main__':
    sys.exit(main())
