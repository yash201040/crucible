---
type: "Concept"
title: "SIGTERM handling and interrupted turns"
description: "Exit code 143 on SIGTERM, what Claude Code does while exiting, and how to resume the interrupted turn."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, signals, resume, sessionend]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "SIGTERM"
  - "SIGINT"
  - "interrupt()"
  - "SessionEnd"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Stopping a `claude -p` run with SIGTERM (for example from `kill` or a process supervisor) exits with code 143. The in-progress turn is left unfinished with no result recorded. To end the turn instead, send SIGINT or call the Agent SDK's `interrupt()` first.

# How to use it

On SIGTERM Claude Code terminates the process tree of any running Bash command, runs `SessionEnd` hooks and exits. While exiting it starts no tool call, sends no model request and runs no hook other than `SessionEnd`.

- Running command: recorded as killed in the session.
- Waiting on a permission prompt: with SIGTERM to the process the prompt is left unanswered; if the program closes the session through the Agent SDK, the SDK ends Claude Code's input first and the prompt is cancelled as soon as input ends.

# Limits and defaults

On resume Claude Code leaves the interrupted turn as it is and your next prompt drives the conversation. Set `CLAUDE_CODE_RESUME_INTERRUPTED_TURN=1` to continue the interrupted turn on resume.
