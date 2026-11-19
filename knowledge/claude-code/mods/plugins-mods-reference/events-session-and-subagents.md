---
type: "Reference"
title: "Events: session and subagents (agent.spawn, session.*)"
description: "Session lifecycle and messaging events plus agent.offer and agent.spawn, including resumed subagent runs and refusing them."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, subagents, sessions, events]
kind: "hook"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "session.start"
  - "session.end"
  - "session.compact"
  - "session.receive"
  - "session.send"
  - "session.append"
  - "session.attach"
  - "session.detach"
  - "session.measure"
  - "agent.offer"
  - "agent.spawn"
  - "e.isTeammate"
  - "e.resume"
  - "SendMessage"
  - "{ isOffered: false }"
  - "{ skip: reason }"
  - "{ consumed: reason }"
  - "{ isDelivered: false, reason }"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `session.start` | once per loaded mod before first prompt, and after a reload of that mod; not after `/clear`, `/resume`, `/branch` | `next(e)` |
| `session.end` | session ends or `/clear`, `/resume`, `/branch` runs; `e.reason` is `clear`, `resume`, `logout`, `prompt_input_exit`, `other` (`/branch` reports `resume`) | `next(e)` |
| `session.compact` | conversation about to be compacted | `{ skip: reason }` |
| `session.receive`, `session.send` | a message arrives from, or is about to go to, another agent or session | `{ consumed: reason }` for receive; `{ isDelivered: false, reason }` for send |
| `session.append` | per row the conversation keeps (prompt, response block, tool result, notice), before storing | `next({ ...e, message })` with changed `message.content` (text blocks or a `tool_result` block's `content`) |
| `session.attach`, `session.detach` | another app connects/disconnects | `next(e)` |
| `session.measure` | after each turn, and when a plan limit's percent used changes | `next(e)` |
| `agent.offer` | a subagent type is offered to Claude | `{ isOffered: false }` to withhold it |
| `agent.spawn` | a subagent or agent-team teammate is about to start, or a finished/stopped subagent is about to run again | `next({ ...e, model })` to choose the model of a starting one, or `{ deny: reason }` |

# Limits and defaults

- For a teammate `e.isTeammate` is `true`. For a resumed run (e.g. Claude sends the subagent a message with `SendMessage`) `e.resume` is `{ agentId }`; skip those when counting subagents.
- `{ deny: reason }` refuses a resumed run: it does not start and the subagent stays as it was; a `SendMessage` call reads `a plugin declined the resume:` plus the reason. A changed event (e.g. different `model`) passed to `next` for a resumed run is ignored.
- The resumed-run event needs v2.1.299+; before that the hook did not run on resume, so match `SendMessage` in a `tool.call` hook to refuse it.
