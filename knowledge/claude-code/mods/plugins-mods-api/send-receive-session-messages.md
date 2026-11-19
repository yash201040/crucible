---
type: "Feature"
title: "Messages between sessions from a mod"
description: "$.session.send delivers text to another session, subagent or teammate; session.receive and session.send events let a mod observe messages."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, messaging, subagents, agent-teams]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.session.send"
  - "session.receive"
  - "session.send"
  - "$.agent.list"
  - "sessionId"
  - "agentId"
  - "isDelivered"
  - "consumed"
  - "e.origin.kind"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod can send a plain-text message to another of your sessions, a subagent of this session, or a teammate in its agent team, and observe messages arriving and leaving. `$.session.send({ to, text })` makes the same delivery as the SendMessage tool.

# How to use it

`to` is `{ sessionId }` (another session), `{ agentId }` (subagent or teammate, id from `$.agent.list()`), or the string address a received message came from. It resolves `{ isDelivered: true }` once queued, otherwise `{ isDelivered: false, reason }`.

| Event | Fires when | Useful fields |
| :- | :- | :- |
| `session.receive` | A message arrives, before Claude reads it | `e.text`, `e.origin.kind` (`peer`, `peer-send-message`, `task-notification`, `scheduled-trigger`); return `{ consumed: reason }` to keep it from Claude |
| `session.send` | A message is about to leave (SendMessage tool or a mod) | `e.to`, `e.text`, `e.origin.kind` (`model` or `plugin`) |

Return `next(e)` from both to pass unchanged.

# Limits and defaults

A session set to refuse inbound messages refuses before `session.receive` fires, so hooks never see it. A message held for approval reaches the hook first. The hook's `next(e)` rejects when not delivered. The sender's name on a received message is whatever the sender wrote; do not base decisions on it.
