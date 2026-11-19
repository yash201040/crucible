---
type: "Feature"
title: "Resuming and relaunching workflow runs"
description: "Pause with p, relaunch stopped runs; which agents replay from saved results and which rerun; recovery after leaving the session."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, resume, replay, sessions, cloud]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.318"
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "nothing to resume"
  - "claude --resume"
  - "Move to background and exit"
  - "Exit and stop tasks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Resume a paused run from `/workflows` (select, press `p`). For a stopped run, ask Claude to relaunch the workflow with the same script; if the stopped run's agents have not exited, the relaunch is refused until they have. Claude Code replays in agent start order; each agent returns its saved result or reruns.

# How to use it

| Agent state | On relaunch |
| :- | :- |
| Completed | Returns saved result. The first agent whose prompt differs (edited script or changed earlier result) reruns, and every agent after it |
| Still running when stopped | Starts over (stopping the whole run does not count anyone failed) |
| Failed at a usage limit (v2.1.318 or later) | Reruns; completed agents return saved results; if the script started another agent after the failure that returned a result, all agents started after the failed one rerun |
| Failed (including one stopped alone with `x`) | Reruns, and every agent started after it, even completed ones |

Example: A, B, C, D with B failed: A from cache; B, C, D rerun. Reordering to A, C, B, D: A cached; C, B, D rerun.

Leaving the session:
- Backgrounded session or `Move to background and exit`: the run does not continue by itself; ask Claude there to relaunch (may need approval; attach if shown under `Needs input`).
- `nothing to resume` on relaunch: ask Claude to start a new run; a run started from a script path outside `~/.claude/projects/` cannot be relaunched in the background session.
- `Exit and stop tasks` (or no background option): the run stops, saved results stay under the session directory in `~/.claude/projects/`; `claude --resume`, then ask Claude to relaunch. A fresh session starts over.
- Cloud sessions: results are saved with the conversation history, so reopening and relaunching returns completed agents' saved results.

# Limits and defaults

- Before v2.1.305, completed agents could rerun when an unedited script's `pipeline()` items or `parallel()` tasks ran more than one agent each.
- Stopping a run keeps it in the task panel while any agent process runs; stopping again re-signals them.
- Missing saved results always give `nothing to resume`, never an automatic restart.
