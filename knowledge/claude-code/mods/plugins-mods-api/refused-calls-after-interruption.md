---
type: "Limit"
title: "Refused and dropped mod calls after an interruption"
description: "After a user Stop, calls that start work are refused until the next input; how to detect and retry, and what each call returns."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, interruption, retry, limits]
kind: "limit"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: "Claude Code v2.1.304 or later (except $.prompt.submit and $.command.run)"
identifiers:
  - "the session was stopped and nobody has sent input since"
  - "was removed from the queue before it ran"
  - "$.prompt.submit"
  - "$.command.run"
  - "$.agent.spawn"
  - "$.session.send"
  - "$.tool.call"
  - "turn.complete"
  - "drop"
  - "deny"
  - "isDelivered"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The reason `the session was stopped and nobody has sent input since` means the user stopped a running turn (Esc or Stop). Until the next user input, calls that start new work are refused. Nothing queues or repeats them for you.

# How to use it

Retry from a `turn.complete` hook: keep the call's arguments when its result or error contains `the session was stopped and nobody has sent input since` (refused) or `was removed from the queue before it ran` (dropped from the queue). The doc's example keeps `pendingText` in a top-level variable and a top-level `submitPrompt($, text)` function (validation refuses `$` passed to a function declared inside `register`); `turn.complete` empties `pendingText` then calls it without awaiting. `turn.complete` can fire for the interrupted turn or a subagent's turn before the next input; calls then are refused again.

| Refused call | Result |
| :- | :- |
| `$.prompt.submit` | resolves `{ drop: '<reason>' }`, queues nothing |
| `$.command.run` | rejects; message ends with `<reason>` |
| `$.agent.spawn` | resolves `{ deny: '<reason>' }`, starts no subagent |
| `$.session.send` to a finished subagent | `{ isDelivered: false, reason: 'Agent "<id>" was not resumed: <reason>.' }` (a running subagent still receives it) |
| `$.session.send` to an agent team teammate | `{ isDelivered: false, reason: 'Teammate "<name>" was not messaged: <reason>.' }` |
| `$.tool.call` of Bash with `run_in_background: true`, Monitor, or CronCreate | `{ deny: '<tool> was not run: it starts background work, a schedule or a goal, and <reason>' }` |

In an interactive session the user can see a `type a message to continue` toast.

# Limits and defaults

Work already started before the interruption:

| Work | Until next input |
| :- | :- |
| `$.prompt.submit` still queued | Dropped: `{ drop: 'the prompt was removed from the queue before it ran' }`; resubmit |
| `$.command.run` still queued | Dropped; rejects with `the command was removed from the queue before it ran`; rerun |
| One-time CronCreate job coming due | Starts no turn then; runs after the input |
| Recurring CronCreate job coming due | Loses that run, keeps schedule |
| Monitor events | Monitor keeps running; events raised meanwhile are dropped |
| Subagent resumed with `$.session.send` that finishes | Finish notice waits until after the input |
| Foreground Bash or PowerShell from `$.tool.call` reaching its timeout | Stopped at timeout instead of moving to background; result `isError` with line `Ended instead of moving to the background: plugins' input is held, by a Stop or by the host's limits.`; rerun after input |
