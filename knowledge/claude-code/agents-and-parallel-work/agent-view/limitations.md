---
type: "Limit"
title: "Agent view limitations"
description: "Rate limits, local-only sessions, and worktree deletion caveats of the agent view research preview."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, limits, rate-limits, local]
kind: "limit"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

- Rate limits apply: background sessions consume subscription usage like interactive ones, so ten agents in parallel use quota roughly ten times as fast as one.
- Sessions are local: preserved across sleep but stop on machine shutdown.
- Claude-created worktrees are deleted with the session in agent view; commit before deleting. Some worktrees stay on disk (see [deleting sessions](./deleting-sessions-and-worktrees.md)).
- Research preview: interface and shortcuts may change; older versions reject unsupported `claude agents` flags with `unknown option`.
