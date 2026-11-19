---
type: "Reference"
title: "Exit code 2 behavior per event"
description: "Table of which hook events can block and what exit code 2 does on each."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, exit-code-2, blocking, reference]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "PreToolUse"
  - "PermissionRequest"
  - "UserPromptSubmit"
  - "UserPromptExpansion"
  - "Stop"
  - "SubagentStop"
  - "TeammateIdle"
  - "TaskCreated"
  - "TaskCompleted"
  - "ConfigChange"
  - "PostToolBatch"
  - "PreCompact"
  - "PreModelSwitch"
  - "Elicitation"
  - "ElicitationResult"
  - "WorktreeCreate"
  - "WorktreeRemove"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Exit 2 means stop; effect depends on whether the event is blockable. If a hook exits 2 and also sets `continue: false`, check the exit-code-2 rules first.

# How to use it

| Event | Can block? | Exit 2 does |
| :- | :- | :- |
| `PreToolUse` | Yes | Blocks the tool call |
| `PermissionRequest` | No | Not honored; deny via the `decision` object |
| `UserPromptSubmit` | Yes | Blocks the prompt (never reaches Claude) |
| `UserPromptExpansion` | Yes | Blocks the expansion |
| `Stop` | Yes | Prevents Claude stopping; conversation continues |
| `SubagentStop` | Yes | Prevents the subagent stopping |
| `TeammateIdle` | Yes | Teammate keeps working |
| `TaskCreated` | Yes | Rolls back task creation |
| `TaskCompleted` | Yes | Prevents marking completed |
| `ConfigChange` | Yes | Blocks the change (except `policy_settings`) |
| `StopFailure` | No | Output and exit code ignored, except `terminalSequence` |
| `PostToolUse` | No | Shows stderr to Claude; tool already ran |
| `PostToolUseFailure` | No | Shows stderr to Claude |
| `PostToolBatch` | Yes | Stops the agentic loop before the next model call |
| `PermissionDenied` | No | Ignored; use `retry: true` JSON (ignored for no-verdict denials) |
| `Notification` | No | Ignored |
| `SubagentStart` | No | Stderr to user only |
| `SessionStart` | No | Stderr to user only |
| `Setup` | No | Ignored |
| `SessionEnd` | No | Stderr to user only |
| `CwdChanged` | No | Stderr to user only |
| `DirectoryAdded` | No | Stderr to debug log |
| `FileChanged` | No | Stderr to user only |
| `PreCompact` | Yes | Blocks compaction |
| `PostCompact` | No | Stderr to user only |
| `PreModelSwitch` | Yes | Blocks switch, shows stderr to user |
| `PostModelSwitch` | No | Stderr to user only |
| `Elicitation` | Yes | Declines the request, no dialog |
| `ElicitationResult` | Yes | Blocks response (becomes decline) |
| `WorktreeCreate` | Yes | Any non-zero exit fails creation |
| `WorktreeRemove` | Yes | Any non-zero exit fails removal if directory still exists |
| `InstructionsLoaded` | No | Ignored |
| `MessageDisplay` | No | Original text displayed |

# Notes

For `SessionStart`, `SubagentStart`, `PostModelSwitch`, exit-2 stderr is rendered in the transcript as a `<hook name> hook error` notice; Claude does not see it and the session proceeds. For `SubagentStart` the notice appears in the subagent's own transcript.
