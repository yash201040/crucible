---
type: "Reference"
title: "User prompt and assistant response events"
description: "claude_code.user_prompt and claude_code.assistant_response events and their attributes and redaction gates."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, prompts, responses, redaction]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.user_prompt"
  - "claude_code.assistant_response"
  - "prompt_length"
  - "prompt"
  - "prompt_text"
  - "command_name"
  - "command_source"
  - "response_length"
  - "response"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Events exported when `OTEL_LOGS_EXPORTER` is set. All events carry the standard attributes plus `event.name`, `event.timestamp`, `event.sequence`.

# How to use it

`claude_code.user_prompt`: logged when a prompt is submitted, including turns Claude Code starts on its own. Attributes: `prompt_length`; `prompt` (redacted unless `OTEL_LOG_USER_PROMPTS=1`); `prompt_text` (same value and gate, for backends that nest dotted names and would lose `prompt` next to `prompt.id`; v2.1.287+); `message.uuid`; `command_name` (built-in and bundled names as-is, aliases as typed, custom/plugin/MCP collapse to `custom`/`mcp` unless `OTEL_LOG_TOOL_DETAILS=1`); `command_source` (`builtin`, `custom`, `mcp`; plugin commands report `custom`).

`claude_code.assistant_response`: logged after each API request that returns text; only text blocks, not thinking or tool-use. Attributes: `response_length`; `response` (truncated at the content limit; `<REDACTED>` unless `OTEL_LOG_ASSISTANT_RESPONSES=1`, which falls back to `OTEL_LOG_USER_PROMPTS` when unset); `model`; `request_id`; `message.uuid`; `query_source` (`repl_main_thread`, `compact`, or a subagent name).
