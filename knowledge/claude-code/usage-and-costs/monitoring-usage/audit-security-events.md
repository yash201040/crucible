---
type: "Guide"
title: "Audit security events with OpenTelemetry"
description: "Attributing actions to users, auditing MCP activity, mapping security questions and egress paths to events, checking retention, SIEM export."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [audit, siem, security, managed-settings]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_EXPORTER_OTLP_LOGS_ENDPOINT"
  - "sandbox.enabled"
  - "sandbox.failIfUnavailable"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.network.allowManagedDomainsOnly"
  - "sandbox.network.allowedDomains"
  - "allowedMcpServers"
  - "allowManagedMcpServersOnly"
  - "deniedMcpServers"
  - "managed-mcp.json"
  - "allowManagedHooksOnly"
  - "allowedHttpHookUrls"
  - "strictKnownMarketplaces"
  - "disableSideloadFlags"
  - "syncClaudeAiPlugins"
  - "syncClaudeAiSkills"
  - "permissions.deny"
  - "allowManagedPermissionRulesOnly"
  - "enableArtifact"
  - "disableRemoteControl"
  - "cleanupPeriodDays"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

OTel events are the audit data source. Every event carries identity (`user.email`, `user.account_uuid`, `user.account_id`, `organization.id`, `user.id`, `session.id`), so MCP calls, Bash commands and file edits are attributed to the developer who started the session (no separate service account); in Claude Tag channel sessions Claude acts as the shared identity. With a direct API key or Amazon Bedrock, Google Cloud's Agent Platform or Microsoft Foundry only `user.id` and `session.id` are populated; add identity with `OTEL_RESOURCE_ATTRIBUTES` such as `enduser.id=jdoe@example.com,enduser.directory_id=S-1-5-21-...`, per user via managed settings or a launch wrapper. Claude Code emits the raw stream only; anomaly detection and alerting are the backend's job.

# How to use it

MCP audit: enable the logs exporter and `OTEL_LOG_TOOL_DETAILS=1`. `mcp_server_connection` gives `server_name`, `transport_type`, `server_scope`, error; `tool_result` gives `tool_name`, `mcp_server_scope`, `tool_parameters` with `mcp_server_name`/`mcp_tool_name`, and `tool_input`; `tool_decision` gives the decision, its source and the names. Without DETAILS: names redacted to the literal `mcp_tool` for user-configured servers, no arguments, `mcp_server_connection` omits `server_name` and error but keeps `is_plugin`, `plugin_id_hash`, `plugin.name` (non-Anthropic redacted to `third-party`).

Security question to event: allowed/denied and why = `tool_decision` (`decision`, `source`, `classifier_verdict`, `permission_mode`); permission mode escalation = `permission_mode_changed`; policy hook blocked = `hook_execution_complete` (`num_blocking`, not tied to `tool_use_id`); call a hook refused = `tool_decision` with reject and `source` `hook`; login/auth failure = `auth`; MCP connect failure = `mcp_server_connection`; plugin installed = `plugin_installed`; commands and files = `tool_result`/`tool_decision` with DETAILS; managed sources and refusals = `managed_settings_resolved`. `safety_event` rows apply only to v2.1.307 through v2.1.311.

Egress paths, managed controls and events:

| Path | Managed controls | Events |
| - | - | - |
| Bash/PowerShell | `sandbox.enabled`, `sandbox.failIfUnavailable`, `sandbox.allowUnsandboxedCommands`, `sandbox.network.allowManagedDomainsOnly`, `sandbox.network.allowedDomains` | `tool_decision`, `tool_result` |
| MCP servers | `allowedMcpServers`, `allowManagedMcpServersOnly`, `deniedMcpServers`, `managed-mcp.json` | `mcp_server_connection`, `tool_decision`, `tool_result` |
| Hooks | `allowManagedHooksOnly`, `allowedHttpHookUrls` (entries merge across files, so a developer can add to an empty managed list; `allowManagedHooksOnly` decides which hooks run) | `hook_registered`, `hook_execution_start`, `hook_execution_complete` |
| Plugins | `strictKnownMarketplaces`, `disableSideloadFlags`, `syncClaudeAiPlugins`, `syncClaudeAiSkills` | `plugin_installed`, `plugin_loaded` |
| WebFetch | `permissions.deny`, `allowManagedPermissionRulesOnly` | `tool_decision`, `tool_result` |
| Tools uploading to claude.ai (e.g. Artifact) | `permissions.deny`, `enableArtifact` | `tool_decision`, `tool_result` |
| Remote Control | `disableRemoteControl` | no dedicated event |
| Local transcript retention | `cleanupPeriodDays` | `retention_sweep` |

Retention check: set `cleanupPeriodDays` in managed settings, collect `retention_sweep`. `result` skipped = sweep paused (see `skip_reason`); `used_default` true or `period_days` differing from managed value = not applied; `error_count` above 0 = leftovers possible; `files_past_cutoff` above 0 = failed deletions or stale synced skills/plugins folders; no event is not a failure by itself.

SIEM: point `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` at the SIEM's OTLP receiver or a collector. Example managed `env`: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_LOGS_EXPORTER=otlp`, `OTEL_LOG_TOOL_DETAILS=1`, `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf`, `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://siem.example.com:4318/v1/logs`, `OTEL_EXPORTER_OTLP_HEADERS=Authorization=Bearer ...`. Confirm with a `claude_code.user_prompt` event; else check `claude --debug-file <path>` for `[3P telemetry]` errors.

# Notes

`OTEL_LOG_TOOL_DETAILS=1` can expose the same sensitive content as the session; enable only for collectors approved to hold it.
