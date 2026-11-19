---
type: "Reference"
title: "Remote Control, gateway and org policy sign-in errors"
description: "Remote Control disconnect and refresh messages, Cloud gateway sign-in errors, and org policy blocks on scheduled tasks."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, remote-control, gateway, scheduled-tasks, managed-settings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud, ide]
requires: "Remote Control requires direct api.anthropic.com access"
identifiers:
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "claude remote-control"
  - "/remote-control"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_UNIX_SOCKET"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_VERTEX"
  - "claude --remote-control"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors around Remote Control sessions, organization policy and the Claude apps gateway.

# How to use it

- **Scheduled tasks / Routines off for your organization:** cloud scheduled tasks ([routines](/docs/en/routines)) are disabled; cannot be turned on with local settings, env vars or flags. A Team or Enterprise Owner toggles "Scheduled tasks (Was Routines)" or "Routines" under Organization settings > Capabilities > Remote sessions.
- **Remote Control requires the Anthropic API:** blocked when a `CLAUDE_CODE_USE_*` provider variable is set, `ANTHROPIC_BASE_URL` points away from `api.anthropic.com` (blocked since v2.1.196), `ANTHROPIC_UNIX_SOCKET` is set, or an enterprise cloud gateway login was used. Unset the variable or check the settings `env` key.
- **Remote Control disconnected lines:** the transcript shows `Remote Control disconnected — <cause> — run /login...`. Causes: `Claude.ai login expired`, `Claude.ai login was rejected`, `OAuth token unavailable`, `OAuth token refresh failed`, `JWT refresh failed: no OAuth token`, `Signed out of Claude`. Run `/login`, then `/remote-control` unless the message says it reconnects on its own. The local session keeps running. When the login service is unreachable Claude Code keeps Remote Control up and retries until the credential expires. Messages changed at v2.1.224, v2.1.225 and v2.1.238.
- **`claude remote-control` renewal warning:** the server warns that the connection keeps working for about 26 hours; if it still cannot sign in it prints `Poll: Authentication failed (401)` and stops. Run `claude /login` in another terminal, then restart the server.
- **Account or organization changed:** Remote Control stops once claude.ai confirms a different account; run `/remote-control` for the new account. Detected since v2.1.234. In the Desktop app or an IDE host, a signed-out or switched account ends the session and cannot continue under the new account.
- **Administrator policy requires a Cloud gateway sign-in:** managed settings set `forceLoginMethod` to `"gateway"` or `forceLoginGatewayUrl`. Messages: `Not signed in to the Cloud gateway — run /login.`; startup exit when an Anthropic-issued credential (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, saved Console key) is present.
- **Cloud gateway session expired:** non-interactive runs, background or unattended sessions, and `claude` subcommands other than `claude auth` exit with `Cloud gateway <url> no longer accepts this session. Start \`claude\` and sign in again with /login.`
- **Sign-in timed out while waiting for you to continue**, **Gateway refused the request** (403, signing in again does not help; admin checks access rules and audit log).

# Notes

A regression in v2.1.265 showed the gateway message in some LLM-gateway configurations; fixed in v2.1.266.
