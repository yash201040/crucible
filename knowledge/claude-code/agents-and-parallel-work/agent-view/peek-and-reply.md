---
type: "Feature"
title: "Peek panel and replies"
description: "Space opens a peek panel to read a session's latest output and reply without attaching; reply routing depends on state."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, peek, reply, queue]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Space"
  - "/stop"
  - "/model"
  - "/effort"
  - "/rename"
  - "/usage"
  - "claude --bg --safe-mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Space` on a row opens the peek panel: the sentence the row truncates (exact question if waiting, result if finished, full status if working), linked pull requests, and a `waiting 3m` line (time waiting, distinct from the row's age) or `safe mode · customizations are off` for sessions started with `claude --bg --safe-mode`.

# How to use it

Type a reply, `Enter` sends; prefix `!` to send a Bash command. `↑`/`↓` peek adjacent sessions, `→` attaches.

- Working session: `/model`, `/effort`, `/rename`, `/usage` run immediately; other replies join the message queue without interrupting; other commands wait for turn end.
- Reply exactly `/stop`: stops the session at once.
- Shell job: reply (including `/stop`) goes to the command's terminal as typed input.
- Waiting on predefined choices: press the choice number with empty input, then `Enter`, or type your own. Free question: type an answer; `Tab` fills a suggested reply.
- Permission prompt, sandbox prompt or MCP elicitation: replying does not answer it; the message waits in the queue. Attach with `→` to answer.

Hook problems: when a `PermissionRequest` or `PreToolUse` hook returns unvalidatable output, the row shows the hook event and `hook output invalid:` with the error; other hook failures say the hook failed. The session still waits.

# Limits and defaults

Undeliverable reply: the error says whether it was saved. Replies starting `!` or `/` are never saved; a saved one is sent as the next prompt on restart. Voice dictation (hold mode) works in the reply and dispatch inputs.
