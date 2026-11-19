---
type: "Reference"
title: "Hook events and when they fire"
description: "All hook event names with their trigger conditions, plus the five handler types."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, events, lifecycle, reference]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
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
  - "type: command"
  - "type: http"
  - "type: mcp_tool"
  - "type: prompt"
  - "type: agent"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When an event fires, Claude Code runs the matching hooks in parallel.

# How to use it

| Event | When it fires |
| --- | --- |
| `SessionStart` | Session begins or resumes |
| `Setup` | `--init-only`, or `--init` / `--maintenance` in `-p` mode; one-time preparation in CI or scripts |
| `UserPromptSubmit` | Prompt submitted, before processing; also on turns Claude Code starts on its own |
| `UserPromptExpansion` | A user-typed command expands into a prompt; can block |
| `PreToolUse` | Before a tool call; can block |
| `PermissionRequest` | A tool call needs a permission decision |
| `PermissionDenied` | Auto mode denies a call (including without a classifier verdict); JSON `hookSpecificOutput.retry: true` tells the model it may retry; ignored when the classifier produced no verdict |
| `PostToolUse` | After a tool call succeeds |
| `PostToolUseFailure` | After a tool call fails |
| `PostToolBatch` | After a full batch of parallel tool calls resolves, before the next model call |
| `Notification` | Claude Code sends a notification |
| `MessageDisplay` | While assistant message text is displayed |
| `SubagentStart` / `SubagentStop` | A subagent is spawned / finishes |
| `TaskCreated` / `TaskCompleted` | A task is being created via `TaskCreate` / marked completed |
| `Stop` | Claude finishes responding |
| `StopFailure` | Turn ends due to an API error |
| `TeammateIdle` | An agent team teammate is about to go idle |
| `InstructionsLoaded` | A CLAUDE.md or `.claude/rules/*.md` file is loaded (session start and lazy loads) |
| `ConfigChange` | A configuration file changes during a session |
| `CwdChanged` | Working directory changes (e.g. a `cd`) |
| `DirectoryAdded` | Directory added mid-session via `/add-dir` or the SDK `register_repo_root` control request |
| `FileChanged` | A watched file changes on disk; `matcher` names files |
| `WorktreeCreate` | A worktree is being created via `--worktree`, `isolation: "worktree"`, or for a background session; replaces default git behavior |
| `WorktreeRemove` | A worktree a `WorktreeCreate` hook created is being removed |
| `PreCompact` / `PostCompact` | Before / after context compaction |
| `PreModelSwitch` | Before a model switch you or a client requested; can block |
| `PostModelSwitch` | After the session model changes, including automatic restores on resume |
| `Elicitation` | MCP server requests user input during a tool call |
| `ElicitationResult` | After a user responds to an elicitation, before the reply goes to the server |
| `SessionEnd` | Session terminates |

Handler types (`"type"`): `command` (shell command; most common), `http` (POST event data to a URL), `mcp_tool` (call a tool on a configured MCP server), `prompt` (single-turn LLM evaluation), `agent` (multi-turn verification with tool access; experimental).
