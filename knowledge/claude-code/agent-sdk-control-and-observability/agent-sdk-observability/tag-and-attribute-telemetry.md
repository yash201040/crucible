---
type: "Feature"
title: "Tag telemetry and attribute actions to end users"
description: "Override service.name and add resource attributes per call, including percent-encoded end-user and tenant IDs for audit trails."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [telemetry, resource-attributes, audit, multi-tenant]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "OTEL_SERVICE_NAME"
  - "OTEL_RESOURCE_ATTRIBUTES"
  - "enduser.id"
  - "tenant.id"
  - "claude_code.tool_decision"
  - "claude_code.tool_result"
  - "tool_decision"
  - "tool_result"
  - "mcp_server_connection"
  - "permission_mode_changed"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default `service.name` is `claude-code`. Override it and add resource attributes, applied to every span, metric and event, so you can filter by agent: `OTEL_SERVICE_NAME=support-triage-agent`, `OTEL_RESOURCE_ATTRIBUTES=service.version=1.4.0,deployment.environment=production`.

# How to use it

The CLI's identity attributes reflect the credential used to call Anthropic, not your end user. To attribute activity to end users, set per `query()` call `OTEL_RESOURCE_ATTRIBUTES` such as `enduser.id=<id>,tenant.id=<id>`, percent-encoding values first (`quote` in Python, `encodeURIComponent` in TypeScript) because commas, spaces and equals signs are reserved.

These events then form a per-user audit trail you can forward to a SIEM; they export as log records with a `claude_code.` prefix (for example `claude_code.tool_decision`):

| Event | Records |
| - | - |
| `tool_decision`, `tool_result` | each tool call, allowed or denied, and its result |
| `mcp_server_connection` | MCP connections and failures |
| `permission_mode_changed` | permission mode changes |
