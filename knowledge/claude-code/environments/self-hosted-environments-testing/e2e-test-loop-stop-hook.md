---
type: "Guide"
title: "End-to-end test loop with Stop-hook read-back"
description: "Dispatch a session with claude -p --environment, capture each reply via a Stop hook, send follow-ups with --cloud, assert in CI."
resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
tags: [self-hosted, testing, ci, stop-hook, headless]
kind: "mixed"
maturity: "beta"
since: "2.1.224"
surfaces: [cloud, cli, headless]
requires: "Claude Code v2.1.224+ on the dispatching machine; jq on the runner"
identifiers:
  - "claude -p"
  - "--environment"
  - "--ref"
  - "--cloud"
  - "--output-format json"
  - "E2E_REPLY_DIR"
  - "E2E_REPLY_URL"
  - "last_assistant_message"
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
  - "CLAUDE_TEST_ENVIRONMENT_ID"
  - "remote.defaultEnvironmentId"
  - "~/.claude/hooks/e2e-stop-hook-capture.sh"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-testing"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
    title: "Test self-hosted environments end to end"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A CI smoke test recipe that verifies a runner image: create a session, read Claude's reply, send a follow-up, read that reply. Claude Code's Stop hook receives `last_assistant_message` in its stdin JSON; a script installed on the (test) runner appends it to `$E2E_REPLY_DIR/<session_id>.txt`. The hook is a no-op unless `E2E_REPLY_DIR` is set and exists, and converts `cse_` to `session_` in `CLAUDE_CODE_REMOTE_SESSION_ID`.

# How to use it

1. Save the Stop hook entry (`type: command`, `timeout: 10`, command `"$CLAUDE_CONFIG_DIR/hooks/e2e-stop-hook-capture.sh"`) in `~/.claude/settings.json` on the runner host and the script as `~/.claude/hooks/e2e-stop-hook-capture.sh` (executable). Install before the runner starts, because the runner snapshots `~/.claude/` once at startup. Export `E2E_REPLY_DIR` to the runner. Install only on test runners.
2. Create: `claude -p "<prompt>" --environment <environment-id> --output-format json` from a git checkout (repo auto-detected from `origin`); optional `--ref <branch>`. It exits without waiting. Outputs: `{"ok":true,"session_id":"session_...","title":"...","url":"...","pool_id":"..."}`; `{"ok":false,"error":"..."}` with exit 1; some early errors go to stderr with no JSON, exit 1.
3. Poll for the reply in the reply file (example script waits 90 s).
4. Follow up: `claude -p "<message>" --cloud <session_id> --output-format json`; check `.ok == true`.

Remote runners: replace the file write with a `curl -X POST --data-binary @-` to `$E2E_REPLY_URL/$sid`.

# Limits and defaults

- `--environment` takes precedence over the `remote.defaultEnvironmentId` setting; does not support `--output-format stream-json`; cannot combine with `--resume`, `--continue`, `--teleport`, `--session-id`, `--init-only`. `--cloud` is rejected with a session ID or URL, and in non-interactive runs when it carries a description; bare `--cloud` is treated as absent.
- Legacy variable `CLAUDE_TEST_POOL_ID` still read as fallback for `CLAUDE_TEST_ENVIRONMENT_ID`.
