---
type: "Reference"
title: "Effort levels"
description: "The effort option values low to max, per-session and per-subagent, and how it differs from extended thinking."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [effort, reasoning, cost, models]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "A model that supports the effort parameter"
identifiers:
  - "effort"
  - "low"
  - "medium"
  - "high"
  - "xhigh"
  - "max"
  - "AgentDefinition"
  - "ThinkingConfig"
  - "display"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`effort` controls how much reasoning Claude applies; lower levels use fewer tokens per turn and cost less. Not all models support it.

# How to use it

| Level | Behavior | Good for |
| :- | :- | :- |
| `"low"` | Minimal reasoning | File lookups, listing directories |
| `"medium"` | Balanced | Routine edits |
| `"high"` | Thorough | Refactors, debugging |
| `"xhigh"` | Extended depth | Coding and agentic tasks on models that support it |
| `"max"` | Maximum depth | Multi-step problems needing deep analysis |

Set in top-level `query()` options for the session, or per subagent with the `effort` field of `AgentDefinition` to override the session level. If unset, Claude Code resolves effort itself in the order described in its model-config docs.

# Notes

`effort` is separate from extended thinking; thinking produces `thinking` blocks, and the `display` field on `ThinkingConfig` controls whether you receive their text. The `model` option chooses the model.
