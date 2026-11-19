---
type: "Feature"
title: "UserPromptExpansion hook event"
description: "Fires when a user-typed slash command or MCP prompt expands into a prompt; can block or add context."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, userpromptexpansion, skills, slash-commands]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "UserPromptExpansion"
  - "expansion_type"
  - "command_name"
  - "command_args"
  - "command_source"
  - "slash_command"
  - "mcp_prompt"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a user-typed command expands into a prompt before reaching Claude. Covers the path `PreToolUse` on the `Skill` tool misses: typing `/skillname` directly bypasses PreToolUse. Use to block commands (e.g. `/deploy` without an approval file), inject context for a skill, or log command use.

# How to use it

Matches on `command_name`; empty matcher fires on every prompt-type command. Input adds `expansion_type` (`slash_command` for skill and custom commands, `mcp_prompt` for MCP server prompts), `command_name` (plugin skills look like `my-plugin:example-skill`), `command_args`, `command_source` (e.g. `plugin`), and `prompt`.

| Output field | Description |
| :- | :- |
| `decision` | `"block"` prevents expansion |
| `reason` | Shown to the user on block |
| `additionalContext` | Added to context with the expanded prompt |

Exit 2 shows stderr to the user like `reason`. Supports all five hook types.
