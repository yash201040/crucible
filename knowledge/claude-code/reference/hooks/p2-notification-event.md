---
type: "Reference"
title: "Notification hook event and types"
description: "Notification hook matchers (permission_prompt, idle_prompt, quota_auto_resume_*, agent_*) with timing and version notes."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, notification, idle, usage-limits]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Notification"
  - "permission_prompt"
  - "idle_prompt"
  - "auth_success"
  - "auth_storage_failure"
  - "elicitation_dialog"
  - "elicitation_url_dialog"
  - "elicitation_complete"
  - "elicitation_response"
  - "agent_needs_input"
  - "agent_completed"
  - "quota_auto_resume_fired"
  - "quota_auto_resume_stale"
  - "quota_auto_resume_disabled"
  - "plugin_notification"
  - "notification_type"
  - "preferredNotifChannel"
  - "notifications_disabled"
  - "autoContinueAtUsageLimit"
  - "terminalSequence"
  - "CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when Claude Code sends notifications. Matches on notification type; omit the matcher for all types. Runs even with desktop notifications off (`preferredNotifChannel`, including `notifications_disabled`, changes only how you are alerted). Input adds `message`, optional `title`, `notification_type`. Hooks cannot block or modify notifications; `systemMessage` and `continue` are discarded but `terminalSequence` is still emitted. Intended for side effects such as forwarding to an external service.

# How to use it

| Matcher | Fires when |
| :- | :- |
| `permission_prompt` | Claude needs approval for a tool or a sandboxed command's network request, and the prompt has waited about six seconds |
| `idle_prompt` | Claude finished about 60 seconds ago and you have not typed; not sent while a background agent (e.g. background subagent) runs, nor while waiting for a usage limit reset |
| `auth_success` | Authentication completes |
| `auth_storage_failure` | Sign-in completes but credentials cannot be saved; fires instead of `auth_success` (v2.1.288 or later) |
| `elicitation_dialog` | MCP elicitation form opens and you have not typed for ~6 s |
| `elicitation_url_dialog` | MCP server asks you to open a browser URL, ~6 s idle |
| `elicitation_complete` | MCP server reports a URL-mode elicitation complete |
| `elicitation_response` | An MCP elicitation response is sent back |
| `agent_needs_input` | A background session waits on input while agent view is open in a terminal; also for an agent team teammate's terminal setup question (v2.1.248 or later) or auto mode classifier charge notice, after ~6 s idle |
| `agent_completed` | A background session finishes or fails; only while agent view is open in a terminal |
| `quota_auto_resume_fired` | Claude Code continues the task after a claude.ai usage limit pause (at reset, or sooner when usage becomes available) |
| `quota_auto_resume_stale` | Limit reset while the computer slept more than ~30 min; waits for `Enter`. Shorter sleep fires `_fired` instead |
| `quota_auto_resume_disabled` | Wait ended without continuing (`autoContinueAtUsageLimit` off, reset more than 24 h away, continued task kept hitting the limit, or continuation blocked); not on `Esc`/`Ctrl+C`/"Don't continue automatically" |
| `plugin_notification` | A mod raises `$.ui.notify`; hook `title` is the mod's name unless set |

The three `quota_auto_resume_*` types need v2.1.234 or later.

# Limits and defaults

- Timing: `permission_prompt`, `idle_prompt`, `elicitation_dialog`, `elicitation_url_dialog` share desktop-notification timing, so in terminals they appear only when you seem away. The six-second timer starts when the dialog appears and each keystroke defers it. A request arriving behind another open dialog keeps the gate, timed from arrival.
- Sessions hosted via the Agent SDK `canUseTool` callback (Claude Desktop, VS Code extension): `permission_prompt` fires about six seconds after the ask, not deferred by typing, and not at all if you or a PermissionRequest hook answer sooner. Set `CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS=1` to turn it off there. Before v2.1.233 it did not fire in these sessions.
- `permission_prompt` for a sandboxed command's network request in terminal sessions needs v2.1.246 or later.
