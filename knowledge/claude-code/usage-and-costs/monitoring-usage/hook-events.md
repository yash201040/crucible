---
type: "Reference"
title: "Hook registered and execution events"
description: "hook_registered, hook_execution_start, hook_execution_complete and hook_plugin_metrics events for hook inventory and outcomes."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, hooks, inventory, audit]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude_code.hook_registered"
  - "claude_code.hook_execution_start"
  - "claude_code.hook_execution_complete"
  - "claude_code.hook_plugin_metrics"
  - "hook_type"
  - "hook_source"
  - "hook_matcher"
  - "managed_only"
  - "total_duration_ms"
  - "stdout_chars"
  - "additional_context_chars"
  - "system_message_chars"
  - "initial_user_message_chars"
  - "num_outputs_persisted"
  - "plugin_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Events describing configured hooks and their runs. One start and one complete event is logged per hook event, covering every matching hook.

# How to use it

- `claude_code.hook_registered`: once per configured hook at session start. `hook_event`, `hook_type` (`command`,`prompt`,`mcp_tool`,`http`,`agent`), `hook_source` (`userSettings`,`projectSettings`,`localSettings`,`flagSettings`,`policySettings`,`pluginHook`), `safe_mode` (v2.1.169+), `hook_matcher` (with DETAILS), `plugin.name` and `plugin_id_hash` (for `pluginHook`).
- `claude_code.hook_execution_start`: `hook_event`, `hook_name` (e.g. `PreToolUse:Write`), `num_hooks`, `managed_only` (`"true"` when only managed-policy hooks permitted), `hook_source` (`policySettings` or `merged`), `safe_mode`, `hook_definitions` (needs both detailed beta tracing and DETAILS).
- `claude_code.hook_execution_complete`: adds `num_success`, `num_blocking`, `num_non_blocking_error`, `num_cancelled`, `total_duration_ms`, and from v2.1.280 `stdout_chars`, `additional_context_chars`, `system_message_chars`, `initial_user_message_chars`, `num_outputs_persisted` (outputs over the 10,000-character cap saved to a file).
- `claude_code.hook_plugin_metrics`: only official-marketplace plugin hooks emit it, for per-invocation metrics (finding rates, costs, durations). `plugin_id` (`<name>@<marketplace>`), `hook_event`, up to 20 plugin-emitted keys matching `^[a-z][a-z0-9_]{0,39}$` with Boolean or number values.

# Notes

An HTTP hook's URL is not recorded by `OTEL_LOG_TOOL_DETAILS=1` alone; the configuration appears only in `hook_definitions`.
