---
type: "Concept"
title: "Accumulating cost across calls and sessions"
description: "Add totals of independent calls yourself; resumed sessions already include earlier spend, so read the latest result."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [cost, resume, sessions, accumulation]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.277"
surfaces: [sdk]
requires: ""
identifiers:
  - "total_cost_usd"
  - "resume"
  - "continue"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to combine `total_cost_usd` across calls depends on whether they share a session.

# How to use it

- Independent calls (no `resume` or `continue`): each result covers only its own call; add totals yourself.
- Calls resuming the same session: Claude Code saves the session totals to its transcript when the process exits normally and restores them when a later call resumes or forks. Each result already includes earlier spend; read the latest result. Summing double-counts.

The combined figure is still a client-side estimate. After a crash see [crash recovery](./output-tokens-failures-and-crash-recovery.md).

# Notes

Before v2.1.277, a session resumed through the SDK or `claude -p` started its totals at zero, so each call's results covered only that call.
