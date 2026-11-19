---
type: "Reference"
title: "Agent, MCP, plugin and integration flags"
description: "Flags that load subagents, MCP servers, plugins, channels, Chrome and IDE integration, or disable skills."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [subagents, mcp, plugins, channels, integrations]
kind: "cli_flag"
maturity: "research-preview"
since: "2.1.281"
surfaces: [cli]
requires: "channels need Anthropic authentication through claude.ai or a Console API key"
identifiers:
  - "--agent"
  - "--agents"
  - "--mcp-config"
  - "--strict-mcp-config"
  - "MCP_TIMEOUT"
  - "--plugin-dir"
  - "--plugin-url"
  - "--disable-slash-commands"
  - "--channels"
  - "--dangerously-load-development-channels"
  - "--chrome"
  - "--no-chrome"
  - "--ide"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flags that add or restrict extensions per session. Only `--channels` carries the label research preview.

# How to use it

| Flag | Version | What it does |
| :- | :- | :- |
| `--agent` | | Agent for the session; overrides the `agent` setting |
| `--agents` | validation v2.1.242+; file form v2.1.281+ | Define subagents as JSON (fields per CLI-defined subagents). With `--print` the value can be a path to a JSON file. Invalid values exit at startup |
| `--mcp-config` | wait v2.1.221+ | Load MCP servers from JSON files or strings. With `-p`, waits for pending servers up to `MCP_TIMEOUT` (30 s default) before turn one; servers with a cached tool list skip the wait |
| `--strict-mcp-config` | | Ignore MCP servers from `.mcp.json`, `~/.claude.json` or plugins; load only `--mcp-config` |
| `--plugin-dir` | folder of plugins v2.1.265+ | Load a plugin directory or `.zip` for this session; repeat the flag per path |
| `--plugin-url` | | Fetch a plugin `.zip` from a URL for this session; repeat or space-separate |
| `--disable-slash-commands` | | Disable all skills and commands for the session |
| `--channels` | research preview | Space-separated `plugin:<name>@<marketplace>` MCP servers whose channel notifications to listen for |
| `--dangerously-load-development-channels` | | Allow channels off the approved allowlist (`plugin:<name>@<marketplace>`, `server:<name>`); prompts for confirmation so it works only interactively; ignored with `-p` |
| `--chrome` / `--no-chrome` | | Enable or disable Chrome browser integration |
| `--ide` | | Auto-connect to the IDE at startup when exactly one valid IDE is available |
