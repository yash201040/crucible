---
type: "Feature"
title: "Notice when another session goes idle"
description: "SendMessage notify_when_idle subscribes to one notice when a local session next goes idle or exits."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, idle, notification, subscription]
kind: "tool"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli]
requires: "v2.1.236+ in both sessions; target on this machine"
identifiers:
  - "notify_when_idle"
  - "SendMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude can ask one of your sessions on this machine to send back one notice when it next goes idle (finished a turn with nothing queued) or exits. Example prompt: `Tell me when the migration session finishes what it's working on`. Claude subscribes via the `notify_when_idle` input of `SendMessage`, on its own or attached to a message. On its own it starts no turn and spends no tokens in the watched session, and sends the notice at once if that session is already idle. Attached to a message, the message is delivered first and the notice later.

# How to use it

The watched session shows a line saying another process asked to be told when it is next idle. The asking session shows a line naming the watched session, possibly with the finish time and a one-line status; if idle it starts a new turn with the notice.

# Limits and defaults

- No notice within 12 hours: the subscription is dropped and Claude is told.
- `crossSessionInbound` `refuse` on either side: nothing arrives (the watched session drops the request silently, so it expires unanswered after 12 hours; an asking session never subscribes). `hold` on either side: the watched session omits the status line; the asking session shows the notice in the transcript without delivering it to Claude.
- Only the Claude in your main conversation can subscribe, and only to your sessions on this machine. Any other target (teammate, subagent, session beyond this machine) makes Claude Code refuse the whole call including any attached message.
