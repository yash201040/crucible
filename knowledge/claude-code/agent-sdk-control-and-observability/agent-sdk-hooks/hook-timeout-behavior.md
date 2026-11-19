---
type: "Limit"
title: "Hook timeouts and per-event outcomes"
description: "Default callback timeouts per event and what Claude Code does for each event when a callback times out."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, timeout, defaults, unattended]
kind: "limit"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [sdk]
requires: ""
identifiers:
  - "timeout"
  - "SessionEnd"
  - "error_during_execution"
  - "SDKInformationalMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

Set seconds with `timeout` on the `HookMatcher`. Defaults: 600 seconds for most events; 30 seconds for `UserPromptSubmit`, `PreModelSwitch`, `PostModelSwitch`; 10 seconds for `MessageDisplay`. `SessionEnd` callbacks run during shutdown under the shorter SessionEnd timeout budget, 1.5 seconds by default.

When a callback times out, Claude Code cancels it, discards its output and the session continues. Outcome by event:

| Event | Result |
| - | - |
| `PreToolUse` | tool call blocked; tool result tells Claude the hook did not respond; another hook's deny still reaches Claude (timeout text may follow) |
| `PostToolUse`, `PostToolUseFailure` | tool result kept, turn continues |
| `UserPromptSubmit`, `UserPromptExpansion` | prompt blocked with a message naming the hook and timeout |
| `Stop`, `SubagentStop` | counts as no decision; stops as if allowed; other hooks' decisions still apply |
| `SessionStart` | counts as no output; other hooks' output used |
| `PreModelSwitch` | model switch blocked |
| `Notification`, `PreCompact`, `PostModelSwitch`, others | logged, continues; with `onFailure: "block"` a timeout on `PreCompact`, `Elicitation`, `WorktreeCreate` blocks |

The first time a `Stop` or `SessionStart` callback times out in the main session, an `SDKInformationalMessage` says the driving app did not respond; later timeouts do not repeat it.

# Notes

Version history: before v2.1.210 a `PreToolUse` timeout was reported to Claude as a user rejection, which made unattended sessions stop and wait; before v2.1.208 a timeout on `UserPromptSubmit` or `UserPromptExpansion` ended the query with `error_during_execution`, and a tool call could proceed if interrupted during a pending `PreToolUse` callback; before v2.1.273 a timed-out `Stop` or `SubagentStop` counted as a failed run and discarded other hooks' decisions. Interrupting the query now cancels the pending tool call. In TypeScript use the `AbortSignal` (third callback argument) to cancel gracefully.
