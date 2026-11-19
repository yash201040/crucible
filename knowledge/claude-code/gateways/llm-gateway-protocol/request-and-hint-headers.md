---
type: "Reference"
title: "Request headers and gateway hint headers"
description: "Headers Claude Code sends to a gateway, including session, agent and parent-agent IDs and the opt-in x-claude-code-* routing hint headers."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, headers, subagents, attribution, observability]
kind: "api"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli]
requires: "Claude Code v2.1.273 or later for hint headers; v2.1.283 for x-claude-code-prompt-id"
identifiers:
  - "Authorization"
  - "x-api-key"
  - "anthropic-version"
  - "anthropic-beta"
  - "x-claude-code-session-id"
  - "x-claude-code-agent-id"
  - "x-claude-code-parent-agent-id"
  - "CLAUDE_CODE_GATEWAY_HINT_HEADERS"
  - "x-claude-code-request-class"
  - "x-claude-code-agent-type"
  - "x-claude-code-compaction"
  - "x-claude-code-context-compacted"
  - "x-claude-code-prev-tool-durations"
  - "x-claude-code-prompt-id"
  - "ANTHROPIC_CUSTOM_HEADERS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Forward `anthropic-version` and `anthropic-beta` unchanged (plus `anthropic-workspace-id` for Claude Platform on AWS, and `Authorization` when the developer's claude.ai login authenticates to Anthropic). The rest may be consumed for routing, attribution and tracing.

# How to use it

| Header | Meaning |
| - | - |
| `Authorization`, `x-api-key` | Developer's gateway credential, in one or both depending on the variable |
| `anthropic-version` | Currently `2023-06-01` |
| `anthropic-beta` | Comma-separated capability values; forward verbatim, never allowlist values. With a claude.ai login it also carries an OAuth value; stripping it gives `401` |
| `x-claude-code-session-id` | Unique session ID; aggregate a session's requests without parsing bodies |
| `x-claude-code-agent-id` | Subagent that issued the request; only on requests from a spawned agent. Use with session ID to attribute cost to parallel agents |
| `x-claude-code-parent-agent-id` | Parent agent, only for nested agents |

Subagent IDs are fresh per spawn; agent-team teammates reuse a stable name-based ID across reconnections. An ID identifies an agent, not a person or device.

Hint headers (per-request facts for scheduling, caching, attribution; never prompt text; printable ASCII):

| Header | Value |
| - | - |
| `x-claude-code-request-class` | `main`, `subagent`, `workflow`, `compaction` or `auxiliary`; on every request |
| `x-claude-code-agent-type` | Built-in type (`Explore`, `Plan`, `general-purpose`), `custom`, `teammate` or `fork`; only on a subagent's own turns; user-chosen names never sent |
| `x-claude-code-compaction` | On the summarizing request: `auto`, `manual` (`/compact`) or `reactive`; `auto` also for idle compaction |
| `x-claude-code-context-compacted` | Once, on the first main request after compaction; cache keyed on the old prefix can be dropped |
| `x-claude-code-prev-tool-durations` | `<name>=<ms>;<name>=<ms>` e.g. `Bash=742;Read=9`; at most 32 entries and 4 KB (first kept); names percent-encoded; excludes permission prompts and hooks; never on compaction, side requests or a new prompt's first request |
| `x-claude-code-prompt-id` | Random UUID shared by requests serving one user prompt, including subagent turns (v2.1.283 or later) |

# Limits and defaults

`CLAUDE_CODE_GATEWAY_HINT_HEADERS`: sent by default on a direct Anthropic connection; off by default with a custom base URL; for other backends (Bedrock, Agent Platform, Foundry, Claude Platform on AWS) only when set to `1`. Setting `0` stops them everywhere. Treat headers and body fields as open lists and pass `anthropic-*` headers through when the upstream is Anthropic-format.
