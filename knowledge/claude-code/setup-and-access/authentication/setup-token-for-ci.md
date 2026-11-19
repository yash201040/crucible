---
type: "Feature"
title: "claude setup-token for CI"
description: "Generates a one-year OAuth token for CI and scripts, set as CLAUDE_CODE_OAUTH_TOKEN."
resource: "https://code.claude.com/docs/en/authentication#generate-a-long-lived-token"
tags: [ci, oauth, token, headless]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: "Pro, Max, Ultra, Team or Enterprise plan"
identifiers:
  - "claude setup-token"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "--bare"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "authentication"
    resource: "https://code.claude.com/docs/en/authentication"
    title: "Authentication"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude setup-token` runs the same browser flow as `/login` and prints a one-year OAuth token. It does not save it; you set it as `CLAUDE_CODE_OAUTH_TOKEN` where needed.

# How to use it

```bash
claude setup-token
export CLAUDE_CODE_OAUTH_TOKEN=your-token   # PowerShell: $env:CLAUDE_CODE_OAUTH_TOKEN = "your-token"
```

# Limits and defaults

- Authenticates with the subscription; model requests only. It cannot establish Remote Control sessions or fetch claude.ai connectors; locally configured MCP servers still work.
- Bare mode (`--bare`) does not read `CLAUDE_CODE_OAUTH_TOKEN`; use `ANTHROPIC_API_KEY` or `apiKeyHelper` there.
- `claude setup-token` enforces only `forceLoginMethod`, so it can mint a token for another organization.
