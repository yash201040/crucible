---
type: "Feature"
title: "MCP servers in a plugin"
description: "Declare MCP servers in .mcp.json or the mcpServers key, with naming, substitution, reload behavior, and packaged MCPB bundles."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, mcp, mcpb, naming]
kind: "file"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - ".mcp.json"
  - "mcpServers"
  - "plugin:<plugin>:<server>"
  - "mcp__plugin_<plugin>_<server>__<tool>"
  - "--config <server>.<key>=<value>"
  - ".mcpb"
  - ".dxt"
  - "user_config"
  - "claude plugin install"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An MCP server gives Claude tools from an external system. Declare it in `.mcp.json` at the plugin root, in the same shape as a project `.mcp.json` (the `mcpServers` wrapper may be omitted). The `mcpServers` manifest key takes an inline map, a path to a JSON file, or an array of those; a manifest server with the same name as one in `.mcp.json` replaces it.

# How to use it

- Server name in `/mcp`: `plugin:<plugin>:<server>`; use the same form in an `mcp_tool` hook.
- Tool name: `mcp__plugin_<plugin>_<server>__<tool>`, used in permission rules and hook matchers.
- `${CLAUDE_PLUGIN_ROOT}` and other path variables are substituted in `command`, `args`, `env`.
- On `/reload-plugins`, an unchanged server keeps its connection, a changed one reconnects, a removed one disconnects.
- Packaged server: `mcpServers` may point to an MCPB file (`.mcpb` or older `.dxt`), as a path inside the plugin or an `https://` URL; the server takes the bundle manifest's `name`. A bundle `user_config` required setting with no saved value stops the server and the `/plugin` Errors tab shows `Bundled MCP server "<name>" was not started: it needs configuration`. Users set values in `/plugin` (Installed tab, Configure) or at install with `claude plugin install --config <server>.<key>=<value>` (v2.1.285+, bundles packaged inside the plugin only).

# Limits and defaults

- `claude plugin validate` checks `.mcp.json` and reports entries Claude Code would drop at load as errors (v2.1.281 or later).
- A local stdio server runs in Claude Code and in Cowork sessions on the user's machine but not on claude.ai; reference a remote `https://` server to reach claude.ai (offered as a connector).
