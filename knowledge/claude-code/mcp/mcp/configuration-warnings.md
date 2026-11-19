---
type: "Reference"
title: "MCP configuration warnings and reserved names"
description: "Warnings for hidden whitespace, duplicate names across scopes, reserved server names and unset ${VAR} references."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, warnings, config, reserved-names]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "workspace"
  - "claude-in-chrome"
  - "computer-use"
  - "Claude Preview"
  - "Claude Browser"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Warnings appear in `claude mcp list` output and in `/mcp`.

| Warning | What is checked | How to clear |
|---|---|---|
| Hidden whitespace | leading/trailing whitespace in `command`, `url`, each `args` entry, values and key names under `env` and `headers`; fields named without echoing values (`Leading or trailing whitespace in: headers.Authorization`) | edit the config; values are not trimmed |
| Same name in several scopes | same name, different endpoints; OAuth sign-ins are stored per endpoint | `claude mcp remove <name> --scope <scope>` |
| Reserved names | built-in servers `workspace`, `claude-in-chrome`, `computer-use`, `Claude Preview`, `Claude Browser` (the last two both name the desktop preview-pane server); configured server is skipped at load; `claude mcp add` rejects with an error | rename |
| Missing environment variable | `${VAR}` with no value and no `:-default`; server still loads with the text unexpanded | set the variable or add a default |

Related: [environment variable expansion](./env-var-expansion-in-mcp-json.md).
