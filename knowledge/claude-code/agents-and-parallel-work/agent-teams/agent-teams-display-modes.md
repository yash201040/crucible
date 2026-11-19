---
type: "Feature"
title: "Display modes and teammateMode"
description: "In-process or split-pane (tmux or iTerm2) display of teammates, set with the teammateMode setting or the experimental --teammate-mode flag, plus agent panel controls."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, tmux, iterm2, agent-panel]
kind: "setting"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: "split panes need tmux or iTerm2 with the it2 CLI"
identifiers:
  - "teammateMode"
  - "--teammate-mode"
  - "it2"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two display modes. In-process: all teammates run inside the main terminal, work in any terminal. Split panes: each teammate gets its own pane; needs tmux or iTerm2 with the `it2` CLI (enable iTerm2 > Settings > General > Magic > Enable Python API). `tmux -CC` in iTerm2 is the suggested entry into tmux; tmux has known limitations on some operating systems and works best on macOS.

# How to use it

Teammates run in-process until `teammateMode` is changed in `~/.claude/settings.json`.

| `teammateMode` value | Effect |
| - | - |
| `"auto"` | split panes when running inside tmux or iTerm2, in-process elsewhere |
| `"tmux"` | use tmux when you are outside tmux and iTerm2; panes open in a separate tmux session, view it with the command on the `View teammates` line |
| `"iterm2"` | use iTerm2's own panes; teammates start only when running in iTerm2 with `it2` set up |

One session only: `claude --teammate-mode auto`. The flag is experimental and does not appear in `claude --help`.

Agent panel (in-process), below the prompt input: Up/Down selects a teammate, Enter opens its transcript and messages it, Escape clears selection (while viewing a transcript, Escape interrupts that teammate's current turn), `x` on a selected teammate stops it, Ctrl+T toggles the task list.

# Limits and defaults

- An idle teammate's row stays while any teammate or subagent is working. Once every agent is idle, idle rows hide after 30 seconds and reappear on the next turn; the teammate stays running and addressable.
- When more than three teammates are idle, rows beyond the first three collapse into one row such as `2 idle agents`; Enter expands, Esc collapses. Working, failed and currently viewed teammates always keep their rows.
