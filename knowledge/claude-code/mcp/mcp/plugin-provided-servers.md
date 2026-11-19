---
type: "Feature"
title: "Plugin-provided MCP servers"
description: "Plugins bundle MCP servers in .mcp.json or plugin.json; lifecycle, path placeholders and the mcp__plugin_ tool-name form."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, plugins, naming, lifecycle]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "${CLAUDE_PLUGIN_ROOT}"
  - "${CLAUDE_PLUGIN_DATA}"
  - "${CLAUDE_PROJECT_DIR}"
  - "plugin.json"
  - ".mcp.json"
  - "mcp__plugin_<plugin-name>_<server-name>__<tool-name>"
  - "plugin:<plugin-name>:<server-name>"
  - "/reload-plugins"
  - "/cd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Plugins define MCP servers in `.mcp.json` at the plugin root or inline under `mcpServers` in `plugin.json`. Enabling the plugin starts them; add or remove them by installing or uninstalling the plugin, not via `/mcp` (you can toggle one off in `/mcp`).

# How to use it

- Lifecycle: connected at startup for enabled plugins (remote ones can show the `cached` status; a stdio plugin server that failed less than 15 minutes ago is skipped). Enabling or disabling mid-session connects or disconnects at apply time; in a session without an interactive terminal `/reload-plugins` does not connect or disconnect plugin MCP servers (next session). Reload keeps live connections of unchanged servers, also when the Agent SDK replaces the server list without naming them. `/cd` (v2.1.246 or later) connects servers of plugins the new directory enables and disconnects those no longer enabled. In cloud sessions a call to an unconnected plugin server starts it on demand.
- Placeholders: `${CLAUDE_PLUGIN_ROOT}` (install directory), `${CLAUDE_PLUGIN_DATA}` (persistent state directory), `${CLAUDE_PROJECT_DIR}` (project root), substituted in stdio `command`, `args`, `env` and in http/sse/ws `url`, `headers`, `headersHelper`.
- Tool names: `mcp__plugin_<plugin-name>_<server-name>__<tool-name>` with characters outside `A-Z a-z 0-9 _ -` replaced by `_`, for example `mcp__plugin_my-plugin_database-tools__query`. Use this in permission rules, a skill's `allowed-tools`, a subagent's `tools` field and hook matchers; a matcher on the bare key such as `mcp__database-tools__.*` never fires. The server registers as `plugin:<plugin-name>:<server-name>` (use it for an `mcp_tool` hook's `server` field).
- `claude mcp get` redacts plugin stdio values (`Command: stdio`, empty `Args:`, `NAME=[REDACTED]`) and WebSocket (`URL: ws`, headers `[REDACTED]`); read the plugin's `.mcp.json` or `plugin.json` on disk.
