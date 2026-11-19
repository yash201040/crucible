---
type: "Reference"
title: "Commands for checking running work"
description: "Which command lists running background sessions, subagents, tasks and workflows."
resource: "https://code.claude.com/docs/en/agents"
tags: [parallel, monitoring, tasks, workflows]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "claude agents"
  - "/agents"
  - "/tasks"
  - "/workflows"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agents"
    resource: "https://code.claude.com/docs/en/agents"
    title: "Run agents in parallel"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Command | What it shows |
| :- | :- |
| `claude agents` | Agent view: every background session, its state, which need input |
| @-mention typeahead | Named background subagents of the current session with status |
| `/agents` | Prints a notice pointing to subagent file locations; to create or edit custom subagents ask Claude or edit the files. Separate from `claude agents` despite the name |
| `/tasks` | Everything running in the background of the current session; check, attach or stop; includes finished subagents |
| `/workflows` | Running and completed dynamic workflow runs, their phase and how many agents finished |

# Notes

The desktop app has its own view of all sessions (parallel sessions in the desktop app).
