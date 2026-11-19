---
type: "Reference"
title: "Decision control patterns by event"
description: "Which decision fields each hook event accepts (top-level decision, permissionDecision, decision.behavior, worktree path) and which events can rewrite content."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, decisions, permissions, rewrite]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "decision"
  - "reason"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "updatedInput"
  - "updatedToolOutput"
  - "decision.behavior"
  - "retry"
  - "worktreePath"
  - "displayContent"
  - "initialUserMessage"
  - "watchPaths"
  - "sessionTitle"
  - "reloadSkills"
  - "action"
  - "content"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Only some events let a hook block or steer via JSON, and each uses its own fields.

# How to use it

| Events | Pattern | Key fields |
| :- | :- | :- |
| `UserPromptSubmit`, `UserPromptExpansion`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Stop`, `SubagentStop`, `ConfigChange`, `PreCompact` | Top-level `decision` | `decision: "block"`, `reason`; `Stop`/`SubagentStop` also take `hookSpecificOutput.additionalContext` for non-error feedback that continues the conversation |
| `TeammateIdle`, `TaskCompleted` | Exit code or `decision` | Exit 2 or `decision: "block"` keeps teammate working / task open; with `continue: false` the teammate goes idle; `continue: false` ignored on a `TaskUpdate` call |
| `TaskCreated` | Exit code or `decision` | Exit 2 or `decision: "block"` cancels the task and returns the message to Claude; `continue: false` ignored |
| `PreToolUse` | `hookSpecificOutput` | `permissionDecision` (allow/deny/ask/defer), `permissionDecisionReason` |
| `PreModelSwitch` | `hookSpecificOutput` or `decision` | `permissionDecision` (allow/deny/ask), `permissionDecisionReason`; `decision: "block"` cancels the switch |
| `PermissionRequest` | `hookSpecificOutput` | `decision.behavior` (allow/deny) |
| `PermissionDenied` | `hookSpecificOutput` | `retry: true`; ignored for no-verdict denials |
| `WorktreeCreate` | path return | Command hook prints path on stdout; HTTP hook returns `hookSpecificOutput.worktreePath`; failure or missing path fails creation |
| `WorktreeRemove` | Exit code | Non-zero fails removal if directory remains; JSON discarded |
| `Elicitation`, `ElicitationResult` | `hookSpecificOutput` or `decision` | `action` (accept/decline/cancel), `content`; `decision: "block"` also declines |
| `MessageDisplay` | `hookSpecificOutput` | `displayContent` replaces displayed text only; transcript and Claude keep the original |
| `SessionStart`, `SubagentStart`, `PostModelSwitch` | Context only | `additionalContext`; `SessionStart` also `initialUserMessage`, `watchPaths`, `sessionTitle`, `reloadSkills`; no blocking |
| `Setup`, `Notification`, `SessionEnd`, `PostCompact`, `InstructionsLoaded`, `StopFailure`, `CwdChanged`, `DirectoryAdded`, `FileChanged` | None | Side effects only |

The only value of top-level `decision` is `"block"`; omit it (or exit 0 with no JSON) to allow.

# Limits and defaults

Rewrites: `PreToolUse` `hookSpecificOutput.updatedInput` replaces tool arguments before it runs; `PermissionRequest` `updatedInput` goes inside the `decision` object (and can apply permission rules so the user is not prompted again); `PostToolUse` `updatedToolOutput` replaces the tool result (ignored for `AskUserQuestion` and `ExitPlanMode` in a Cowork cloud session); `UserPromptSubmit` cannot replace the prompt, only add `additionalContext`. `PostToolUseFailure` cannot rewrite a result. For redaction use `PreToolUse` (outbound inputs) and `PostToolUse` (successful results).

# Notes

A hook can use `decision.behavior` allow with `updatedInput` such as `{"command":"npm run lint"}`. Reference implementation: Bash command validator example in the anthropics/claude-code repo (`examples/hooks/bash_command_validator_example.py`). See [exit code 2 behavior](./p1-exit-code-2-per-event.md).
