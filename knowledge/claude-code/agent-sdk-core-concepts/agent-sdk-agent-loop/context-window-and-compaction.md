---
type: "Concept"
title: "Context window, caching and compaction"
description: "What consumes context in the SDK, prompt caching, automatic compaction and how to influence it."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [context, compaction, caching, claude-md]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "compact_boundary"
  - "SDKCompactBoundaryMessage"
  - "PreCompact"
  - "/compact"
  - "settingSources"
  - "CLAUDE.md"
  - "trigger"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The context window does not reset between turns; the system prompt, tool definitions, history, tool inputs and outputs accumulate. Content constant across turns (system prompt, tool definitions, CLAUDE.md) is automatically prompt cached.

| Source | When it loads | Impact |
| :- | :- | :- |
| System prompt | Every request | Small fixed cost |
| CLAUDE.md files | Session start via `settingSources` | Full content each request (cached) |
| Tool definitions | Every request for core built-ins; on demand for MCP and other built-ins (tool search defers by default) | Every schema loads upfront in configurations under tool-search docs |
| Conversation history | Accumulates | Grows each turn |
| Skill descriptions | Session start | Short summaries; full content only when invoked |

# How to use it

On nearing the limit the SDK compacts automatically: summarizes older history, keeps recent exchanges and key decisions, emits `type: "system"`, `subtype: "compact_boundary"` (Python `SystemMessage`; TypeScript `SDKCompactBoundaryMessage`). Customize by:
- a summarization-instructions section in CLAUDE.md (header free-form)
- a `PreCompact` hook (receives `trigger`: `manual` or `auto`), e.g. to archive the transcript
- sending `/compact` as a prompt string for manual compaction

# Limits and defaults

Compaction can drop early-conversation instructions; put persistent rules in CLAUDE.md, which is re-injected every request.

# Notes

Efficiency: use subagents (parent context grows only by their final response), scope subagent `tools`, watch MCP server schema cost (tool search defers by default), use low effort for routine tasks.
