---
type: "Feature"
title: "hooks setting"
description: "The settings key that registers hooks per event as matcher groups with command, prompt, agent, http or mcp_tool handlers."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, hooks, lifecycle, merge]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "hooks"
  - "matcher"
  - "PreToolUse"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`hooks` (any file, default unset) runs commands, prompts, agents, HTTP requests or MCP tools at lifecycle points such as before a tool call or at session start. Hooks merge across files rather than replacing each other, and hooks from managed settings cannot be removed from other files.

# How to use it

Object keyed by hook event; each value is an array of `{ "matcher", "hooks" }` groups; each handler has `type` of `"command"`, `"prompt"`, `"agent"`, `"http"` or `"mcp_tool"`.

```json
{ "hooks": { "PreToolUse": [ { "matcher": "Bash", "hooks": [ { "type": "command", "command": "~/.claude/hooks/check-bash.sh" } ] } ] } }
```

# Notes

Event list, payloads, matcher patterns and handler fields are in the hooks reference. To turn off see [disableAllHooks](./p2-disable-all-hooks-and-gates.md); to limit see [allowManagedHooksOnly](./p2-allow-managed-hooks-only.md).
