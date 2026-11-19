---
type: "Feature"
title: "Stopping and detaching loops"
description: "How self-paced and fixed-interval loops are stopped, and how to detach from a background session without stopping one."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [loop, cancel, background-session, wakeup]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: "Detaching with Ctrl+C without stopping the loop needs v2.1.295 or later"
identifiers:
  - "ScheduleWakeup"
  - "stop: true"
  - "Esc"
  - "Ctrl+C"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Self-paced and fixed-interval loops stop differently.

# How to use it

| Loop | How to stop |
| :- | :- |
| Self-paced | While waiting for the next iteration, press `Esc` on an empty prompt, or `Ctrl+C` while Claude is idle (not in a background session you attached to). A `Pending wakeup cancelled` notice confirms. |
| Fixed-interval (e.g. `/loop 5m`) | Ask Claude to cancel it ("cancel the deploy check loop"). `Esc` and `Ctrl+C` do not stop it, nor any task scheduled by asking Claude directly. |

An uncancelled loop ends when seven days elapse.

In self-paced mode Claude can end the loop itself by calling the `ScheduleWakeup` tool with `stop: true`, which cancels the pending wakeup. If an iteration neither reschedules nor stops, Claude Code schedules one fallback wakeup about 20 minutes later and ends the loop if that iteration does not reschedule either.

# Notes

When attached to a background session with Claude idle, press `Ctrl+C` twice on an empty prompt to detach; a waiting self-paced loop keeps running and fires on schedule. To stop it, press `Esc` before detaching.
