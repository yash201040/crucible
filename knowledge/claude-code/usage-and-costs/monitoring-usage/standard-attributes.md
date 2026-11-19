---
type: "Reference"
title: "Standard attributes on metrics and events"
description: "Attributes shared by all metrics and events, plus event-only attributes and gateway identity stamping."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, attributes, identity, correlation]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "session.id"
  - "ccr.session.id"
  - "app.version"
  - "app.entrypoint"
  - "organization.id"
  - "user.account_uuid"
  - "user.account_id"
  - "user.id"
  - "user.email"
  - "terminal.type"
  - "user.groups"
  - "identity.source"
  - "prompt.id"
  - "workspace.host_paths"
  - "workflow.run_id"
  - "workflow.name"
  - "agent_id"
  - "parent_agent_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Attributes attached to every metric and event.

# How to use it

| Attribute | Meaning / control |
| - | - |
| `session.id` | Claude Code's session ID; `/clear` replaces it. `OTEL_METRICS_INCLUDE_SESSION_ID` (default true) |
| `ccr.session.id` | Cloud session ID (`CLAUDE_CODE_REMOTE_SESSION_ID`); same switch |
| `app.version` | Claude Code version; `OTEL_METRICS_INCLUDE_VERSION` (default false) |
| `app.entrypoint` | `cli`, `sdk-cli`, `sdk-ts`, `sdk-py`, `claude-vscode`, `claude-desktop`, `claude-desktop-3p`, `claude-in-slack`; cloud values include `remote`, `remote_desktop`, `remote_mobile`; `OTEL_METRICS_INCLUDE_ENTRYPOINT` (default false) |
| `organization.id` | Organization UUID when authenticated; always included when available |
| `user.account_uuid`, `user.account_id` | Account IDs (the latter in tagged form like `user_01BWBeN28...`); `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default true) |
| `user.id` | Random anonymous ID generated on first run and stored in `~/.claude.json`; always included |
| `user.email` | From sign-in or cloud session credentials; always when available |
| `terminal.type` | e.g. `iTerm.app`, `vscode`, `cursor`, `tmux` |
| `OTEL_RESOURCE_ATTRIBUTES` keys | `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES` (default true) |
| `vcs.repository.url.full`, `vcs.owner.name`, `vcs.repository.name`, `vcs.provider.name` | `OTEL_METRICS_INCLUDE_REPOSITORY` (default false; v2.1.269+) |

Event-only attributes (never on metrics, to avoid unbounded cardinality): `prompt.id` (UUID per prompt), `workspace.host_paths` (desktop workspace directories), `workflow.run_id` (prefixed `wf_`, on API and tool events of agents in a Workflow tool run, including agents those spawn; matches the run ID in the Workflow tool result), `workflow.name` (script `meta.name`; user-authored and edited-copy names become `custom` unless `OTEL_LOG_TOOL_DETAILS=1`), `agent_id` (subagent ID like `a3f2c1b4d5e6f7a80`; on subagent API/tool events, `assistant_response` and `subagent_completed`; absent on main-session and in-process teammate events; span form may add a label e.g. `acompact-...`; v2.1.310+), `parent_agent_id` (ID of the agent that spawned or last resumed the subagent; absent when that is the main session; v2.1.310+).

# Notes

In sessions signed in to a Claude apps gateway via `/login`, exports carry the authenticated identity: `user.id` is the IdP subject, `user.email` the signed-in email, `user.groups` the IdP groups (comma-separated), and `identity.source: gateway-oidc`. The gateway identity is applied last, so `user.*` and `identity.*` keys in `OTEL_RESOURCE_ATTRIBUTES` are ignored there. Events logged before sign-in (`managed_settings_resolved`, `plugin_loaded`, `mcp_server_connection`) carry the anonymous `user.id` and no `identity.source`.
