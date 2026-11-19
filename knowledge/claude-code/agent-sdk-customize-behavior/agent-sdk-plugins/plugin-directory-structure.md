---
type: "Reference"
title: "Plugin directory structure"
description: "Layout of a plugin directory the SDK can load: optional manifest, skills, commands, agents, hooks and MCP definitions."
resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
tags: [plugins, layout, manifest, files]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - ".claude-plugin/plugin.json"
  - "skills/"
  - "skills/my-skill/SKILL.md"
  - "commands/"
  - "agents/"
  - "hooks/hooks.json"
  - ".mcp.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-plugins"
    resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
    title: "Plugins in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The directory a `plugins` path points at. The manifest is optional; without it Claude Code auto-discovers components from the layout.

# How to use it

| Path | Holds |
| --- | --- |
| `.claude-plugin/plugin.json` | Plugin manifest (optional) |
| `skills/<name>/SKILL.md` | Agent Skills, invoked autonomously or via `/plugin-name:skill-name` |
| `commands/*.md` | Skills as flat Markdown files |
| `agents/*.md` | Custom agents |
| `hooks/hooks.json` | Event handlers |
| `.mcp.json` | MCP server definitions |

# Notes

The `commands/` directory holds skills as flat Markdown files; the docs say to use `skills/` for new plugins, and both locations are supported. Full plugin authoring is on the separate Plugins pages.
