---
type: "Guide"
title: "Agent team token costs"
description: "Agent teams run several Claude Code instances, so tokens scale with team size; tips and the roughly 7x figure in plan mode."
resource: "https://code.claude.com/docs/en/costs"
tags: [agent-teams, cost, tokens, teammates, experimental]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1"
identifiers:
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agent teams spawn multiple Claude Code instances, each with its own context window. Usage scales with active teammates and how long each runs. They use approximately 7x more tokens than standard sessions when teammates run in plan mode. Agent teams are disabled by default (the experimental flag name is in the identifiers).

# How to use it

- Use Sonnet for teammates.
- Keep teams small; tokens are roughly proportional to team size.
- Keep spawn prompts focused: teammates load CLAUDE.md, MCP servers and skills automatically, and the spawn prompt adds to context from the start.
- Shut down teammates when done; each active one keeps consuming tokens until it exits or the session ends.
- Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json or the environment.
- Keep tasks small and self-contained.
