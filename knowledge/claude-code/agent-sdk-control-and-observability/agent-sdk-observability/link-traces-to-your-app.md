---
type: "Feature"
title: "Trace context propagation into the CLI"
description: "The SDK injects TRACEPARENT and TRACESTATE so agent spans nest under your application's active span."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [tracing, w3c, traceparent, propagation]
kind: "behavior"
maturity: "beta"
since: "2.1.212"
surfaces: [sdk, headless]
requires: "tracing enabled"
identifiers:
  - "TRACEPARENT"
  - "TRACESTATE"
  - "trace_id"
  - "span_id"
  - "claude_code.tool.execution"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When `query()` is called while an OpenTelemetry span is active in your application, the SDK injects `TRACEPARENT` and `TRACESTATE` into the child process environment; the CLI's `claude_code.interaction` span becomes a child of your span.

# How to use it

- OTLP event log records carry the same trace context (`trace_id`, `span_id`) when `TRACEPARENT` is set, so you can join events to spans. Before v2.1.212, event records outside an active span lacked `trace_id` and `span_id`.
- With propagation enabled the CLI also forwards `TRACEPARENT` to every Bash and PowerShell command; spans emitted by such a command nest under `claude_code.tool.execution`.
- Auto-injection is skipped if you set `TRACEPARENT` explicitly in `options.env`, to pin a parent context.

# Limits and defaults

Interactive CLI sessions ignore inbound `TRACEPARENT`; only Agent SDK and `claude -p` runs honor it.
