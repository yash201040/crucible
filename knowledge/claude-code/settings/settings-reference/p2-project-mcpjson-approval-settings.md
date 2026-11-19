---
type: "Reference"
title: "Project .mcp.json approval settings"
description: "Settings that approve or reject MCP servers from a project's .mcp.json file without prompting."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, mcp, approval, trust]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "disabledMcpjsonServers"
  - "enableAllProjectMcpServers"
  - "enabledMcpjsonServers"
  - ".mcp.json"
  - ".claude/settings.local.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three any-file keys controlling approval of servers from `.mcp.json`. The approval dialog writes them to `.claude/settings.local.json`.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `disabledMcpjsonServers` | array of server names | unset | Reject servers so they never connect or prompt. A rejection in any file applies, including the checked-in project file. `claude mcp get <name>` shows `✘ Rejected (see disabledMcpjsonServers in settings)`. Beats the two keys below |
| `enableAllProjectMcpServers` | Boolean | unset (ask per server) | `true` approves every project `.mcp.json` server without prompt. In a trusted folder a higher-precedence `false` overrides a lower `true`; in an untrusted folder a `true` in any honored file suffices |
| `enabledMcpjsonServers` | array of server names | unset | Approve named servers without asking |

# Limits and defaults

In a folder whose trust dialog is not accepted, `enableAllProjectMcpServers` and `enabledMcpjsonServers` are honored from user settings, managed settings and `--settings` and ignored in the shared project file, in the session and for `claude mcp list` and `claude mcp get`.
