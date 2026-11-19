---
type: "Feature"
title: "PostToolUse hook event"
description: "Runs after a tool succeeds; can add feedback, replace the tool output Claude sees, and handle interrupts."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, posttooluse, tool-output, interrupts]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "PostToolUse"
  - "tool_response"
  - "duration_ms"
  - "decision"
  - "reason"
  - "additionalContext"
  - "updatedToolOutput"
  - "updatedMCPToolOutput"
  - "classifierContext"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs immediately after a tool completes successfully. Matches tool name like PreToolUse; omit the matcher or use `"*"` to run after any tool (the hook can discover changes itself, e.g. `git status --porcelain`, which also lists untracked files). For failed calls add the same hook under PostToolUseFailure. It does not fire for a file rewritten by a `Bash` command or an outside process, so use FileChanged for that.

# How to use it

Input adds `tool_input`, `tool_response` (structured Output object, schema depends on the tool; file-tool paths absolute with native separators; `mcp_server` for MCP tools), `tool_use_id`, optional `duration_ms` (excludes permission prompts and PreToolUse hooks).

| Output field | Description |
| :- | :- |
| `decision` | `"block"` adds `reason` next to the tool result; Claude still sees the original output |
| `reason` | Explanation shown to Claude on block |
| `additionalContext` | Added to Claude's context with the result |
| `classifierContext` | Note for the auto mode classifier, see [classifierContext](./p2-classifier-context.md); v2.1.236 or later |
| `updatedToolOutput` | Replaces the output sent to Claude; must match the tool's output shape (e.g. Bash: `stdout`, `stderr`, `interrupted`, `isImage`). In a Cowork cloud session ignored for `AskUserQuestion` and `ExitPlanMode` |
| `updatedMCPToolOutput` | MCP tools only; prefer `updatedToolOutput` |

# Limits and defaults

- `updatedToolOutput` changes only what Claude sees: the tool already ran, and telemetry (OpenTelemetry spans, analytics) records the original. A non-matching value for a built-in tool is ignored and the original used; MCP output is not schema-validated. Stripping error details can make Claude proceed on a false assumption. To stop a call use PreToolUse.
- After an interrupt: `Ctrl+Enter` ending the turn while a tool runs lets PostToolUse hooks run with 10 seconds to finish (acts as `Esc` if a `!` command was queued first or background tasks are disabled, e.g. `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`); `Enter` queues without interrupting, usual `timeout` applies; `Esc` cancels hooks at once. After 10 s a running command hook is killed regardless of `timeout`; use `async: true` for longer ones (they can then not block or rewrite). Before v2.1.319 the hooks did not start after a message interrupt.
