---
type: "Reference"
title: "Span hierarchy and span attributes"
description: "Span tree (interaction, llm_request, tool, hook) and the attributes each span carries, including agent, workflow and token fields."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [tracing, spans, subagents, workflows, tokens]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cli, headless, sdk]
requires: "Tracing enabled"
identifiers:
  - "claude_code.interaction"
  - "claude_code.llm_request"
  - "claude_code.tool"
  - "claude_code.tool.blocked_on_user"
  - "claude_code.tool.execution"
  - "claude_code.hook"
  - "span.type"
  - "agent_id"
  - "parent_agent_id"
  - "workflow.run_id"
  - "workflow.name"
  - "query_source"
  - "query_source_safe"
  - "tool_name_safe"
  - "bash_command_class"
  - "bash_argv0"
  - "tool.output"
  - "gen_ai.request.attempt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each user prompt starts a `claude_code.interaction` root span; API calls, tool calls and hook executions are children. A tool span has two children: `claude_code.tool.blocked_on_user` (permission wait) and `claude_code.tool.execution`. When the Agent tool (or legacy Task tool) spawns a subagent, its `llm_request` and `tool` spans nest under the parent's `claude_code.tool` span. With `TRACEPARENT` set in Agent SDK and `claude -p`, the interaction span becomes a child of the caller's span. When a `PreToolUse` hook defers a tool call, the saved trace context lets the re-run tool's spans join the earlier turn's trace on resume.

Every span carries the standard attributes plus `span.type`. `llm_request`, `tool.execution` and `hook` set status `ERROR` on failure; others end `UNSET`.

# How to use it

| Span | Attributes (selection; gate in brackets) |
| - | - |
| `claude_code.interaction` | `user_prompt` [OTEL_LOG_USER_PROMPTS, else `<REDACTED>`], `user_prompt_length`, `interaction.sequence`, `parent.source` (`env` or `none`; v2.1.268+), `interaction.duration_ms` |
| `claude_code.llm_request` | `model`, `gen_ai.system` (`anthropic`), `gen_ai.request.model`, `query_source` [ENABLE_BETA_TRACING_DETAILED], `query_source_safe` (v2.1.268+), `agent_id`, `parent_agent_id`, `workflow.run_id` (prefixed `wf_`), `workflow.name` (user-authored names become `custom` unless OTEL_LOG_TOOL_DETAILS), `speed` (`fast`/`normal`), `effort` (`low`,`medium`,`high`,`xhigh`,`max`; v2.1.274+), `llm_request.context` (`interaction`,`tool`,`standalone`), `duration_ms`, `ttft_ms`, `first_content_ms` (v2.1.268+), `input_tokens` (excludes cache), `output_tokens`, `cache_read_tokens`, `cache_creation_tokens`, `request_id`, `gen_ai.response.id`, `client_request_id`, `attempt`, `success`, `status_code`, `error`, `error_class` (v2.1.268+, e.g. `api_timeout`, `server_overload`), `response.has_tool_call`, `stop_reason` (`end_turn`,`tool_use`,`max_tokens`,`stop_sequence`,`pause_turn`,`refusal`), `gen_ai.response.finish_reasons`. Retries are `gen_ai.request.attempt` span events |
| `claude_code.tool` | `tool_name`, `tool_name_safe` (MCP names show `mcp_other`; v2.1.268+), `bash_command_class`, `bash_argv0` (v2.1.268+), `duration_ms`, `result_tokens`, `agent_id`, `parent_agent_id`, `workflow.run_id`, `workflow.name`, `tool_use_id`, `gen_ai.tool.call.id`; gated by OTEL_LOG_TOOL_DETAILS: `file_path`, `full_command`, `skill_name`, `subagent_type` |
| `claude_code.tool.blocked_on_user` | `duration_ms`, `decision` (`accept`,`reject`,`cancelled`), `source` (`config`,`hook`,`user_temporary`, or for cancelled e.g. `user_abort`) |
| `claude_code.tool.execution` | `duration_ms`, `tool_use_id`, `gen_ai.tool.call.id`, `success`, `error`, `error_class` (v2.1.268+) |

`agent_id` is absent on the main session; `parent_agent_id` is absent for the main session and for agents spawned directly from it.

# Notes

`tool.output` span event: with `OTEL_LOG_TOOL_CONTENT=1`, Read and Bash calls can record it on the tool span; Edit and Write only when `OTEL_LOG_TOOL_DETAILS=1` also set; MCP tools, WebFetch and WebSearch record it from v2.1.283. Attributes: `content` (Read text or Write text; Write needs DETAILS), `output` (Bash combined output, or MCP/WebFetch/WebSearch result with `[image]` placeholders), `diff` (Edit, DETAILS), `file_path` (DETAILS), `bash_command` (DETAILS). Truncated attributes get `<attribute>_truncated` and `<attribute>_original_length`. No event for: other tools, Read returning non-text or unchanged re-reads, Edit/Write without DETAILS, a WebFetch/WebSearch moved to background, or any call that raised an error.
