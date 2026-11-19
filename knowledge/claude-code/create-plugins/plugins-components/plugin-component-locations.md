---
type: "Reference"
title: "Plugin component default locations"
description: "Where each plugin component lives by default, how it is named for the user, and which manifest key replaces or adds to the folder."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, components, layout, manifest]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude-plugin/plugin.json"
  - "skills/"
  - "commands/"
  - "agents/"
  - "hooks/hooks.json"
  - ".mcp.json"
  - ".lsp.json"
  - "monitors/monitors.json"
  - "output-styles/"
  - "themes/"
  - "workflows/"
  - "bin/"
  - "/reload-plugins"
  - "claude plugin validate ."
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin is built from components. Each has a default folder in the plugin, an optional manifest key in `.claude-plugin/plugin.json` that replaces or adds to that folder, and a name the user sees. The `plugin.json` manifest needs only `name`; `description` is the text shown in `/plugin` and `version` pins users to that version until changed. Components are all optional.

# How to use it

After adding a component, run `/reload-plugins` in a running session or start a new one. To check a component file before loading, run `claude plugin validate .` from the plugin directory.

| Component | Default location | Name the user sees | Manifest key |
| :- | :- | :- | :- |
| Skill | `skills/<dir>/SKILL.md` | `/<plugin>:<dir>` | `skills` (adds to scan) |
| Command | `commands/<file>.md` | `/<plugin>:<file>` | `commands` (replaces scan) |
| Subagent | `agents/<file>.md` | `<plugin>:<name>`, `@agent-<plugin>:<name>` | `agents` (replaces scan) |
| Hook | `hooks/hooks.json` | none | `hooks` (both load) |
| Monitor | `monitors/monitors.json` | none | `experimental.monitors` |
| Output style | `output-styles/<name>.md` | `<plugin>:<name>` in `/output-style` | `outputStyles` |
| Theme | `themes/<slug>.json` | file `name` in `/theme` | `experimental.themes` |
| Workflow | `workflows/*.js` | `/<plugin>:<name>` (e.g. `/my-plugin:audit-routes`) | none stated |
| Executable | `bin/` | bare command on `PATH` | none |
| MCP server | `.mcp.json` | `plugin:<plugin>:<server>` | `mcpServers` |
| LSP server | `.lsp.json` | none | `lspServers` |

# Notes

- The example plugin `my-plugin` shows each file as the smallest valid example.
- A workflow file is a `.js` with an exported `meta` block (`name`, `description`) and a script body that orchestrates several subagents using calls such as `agent(...)` and `pipeline(...)`.
- The `scripts/` folder name is only a convention; a hook points at the file by path.
- Claude.ai and Cowork load a different component set; see the component support table on claude.com.
