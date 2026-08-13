"""Claude Code hook entry point. Two modes:

  hook.py pretooluse   reads the hook JSON on stdin, blocks a Write/Edit whose
                       content breaks a [LINT] rule
  hook.py stop         lints every article file in the tree, exits 2 to keep the
                       turn open while errors remain

Only files under drafts/ and articles/ are checked. The rules files carry the
banned lists in prose and would flag themselves.
"""
import sys, os, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check as C

SCOPES = ('drafts/', 'articles/')

def in_scope(path):
    p = (path or '').replace('\\', '/')
    return p.endswith('.md') and any(s in p for s in SCOPES)

def errors_in(text, title='', meta=''):
    findings, _ = C.check(title, meta, text, 'hook')
    return [f for f in findings if f[0] == 'ERROR']

def pretooluse():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    ti = data.get('tool_input') or {}
    path = ti.get('file_path') or ti.get('path') or ''
    if not in_scope(path):
        return 0
    text = ti.get('content') or ti.get('new_string') or ''
    if not text.strip():
        return 0
    errs = errors_in(text)
    if not errs:
        return 0
    lines = ['%s  %s' % (r, d) for _, r, d in errs[:12]]
    if len(errs) > 12:
        lines.append('...and %d more' % (len(errs) - 12))
    reason = ('Blocked by the house style gate. %d error(s) in %s:\n%s\n\n'
              'Fix each named violation at its location, then write again. '
              'Rules are in rules/writing.md.' % (len(errs), path, '\n'.join(lines)))
    print(json.dumps({
        'systemMessage': 'Style gate blocked a write to %s (%d errors)' % (path, len(errs)),
        'hookSpecificOutput': {
            'hookEventName': 'PreToolUse',
            'permissionDecision': 'deny',
            'permissionDecisionReason': reason,
        },
    }))
    return 0

def stop():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = []
    for scope in SCOPES:
        for f in glob.glob(os.path.join(root, scope, '**', '*.md'), recursive=True):
            text = open(f, encoding='utf-8', errors='replace').read()
            title = text.splitlines()[0].lstrip('# ').strip() if text.strip() else ''
            m = re.search(r'\*\*Meta:\*\*\s*(.+)', text)
            errs = errors_in(text, title, m.group(1).strip() if m else '')
            for _, r, d in errs:
                total.append('%s: %s  %s' % (os.path.relpath(f, root), r, d))
    if not total:
        return 0
    sys.stderr.write('Style gate: %d error(s) still open.\n%s\n'
                     % (len(total), '\n'.join(total[:25])))
    return 2

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'pretooluse'
    sys.exit(stop() if mode == 'stop' else pretooluse())
