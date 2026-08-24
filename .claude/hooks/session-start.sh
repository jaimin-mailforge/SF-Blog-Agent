#!/bin/bash
# SessionStart hook. This repo installs nothing, because the whole toolchain is Python
# stdlib plus curl, both already present in every environment. So the hook's job is not
# dependency install, it is a health check: confirm the toolchain is there and the rules
# engine still passes its own selftest, so a fresh session learns about a broken linter
# on open rather than three steps into a drafting job.
#
# It never fails the session. A warning here is informational; the Stop hook is the gate
# that actually blocks a bad turn. Synchronous, because the checks take under two seconds
# and there is no reason to race them.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

warn=0

# 1. toolchain. The scripts assume both.
command -v python3 >/dev/null 2>&1 || { echo "SESSION-START WARN: python3 not found"; warn=1; }
command -v curl    >/dev/null 2>&1 || { echo "SESSION-START WARN: curl not found, URL audits and price checks will fail"; warn=1; }

# 2. future-proofing. There is no requirements.txt today, and if one is ever added this
#    installs it. Idempotent, and only in the remote env so a local CLI session is not
#    surprised by a pip run it did not ask for.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && [ -f requirements.txt ]; then
  python3 -m pip install -q -r requirements.txt || echo "SESSION-START WARN: pip install failed"
fi

# 3. the rules engine has to pass its own regression test, or every lint this session
#    runs is suspect. --rules is the fast hermetic half: micro-cases plus the vendored
#    benchmark, no dependence on the live draft's state.
if command -v python3 >/dev/null 2>&1; then
  if python3 lint/selftest.py --rules >/tmp/sf-selftest.out 2>&1; then
    echo "SESSION-START: rules selftest PASS. Style gates are live (PreToolUse + Stop)."
  else
    echo "SESSION-START WARN: rules selftest FAILED. The linter may mis-report until fixed:"
    tail -6 /tmp/sf-selftest.out
    warn=1
  fi
fi

# 4. remind a fresh session what the entry points are, so it does not reinvent them.
echo "Entry points: /new-article <keyword>  /rewrite-article <url>  /polish-draft <path>  /verify-prices <path|url>"
echo "Read CLAUDE.md first. Rules in rules/, checkers in lint/."

[ "$warn" = "0" ] && echo "SESSION-START: environment healthy." || echo "SESSION-START: started with warnings above."
exit 0
