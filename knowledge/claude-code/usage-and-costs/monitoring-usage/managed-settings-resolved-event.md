---
type: "Reference"
title: "Managed settings resolved event"
description: "claude_code.managed_settings_resolved reports managed sources, policy helper state and why a session refused to start."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, managed-settings, policy, audit]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [cli]
requires: "Claude Code v2.1.274 or later"
identifiers:
  - "claude_code.managed_settings_resolved"
  - "managed_settings.trigger"
  - "error.type"
  - "managed_settings.sources"
  - "managed_settings.source_behavior"
  - "managed_settings.helper.state"
  - "managed_settings.helper.applied"
  - "managed_settings.helper.entry"
  - "managed_settings.helper.path"
  - "managed_settings.resolved_sha256"
  - "managed_settings.settings"
  - "managed_settings.settings_truncated"
  - "managedSourcesBehavior"
  - "policyHelper"
  - "allowedProviders"
  - "forceRemoteSettingsRefresh"
  - "requiredMinimumVersion"
  - "requiredMaximumVersion"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Logged with the managed settings a session resolved: at session start, when managed settings or the policy helper's state change mid-session, and when Claude Code refuses to start or ends the session. Use it to find machines on an unexpected managed source, failing helpers and refusal reasons. In an interactive session in an untrusted folder the refusal event is not exported.

# How to use it

By default it carries sources and helper state, not the settings. `OTEL_LOG_MANAGED_SETTINGS=1` adds `managed_settings.settings` and `managed_settings.resolved_sha256`; set it in managed settings, user settings, `--settings` or the launch environment, not project/local settings. Server-managed settings can set it without the security approval dialog.

| Attribute | Values |
| - | - |
| `managed_settings.trigger` | `startup`, `change` (only when an attribute differs from the last event; a changed setting value counts even with logging off), `refused` |
| `error.type` (refused only) | `helper_failed`, `policy_invalid`, `provider_not_allowed` (v2.1.285+; `allowedProviders`), `consent_rejected`, `force_refresh_failed` (`forceRemoteSettingsRefresh`), `gateway_rejected` (HTTP 403 from a Claude apps gateway), `version_below_minimum` (`requiredMinimumVersion`/`requiredMaximumVersion`), `_OTHER` |
| `managed_settings.sources` | array, highest priority first: `remote`, `plist`, `hklm`, `file`, `parent`, `hkcu` |
| `managed_settings.source_behavior` | `managedSourcesBehavior`: `first-wins` (default) or `merge` |
| `managed_settings.helper.state` | `ok`, `bad_path`, `not_a_file`, `exit_nonzero`, `timed_out`, `oversize`, `parse_failed`, `envelope_invalid`, `schema_rejected`, `none` |
| `managed_settings.helper.applied` | `output` or `none` |
| `managed_settings.helper.entry` | `policyHelper` when selected |
| `managed_settings.helper.path` | helper `path`, always present when a helper is selected |
| `managed_settings.resolved_sha256` | SHA-256 of resolved settings (sorted keys, no whitespace); same digest = same settings; absent on refused |
| `managed_settings.settings` | redacted shape as JSON, cut at 8 KB (then invalid JSON); `managed_settings.settings_truncated` Boolean |

# Notes

Redaction: declared setting names exported; undeclared keys left out; booleans, numbers and fixed-option strings (e.g. `permissions.defaultMode`) as-is; all other strings, env values, URLs, commands `"[REDACTED]"`; map entry names kept; lists keep length; `permissions.allow/deny/ask` rules shown as tool name with content redacted (e.g. `Read([REDACTED])`) for built-in or `mcp__` tools; hooks show `type` and `timeout`, other fields redacted.
