---
type: "Limit"
title: "Concurrent subagent limit"
description: "At 20 running subagents, spawning another with the Agent tool fails; change it with CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, limits, concurrency, ultracode]
kind: "limit"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS"
  - "Concurrent subagent limit reached"
  - "/subtask"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Default cap of 20 concurrently running subagents per session. The 21st Agent tool spawn fails with `Concurrent subagent limit reached` and the error tells Claude not to retry. Spawning works again when the running count drops below the limit. There is no cap on total subagents over a session.

# How to use it

Set `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` to any positive whole number (v2.1.217 or later). Sessions with ultracode active are exempt.

# Limits and defaults

- Only subagents Claude spawns with the Agent tool are blocked, but other runs occupy slots: an in-session fork from `/subtask` takes a slot and is never blocked; resuming a finished subagent takes a slot without checking, so resumes can exceed the limit.
- Workflow agents and agent team teammates follow their own limits. This limit is separate from the nesting depth limit.
