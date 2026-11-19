---
type: "Reference"
title: "Built-in tools and parallel execution"
description: "Built-in tool categories in the SDK, tool permission options, and which tools run concurrently."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [tools, built-in, parallel, tool-search]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Read"
  - "Edit"
  - "Write"
  - "Glob"
  - "Grep"
  - "Bash"
  - "WebSearch"
  - "WebFetch"
  - "ToolSearch"
  - "Agent"
  - "Skill"
  - "AskUserQuestion"
  - "TaskCreate"
  - "TaskUpdate"
  - "readOnlyHint"
  - "allowed_tools"
  - "disallowed_tools"
  - "permission_mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Category | Tools |
| :- | :- |
| File operations | `Read`, `Edit`, `Write` |
| Search | `Glob`, `Grep` |
| Execution | `Bash` |
| Web | `WebSearch`, `WebFetch` |
| Discovery | `ToolSearch` (find and load tools on demand) |
| Orchestration | `Agent`, `Skill`, `AskUserQuestion`, `TaskCreate`, `TaskUpdate` |

On models without task-tracking tools by default, `TaskCreate`/`TaskUpdate` exist only on opt-in. Extend with MCP servers, custom tool handlers, and skills loaded via setting sources.

# How to use it

- `allowed_tools`/`allowedTools` auto-approves listed tools (not network-path reads); unlisted tools stay available and fall to the permission mode and `canUseTool`.
- `disallowed_tools`/`disallowedTools` blocks listed tools regardless of other settings.
- Scope with rules like `"Bash(npm *)"`.
- A denied tool returns a rejection message as the tool result; Claude typically tries another approach.

# Limits and defaults

Parallel execution: read-only tools (`Read`, `Glob`, `Grep`, MCP tools marked read-only) can run concurrently; state-modifying tools (`Edit`, `Write`, `Bash`) run sequentially. Custom tools default to sequential; set `readOnlyHint` in annotations to allow parallel (same field name in TypeScript and Python SDKs).
