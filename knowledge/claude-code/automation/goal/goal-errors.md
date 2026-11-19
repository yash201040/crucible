---
type: "Reference"
title: "Goal behavior on turn errors"
description: "Which failures clear a goal, which retry or pause it, and the v2.1.269 interactive notices."
resource: "https://code.claude.com/docs/en/goal"
tags: [goal, errors, retry, unattended]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli]
requires: "Retry and pause notices need an interactive session on v2.1.269+"
identifiers:
  - "CLAUDE_CODE_GOAL_CHECKIN_MINUTES"
  - "Goal cleared after an unrecoverable error"
  - "Run /goal again to continue"
  - "Goal still active"
  - "Goal paused"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "goal"
    resource: "https://code.claude.com/docs/en/goal"
    title: "Keep Claude working toward a goal"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a turn fails, Claude Code clears the goal if the error is one you have to fix; after any other error the goal stays set.

# How to use it

| Outcome | Failures | Notice |
| --- | --- | --- |
| Goal cleared | Authentication failure when Claude Code manages its own credentials (not when a host such as the desktop app or a cloud session restores access); disk too full to renew the claude.ai login (`(disk full)`); exhausted credit balance; context overflow auto-compaction could not clear; model not available | Starts `Goal cleared after an unrecoverable error`, ends `Run /goal again to continue` |
| Retry | Failures that tend to clear (overloaded server, dropped connection) | `Goal still active` with the wait; after three automatic retries the goal pauses |
| Pause | Failures a retry would repeat (API rate limit, claude.ai usage limit, a hook that ended the turn) | `Goal paused` naming the cause; if the session waits to continue when a usage limit resets, work resumes then |

Send a message to start the next turn immediately. Set `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` to `0` to turn off automatic retries (and check-ins).

# Limits and defaults

Retry and pause notices are interactive-session behavior from v2.1.269. After a cleared goal, fix the cause then set it again with `/goal <condition>`.
