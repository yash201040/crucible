---
type: "Concept"
title: "Message delivery, refusal and usage"
description: "How messages arrive between turns or start a turn, when Claude Code refuses them, and that they count as prompts."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, delivery, permissions, usage]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The receiving Claude reads a message between tool calls in an active turn; an idle session gets a new turn started with the message. A message is plain text: an `@` file or MCP resource mention is seen as written and nothing is attached (Claude can still open the path with its own tools under that session's permissions).

# How to use it

Claude Code refuses a message when: it is over the size cap (refused in the sender); a rapid burst to a session on this machine hit that inbox's limit; the target beyond this machine is listed as unable to receive (refused before leaving this machine); the reply target on this machine fails a safety check such as a symlink.

The receiving session's inbound controls give one of three outcomes: Delivered, Held (set aside until you approve it or a mode or settings change allows it), Refused (dropped).

# Limits and defaults

A delivered message counts toward usage like a typed prompt. The receiver can reply with `SendMessage`. Permission boundaries are per session: Claude is instructed never to ask another session for an action denied or blocked in its own session, and the receiving session's own prompts and rules still apply.
