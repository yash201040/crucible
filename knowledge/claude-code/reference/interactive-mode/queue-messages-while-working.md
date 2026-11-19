---
type: "Feature"
title: "Queue messages while Claude works"
description: "Messages typed during a turn are queued; rules for when they are sent, taken back or moved to a background session."
resource: "https://code.claude.com/docs/en/interactive-mode#queue-messages-while-claude-works"
tags: [queue, messages, interrupt, model, effort]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.275"
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+Enter"
  - "Ctrl+X Ctrl+S"
  - "chat:sendNow"
  - "/model"
  - "/effort"
  - "/fast"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Pressing `Enter` while Claude works queues the message instead of interrupting. Queued entries show in the conversation (gray until Claude starts on them). `!` shell commands and most commands can be queued too, except commands such as `/status` that run immediately.

# How to use it

- Messages queued during tool calls reach Claude once those calls finish, within the same turn; messages left when the turn ends go out in order without a key press.
- Commands and `!` commands wait until the turn ends and run one at a time.
- `Ctrl+Enter` or `Ctrl+X Ctrl+S` (action `chat:sendNow`, v2.1.275+) sends now. Work that can move to the background (shell commands, subagents) is backgrounded and Claude reads the messages in the same turn; otherwise the turn is interrupted. Before v2.1.281 it always interrupted. A queued `!` command ahead of messages makes the key interrupt. In shell mode the key only queues. `Esc` interrupts without submitting the draft and sends what was queued.
- `Up` from the first line takes queued items back into the input (shell commands only when the box is empty and nothing else is queued).
- Settings commands run at once: `/model` applies from the next request in the same turn (after any cache warning); `/effort` applies from the next message you send (queue a message during tool calls to start it mid-turn); `/fast` keeps the turn's setting and applies next turn.
- Pressing `←` to background the session moves queued messages with it; commands, `!` commands and messages with an IDE selection cannot move and block the switch with a `Cannot open agents` notice.

# Limits and defaults

Taking back text while `←` waits cancels the switch; taking it back at the moment the session moves loses it (not sent). Each taken-back message is saved in command history.
