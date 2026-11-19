---
type: "Reference"
title: "Hooks commonly used in the loop"
description: "Hook events that fire in the SDK loop and how hooks relate to context and short-circuiting."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [hooks, pretooluse, subagent, compaction]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "PreToolUse"
  - "PostToolUse"
  - "UserPromptSubmit"
  - "Stop"
  - "SubagentStart"
  - "SubagentStop"
  - "PreCompact"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Hook | Fires | Uses |
| :- | :- | :- |
| `PreToolUse` | Before a tool runs | Validate inputs, block commands |
| `PostToolUse` | After a tool returns | Audit, side effects |
| `UserPromptSubmit` | When a prompt is sent | Inject context |
| `Stop` | When the agent finishes | Validate result, save state |
| `SubagentStart` / `SubagentStop` | Subagent spawns/completes | Aggregate parallel results |
| `PreCompact` | Before compaction | Archive transcript |

# Notes

Hooks run in your application process, not in the context window, so they use no context. A `PreToolUse` hook that rejects a call prevents it; Claude gets the rejection message. Both SDKs support all these events; TypeScript supports additional events Python does not yet.
