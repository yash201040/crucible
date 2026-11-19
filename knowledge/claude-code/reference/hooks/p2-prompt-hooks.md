---
type: "Feature"
title: "Prompt-based hooks and event support matrix"
description: "type: prompt hooks have an LLM return ok/reason; lists which events support which hook types and what ok:false does per event."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, prompt-hooks, llm, stop]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "prompt"
  - "$ARGUMENTS"
  - "model"
  - "timeout"
  - "continueOnBlock"
  - "ok"
  - "reason"
  - "impossible"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `type: "prompt"` hook sends the hook input and your prompt to a Claude model (by default the one used for background functionality), which returns structured JSON that Claude Code applies. Agent hooks (`type: "agent"`) are described in [Agent-based hooks](./p2-agent-hooks.md). The prompt can be a rule ("Block any Bash command that reads `.env` files") or a condition ("All unit tests pass").

# How to use it

Config: `{"type": "prompt", "prompt": "Evaluate if Claude should stop: $ARGUMENTS ..."}`.

| Field | Required | Description |
| :- | :- | :- |
| `type` | yes | `"prompt"` |
| `prompt` | yes | Text sent to the LLM; `$ARGUMENTS` injects the hook input JSON, appended if absent |
| `model` | no | Evaluation model; default is the background-functionality model |
| `timeout` | no | Seconds; default 30 |
| `continueOnBlock` | no | `true` feeds an `ok: false` reason back to Claude and continues instead of ending the turn; default `false` |

The model must answer `{"ok": true|false, "reason": "...", "impossible": true|false}`: `reason` required with `ok: false`; `impossible` optional, set with `ok: false` when the condition can never be met (on `Stop` and `SubagentStop` the turn then ends instead of feeding the reason back; ignored by agent hooks and other events).

Event support:
- All five types (`command`, `http`, `mcp_tool`, `prompt`, `agent`): `PermissionDenied`, `PostToolBatch`, `PostToolUse`, `PostToolUseFailure`, `PreToolUse`, `Stop`, `SubagentStop`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`, `UserPromptExpansion`, `UserPromptSubmit`.
- `PermissionRequest`: `command`, `http`, `mcp_tool`, `prompt`, not `agent` (skipped).
- `command`, `http`, `mcp_tool` only: `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `Elicitation`, `ElicitationResult`, `FileChanged`, `InstructionsLoaded`, `MessageDisplay`, `Notification`, `PostCompact`, `PostModelSwitch`, `PreCompact`, `PreModelSwitch`, `SessionEnd`, `StopFailure`, `SubagentStart`, `WorktreeCreate`, `WorktreeRemove`.
- `Setup`: only `command`. `SessionStart`: `command` and `mcp_tool` only.

`ok: false` by event:

| Event | Effect |
| :- | :- |
| `Stop`, `SubagentStop` | Reason fed back as next instruction and the turn continues (unless `impossible: true`, then the turn ends) |
| `PreToolUse` | Tool call denied; by default the turn ends with the reason as a warning line; `continueOnBlock: true` returns it to Claude as the tool error (like `permissionDecision: "deny"`) |
| `PostToolUse` | By default turn ends with warning; `continueOnBlock: true` feeds reason back and continues |
| `PostToolBatch`, `UserPromptSubmit`, `UserPromptExpansion` | Turn ends, reason as warning (these end the turn on `decision: "block"` regardless of `continue`) |
| `PostToolUseFailure`, `TaskCreated` | Reason returned to Claude as a tool error, turn continues, regardless of `continueOnBlock` |
| `TaskCompleted` on `TaskUpdate` | Claude gets the reason as the tool result; turn continues regardless |
| `TeammateIdle`, `TaskCompleted` at end of teammate's turn | Teammate goes idle with the reason in its transcript; `continueOnBlock: true` keeps it working |
| `PermissionRequest` | No effect; use a command hook returning `hookSpecificOutput.decision.behavior: "deny"` |
| `PermissionDenied` | No effect; output discarded (only `hookSpecificOutput.retry` is read, which prompt and agent hooks cannot set) |

# Limits and defaults

For finer control on any event use a command hook with the per-event fields.
