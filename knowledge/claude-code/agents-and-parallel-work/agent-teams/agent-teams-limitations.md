---
type: "Limit"
title: "Agent teams limitations"
description: "Known limits of the experimental feature: no resume of in-process teammates, task lag, one team per session, no nested teams, no background subagents from teammates."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, limitations, resume, experimental]
kind: "limit"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/resume"
  - "/rewind"
  - "background: true"
  - "run_in_background: true"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Documented limitations of agent teams.

# Limits and defaults

| Limitation | Detail |
| - | - |
| No session resumption with in-process teammates | `/resume` and `/rewind` do not restore them; after resume the lead may message teammates that no longer exist, so tell it to spawn new ones |
| Task status can lag | teammates sometimes fail to mark tasks completed, blocking dependents; check and update manually or have the lead nudge |
| Shutdown can be slow | teammates finish the current request or tool call first |
| One team per session | exactly one team, scoped to the session; no extra named teams, no sharing across sessions |
| No nested teams | teammates cannot spawn teammates; only the lead manages the team |
| No background subagents from in-process teammates | a teammate's subagents run in the foreground; spawning one whose definition sets `background: true` errors; `run_in_background: true` also fails, either with an error or by running silently in the foreground |
| Lead is fixed | the main session is lead for its lifetime; no promotion or transfer |
| No per-teammate permission modes at spawn | teammates start with the lead's mode |
| Split panes need tmux or iTerm2 | in-process mode works in any terminal |
| Non-interactive | no teammates in `-p` or Agent SDK sessions |
