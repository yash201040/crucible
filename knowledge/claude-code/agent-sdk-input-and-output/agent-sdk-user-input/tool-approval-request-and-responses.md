---
type: "Reference"
title: "Tool approval arguments and response options"
description: "Arguments passed to canUseTool, common tool input fields, allow/deny return shapes, and the ways to respond including remembered rules."
resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
tags: [agent-sdk, permissions, allow-deny, permission-update]
kind: "api"
maturity: "unlabelled"
since: "2.1.207"
surfaces: [sdk]
requires: ""
identifiers:
  - "toolName"
  - "input"
  - "options.signal"
  - "options.suggestions"
  - "PermissionResultAllow"
  - "PermissionResultDeny"
  - "updatedInput"
  - "updated_input"
  - "updatedPermissions"
  - "updated_permissions"
  - "behavior"
  - "message"
  - "suppressAlwaysAllowRule"
  - "localSettings"
  - ".claude/settings.local.json"
  - "PermissionUpdate"
  - "ToolPermissionContext"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-user-input"
    resource: "https://code.claude.com/docs/en/agent-sdk/user-input"
    title: "Handle approvals and user input"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The contract of the `canUseTool` callback for tool approvals.

# How to use it

Arguments:

| Argument | Description |
| - | - |
| `toolName` | tool Claude wants to use, such as `"Bash"`, `"Write"`, `"Edit"` |
| `input` | tool parameters, varies by tool |
| `options` (TS) / `context` (Python) | optional `suggestions` (proposed `PermissionUpdate` entries to avoid re-prompting) and a cancellation signal; TS `signal` is an `AbortSignal`, Python's signal field is reserved for future use (`ToolPermissionContext`) |

Common input fields: `Bash` has `command`, `description`, `timeout`; `Write` has `file_path`, `content`; `Edit` has `file_path`, `old_string`, `new_string`; `Read` has `file_path`, `offset`, `limit`.

Return values:

| Response | Python | TypeScript |
| - | - | - |
| Allow | `PermissionResultAllow(updated_input=...)` | `{ behavior: "allow", updatedInput }` |
| Deny | `PermissionResultDeny(message=...)` | `{ behavior: "deny", message }` |

Ways to respond: approve as-is; approve with changes (modify the input; Claude is not told you changed it); approve and remember (echo a suggestion back in `updatedPermissions` / `updated_permissions`; a suggestion with destination `localSettings` writes the rule to `.claude/settings.local.json` so future sessions skip the prompt); reject (Claude sees the deny message); suggest an alternative (deny with guidance in the message); redirect entirely (send new instructions with streaming input).

# Limits and defaults

- Before v2.1.207, Claude Code rejected an allow result that omitted `updatedInput` and denied the call with a validation error.
- TS: skip the always-allow choice when options carry `suppressAlwaysAllowRule: true`; needs Agent SDK v0.3.268 or later, and the Python `context` does not carry it.
- The Python "approve and remember" example requires `claude-agent-sdk` 0.1.80 or later.
