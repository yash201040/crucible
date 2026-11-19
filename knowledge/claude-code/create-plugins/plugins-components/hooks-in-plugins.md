---
type: "Feature"
title: "Hooks in a plugin"
description: "Plugin hooks live in hooks/hooks.json, register when the plugin loads, get plugin env vars, and have MCP-tool matcher naming rules."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, hooks, environment, matcher]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "hooks/hooks.json"
  - "hooks"
  - "modules"
  - "CLAUDE_PLUGIN_ROOT"
  - "CLAUDE_PLUGIN_DATA"
  - "CLAUDE_PLUGIN_OPTION_<KEY>"
  - "PostToolUse"
  - "mcp__plugin_<plugin>_<server>__<tool>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook runs automatically at a lifecycle point: a shell command, HTTP request, MCP tool call, model prompt or subagent. A plugin saves hooks in `hooks/hooks.json` under a top-level `"hooks"` key, in the same shape as `hooks` in `settings.json`, so an existing settings hook can be copied unchanged. Hooks in `hooks/hooks.json` and in the `hooks` manifest key both load.

# How to use it

Example: `{"hooks":{"PostToolUse":[{"matcher":"Write|Edit","hooks":[{"type":"command","command":"\"${CLAUDE_PLUGIN_ROOT}/scripts/format.sh\""}]}]}}`. Make the script executable.

- Hooks register when a session loads the plugin and fire on their events from then on; they do not wait for a plugin skill to be used. Narrow the `matcher` to limit them.
- Environment: every hook process receives `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA`, and `CLAUDE_PLUGIN_OPTION_<KEY>` for each user config value.
- Quoting: with no `args`, `command` runs through a shell, so double-quote the `${CLAUDE_PLUGIN_ROOT}` path. With `args`, each element is one argument with no shell and needs no quoting.
- A plugin's own MCP tool is named `mcp__plugin_<plugin>_<server>__<tool>`; write the full name in the matcher. A matcher on the server name alone never fires.
- A `PostToolUse` hook that exits 0 shows nothing in the transcript; confirm with debug logging.
- JavaScript hook functions: list a module file under a `modules` key in the same `hooks/hooks.json`; the plugin then is a mod (see mods pages).

# Limits and defaults

When another enabled plugin has the same name, only one of the two registers its `hooks/hooks.json` hooks.
