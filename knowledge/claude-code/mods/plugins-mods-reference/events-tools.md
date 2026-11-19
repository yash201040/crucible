---
type: "Reference"
title: "Events: tools (tool.call, tool.check, tool.describe)"
description: "Tool events fire around each tool call, with the tool.check agentId, ceiling and isReadOnly fields and tool.describe options."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, events, tools, permissions]
kind: "hook"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "tool.call"
  - "tool.check"
  - "tool.describe"
  - "e.agentId"
  - "e.ceiling"
  - "e.isReadOnly"
  - "isDeferred"
  - "breakPromptCache"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks on `turn.step` and `process.spawn` are async generators; others are async functions. Shorthand in tables: `next(e)` passes on unchanged; `next({ ...e, text })` passes a changed copy; an object answers without `next`.

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `tool.call` | a tool is about to run | `next(e)`, `{ deny: reason }`, `{ result }` |
| `tool.check` | Claude Code decides whether the call may run, after `tool.call` and `PreToolUse` hooks; `next(e)` resolves to the decision rules, permission mode and those hooks reached | `next(e)` or `{ decision }` of `allow`, `ask`, `deny` with optional `reason` |
| `tool.describe` | once per tool when its description is first sent; again for an MCP tool when Claude loads it through tool search (`e.description` is the loaded text) | `{ description }`, optionally `isDeferred: true` (behind tool search) or `false` (load upfront); add `breakPromptCache: true` to send a changed description next turn |

# Limits and defaults

On `tool.check`: `e.agentId` is set when a subagent or an in-process agent-team teammate makes the call (absent for main conversation); `e.ceiling` is `ask` for a connector tool the organization set to `ask`, where that setting reaches Claude Code. Both need v2.1.290+. `e.isReadOnly` is `true` when the tool reports read-only, else absent; it is the tool's own report, so read the events guide before approving on it; needs v2.1.304+.
