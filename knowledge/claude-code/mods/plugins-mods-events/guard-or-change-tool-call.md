---
type: "Feature"
title: "Guard or change a tool call (tool.call)"
description: "A tool.call hook can refuse, change, retry, answer or withhold the result of any tool call, including subagent and MCP calls."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, tool-call, deny, permissions]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "tool.call"
  - "{ deny: reason }"
  - "{ result }"
  - "isError"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`tool.call` fires when Claude Code is about to run a tool, including calls made by a subagent and calls to MCP tools. `e.tool` is the tool name; its arguments are fields of `e` (e.g. `e.command` for Bash). Calling `next(e)` runs the permission check and then the tool.

# How to use it

| Intent | How |
| :- | :- |
| Refuse | return `{ deny: 'text' }` without `next`; no command runs, no permission prompt; Claude reads the text as the tool result |
| Change the call | pass changed arguments to `next` |
| Retry | call `next(e)` again (e.g. after seeing `isError`) |
| Answer yourself | return `{ result }` without `next`; for built-in tools use that tool's own result shape; no prompt, tool does not run |
| Withhold result | `await next(e)` then return `{ deny: reason }`; Claude reads the reason instead; undoes nothing the tool did; a note like `Bash ran, and a plugin withheld its result:` precedes it when it succeeded |

After `await next(e)`, a refused call comes back as `{ deny }` and a failed one has `isError` set.

# Limits and defaults

- A hook that throws or times out is skipped and the call proceeds; add a `.catch` handler to fail closed (see [failures](./hook-failure-catch-handler.md)).
- Managed-settings hooks (`PreToolUse`) run before any mod's `tool.call` hook; if a managed hook blocks, no mod hook runs for that call.
