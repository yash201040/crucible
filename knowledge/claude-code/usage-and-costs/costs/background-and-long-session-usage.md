---
type: "Concept"
title: "Background token use and long-session growth"
description: "Idle-time token consumers (recap, suggestions, loops, goal check-ins, cross-session messages) and why long sessions use more of the plan."
resource: "https://code.claude.com/docs/en/costs"
tags: [background-usage, goal, scheduled-tasks, cache-miss, idle]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli]
requires: "Idle goal check-ins need v2.1.236 or later"
identifiers:
  - "CLAUDE_CODE_GOAL_CHECKIN_MINUTES"
  - "crossSessionInbound"
  - "idleCompaction"
  - "/compact"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Several things spend tokens while you are idle, and long sessions cost more because the full conversation is sent on every request.

# How to use it

Background consumers: session recap and idle compaction (`idleCompaction`); prompt suggestions (a short request after each response on the session's model, mostly cache reads, skipped near or at the usage limit; can be turned off).

Why usage climbs:
- Long context: full conversation is sent each request and again after each tool batch, re-read at the cached token rate.
- Cache misses: the first message after a break longer than the cache lifetime reprocesses the full context.
- Scheduled tasks: a session-scoped task fires on its interval even when idle, sending full context.
- Cross-session messages arrive as a new turn when idle; set `crossSessionInbound` to `hold` to hold them instead.
- Goal check-ins: while background work keeps an active goal waiting, Claude Code asks Claude to check on it even when idle. At most three idle check-ins per goal between your prompts (uncapped before v2.1.246). Set `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` to `0` to turn them off.
- Subagents and workflows: each subagent and each agent a dynamic workflow spawns sends its own requests; the plan usage breakdown shows the subagent share.
- Agent teammates keep consuming tokens until they exit.
- Compaction: `/compact` reads the conversation it summarizes, so compacting a large context is a large request; `/clear` costs nothing.

On subscription plans `/usage` recommends a change for behaviors behind 10% or more of recent usage.
