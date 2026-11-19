---
type: "Reference"
title: "Tool decision event"
description: "claude_code.tool_decision: accept/reject with source, auto mode classifier verdict, permission mode and tool provenance."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, permissions, classifier, audit]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.301"
surfaces: [cli, headless, sdk]
requires: "classifier_verdict, classifier_category and permission_mode need Claude Code v2.1.301 or later"
identifiers:
  - "claude_code.tool_decision"
  - "decision"
  - "source"
  - "tool_source"
  - "classifier_verdict"
  - "classifier_category"
  - "permission_mode"
  - "user_permanent"
  - "user_temporary"
  - "user_abort"
  - "user_reject"
  - "sdk_host_builtin_mcp"
  - "OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Logged when a tool permission decision is made. It is the way to see refusals, including in unattended runs.

# How to use it

Attributes: `tool_name` (for user-configured MCP servers always the literal `mcp_tool`), `tool_use_id` (matches hooks), `request_id` (v2.1.310+), `decision` (`accept`/`reject`), `tool_source` (`builtin`, `mcp`, `sdk_host_builtin_mcp`: Claude Desktop's own in-process servers in sessions it owns; nested sessions report `mcp`), `source`, `classifier_verdict`, `classifier_category`, `permission_mode`, `tool_parameters` (with DETAILS; same shape as `tool_result` minus post-execution fields; may differ if `updatedInput` rewrote input).

| `source` | Meaning |
| - | - |
| `config` | Automatic: project settings, personal allow/deny rules, enterprise managed policy, `--allowedTools`/`--disallowedTools`, active permission mode, auto mode classifier, an earlier session-wide grant in the same interactive session, or inherently safe tool. Does not say which rule matched. Also reported when the permission prompt request itself fails (`canUseTool` callback or `--permission-prompt-tool` returns an invalid result, or input stream closes while pending) |
| `hook` | A `PreToolUse` or `PermissionRequest` hook decided |
| `user_permanent` | "Yes, and don't ask again" (saves an allow rule). Interactive CLI: only that choice; later matches emit `config`. In SDK or `-p`, choice and later rule matches both emit it. Accept |
| `user_temporary` | One-time "Yes" or session-scoped file grant; same CLI vs SDK/`-p` difference. Accept |
| `user_abort` | Prompt dismissed unanswered; in SDK/`-p` includes interrupting while a `canUseTool` or `--permission-prompt-tool` request is pending. Reject |
| `user_reject` | User chose "No". In SDK/`-p`, personal deny-rule matches also emit it (interactive emits `config`). Reject |

`classifier_verdict`: `allow`, `block` (a failing check can also end as block), `no_verdict` (no usable verdict, call denied), `unavailable` (classifier request failed, e.g. rate limit or timeout; also a server-side classifier review returning no safety verdict). Also appears on plan mode calls when the classifier reviews plan-mode commands. Absent when a permission rule decided, when auto mode approved without the classifier, when the user answered the prompt shown after repeated blocks, or in a `-p` run without `--permission-prompt-tool` where Claude Code denied after repeated blocks (that event: `decision` reject, `source` config).

`classifier_category` (with DETAILS): policy or built-in rule name in lowercase underscores, e.g. `data_exfiltration`, when verdict is `block` and exactly one recognized name was given. Before v2.1.302 absent on server-side-review blocks; before v2.1.323 absent on blocks naming a policy.

`permission_mode`: `default` (manual), `plan`, `acceptEdits`, `bypassPermissions`, `dontAsk`, `auto`; a subagent call reports the subagent's mode.

# Limits and defaults

If `OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT` is below the event's attribute count, the SDK drops in order: `parent_agent_id`, `agent_id`, `request_id`, `permission_mode`, `classifier_category`, `classifier_verdict` (the first three need v2.1.310+; the permission_mode/category/verdict order needs v2.1.302+).
