---
type: "Feature"
title: "/goal completion condition"
description: "Set a completion condition; Claude keeps taking turns until an evaluator model judges it met or impossible."
resource: "https://code.claude.com/docs/en/goal"
tags: [goal, autonomy, loops, stop-hook]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, desktop]
requires: "Workspace trust as for hooks; unavailable if disableAllHooks is true or allowManagedHooksOnly is set"
identifiers:
  - "/goal"
  - "/goal clear"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "goal"
    resource: "https://code.claude.com/docs/en/goal"
    title: "Keep Claude working toward a goal"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/goal <condition>` sets a completion condition and Claude keeps working without a prompt per step. After each turn a model checks whether the condition holds; if not, another turn starts. The goal clears when met, when judged impossible, or when a turn fails on an error you must fix. One goal per session; a new one replaces the old. Setting a goal starts a turn immediately with the condition as directive; a `◎ /goal active` indicator shows elapsed time. A goal does not change the permission mode: run it in auto mode for unattended turns (in Manual mode Claude still asks).

# How to use it

| Command | Effect |
| --- | --- |
| `/goal <condition>` | Set (condition up to 4,000 characters) |
| `/goal` | Status: condition, running time, turns evaluated, token spend, latest reason (turn count and reason appear after first evaluation); if achieved earlier, shows that condition with duration, turns, tokens |
| `/goal clear` | Remove; prints `Goal cleared:` plus condition, or `No goal set`. Aliases `stop`, `off`, `reset`, `none`, `cancel` |

`/clear` also removes an active goal. Each verdict appears in the transcript; Ctrl+O shows the reason.

Writing a condition: the evaluator does not run commands or read files, so state something Claude's output can demonstrate: one measurable end state, a stated check (such as `npm test` exits 0), and constraints. To bound a run, include a clause like `or stop after 20 turns`.

# Limits and defaults

- Resume: a still-active goal is restored on `--continue`, `--resume` (ID, name or transcript path) and the session picker (the picker route was missing before v2.1.239). The condition carries over; turn count, timer and token baseline reset. Achieved or cleared goals are not restored.
- Non-interactive: `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"` runs the loop to completion in one invocation. Default text output prints only at the end, so add `--output-format stream-json --verbose`. Ctrl+C stops it. Also works in the desktop app and Remote Control.

# Notes

Compared with `/loop` (next turn on a time interval) and a Stop hook (your script or prompt decides, lives in settings, applies to every session in scope). `/goal` is a session-scoped shortcut for a prompt-based Stop hook. Auto mode removes per-tool prompts; `/goal` removes per-turn prompts.
