# usage-and-costs/monitoring-usage

* [Administrator configuration of telemetry](administrator-configuration.md) - Set OTel variables for all users via managed settings; repository settings cannot enable telemetry; OTEL_* variables are not passed to subprocesses.
* [API request, error, refusal and retry events](api-request-error-refusal-events.md) - claude_code.api_request, api_error, api_refusal and api_retries_exhausted events with cost, token, effort and refusal fields. **[high]**
* [Audit security events with OpenTelemetry](audit-security-events.md) - Attributing actions to users, auditing MCP activity, mapping security questions and egress paths to events, checking retention, SIEM export.
* [Backends, service resource attributes and privacy defaults](backends-service-info-privacy.md) - Backend choices per signal, resource attributes on all exports, ROI guide, Bedrock monitoring pointer and what is collected by default.
* [Telemetry from cloud sessions and Claude Tag](cloud-session-telemetry.md) - Where to set telemetry variables for cloud sessions, network reachability, and how to tell cloud and Claude Tag sessions apart.
* [Common OpenTelemetry configuration variables](common-configuration-variables.md) - Exporters, endpoints, protocols, headers, intervals, content-logging gates and limits shared by metrics, logs and traces. **[high]**
* [Compaction and subagent completed events](compaction-and-subagent-events.md) - claude_code.compaction and claude_code.subagent_completed events for context compaction and subagent rollups. **[high]**
* [Cost and token counter attributes](cost-and-token-counters.md) - Attributes on claude_code.cost.usage and claude_code.token.usage: model, query_source, effort, agent, skill, plugin and MCP attribution with redaction rules. **[high]**
* [Custom attributes via OTEL_RESOURCE_ATTRIBUTES](custom-resource-attributes.md) - Add team or cost-center attributes to all metrics and events; strict formatting rules apply.
* [Attribute telemetry to Desktop SSH sessions](desktop-ssh-attribution.md) - Name the remote machine of a Desktop SSH session with OTEL_RESOURCE_INCLUDE_HOST or a custom attribute set on that machine.
* [Detailed beta tracing](detailed-beta-tracing.md) - Debug-only tracing mode that adds hook spans and content attributes and exports to BETA_TRACING_ENDPOINT.
* [Dynamic OTLP headers via helper script](dynamic-headers.md) - otelHeadersHelper runs a script that prints JSON headers, refreshed periodically, for http protocols only.
* [Event correlation attributes](event-correlation-attributes.md) - prompt.id, event.sequence, message.uuid, request_id and client_request_id link events to prompts, transcripts and API calls. **[high]**
* [Example telemetry configurations](example-configurations.md) - Ready-made environment variable sets for console, OTLP gRPC, Prometheus, multi-exporter, split endpoints, metrics-only and logs-only.
* [Hook registered and execution events](hook-events.md) - hook_registered, hook_execution_start, hook_execution_complete and hook_plugin_metrics events for hook inventory and outcomes. **[high]**
* [Identify the machine a session ran on](host-name-and-id-attributes.md) - OTEL_RESOURCE_INCLUDE_HOST adds host.name and host.id resource attributes; includes a troubleshooting checklist.
* [Interpreting usage, cost and retry data](interpreting-usage-and-cost-data.md) - How to analyze tokens, cost, retries and tool events, and how Claude Code's input tokens map to GenAI conventions. **[high]**
* [Managed settings resolved event](managed-settings-resolved-event.md) - claude_code.managed_settings_resolved reports managed sources, policy helper state and why a session refused to start.
* [Metrics cardinality control](metrics-cardinality-control.md) - Environment variables that include or drop attributes on metrics and events to manage cardinality.
* [Exported metrics](metrics-list.md) - The eight claude_code.* metrics with units, plus session, lines-of-code, PR, commit, decision and active-time counter details. **[high]**
* [mTLS for the OTLP exporter](mtls-authentication.md) - Which client certificate variables apply per OTLP protocol, and which variable trusts the collector's CA.
* [How managed settings lock the OTLP destination](otlp-destination-locking.md) - When managed settings set OTLP variables, Claude Code removes conflicting developer-set endpoint, protocol and credential variables at startup.
* [Plugin, skill and at-mention events](plugin-skill-mention-events.md) - plugin_installed, plugin_loaded, skill_activated and at_mention events for inventory and usage of plugins and skills. **[high]**
* [Quick start for OpenTelemetry export](quick-start-telemetry.md) - Turn on OTel export with environment variables, choose exporters and verify that data arrives. **[high]**
* [Raw API request and response body events](raw-api-body-events.md) - api_request_body and api_response_body events, inline or file mode with index.jsonl, enabled by OTEL_LOG_RAW_API_BODIES.
* [Repository identity attributes](repository-attributes.md) - OTEL_METRICS_INCLUDE_REPOSITORY tags metrics and events with vcs.* attributes derived from the origin remote.
* [Retention sweep event](retention-sweep-event.md) - claude_code.retention_sweep reports cleanupPeriodDays cleanup of transcripts and data, including skip reasons.
* [Safety event (no longer sent)](safety-event-retired.md) - claude_code.safety_event categories and attributes; sent only by v2.1.307 through v2.1.311 and stopped from v2.1.312.
* [Permission mode, auth, MCP, error and survey events](session-lifecycle-events.md) - permission_mode_changed, auth, mcp_server_connection, internal_error and feedback_survey events.
* [Span hierarchy and span attributes](span-hierarchy-and-attributes.md) - Span tree (interaction, llm_request, tool, hook) and the attributes each span carries, including agent, workflow and token fields. **[high]**
* [Standard attributes on metrics and events](standard-attributes.md) - Attributes shared by all metrics and events, plus event-only attributes and gateway identity stamping. **[high]**
* [Tool decision event](tool-decision-event.md) - claude_code.tool_decision: accept/reject with source, auto mode classifier verdict, permission mode and tool provenance. **[high]**
* [Tool result event](tool-result-event.md) - claude_code.tool_result: emitted when a tool completes, with success, timing, decision source and git commit identity. **[high]**
* [Distributed traces (beta)](traces-beta.md) - Span tracing linking each prompt to its API requests, tools and subagents, with W3C trace-context propagation. **[high]**
* [User prompt and assistant response events](user-prompt-and-assistant-events.md) - claude_code.user_prompt and claude_code.assistant_response events and their attributes and redaction gates.
