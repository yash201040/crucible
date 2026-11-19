---
type: "Feature"
title: "claude.ai connectors in Claude Code"
description: "Connectors added at claude.ai load automatically when signed in with a claude.ai subscription; auth conditions and display states."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, claude-ai, connectors, authentication]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, sdk, cloud, desktop]
requires: "claude.ai subscription login as the active authentication method"
identifiers:
  - "claude.ai/customize/connectors"
  - "claude.ai Claude Docs"
  - "Show unused connectors"
  - "managed"
  - "session token rejected"
  - "/login"
  - "/status"
  - "ANTHROPIC_PROFILE"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "apiKeyHelper"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

MCP servers added in claude.ai (connectors) appear in `/mcp` when you are logged in with a claude.ai account. On Team and Enterprise plans only admins can add them. Anthropic also provides some itself: where Claude Docs is available, `claude.ai Claude Docs` appears with no setup. `managed` marks a connector whose auth your organization manages. Never-signed-in connectors are collapsed behind `Show unused connectors`.

# Limits and defaults

- Fetched only when the active auth method is a claude.ai subscription login. Not loaded when `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` is active; a third-party provider (Bedrock, Google Cloud's Agent Platform) is active; `ANTHROPIC_PROFILE`, federation variables or an Anthropic profile supplies the credential; or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`, model requests only) holds the credential. Run `/status` to check, fix, then `/login`.
- A temporary network failure at start is retried up to three times in the background; otherwise restart.
- `session token rejected` (detail `claude.ai rejected the session token`): run `/login` then reconnect from `/mcp`; re-authorizing the connector does not help. Before v2.1.222 these were marked needs-auth.
- A server you added in Claude Code with the same URL takes precedence; `/mcp` lists the connector as hidden.
- Anthropic-hosted connectors such as Microsoft 365, Gmail and Google Calendar do not support local OAuth (message `is Anthropic-hosted and doesn't support local OAuth`); remove your entry with `claude mcp remove <name>` and connect at claude.ai.
