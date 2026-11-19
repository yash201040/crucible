---
type: "Feature"
title: "Environment variable expansion in .mcp.json"
description: "${VAR} and ${VAR:-default} in command, args, env, url and headers, empty-string behavior and credential variables read as empty."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, env-vars, secrets, config]
kind: "setting"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli]
requires: ""
identifiers:
  - "${VAR}"
  - "${VAR:-default}"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "AWS_BEARER_TOKEN_BEDROCK"
  - "HTTPS_PROXY"
  - "NPM_TOKEN"
  - "ANTHROPIC_BASE_URL"
  - "--debug-file"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A server's `command`, `args`, `env`, `url` or `headers` may reference environment variables: `${VAR}` or `${VAR:-default}` (default used if unset).

# How to use it

```json
{ "mcpServers": { "api-server": { "type": "http",
  "url": "${API_BASE_URL:-https://api.example.com}/mcp",
  "headers": { "Authorization": "Bearer ${API_KEY}" } } } }
```

# Limits and defaults

- Unset with no default: config still loads, a warning appears in `claude mcp list`, and the `${VAR}` text is used as is.
- Set to an empty string counts as set: `${VAR:-default}` yields empty (the example `url` becomes `/mcp`, reported as `'url' is not a valid URL`). Unset the variable to get the default.
- Credential variables read as empty in a remote server's `url` and `headers` (whether set or not; a `:-default` is ignored): Claude Code's own credentials such as `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN`, cloud provider credentials such as `AWS_BEARER_TOKEN_BEDROCK`, other credentials such as `HTTPS_PROXY` and `NPM_TOKEN`. `Bearer ${ANTHROPIC_AUTH_TOKEN}` sends `Bearer ` and usually gets a `401`. `ANTHROPIC_BASE_URL` still expands unless its value embeds credentials. Names outside the set (such as `API_KEY`) expand; to pass a covered credential, copy it to a variable of your own name. A debug-log line `never expanded toward a remote server` names a covered variable you had set (read it with `claude --debug-file /tmp/claude-debug.log`).
- Display: local/project/user servers show `${VAR}` by name, not resolved value, in `/mcp` detail (v2.1.268 or later), `claude mcp list` and `claude mcp get`; managed servers show the URL's host only.
