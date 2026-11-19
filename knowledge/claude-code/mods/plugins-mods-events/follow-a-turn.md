---
type: "Feature"
title: "Follow a turn: turn.start, turn.step, turn.complete"
description: "Turn events expose each model request's token usage, allow routing a request to another model, and report the turn's final answer and totals."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, turn, usage, model-routing]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "turn.start"
  - "turn.step"
  - "turn.complete"
  - "e.turnId"
  - "e.agentId"
  - "e.isAborted"
  - "e.answer"
  - "e.durationMs"
  - "e.usage"
  - "result.usage"
  - "result.serverToolUses"
  - "cache_read_input_tokens"
  - "cache_creation_input_tokens"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A turn is everything Claude does for one prompt.

| Event | Fires | A hook can |
| :- | :- | :- |
| `turn.start` | turn begins | observe; `e.turnId` identifies the turn |
| `turn.step` | before one request to the model (a turn with tool calls has several); `e.agentId` set for a subagent's request | read token usage, reroute with `next({ ...e, model })`, or answer without calling the model |
| `turn.complete` | turn ended, including interrupted (`e.isAborted` true); `e.answer`, `e.durationMs`, `e.usage`; fires for a subagent turn with `e.agentId` | observe, or return `{ text: '...' }` to show a line under the answer |

# How to use it

`turn.step` hooks are async generators: `on('turn.step', async function* ($, e, next) { const result = yield* next(e); ... return result })`. `result.usage` has `input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation_input_tokens` and the answering `model`. The hook also runs for subagent requests, so check `e.agentId` for main-only.

`result.serverToolUses` lists tool calls the API ran itself (e.g. the advisor tool); no `tool.call`/`tool.check` fires for them; absent when none; requires v2.1.290 or later.

Send a request to another model: `yield* next({ ...e, model: 'haiku' })`.

# Limits and defaults

If a `turn.step` request fails with a model error when `model` is an alias such as `haiku`, update to v2.1.309 or later or use a full model id; before v2.1.309 an alias went out as written.
