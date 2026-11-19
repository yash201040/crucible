---
type: "Feature"
title: "Project thread models, approvals and local threads"
description: "Thread and coordinator model settings, auto mode approvals, tuning concurrency, and running a thread on your own computer via Remote Control."
resource: "https://code.claude.com/docs/en/claude-projects"
tags: [projects, models, auto-mode, remote-control, local-threads]
kind: "behavior"
maturity: "beta"
since: "2.1.280"
surfaces: [web, desktop, cli]
requires: "Claude Code v2.1.280 or later on the local computer for local threads"
identifiers:
  - "claude remote-control"
  - "--spawn worktree"
  - "--settings"
  - "permissions.defaultMode"
  - "CLAUDE_CODE_MAX_TURNS"
  - "Work locally"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-projects"
    resource: "https://code.claude.com/docs/en/claude-projects"
    title: "Let Claude coordinate ongoing work with Projects"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls for how project threads run.

# How to use it

- Models: a new project runs Opus everywhere, high effort for threads and low for the conversation. Project settings > General has Thread model, Thread effort, Coordinator model, Coordinator effort. A per-task model can be requested in the task, or via a running thread's model picker. Threads compact automatically; the conversation works from recent messages, recent threads and project memory.
- Tuning by telling Claude: propose-before-start or start now; "run at most two threads at a time"; reuse a thread for follow-ups; shorter updates; smaller model; no PR until plan seen. These are preferences, not hard caps.
- Approvals: threads run in auto mode when the model supports it. Approval prompts live inside the thread; saying go ahead in the project conversation does not reach it. Cloud threads ignore repo permission rules.
- Local thread: needs a folder connected via Remote Control (desktop app: Settings > Code, "Use this computer from your phone and claude.ai", add folder; or terminal `claude remote-control` in the folder, with `--spawn worktree` for a worktree per thread). Request with **Work locally** (**Work in a local folder** on desktop) then **Allow once** on the card. It uses that machine's files, tools, MCP servers, settings, hooks and permission rules, starts with project instructions but not memory files, and runs in auto mode (without it, prompts wait in the thread). Another mode: start `claude remote-control` with `--settings` and `permissions.defaultMode`.

# Limits and defaults

- Two threads in one folder can overwrite each other; use the folder's Worktree option.
- Local threads run only while the computer is awake with Remote Control on; they pause on sleep and stop if the app or `claude remote-control` quits ("Lost contact with your folder"). Desktop option "Keep this computer awake for Remote Control".
- Greyed out Work locally means **Require trusted devices** is on.
- Messages: "Claude is out of date on your device" (below v2.1.280), "Couldn't start in <folder>", "Reached the turn limit" (cap from `CLAUDE_CODE_MAX_TURNS`), "Claude ran out of context on this turn".
