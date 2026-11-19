---
type: "Reference"
title: "Tool annotations"
description: "Optional MCP hint fields on a tool (readOnlyHint and others); readOnlyHint lets calls run in parallel, and none are enforced."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [annotations, parallel, read-only, hints]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "annotations"
  - "ToolAnnotations"
  - "readOnlyHint"
  - "destructiveHint"
  - "idempotentHint"
  - "openWorldHint"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Metadata describing how a tool behaves. Pass as the fifth argument to `tool()` (as `{ annotations: {...} }`) in TypeScript, or the `annotations=ToolAnnotations(...)` keyword of `@tool` in Python. All fields are Booleans.

# How to use it

| Field | Default | Meaning |
| --- | --- | --- |
| `readOnlyHint` | `false` | Tool does not modify its environment; controls whether it can be called in parallel with other read-only tools |
| `destructiveHint` | `true` | Tool may perform destructive updates; set `true` explicitly on any tool marked `always_ask` |
| `idempotentHint` | `false` | Repeated calls with same arguments have no additional effect |
| `openWorldHint` | `true` | Tool reaches systems outside your process |

# Notes

Annotations are metadata, not enforcement: a `readOnlyHint: true` tool can still write if its handler does. Keep them accurate.
