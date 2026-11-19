---
type: "Reference"
title: "Plugin starter layout"
description: "The directories most plugins start with and what the manifest-less default does."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, layout, manifest]
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
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each component kind goes in a fixed directory under the plugin root (the directory passed to `--plugin-dir`). Add only the ones you use.

| Location | Contents |
| :- | :- |
| `.claude-plugin/plugin.json` | Manifest. Loaded via `--plugin-dir` with no manifest, the plugin is named after its directory |
| `skills/` | One `<name>/SKILL.md` per skill |
| `commands/` | Flat Markdown files, older form of skills; use `skills/` for new plugins |
| `agents/` | One Markdown file per subagent |
| `hooks/hooks.json` | Top-level `"hooks"` key, same shape as `hooks` in a settings file |
| `.mcp.json` | MCP server definitions |

# Notes

Full layout is in the manifest reference (standard layout). See [component locations](../plugins-components/plugin-component-locations.md).
