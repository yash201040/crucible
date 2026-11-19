---
type: "Reference"
title: "Observing and steering running forks"
description: "Panel keys and follow-up messaging for running forks and subagents, and which commands act on the viewed agent."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, fork, panel, keybindings, steering]
kind: "ui"
maturity: "unlabelled"
since: "2.1.286"
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+Enter"
  - "Ctrl+X Ctrl+S"
  - "/btw"
  - "/compact"
  - "/clear"
  - "/rewind"
  - "/model"
  - "/fast"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Running forks appear in a panel below the prompt (one row for main, one per fork). A successful fork's row is removed; a failed or stopped one stays 30 seconds (before v2.1.232 finished forks also stayed 30 seconds).

# How to use it

| Key | Action |
| :- | :- |
| Up / Down | Move between rows |
| Enter | Open the fork's transcript and send follow-ups |
| `x` | Stop a running fork, or dismiss a finished row; on the main row or an opened fork's transcript it types into the prompt |
| Esc | Return to the prompt |

With a transcript open, follow-up messages and skills go to that agent. `/btw` answers from the open transcript (v2.1.314 or later). Other built-in commands go to the main conversation: `/compact`, `/clear`, `/rewind` ask for confirmation first; `/model` and `/fast` set the main conversation's model and fast mode and do not run from this view.

# Limits and defaults

To make the viewed agent read your message before its pending work ends, send with `Ctrl+Enter` or `Ctrl+X Ctrl+S` (v2.1.286 or later): shell commands or subagents it waits on that can move to the background do so; otherwise it reads your message after finishing.
