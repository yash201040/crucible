---
type: "Reference"
title: "SDK hook events and SDK support"
description: "Every hook event with whether the Python and TypeScript SDKs support it and what triggers it."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, events, python, typescript]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "PreToolUse"
  - "PostToolUse"
  - "PostToolUseFailure"
  - "PostToolBatch"
  - "UserPromptSubmit"
  - "UserPromptExpansion"
  - "MessageDisplay"
  - "Stop"
  - "StopFailure"
  - "SubagentStart"
  - "SubagentStop"
  - "PreCompact"
  - "PostCompact"
  - "PreModelSwitch"
  - "PostModelSwitch"
  - "PermissionRequest"
  - "PermissionDenied"
  - "SessionStart"
  - "SessionEnd"
  - "Notification"
  - "Setup"
  - "TeammateIdle"
  - "TaskCreated"
  - "TaskCompleted"
  - "Elicitation"
  - "ElicitationResult"
  - "ConfigChange"
  - "InstructionsLoaded"
  - "WorktreeCreate"
  - "WorktreeRemove"
  - "CwdChanged"
  - "FileChanged"
  - "DirectoryAdded"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Some hook events work in both SDKs; many are TypeScript-only. Event names are case-sensitive (`PreToolUse`, not `preToolUse`).

# How to use it

| Event | Python | TypeScript | Triggered by |
| - | - | - | - |
| `PreToolUse` | Yes | Yes | tool call request (can block or modify) |
| `PostToolUse` | Yes | Yes | tool execution result |
| `PostToolUseFailure` | Yes | Yes | tool execution failure |
| `PostToolBatch` | No | Yes | a full batch of tool calls resolves, once per batch before the next model call |
| `UserPromptSubmit` | Yes | Yes | a prompt is submitted, including a turn Claude Code starts on its own |
| `UserPromptExpansion` | No | Yes | a user-typed command or MCP prompt expands into a prompt; not when Claude invokes a skill itself |
| `MessageDisplay` | No | Yes | an assistant message with text completes, once per message; redact or reformat displayed text without changing the transcript |
| `Stop` | Yes | Yes | agent execution stop |
| `StopFailure` | No | Yes | turn ends with an API error instead of a normal stop |
| `SubagentStart` | Yes | Yes | subagent initialization |
| `SubagentStop` | Yes | Yes | subagent completion |
| `PreCompact` | Yes | Yes | conversation compaction request |
| `PostCompact` | No | Yes | compaction completes |
| `PreModelSwitch` | No | Yes | requested model switch, before it happens (can block) |
| `PostModelSwitch` | No | Yes | session model changes, including automatic fallback |
| `PermissionRequest` | Yes | Yes | a tool call needs a permission decision |
| `PermissionDenied` | No | Yes | auto mode denies a tool call, including denials without a classifier verdict; Claude Code ignores `retry: true` for no-verdict denials |
| `SessionStart` | No | Yes | session initialization |
| `SessionEnd` | No | Yes | session termination |
| `Notification` | Yes | Yes | agent status messages |
| `Setup` | No | Yes | session setup/maintenance |
| `TeammateIdle` | No | Yes | teammate becomes idle |
| `TaskCreated` | No | Yes | a task created via the `TaskCreate` tool |
| `TaskCompleted` | No | Yes | a task marked completed |
| `Elicitation` | No | Yes | an MCP server requests user input mid-task |
| `ElicitationResult` | No | Yes | a user responds to an MCP elicitation |
| `ConfigChange` | No | Yes | configuration file changes |
| `InstructionsLoaded` | No | Yes | a `CLAUDE.md` or rules file loads into context |
| `WorktreeCreate` | No | Yes | git worktree created |
| `WorktreeRemove` | No | Yes | a worktree created by a `WorktreeCreate` hook is being removed |
| `CwdChanged` | No | Yes | working directory changes |
| `FileChanged` | No | Yes | a watched file is modified, created or deleted |
| `DirectoryAdded` | No | Yes | a working directory is added during a session |

# Notes

Python has no `SessionStart` or `SessionEnd` callbacks; see [Python session hooks](./hook-troubleshooting.md).
