---
type: "Concept"
title: "When to make a plugin"
description: "Standalone .claude/ setups suit one project or person; a plugin adds sharing, multi-project install and versioned releases, with plugin-name prefixes."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, decision, naming, packaging]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/my-plugin:hello"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin is a directory of skills, agents, hooks and MCP servers plus a `plugin.json` manifest, loaded as one unit. Skills, agents, hooks and MCP servers all work standalone; keep that while the setup serves one project or only you. Make a plugin to share with teammates, install in several projects, or publish versioned releases.

# Limits and defaults

Moving a setup into a plugin changes locations (`skills/`, `agents/`, `hooks/hooks.json`, `.mcp.json` under the plugin root) and names: plugin skills and agents get the plugin name as prefix (`/my-plugin:hello`), so two plugins can each provide `hello` without collision.
