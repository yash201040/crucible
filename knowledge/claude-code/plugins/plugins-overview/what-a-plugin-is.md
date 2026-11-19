---
type: "Concept"
title: "What a plugin is"
description: "A plugin is a directory of skills, agents, hooks, MCP servers and a hooks module that Claude Code installs and loads as one unit."
resource: "https://code.claude.com/docs/en/plugins/overview"
tags: [plugins, components, manifest, packaging]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - ".claude-plugin/plugin.json"
  - "SKILL.md"
  - "hooks/hooks.json"
  - ".mcp.json"
  - "agents/"
  - "/plugin"
  - "--plugin-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-overview"
    resource: "https://code.claude.com/docs/en/plugins/overview"
    title: "Plugins overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin is a directory of components, usually with a manifest at `.claude-plugin/plugin.json` (name, optionally version, description and other metadata). Components: skills (`SKILL.md`, runnable as a command), agents (subagent definitions), hooks (lifecycle commands), a hooks module (hooks as JavaScript functions that can also draw panes and add commands; a plugin with one is called a mod, and some mods are built into Claude Code), and MCP servers. A skill `review` in plugin `my-plugin` runs as `/my-plugin:review`.

# How to use it

Try one with `/plugin` and the **Discover** tab. Load a plugin straight from a folder with `--plugin-dir` while developing (no marketplace needed). Skills, subagents, hooks and MCP servers work standalone (e.g. a skill in `~/.claude/skills/` is available in every project); use a plugin to package several as one unit, share with teammates, install across projects, or publish versioned releases.

# Notes

Not covered here: claude.ai chat and Cowork plugins (separate claude.com docs), publishing an MCP server to Anthropic's directory, and the VS Code extension or JetBrains plugin (those are not Claude Code plugins).
