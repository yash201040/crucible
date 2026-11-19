---
type: "Guide"
title: "Agent team best practices and sizing"
description: "Team size, task sizing, spawn-prompt context, avoiding file conflicts and monitoring guidance for agent teams."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, best-practices, team-size, tasks]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Guidance from the docs for getting value from agent teams.

# How to use it

- Give context: teammates do not inherit the lead's history, so put task-specific details (paths, stack, expected output) in the spawn prompt.
- Team size: no hard limit. Start with 3-5 teammates; token costs scale linearly, coordination overhead and diminishing returns grow. Example: with 15 independent tasks, 3 teammates is a good start. Three focused teammates often outperform five scattered ones.
- Task size: too small and coordination overhead dominates; too large and teammates work long without check-ins; just right is a self-contained unit with a clear deliverable (function, test file, review). 5-6 tasks per teammate keeps everyone productive; ask the lead to split work if it creates too few tasks.
- If the lead starts implementing itself, tell it: "Wait for your teammates to complete their tasks before proceeding".
- Start with research and review tasks (no code writing) if new to teams.
- Avoid file conflicts: two teammates editing one file leads to overwrites; give each a distinct set of files.
- Monitor and steer; letting a team run unattended too long increases wasted-effort risk.
