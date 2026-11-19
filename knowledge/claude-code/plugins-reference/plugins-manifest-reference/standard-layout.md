---
type: "Reference"
title: "Plugin standard layout"
description: "Default locations of each plugin component type and the bin/ directory that puts executables on the Bash tool PATH."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, layout, directories, bin]
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
  - "output-styles/"
  - "workflows/"
  - "themes/"
  - "monitors/monitors.json"
  - "bin/"
  - "SKILL.md"
  - "CLAUDE.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each component type has a default location under the plugin root, used when the manifest does not point elsewhere.

# How to use it

| Component | Default location | Contents |
| :- | :- | :- |
| Manifest | `.claude-plugin/plugin.json` | Metadata and configuration; optional |
| Skills | `skills/` | One `<name>/SKILL.md` per skill. A plugin with `SKILL.md` at its root, no `skills/` and no `skills` key loads as a single skill |
| Commands | `commands/` | Flat Markdown command files; prefer `skills/` for new plugins |
| Agents | `agents/` | Agent Markdown files; subfolders are part of the agent name |
| Hooks | `hooks/hooks.json` | Hook configuration |
| MCP servers | `.mcp.json` | MCP definitions |
| LSP servers | `.lsp.json` | LSP configurations |
| Output styles | `output-styles/` | Output style Markdown |
| Workflows | `workflows/` | Workflow `.js` files |
| Themes | `themes/` | Theme JSON |
| Monitors | `monitors/monitors.json` | The monitors array |
| Executables | `bin/` | On the Bash tool's `PATH` while the plugin is enabled, so Claude runs them as bare commands. claude.ai and Cowork do not install a plugin that has this directory, including via claude.ai organization settings |

# Limits and defaults

A `CLAUDE.md` at the plugin root is not loaded as context and `claude plugin validate` warns; put instructions meant for Claude's context in a skill.
