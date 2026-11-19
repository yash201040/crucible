---
type: "Reference"
title: "tool_input fields per tool"
description: "The tool_input fields that PreToolUse and PostToolUse hooks receive for Bash, PowerShell, Write, Edit, Read, Glob, Grep, WebFetch, WebSearch, AskUserQuestion, ExitPlanMode."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, tool-input, reference, tools]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "Bash"
  - "PowerShell"
  - "Write"
  - "Edit"
  - "Read"
  - "Glob"
  - "Grep"
  - "WebFetch"
  - "WebSearch"
  - "AskUserQuestion"
  - "ExitPlanMode"
  - "command"
  - "run_in_background"
  - "file_path"
  - "old_string"
  - "new_string"
  - "replace_all"
  - "output_mode"
  - "multiline"
  - "allowed_domains"
  - "blocked_domains"
  - "mode"
  - "questions"
  - "answers"
  - "plan"
  - "planFilePath"
  - "allowedPrompts"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `tool_input` object differs per tool. Fields below are what a hook sees (the `Agent` tool is in [Agent tool input and response](./p2-agent-tool-hook-fields.md)).

# How to use it

| Tool | Fields (type) |
| :- | :- |
| `Bash` | `command` (string), `description` (optional), `timeout` (ms, optional; values above the maximum are reduced, not rejected), `run_in_background` (boolean) |
| `PowerShell` | Same as Bash: `command`, `description`, `timeout`, `run_in_background` |
| `Write` | `file_path` (absolute), `content` |
| `Edit` | `file_path`, `old_string`, `new_string`, `replace_all` (boolean) |
| `Read` | `file_path`, `offset` (optional line), `limit` (optional lines) |
| `Glob` | `pattern`, `path` (optional; defaults to cwd) |
| `Grep` | `pattern` (regex), `path`, `glob`, `output_mode` (`"content"`, `"files_with_matches"` default, `"count"`), `-i` (boolean), `multiline` (boolean) |
| `WebFetch` | `url`, `prompt`, `offset` (optional chars to skip; v2.1.290 or later) |
| `WebSearch` | `query`, `allowed_domains`, `blocked_domains`, `mode` (`"standard"` lighter or `"extended"` full; sessions may not send it and then run the full search; v2.1.282 or later) |
| `AskUserQuestion` | `questions` (1-4 multiple-choice, each with `question`, `header`, `options`, optional `multiSelect`), `answers` (optional object mapping question text to chosen label; multi-select joined by commas; Claude never sets it, supply via `updatedInput`) |
| `ExitPlanMode` | `plan` (Markdown, injected from plan file), `planFilePath` (injected), `allowedPrompts` (deprecated, accepted but ignored; before v2.1.205 it carried prompt-based permissions). The literal model input is typically empty because Claude writes the plan to a file first |

In `PostToolUse` for `ExitPlanMode`, `tool_response` has `plan` and `filePath`; read `tool_response.plan` instead of re-reading the file.

# Notes

- Match `Bash|PowerShell` in hooks that inspect shell commands. On Windows where the PowerShell tool is enabled, Claude treats PowerShell as the primary shell; on Windows without Git Bash the tool is enabled automatically and the Bash tool is not registered at all, so a `Bash`-only matcher never fires.
