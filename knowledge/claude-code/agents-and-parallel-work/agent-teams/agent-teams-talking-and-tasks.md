---
type: "Feature"
title: "Messaging teammates, shared tasks and shutdown"
description: "Direct messaging of teammates, the shared task list with pending/in-progress/completed states and file-locked claiming, and graceful shutdown requests."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, task-list, messaging, shutdown]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: "task list needs a session that has the Task tools"
identifiers:
  - "/compact"
  - "/clear"
  - "/rewind"
  - "/model"
  - "/fast"
  - "SendMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each teammate is a full, independent Claude Code session you can message directly. The lead and teammates coordinate through a shared task list.

# How to use it

- In-process: select a teammate in the agent panel, press Enter, type to message it. Split-pane: click into its pane.
- While viewing an in-process teammate, plain text and skills go to that teammate, and built-in commands go to the lead's session. `/compact`, `/clear` and `/rewind` act on the lead's conversation and ask for confirmation first. `/model` and `/fast` set the lead's model and fast mode, not the teammate's, so they do not run from this view (a notice says why).
- Tasks have three states: pending, in progress, completed. A task can depend on others and shows as blocked until they complete. Teammates do not self-claim a blocked task, but you or the lead can assign it. The lead can assign explicitly, or a teammate self-claims the next unassigned, unblocked task after finishing one.
- Task claiming uses file locking to prevent races. Completing a task unblocks dependents automatically.
- Agents without the Task tools coordinate through messages instead of the shared task list.
- Shutdown: ask by name, for example "Ask the researcher teammate to shut down". The lead sends a shutdown request; the teammate approves (exits gracefully) or rejects with an explanation.

# Notes

The team's shared directories are cleaned up when the session ends; see [architecture](./agent-teams-architecture-and-storage.md).
