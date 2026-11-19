---
type: "Feature"
title: "Detailed beta tracing"
description: "Debug-only tracing mode that adds hook spans and content attributes and exports to BETA_TRACING_ENDPOINT."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [tracing, beta, debugging, hooks]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [cli, headless, sdk]
requires: "Interactive CLI sessions need the organization to be allowlisted; Agent SDK and -p sessions do not"
identifiers:
  - "ENABLE_BETA_TRACING_DETAILED"
  - "BETA_TRACING_ENDPOINT"
  - "claude_code.hook"
  - "claude_code.system_prompt"
  - "new_context"
  - "system_reminders"
  - "system_prompt_preview"
  - "user_system_prompt"
  - "tool_input"
  - "response.model_output"
  - "hook_event"
  - "hook_name"
  - "num_hooks"
  - "hook_definitions"
  - "num_success"
  - "num_blocking"
  - "num_non_blocking_error"
  - "num_cancelled"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Detailed beta tracing needs `ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT`, a pair that also changes where logs and traces go. Set them in shell, user or managed settings (both ignored in project/local settings). `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` alone does not produce the hook span. Warning from the docs: use only for debugging, not production; export volume is high and the content attributes are not part of the stable span schema.

# How to use it

`claude_code.hook` span (only in this mode): `hook_event` (e.g. `PreToolUse`), `hook_name` (e.g. `PreToolUse:Write`), `num_hooks`, `hook_definitions` [OTEL_LOG_TOOL_DETAILS], `duration_ms`, `num_success`, `num_blocking`, `num_non_blocking_error`, `num_cancelled`.

Content attributes (truncated at the content limit, 60 KB by default):

| Attribute | Span | Gate |
| - | - | - |
| `new_context` | `claude_code.interaction` (the prompt), `claude_code.llm_request` (new user messages and tool results) | `OTEL_LOG_USER_PROMPTS` |
| `system_reminders`, `system_prompt_preview` (first 500 chars), `user_system_prompt` (text from `systemPrompt` SDK option, `--system-prompt`, `--append-system-prompt`; once per session), `response.model_output` | `claude_code.llm_request` | `OTEL_LOG_USER_PROMPTS` |
| `new_context` (tool result) | `claude_code.tool` | `OTEL_LOG_TOOL_CONTENT` |
| `tool_input` | `claude_code.tool` | `OTEL_LOG_TOOL_DETAILS` |

With `OTEL_LOG_USER_PROMPTS=1` the `claude_code.system_prompt` event carries the complete system prompt (truncated), the first time each distinct prompt is sent and again after compaction.
