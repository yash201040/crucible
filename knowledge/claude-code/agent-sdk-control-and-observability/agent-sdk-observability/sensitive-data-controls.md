---
type: "Reference"
title: "Opt-in variables for sensitive telemetry content"
description: "OTEL_LOG variables that add prompts, tool details, tool output and raw API bodies to exports, with truncation limits and version gates."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [telemetry, privacy, logging, tool-content]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.214"
surfaces: [sdk]
requires: "Claude Code v2.1.214+ for content length cap; v2.1.283+ for MCP, WebFetch and WebSearch results in OTEL_LOG_TOOL_CONTENT"
identifiers:
  - "OTEL_LOG_USER_PROMPTS"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_LOG_TOOL_CONTENT"
  - "OTEL_LOG_RAW_API_BODIES"
  - "CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH"
  - "claude_code.user_prompt"
  - "claude_code.api_request_body"
  - "claude_code.api_response_body"
  - "classifier_category"
  - "tool.output"
  - "body_ref"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Telemetry is structural by default: durations, model names, tool names; token counts when the API returned usage (failed or aborted requests may omit them). Content your agent reads and writes is not recorded unless you opt in.

# How to use it

| Variable | Adds |
| - | - |
| `OTEL_LOG_USER_PROMPTS=1` | prompt text on `claude_code.user_prompt` events and the `claude_code.interaction` span |
| `OTEL_LOG_TOOL_DETAILS=1` | tool input arguments (file paths, shell commands, search patterns) on `claude_code.tool_result` events; real agent, skill, plugin and MCP server names on cost and token metrics; the auto mode classifier's rule as `classifier_category` on `claude_code.tool_decision` |
| `OTEL_LOG_TOOL_CONTENT=1` | a `tool.output` span event on `claude_code.tool` with file contents, Bash output, MCP/WebFetch/WebSearch results; truncated at 60 KB by default, configurable via `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`; requires tracing enabled |
| `OTEL_LOG_RAW_API_BODIES` | full Messages API request and response JSON as `claude_code.api_request_body` and `claude_code.api_response_body` events; `1` for inline bodies (60 KB default truncation) or `file:<dir>` for untruncated bodies on disk with a `body_ref` path |

# Limits and defaults

Raw bodies include the entire conversation history (extended-thinking content redacted), and enabling them implies consent to everything the other three would reveal. Leave all unset unless the pipeline is approved to store that data.
