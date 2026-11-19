---
type: "Limit"
title: "Remote Control limitations and recovery"
description: "Process, network and reconnection limits of Remote Control, including crash handling in server mode and outage timeouts."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [remote-control, limits, reconnect, server-mode, tmux]
kind: "limit"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "tmux"
  - "screen"
  - "claude doctor"
  - "claude auth login"
  - "claude auth logout"
  - "claude setup-token"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "apiKeyHelper"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

- One remote session per interactive Claude Code process; use server mode for multiple concurrent sessions from one process (default capacity 32).
- The local process must keep running; closing the terminal or quitting Desktop/VS Code takes the session offline. On a remote machine, run inside `tmux` or `screen`.
- A crashed session in server mode is served again when you send it a message from a device (v2.1.238+); no server restart needed.
- HTTP 403 on a connected interactive session: retried up to three minutes, then disconnects naming the refuser.
- Extended network outage: server mode gives up after roughly 10 minutes and the process exits; an interactive session retries indefinitely and reconnects itself.
- Presence heartbeat failure message: `could not reach the Remote Control server for about 30 minutes` (run `/remote-control`).
- Open sessions fetch the org policy about once an hour; policy change while connected archives the session or stops the server.
- If compaction rewrote the conversation or `/resume` switched conversations before a reconnect, the old server session is archived (findable in archived sessions at claude.ai/code).

# Notes

Troubleshooting pointers given on the page:
- Long-lived tokens from `claude setup-token` or `CLAUDE_CODE_OAUTH_TOKEN` cannot establish sessions ("requires a full-scope login token"): run `claude auth login`.
- `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` take precedence and trigger "requires claude.ai subscription auth": remove them.
- Stale entitlements: `claude auth logout` then `claude auth login`; `claude doctor` shows which eligibility check failed and the `Organization policy` line.
- Debug credential failures with `claude --remote-control --debug-file claude-debug.log` and search for `code-session`; Remote Control needs outbound port 443 to the Anthropic API.
- `Session failed: working folder not found:` means the session folder is missing (before v2.1.318 shown as `spawn error:` / `ENOENT`).
- Warning "The program file this Remote Control started from is gone": restart the server; new sessions run the newer installed version.
- "Previous session is unavailable" / "Couldn't reconnect": run `/remote-control`; doing so after "Previous session is unavailable" without restarting leaves earlier messages out of the new session.
- Local process uses outbound HTTPS only and opens no inbound ports.
