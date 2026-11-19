---
type: "Feature"
title: "/background and /fork inside a session"
description: "/background (/bg) moves a session to the background; /fork copies it into a new background session."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, fork, background, worktrees]
kind: "slash_command"
maturity: "research-preview"
since: "2.1.212"
surfaces: [cli]
requires: ""
identifiers:
  - "/background"
  - "/bg"
  - "/fork"
  - "/subtask"
  - "claude attach <id>"
  - "--fork-session"
  - "WorktreeCreate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/background` (alias `/bg`) moves the current conversation to a background session (an in-flight response continues there). `/fork` (v2.1.212; earlier forked-subagent behaviour moved to `/subtask`) copies the conversation into a new background session while the original keeps running. The copy carries model, permission mode, effort, added directories and "don't ask again" grants. Afterwards the two are independent, though with cross-session messaging enabled either can message the other. With agent view turned off, `/fork` starts a forked subagent instead.

# How to use it

- `/bg run the test suite and fix any failures` gives one more instruction first. Exiting with subagents/workflows running shows `Background work is running`; choose `Move to background and exit`. A same-named row gets a number, e.g. `my-session (2)`.
- `/fork open a draft pull request with the work so far` starts the copy on that prompt. Without a prompt it waits: select its row and press `Space`, or `claude attach <id>` (row shows `space to send it a prompt`). The one-line confirmation shows state, row name and session ID; clicking the name switches into the copy.

# Limits and defaults

Where the copy runs: Claude instructs it to create its own worktree before code changes (outside a git repo, only a copy moved out of a hook-created worktree gets the instruction; with no `WorktreeCreate` hook it edits in place). It is told never to touch the original's worktree. Confirmations: nothing extra when it moves into its own worktree; `runs in the origin tree` when your session moved into a linked worktree after start, or was launched inside a linked worktree of a repo with a main working tree (copy starts in the main tree; branch hint only in the first case); `edits this checkout` for bare-repository layout worktrees or when isolation is off outside a linked worktree.

Cannot be forked: sessions started with flags the copy would not inherit (replaced system prompt, `--tools` allowlist); Claude Code says so. A session dispatched from agent view forks normally with the same agent definition and appended instructions. Since v2.1.246 `/fork` copies the full conversation even from a session that itself started as a copy.
