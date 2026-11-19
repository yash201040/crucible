---
type: "Reference"
title: "Notification hook and matcher values"
description: "Desktop-notification commands per OS and the Notification matcher values with versions where stated."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, notification, matchers, quota]
kind: "hook"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: "quota_auto_resume_* v2.1.234+; auth_storage_failure v2.1.288+; sandbox network permission_prompt v2.1.246+; teammate agent_needs_input v2.1.248+"
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
  - "autoContinueAtUsageLimit"
  - "osascript"
  - "notify-send"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `Notification` event fires when Claude waits for input or permission. An empty `matcher` fires on all types; set a notification type to narrow it. Per-OS commands: macOS `osascript -e 'display notification ...'` (Script Editor needs notification permission, else it fails silently); Linux `notify-send 'Claude Code' '...'` (needs a notification daemon and `libnotify-bin` on Debian/Ubuntu; absent on headless servers, SSH, most containers); Windows PowerShell `MessageBox` dialog (may open behind the terminal; WSL needs `powershell.exe` on `PATH`).

# How to use it

| Matcher | Fires when |
| --- | --- |
| `permission_prompt` | Claude needs approval of a tool use or a sandboxed command's network request and the prompt waited about six seconds |
| `idle_prompt` | Claude finished responding about 60 seconds ago and you have not typed |
| `auth_success` | Authentication completes |
| `auth_storage_failure` | Sign-in completes but credentials cannot be saved; fires in place of `auth_success` |
| `elicitation_dialog` | MCP server opens an elicitation form, no typing for about six seconds |
| `elicitation_url_dialog` | MCP server asks to open a browser URL, no typing for about six seconds |
| `elicitation_complete` | MCP server reports a URL-mode elicitation complete |
| `elicitation_response` | An MCP elicitation response is sent to the server |
| `agent_needs_input` | A background session waits on input while agent view is open; also a teammate terminal setup question or auto mode classifier-billing notice with no typing for about six seconds |
| `agent_completed` | A background session finishes or fails; only while agent view is open |
| `quota_auto_resume_fired` | Claude Code continues the task after a claude.ai usage limit paused it (at reset or sooner if usage becomes available) |
| `quota_auto_resume_stale` | Limit reset while the computer slept over about 30 minutes; waits for `Enter` (shorter sleep continues and fires `quota_auto_resume_fired`) |
| `quota_auto_resume_disabled` | Claude Code ends its wait without continuing: `autoContinueAtUsageLimit` off or reset more than 24 hours away, repeated limit hits, or continuation blocked. Not on `Esc`, `Ctrl+C` or **Don't continue automatically** |
| `plugin_notification` | A mod raises a notification with `$.ui.notify`; hook `title` is the mod name unless set |

# Limits and defaults

`permission_prompt` is timed differently in a terminal than in Claude Desktop, the VS Code extension and other Agent SDK hosts.
