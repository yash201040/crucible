---
type: "Feature"
title: "Import servers from Claude Desktop"
description: "claude mcp add-from-claude-desktop imports selected servers on macOS and WSL, with name restrictions."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, import, desktop, migration]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "macOS or Windows Subsystem for Linux (WSL)"
identifiers:
  - "claude mcp add-from-claude-desktop"
  - "claude_desktop_config.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Run `claude mcp add-from-claude-desktop`, pick servers in the interactive dialog, then check with `claude mcp list`. Add `--scope user` for user config.

# Limits and defaults

Works only on macOS and WSL, reading Claude Desktop's standard config file. Names may contain only letters, numbers, hyphens and underscores; others are reported and skipped while the rest import. Same-named existing servers get a numeric suffix (`server_1`).
