---
type: "Feature"
title: "VS Code sessions, resume and background tasks"
description: "Session history, archiving, groups, cloud-session resume, reload recovery, checkpoints and moving commands or subagents to the background."
resource: "https://code.claude.com/docs/en/vs-code"
tags: [vscode, sessions, resume, background-tasks, subagents]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [ide]
requires: "claude.ai sign-in for the Web tab"
identifiers:
  - "claudeCode.archiveInactiveSessions"
  - "continueAfterReload"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN"
  - "Run in background"
  - "Open here anyway"
  - "Fork conversation from here"
  - "Rewind code to here"
  - "Fork conversation and rewind code"
  - "vscode://anthropic.claude-code/open"
  - "vscode://anthropic.claude-code/install-plugin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "vs-code"
    resource: "https://code.claude.com/docs/en/vs-code"
    title: "Use Claude Code in VS Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Session history: search by keyword or time; AI-generated titles; rename and archive; sessions idle 14 days auto-archive (v2.1.265+) unless open, unread or grouped; unarchive one or all (v2.1.277+). Before v2.1.257 the action was Delete session. Groups (v2.1.229+, tab action v2.1.257+), saved per workspace folder; filters Active and by status (v2.1.271+).
- Resume restores plan mode (v2.1.246+) except when `initialPermissionMode` or a carried-over pick applies, `claudeProcessWrapper` is set, a deny rule removes `ExitPlanMode`, or `permissions.denyInsteadOfPrompting` is on.
- A conversation still open in another Claude process shows a notice; wait about 10 minutes or click **Open here anyway**. With `claudeProcessWrapper` set the check is skipped.
- Cloud sessions: Session history > Web tab (claude.ai subscription sign-in only, not Console). Downloads a copy; changes do not sync back. Remote Control sessions in the open folder reopen the local conversation instead.
- Reload recovery: sidebar conversations return if active within the last 10 minutes; an interrupted step continues (v2.1.274+, unless interrupted over an hour ago or open elsewhere); toggle with `continueAfterReload`. A conversation whose last two opens did not finish is not reopened ("Open it anyway").
- Checkpoints via the rewind button: fork conversation, rewind code, or both.
- Worktrees: banner "This session is in worktree"; resumes in worktree if under `.claude/worktrees/` and it still exists (before v2.1.300 an empty conversation opened).

# How to use it

Run in background (v2.1.287+): button appears under a command after about two seconds, or when Claude waits on a subagent it spawned from the main conversation. Claude continues the turn and the task notifies on completion. `/tasks` opens the agent map (commands listed below agents with latest output). By default subagents spawned in the background show no Run in background action; nested subagents never show it (use **Stop agent**). From v2.1.286, Stop or `Esc` ends the turn but background agents keep running until finished or stopped from the map.

Launch from tooling: `open "vscode://anthropic.claude-code/open?prompt=review%20my%20changes"`. Parameters: `prompt` (URL-encoded, prefilled not submitted) and `session` (ID to resume from the open folder; worktree sessions of the same repo also resume with v2.1.300+; fresh conversation if not found; focuses tab if open).

# Notes

Windows credential-leak caution: files whose path names a network host (UNC paths) are not linked in the "Sent files" row.
