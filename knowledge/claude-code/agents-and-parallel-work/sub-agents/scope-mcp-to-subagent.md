---
type: "Feature"
title: "Scoping MCP servers to a subagent"
description: "The mcpServers field gives a subagent its own inline or referenced MCP servers, subject to folder trust and managed MCP policy."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, mcp, trust, security]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "mcpServers"
  - "--strict-mcp-config"
  - "--bare"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "hasTrustDialogAccepted"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each `mcpServers` entry is either an inline definition (server name as key, full MCP config as value; types `stdio`, `http`, `sse`, `ws`) or a string naming an already-configured server. Inline servers connect when the subagent starts and disconnect when it finishes; string references share the parent's connection. Defining a server inline keeps its tool descriptions out of the main conversation context.

# How to use it

```yaml
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - github
```

Applies both when the agent runs as a subagent (Agent tool or @-mention) and as the main session via `--agent` or the `agent` setting (inline servers then connect at startup).

# Limits and defaults

- Main-session restrictions also cover these servers: `--strict-mcp-config`, `--bare`, managed MCP configuration, `allowedMcpServers` / `deniedMcpServers`. Blocked servers are skipped with a warning. `--strict-mcp-config` does not filter servers passed via `--agents` or the SDK `agents` option.
- Trust: inline servers in a project `.claude/agents/` (or `--add-dir` directory's) agent file load only after you trust that folder; a parent folder's trust and the automatic trust of `-p`/SDK sessions do not count. Until then they are skipped and the exact `projects["<path>"].hasTrustDialogAccepted` key for `~/.claude.json` is written to the debug log. Before v2.1.238 no trust check was made.
- Loaded without a trust check: name references to configured servers; inline servers from `~/.claude/agents/`, `--agents`/SDK `agents`, or managed settings.
- In `/mcp` a remote server used before can show `cached` status and connects on first tool call.
