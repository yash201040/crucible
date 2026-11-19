---
type: "Feature"
title: "Mod commands and tools"
description: "A mod registers a user command with $.command.register and a Claude-callable tool with $.tool.register in a session.start hook."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, commands, tools, hooks]
kind: "api"
maturity: "unlabelled"
since: "2.1.293"
surfaces: [cli]
requires: ""
identifiers:
  - "$.command.register"
  - "$.tool.register"
  - "session.start"
  - "command.run"
  - "tool.call"
  - "argumentHint"
  - "immediate"
  - "isTextDisplayOnly"
  - "isDeferred"
  - "inputSchema"
  - "mcp__<plugin>__<tool>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every hook receives the mods API as `$`. Register commands and tools in a `session.start` hook; Claude Code waits for it before the first prompt, so they exist from the first turn.

# How to use it

Command (for the user): `await $.command.register({ name, description, argumentHint })` in `session.start`, then handle `on('command.run', { command: 'standup' }, async ($, e) => ({ text }))`. `e.args` is the text after the command name or `''`. The returned `text` prints in the transcript and Claude reads it. Return `{}` to print nothing. Add `immediate: true` to let the command run while Claude is working. Return `{ text, isTextDisplayOnly: true }` from a hook that does not call `next`, with `immediate` off, to hide the text from Claude (earlier than v2.1.326 Claude can read it).

Tool (for Claude): `await $.tool.register({ name, description, inputSchema })` where `inputSchema` is JSON Schema. Claude sees it as `mcp__<plugin name>__<name>` (e.g. `mcp__my-mod__ticket`). Handle with `on('tool.call', { tool: 'mcp__my-mod__ticket' }, async ($, e) => ({ result }))`; arguments are fields of `e`. Return a result even on failure so Claude learns of it.

# Limits and defaults

- `$.command.register` throws for a name a built-in command uses (`"/focus" refused: it is the built-in /focus`). A throwing hook is skipped and the rest of the `session.start` hook does not run: register commands last or use `try`/`catch`.
- When MCP tool search defers a registered tool, Claude sees only its name; add `isDeferred: false` to load it upfront. Requires v2.1.293 or later (earlier versions ignore it).
