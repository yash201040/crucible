---
type: "Reference"
title: "Agent trace spans (beta)"
description: "Span names for interaction, LLM request, tool and hook, their nesting including subagents, and the session.id attribute."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [tracing, spans, subagents, beta]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [sdk]
requires: "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1; hook spans need ENABLE_BETA_TRACING_DETAILED=1 and BETA_TRACING_ENDPOINT"
identifiers:
  - "claude_code.interaction"
  - "claude_code.llm_request"
  - "claude_code.tool"
  - "claude_code.tool.blocked_on_user"
  - "claude_code.tool.execution"
  - "claude_code.hook"
  - "ENABLE_BETA_TRACING_DETAILED"
  - "BETA_TRACING_ENDPOINT"
  - "session.id"
  - "OTEL_METRICS_INCLUDE_SESSION_ID"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, each step of the agent loop becomes a span. Tracing is in beta: span names and attributes may change between releases.

# How to use it

| Span | Wraps |
| - | - |
| `claude_code.interaction` | one turn, from prompt to response |
| `claude_code.llm_request` | each Claude API call, with model name, latency and token counts |
| `claude_code.tool` | each tool invocation; child spans `claude_code.tool.blocked_on_user` (permission wait) and `claude_code.tool.execution` |
| `claude_code.hook` | each hook execution; needs detailed beta tracing (`ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT`), a pair that also changes where logs and traces go |

`llm_request`, `tool` and `hook` spans are children of the enclosing `claude_code.interaction`. A subagent spawned via the Agent tool nests its `llm_request` and `tool` spans under the parent's `claude_code.tool` span, so the delegation chain is one trace.

Spans carry `session.id` by default; filter on it to see several `query()` calls of one session as a timeline. It is omitted if `OTEL_METRICS_INCLUDE_SESSION_ID` is set to a falsy value.
