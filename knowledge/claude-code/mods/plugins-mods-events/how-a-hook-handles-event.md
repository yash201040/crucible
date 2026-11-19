---
type: "Concept"
title: "How a mod hook handles an event"
description: "A mod hook is a middleware function that can observe, rewrite or answer an event, using the $, e and next arguments."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, hooks, middleware, events]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "on"
  - "next"
  - "$.ui.log"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod hook is an event handler registered with `on(eventName, handler)`. Claude Code fires an event at each point where it is about to act (running a tool, submitting a prompt, sending a model request, starting or ending a session). The hook runs before Claude Code acts. Hooks for one event form a middleware chain; `next(e)` calls the next handler (another mod's hook or, at the end, Claude Code's own behavior) and resolves to the result.

The hook gets three arguments: the mods API as `$`, the event as `e`, and the next handler as `next`.

# How to use it

| Goal | Pattern |
| :- | :- |
| Observe before | do work, `return next(e)` |
| Observe after | `const result = await next(e)`, do work, `return result` |
| Rewrite | `next({ ...e, text: e.text.trim() })` (event is deeply frozen; assigning throws) |
| Change the result | `await next(e)`, return a modified copy |
| Answer | return a result without calling `next`; later mods and Claude Code's behavior do not run, e.g. `return { deny: 'reason' }` |

Each event has its own result shape, listed in the [events reference](../plugins-mods-reference/events-tools.md).

# Notes

`$.ui.log(text)` adds a dim transcript line (shown as `● my-mod: ...`) that Claude does not read. For hook order and failure handling see [order](./hook-order-in-chain.md) and [failures](./hook-failure-catch-handler.md).
