---
type: "Feature"
title: "Send follow-ups to a cloud session from the CLI"
description: "claude -p with --cloud <session-id> queues a message into an existing cloud session and exits, usable from scripts and CI."
resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
tags: [cloud, headless, follow-up, scripting]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: "claude auth login; Anthropic account; allow_remote_sessions policy enabled; not Bedrock or other third-party provider"
identifiers:
  - "claude -p"
  - "--cloud <session-id>"
  - "--output-format json"
  - "allow_remote_sessions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-code-on-the-web"
    resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
    title: "Use Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Post one message to a running cloud session (wherever it executes) from any machine logged in with `claude auth login`. The CLI sends no local session state, queues the message and exits without waiting for a reply. Use it to steer long sessions or queue the next step from a CI script.

# How to use it

```bash
claude -p "your message" --cloud <session-id>
echo "your message" | claude -p --cloud <session-id>
```

`<session-id>` is a bare `session_...` or `cse_...` ID, or a `claude.ai/code/<id>` URL (scheme and query optional). Success prints "Sent to cloud session.", the Session ID and a View link. `--output-format json` gives `{ok, session_id, url}` or `{ok: false, session_id, error}`; configuration errors print to stderr without JSON. `--output-format stream-json` is not supported with `--cloud <session-id>`. Errors are prefixed `Error: `; delivery failures read `failed to send message to cloud session <id>: <reason>`.

# Limits and defaults

| Message | Meaning |
| - | - |
| `Cloud sessions aren't available with <provider>...` | third-party provider configured (for example `CLAUDE_CODE_USE_BEDROCK`) |
| `Cloud sessions are disabled by your organization's policy...` | `allow_remote_sessions` off |
| `Couldn't verify your organization's policy for cloud sessions...` | policy not loaded; refuses the send; retry |
| `Cloud sessions aren't available:` plus cause | loading policy failed |
| `Attaching to an existing cloud session is not enabled for your account.` | used `--cloud <session-id>` without `-p` |
| `Session not found: <id>` | wrong ID or no access |
| `cloud session <id> is archived and cannot accept new messages` | archived; start a new session |

An LLM gateway set only via `ANTHROPIC_BASE_URL` is not a third-party provider for this check, but sign-in is still required. Other sign-in errors: `Unable to get organization UUID`, "Cloud sessions need a claude.ai sign-in" (run `claude auth login`); Remote Control wording such as `Remote Control session expired`, `Access denied`, `Remote Control may not be available for this organization`.
