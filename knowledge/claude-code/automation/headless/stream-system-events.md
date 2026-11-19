---
type: "Reference"
title: "Stream system events: api_retry, init, plugin_install"
description: "Fields of system/api_retry, system/init (plugins, mcp_servers and error arrays, capabilities) and system/plugin_install events."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, stream-json, init, api-retry, ci]
kind: "api"
maturity: "unlabelled"
since: "2.1.221"
surfaces: [headless, sdk]
requires: "Several fields need v2.1.221, v2.1.246, v2.1.261, v2.1.283"
identifiers:
  - "system/api_retry"
  - "system/init"
  - "system/plugin_install"
  - "plugin_errors"
  - "plugins"
  - "mcp_servers"
  - "mcp_server_errors"
  - "capabilities"
  - "interrupt_receipt_v1"
  - "interrupt_cancel_queued_v1"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL"
  - "MCP_TIMEOUT"
  - "hook_started"
  - "hook_progress"
  - "hook_response"
  - "permission_denied"
  - "permission_denials"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Events in `stream-json` output that report retries, session metadata and install progress.

# How to use it

`system/api_retry` is emitted before retrying a retryable API failure:

| Field | Type | Meaning |
| --- | --- | --- |
| `type` / `subtype` | `"system"` / `"api_retry"` | identifies event |
| `attempt` | integer | current attempt, from 1 |
| `max_retries` | integer | retries permitted for this cause |
| `retry_delay_ms` | integer | ms until next attempt |
| `error_status` | integer or null | HTTP status, `null` if no HTTP response |
| `no_response` | object, optional | when no response headers in time: `waited_ms`, `retry_wait_ms` (v2.1.261+) |
| `error` | string | `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `rate_limit`, `overloaded`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown` |
| `uuid`, `session_id` | string | event and session IDs |

From v2.1.246, when a 401 or 403 rejects an `apiKeyHelper` credential the first two retries are quiet (no event) but count toward `attempt`; events resume from the third consecutive retry.

`system/init` is the first event unless preceded by `plugin_install` events (when `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` is set) or `hook_started`/`hook_progress`/`hook_response` for `SessionStart` or `Setup` hooks. It reports model, tools, MCP servers and plugins, and an optional `capabilities` string array (e.g. `interrupt_receipt_v1`, `interrupt_cancel_queued_v1`) for feature detection; ignore unknown values.

CI gates on `system/init`: `plugins` (loaded: `name`, `path`); `plugin_errors` (`plugin`, `type`, `message`; omitted when empty; `path` for `--plugin-dir` failures needs v2.1.283+); `mcp_servers` (`name`, `status`); `mcp_server_errors` (`name`, `type`, `message`; type such as `unknown_type`, `url_missing_type`, `invalid_config`, `reserved_name`; omitted when empty, so fail on a non-empty array).

`system/plugin_install` (when `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` is set): `status` is `started`, `installed`, `failed` or `completed` (started/completed bracket the install; installed/failed per marketplace), plus optional `name` and `error`.

# Limits and defaults

- With `--mcp-config` and `-p`, Claude Code waits for pending servers before the first turn, up to `MCP_TIMEOUT` (30 seconds default; v2.1.221+). A remote server with a cached tool list skips the wait, shows `pending`, and connects on first call. Self-hosted environments use a shorter wait.
- Invalid `--mcp-config` entries are skipped and the run exits cleanly. A terminal run prints `Warning: 1 MCP server skipped due to invalid config:` to stderr; redirected or captured stderr gets no warning, only `mcp_server_errors`.
- With `stream-json`, permission denials appear as `permission_denied` system messages and the final result lists `permission_denials`.
