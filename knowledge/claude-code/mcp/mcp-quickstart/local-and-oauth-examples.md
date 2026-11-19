---
type: "Guide"
title: "Local stdio and OAuth server examples"
description: "Playwright as a stdio server via npx, Sentry as an OAuth server, and a hand-written .mcp.json with approval."
resource: "https://code.claude.com/docs/en/mcp-quickstart"
tags: [mcp, quickstart, stdio, oauth]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Node.js 18 or later for the Playwright example"
identifiers:
  - "claude mcp add playwright -- npx -y @playwright/mcp@latest"
  - "claude mcp add --transport http sentry https://mcp.sentry.dev/mcp"
  - "--browser"
  - "--header"
  - "type"
  - "command"
  - "args"
  - "url"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp-quickstart"
    resource: "https://code.claude.com/docs/en/mcp-quickstart"
    title: "Connect to MCP servers"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

- Local server: `claude mcp add playwright -- npx -y @playwright/mcp@latest`. No `--transport` (stdio default), everything after `--` is the start command, `-y` skips npx prompts. Playwright drives the installed Chrome; append `--browser firefox` after `@playwright/mcp@latest` for another browser. The `Added` message only means the entry was saved: the first `claude mcp list` may show `✘ Failed to connect` while `npx` downloads, so retry.
- OAuth server: `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` shows `! Needs authentication` (expected); in a session run `/mcp`, select `sentry`, Enter, `Authenticate`, approve in the browser. Servers using a static token take `--header "Authorization: Bearer <token>"` at add time.
- Hand-written `.mcp.json` in the project root, same JSON for all scopes: HTTP entry `{"type":"http","url":"https://code.claude.com/docs/mcp"}`, stdio entry `{"type":"stdio","command":"npx","args":["-y","@playwright/mcp@latest"]}` under `mcpServers`. Claude Code reads `.mcp.json` at session start. The first time it sees a project-scoped server it asks for approval (so a cloned repo cannot launch processes without consent); `claude mcp reset-project-choices` plus a restart shows the prompt again.
