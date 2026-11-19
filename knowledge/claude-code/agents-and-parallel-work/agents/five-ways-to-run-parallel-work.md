---
type: "Reference"
title: "Five ways to run parallel work"
description: "Comparison of subagents, agent view, agent teams, projects and dynamic workflows, and the supporting tools."
resource: "https://code.claude.com/docs/en/agents"
tags: [parallel, subagents, agent-teams, workflows, comparison]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web]
requires: "Projects: Pro, Max or Ultra plan"
identifiers:
  - "claude agents"
  - "/batch"
  - "/subtask"
  - "/fork"
  - "/agents"
  - "/tasks"
  - "/workflows"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agents"
    resource: "https://code.claude.com/docs/en/agents"
    title: "Run agents in parallel"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five ways to work on several tasks at once, differing in how involved you stay and whether work runs locally or in the cloud. In every approach the workers are Claude sessions; to involve a different tool, expose it as an MCP server. Running several sessions or subagents multiplies token usage.

# How to use it

| Approach | What it gives you | Use when |
| :- | :- | :- |
| Subagents | Delegated workers in one session, own context, return a summary | A side task would flood the main conversation |
| Agent view (research preview) | One screen to dispatch and monitor background sessions, `claude agents` | Several independent tasks to hand off |
| Agent teams (experimental, disabled by default) | Coordinated sessions with a shared task list and messaging, managed by a lead | Claude should split, assign and sync a project |
| Projects (public beta on Pro, Max, Ultra) | One ongoing conversation at claude.ai/code or in the desktop app; Claude starts parallel threads in the cloud or via Remote Control on your computer | Multi-day work that keeps running with your machine off |
| Dynamic workflows | A script that runs many subagents and cross-checks results | Codebase-wide audit, 500-file migration, cross-checked research |

Supporting tools (not ways to run agents): worktrees (separate git checkout per session; agent-view sessions move into one before editing; subagents can get one), cross-session messaging (list and message other sessions on this machine, another machine or in the cloud), `/batch` (a skill splitting one large change into 5 to 30 worktree-isolated subagents).

Not parallel-agent features: a background bash command (no agent spawned); a forked subagent (inherits full conversation; start with `/subtask`, or Claude spawns one where fork mode is on; `/fork` instead copies the whole session into a new background session, but with agent view turned off `/fork` is the forked-subagent command and `/subtask` is unavailable); a cloud scheduled task (runs on a schedule in the cloud).

# Notes

Choosing: who coordinates (subagents: Claude inside one conversation; agent view: you; agent teams: Claude supervising; workflows: a script). Do workers need to talk: subagents report to their spawner; agent view sessions report only to you; cross-session messaging passes findings between sessions you run, including agent-view ones; teammates message each other and share a task list when they have the Task tools. Same files: use worktrees; agent teams do not isolate teammates in worktrees, so partition files per teammate.
