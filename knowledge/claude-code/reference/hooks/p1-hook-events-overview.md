---
type: "Reference"
title: "Hook events and when they fire"
description: "All hook event names, the three cadences they fall into, and when each one fires."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, events, lifecycle, reference]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop, cloud]
requires: ""
identifiers:
  - "SessionStart"
  - "Setup"
  - "UserPromptSubmit"
  - "UserPromptExpansion"
  - "PreToolUse"
  - "PermissionRequest"
  - "PermissionDenied"
  - "PostToolUse"
  - "PostToolUseFailure"
  - "PostToolBatch"
  - "Notification"
  - "MessageDisplay"
  - "SubagentStart"
  - "SubagentStop"
  - "TaskCreated"
  - "TaskCompleted"
  - "Stop"
  - "StopFailure"
  - "TeammateIdle"
  - "InstructionsLoaded"
  - "ConfigChange"
  - "CwdChanged"
  - "DirectoryAdded"
  - "FileChanged"
  - "WorktreeCreate"
  - "WorktreeRemove"
  - "PreCompact"
  - "PostCompact"
  - "PreModelSwitch"
  - "PostModelSwitch"
  - "Elicitation"
  - "ElicitationResult"
  - "SessionEnd"
  - "--init-only"
  - "--init"
  - "--maintenance"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks are user-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts or subagents that run automatically at set points in the Claude Code lifecycle. The same events fire in the terminal, IDE extensions, the Desktop app and cloud sessions. When an event fires and a matcher matches, Claude Code passes JSON about the event to the handler (stdin for command hooks, POST body for HTTP hooks).

Three cadences:
- per session: `SessionStart`, `SessionEnd`
- per turn: `UserPromptSubmit`, `Stop`, `StopFailure`
- on every tool call in the agentic loop: `PreToolUse`, `PostToolUse` (`EndConversation` calls skip both)

A plugin can also register hooks as JavaScript functions run in Claude Code's own process; such a plugin is a mod, documented elsewhere (React to events). Those keep working alongside the hooks here.

# How to use it

| Event | When it fires |
| :- | :- |
| `SessionStart` | Session begins or resumes |
| `Setup` | Start with `--init-only`, or `--init` / `--maintenance` in `-p` mode; for one-time prep in CI or scripts |
| `UserPromptSubmit` | Prompt submitted, before Claude processes it; also on turns Claude Code starts on its own |
| `UserPromptExpansion` | A user-typed command expands into a prompt; can block the expansion |
| `PreToolUse` | Before a tool call runs; can block it |
| `PermissionRequest` | A tool call needs a permission decision |
| `PermissionDenied` | Auto mode denies a tool call (including denials without a classifier verdict); JSON `hookSpecificOutput.retry: true` tells the model it may retry; ignored when the classifier gave no verdict |
| `PostToolUse` | After a tool call succeeds |
| `PostToolUseFailure` | After a tool call fails |
| `PostToolBatch` | After a full batch of parallel tool calls resolves, before the next model call |
| `Notification` | Claude Code sends a notification |
| `MessageDisplay` | While assistant message text is displayed (display-only) |
| `SubagentStart` | A subagent is spawned |
| `SubagentStop` | A subagent finishes |
| `TaskCreated` | A task is being created via `TaskCreate` |
| `TaskCompleted` | A task is being marked completed |
| `Stop` | Claude finishes responding |
| `StopFailure` | The turn ends due to an API error |
| `TeammateIdle` | An agent-team teammate is about to go idle |
| `InstructionsLoaded` | A CLAUDE.md or `.claude/rules/*.md` file loads (at start and lazily) |
| `ConfigChange` | A configuration file changes during a session |
| `CwdChanged` | Working directory changes (for example a `cd`); useful with direnv |
| `DirectoryAdded` | A directory is added via `/add-dir` or the SDK `register_repo_root` control request |
| `FileChanged` | A watched file changes on disk; `matcher` names the files |
| `WorktreeCreate` | A worktree is being created via `--worktree`, `isolation: "worktree"`, or for a background session; replaces default git behavior |
| `WorktreeRemove` | A worktree created by a `WorktreeCreate` hook is being removed |
| `PreCompact` | Before context compaction |
| `PostCompact` | After compaction completes |
| `PreModelSwitch` | Before a requested model switch is applied; can block it |
| `PostModelSwitch` | After the session model changes, including self-made changes such as restoring the model on resume |
| `Elicitation` | An MCP server requests user input during a tool call |
| `ElicitationResult` | After the user answers an MCP elicitation, before the reply goes to the server |
| `SessionEnd` | Session terminates |

# Notes

`PreModelSwitch` is a standalone sequential event; `PostModelSwitch`, `Notification`, `ConfigChange`, `InstructionsLoaded`, `CwdChanged`, `FileChanged`, `DirectoryAdded` are standalone asynchronous events in the lifecycle diagram. `PermissionDenied` branches from `PermissionRequest` for auto-mode denials. See [exit-code behavior per event](./p1-exit-code-2-per-event.md) and [decision control](./p1-decision-control.md).
