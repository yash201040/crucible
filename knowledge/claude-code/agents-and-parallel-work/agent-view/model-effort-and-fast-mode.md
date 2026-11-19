---
type: "Feature"
title: "Model, effort and fast mode for dispatched sessions"
description: "Set the model, effort and fast mode for sessions dispatched next, per agent view window or per session."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, model, effort, fast-mode]
kind: "slash_command"
maturity: "research-preview"
since: "2.1.299"
surfaces: [cli]
requires: "Fast mode needs availability and a supporting model"
identifiers:
  - "/model"
  - "/effort"
  - "/fast"
  - "--model"
  - "--effort"
  - "ultracode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Typed in the dispatch input, `/model`, `/effort` and `/fast` set what later dispatched sessions start with. The choice stays with that agent view window and is not saved to a settings file. `/effort`, `/fast` and bare `/model` (picker) need v2.1.299+; `/model` with a value dates from v2.1.172.

# How to use it

| Command | Values |
| :- | :- |
| `/model <name>` | e.g. `/model opus` |
| `/effort <level>` | `low`, `medium`, `high`, `xhigh`, `max` |
| `/fast on` / `/fast off` | Fast mode only applies if available to you and the model supports it, else it starts off; the hint under the input confirms |
| `... default` | Undo, e.g. `/effort default` |

```text
/model opus
refactor auth
/model sonnet
run the test suite
```

The dispatch input does not accept `/effort ultracode`; use `claude agents --effort ultracode` from the shell.

Per-session override: `--model` with `claude --bg`; attach and run `/model` (a pick or typed name saves as your default for new sessions unless you press `s` for session-only, which persists on respawn); or dispatch a subagent whose frontmatter sets `model` (ignored while a `/model` choice in the dispatch input or `claude agents --model` applies; use `/model default` or drop `--model`).
