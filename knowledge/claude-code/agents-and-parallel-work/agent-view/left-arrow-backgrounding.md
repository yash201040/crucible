---
type: "Feature"
title: "Backgrounding with the left arrow"
description: "Pressing left arrow on an empty prompt backgrounds a foreground session and opens agent view, with defined waiting rules."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, backgrounding, left-arrow, switching]
kind: "ui"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "leftArrowOpensAgents"
  - "Ctrl+B"
  - "claude --resume"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In a foreground session, `←` on an empty prompt backgrounds it and opens agent view with that row selected (the same single press detaches an attached session). The row keeps a bold name so you know where you came from. Claude's task list moves with the conversation. The row exists even for an empty conversation. If reopening fails, Claude Code exits and prints a `claude --resume` command.

# How to use it

After backgrounding: `Enter` reopens the conversation, `Esc` undoes the switch (if `Still starting — try again in a moment`, press again), `Ctrl+C` twice exits to the shell. Pressing `←` right after deleting the last prompt text or moving through history shows `Press ← again to open agents` (`Press ← again to go back to agents` when attached); a second press at least a second later switches.

# Limits and defaults

- A running tool: Claude Code waits for it (press `←` again to skip waiting). After about ten seconds it backgrounds anyway, except:
  - Foreground subagents running: keeps waiting (`Still backgrounding after the current tool`); pressing again restarts those subagents from scratch.
  - Permission prompt or question waiting: keeps waiting.
  - You type text: switch cancelled (`Backgrounding cancelled — you have unsent text in the input...`).
  - Turn stopped (Esc, "No" without comment): cancelled.
  - A queued message that cannot move: stays foreground with a notice.
- A foreground shell command Claude is running is stopped on backgrounding (no `Background this session?` dialog for it); Claude may re-run it. Press `Ctrl+B` first to turn it into a background command.
- A prompt or `!` command entered as the session moves is stopped or left unsent (not sent if `SessionStart` hooks still run); the text stays in prompt history (press `↑` in the backgrounded session).
- Turn the shortcut off via `leftArrowOpensAgents` in `/config`.
