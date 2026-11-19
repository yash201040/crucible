---
type: "Reference"
title: "Configuration flags accepted by claude agents"
description: "Flags that load settings, plugins, MCP servers and directories in agent view and pass through to dispatched sessions."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, flags, mcp, plugins]
kind: "cli_flag"
maturity: "research-preview"
since: "2.1.142"
surfaces: [cli]
requires: ""
identifiers:
  - "--settings"
  - "--setting-sources"
  - "--add-dir"
  - "--plugin-dir"
  - "--mcp-config"
  - "--strict-mcp-config"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

`--settings`, `--setting-sources` and `--plugin-dir` apply to agent view itself; every configuration flag is passed through to dispatched sessions.

| Flag | Effect |
| :- | :- |
| `--settings <file-or-json>` | Override settings for the view and dispatched sessions; a file path must exist or it exits with `Settings file not found` |
| `--setting-sources <sources>` | Load only named settings sources |
| `--add-dir <path>` | Grant access to an extra directory |
| `--plugin-dir <path>` | Load a plugin from a local directory |
| `--mcp-config <file-or-json>` | Load MCP servers from a file or JSON |
| `--strict-mcp-config` | Skip MCP servers from places such as `.mcp.json`; load only those passed with `--mcp-config` |

```bash
claude agents --settings ./ci-settings.json --add-dir ../shared-lib
```

# Limits and defaults

Repeat `--add-dir`, `--plugin-dir`, `--mcp-config` once per value; the space-separated form (`--add-dir a b c`) is not supported. `--settings`, `--setting-sources`, `--plugin-dir` can go before or after `agents`; keep `--add-dir` and `--mcp-config` after `agents` or `claude agents --json` fails with `unknown option`. `--plugin-dir` after `agents` also feeds the view's subagent/skill autocomplete (v2.1.200). `--setting-sources` carries over to backgrounded and dispatched sessions since v2.1.281.
