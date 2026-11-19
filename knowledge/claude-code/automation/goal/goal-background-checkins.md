---
type: "Feature"
title: "Background work and goal check-ins"
description: "Evaluation is deferred while subagents or background commands run; timed check-ins with backoff and an idle-check-in cap."
resource: "https://code.claude.com/docs/en/goal"
tags: [goal, background-tasks, check-ins, subagents]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli, headless]
requires: "Check-ins v2.1.234+; idle check-ins v2.1.236+"
identifiers:
  - "CLAUDE_CODE_GOAL_CHECKIN_MINUTES"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "goal"
    resource: "https://code.claude.com/docs/en/goal"
    title: "Keep Claude working toward a goal"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If a subagent or background shell command is still running when a turn ends, Claude Code skips evaluation for that turn and evaluates at the end of the next turn that finishes with no background work. When the work finishes, its result arrives as a new turn.

# How to use it

After background work has kept the goal waiting for 30 minutes, a check-in is due: Claude Code lists running tasks and asks Claude to read their output, keep waiting if progressing, and fix or stop stuck ones. Each later check-in waits twice as long, up to four times the first interval (default: 30 minutes, then 1 hour, then every 2 hours). Set `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` to change the first interval (later ones scale); `0` turns off check-ins and automatic retries.

Delivery:
- At turn end: at the end of the next turn that finishes with the work still running. In non-interactive sessions (`-p`) this is the only way.
- While idle (interactive only): Claude Code starts a turn itself; if background work stopped without a result it asks Claude to continue. At most three idle check-ins per goal between your prompts; the third says they pause until you send a prompt.

# Limits and defaults

Version notes: idle check-ins uncapped before v2.1.246; before v2.1.239 only idle check-ins backed off (turn-end check-ins recurred at the first interval).
