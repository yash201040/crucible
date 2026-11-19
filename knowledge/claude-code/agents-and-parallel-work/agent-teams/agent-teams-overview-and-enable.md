---
type: "Feature"
title: "Agent teams overview and enabling"
description: "Experimental, off by default: a lead session coordinates teammate sessions with a shared task list and direct messaging; enable with CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, experimental, teammates, enable]
kind: "env_var"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: "interactive session; not available with -p or Agent SDK sessions"
identifiers:
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agent teams coordinate several Claude Code instances. One session is the team lead (assigns tasks, synthesizes results). Teammates work independently, each in its own context window, and message each other directly; you can also talk to any teammate without going through the lead. The feature is experimental and disabled by default, with known limitations around session resumption, task coordination and shutdown.

# How to use it

Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to `1` in the environment or in settings.json:

```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

Then describe the task and teammates in natural language, for example "Spawn three teammates ...". Claude populates a shared task list (in a session that has the Task tools), spawns teammates and synthesizes findings. Claude may sometimes use subagents instead; subagents appear in the same agent panel, so ask again and explicitly request an agent team.

# Limits and defaults

- Enabling also changes ordinary delegation: a subagent that Claude names launches as a teammate, so teams can form unasked. Set the variable to `0` to turn this off.
- Spawning teammates needs an interactive session. In non-interactive mode with `-p`, including Agent SDK sessions, Claude does not spawn teammates; a named subagent runs as an ordinary subagent even with teams enabled.
- Teams add coordination overhead and use significantly more tokens than one session; they suit parallel exploration, not sequential tasks, same-file edits or heavily dependent work.

# Notes

Lighter alternatives: subagents (within one session) and cross-session messaging (between sessions you run yourself).
