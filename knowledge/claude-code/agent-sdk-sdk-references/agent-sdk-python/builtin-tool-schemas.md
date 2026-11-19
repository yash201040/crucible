---
type: "Reference"
title: "Built-in tool input and output schemas"
description: "Input and output dict shapes for Claude Code built-in tools as seen in Python tool_use_result, with version gates and limits."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [tools, schemas, bash, monitor, tasks]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Agent"
  - "AskUserQuestion"
  - "Bash"
  - "Monitor"
  - "Edit"
  - "Read"
  - "Write"
  - "Glob"
  - "Grep"
  - "NotebookEdit"
  - "WebFetch"
  - "WebSearch"
  - "TodoWrite"
  - "TaskCreate"
  - "TaskUpdate"
  - "TaskGet"
  - "TaskList"
  - "TaskStop"
  - "ExitPlanMode"
  - "ListMcpResourcesTool"
  - "ReadMcpResourceTool"
  - "CLAUDE_CODE_ENABLE_TASKS"
  - "timeout_ms"
  - "truncatedByTokenCap"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Python SDK does not export types for built-in tool inputs and outputs; the page documents the dict shapes. Outputs are what you read from `UserMessage.tool_use_result`, with key names exactly as Claude Code emits them. Keys marked optional are omitted when they do not apply. The `Agent` tool is covered in [AgentDefinition and Agent tool](./agent-definition-and-agent-tool.md).

# How to use it

| Tool | Key input fields | Notable output or limits |
| :- | :- | :- |
| `Bash` | `command`, `timeout`, `description`, `run_in_background` | foreground `timeout` capped at 600000 ms by default; with `run_in_background` (Claude Code 2.1.285+) the limit is 1800000 when omitted, capped at 7200000 unless raised; output `stdout` (stdout and stderr merged), `stderr` (tool notices only), `interrupted`, `isImage`, `backgroundTaskId` |
| `Monitor` | exactly one of `command` (each stdout line is an event) or `ws` (`url`, `protocols`; each text frame is an event; needs Claude Code 2.1.195+); `description`, `timeout_ms` | `timeout_ms` default 300000, max 3600000, effective deadline at most 1800000; same permission rules as Bash for commands; output `taskId`, `timeoutMs`, `persistent` (False) |
| `Edit` | `file_path`, `old_string`, `new_string`, `replace_all` | `structuredPatch`, `userModified`, optional `gitDiff` |
| `Read` | `file_path`, `offset`, `limit` | types `text` (`truncatedByTokenCap` when over the token cap), `image` (jpeg, png, gif, webp), `notebook`, `pdf`, `parts` (PDF pages as images), `file_unchanged` |
| `Write` | `file_path`, `content` | `type` `create` or `update`, `structuredPatch`, `originalFile` |
| `Glob` | `pattern`, `path` | truncated at 100 files; `totalMatches`, `countIsComplete` need Claude Code 2.1.191+ |
| `Grep` | `pattern`, `path`, `glob`, `type`, `output_mode` (`content`, `files_with_matches`, `count`), `-i`, `-n`, `-B`, `-A`, `-C`, `context`, `-o`, `head_limit`, `offset`, `multiline` | `totalFiles` needs 2.1.208+, `totalLines` 2.1.210+, `timedOut` 2.1.317+ |
| `NotebookEdit` | `notebook_path`, `cell_id`, `new_source`, `cell_type`, `edit_mode` (`replace`, `insert`, `delete`) | old and new file content |
| `WebFetch` | `url`, `prompt`, `offset` (Python SDK 0.2.164+) | `bytes`, `code`, `result`, `durationMs` |
| `WebSearch` | `query`, `allowed_domains`, `blocked_domains` | `results`, `durationSeconds` |
| `AskUserQuestion` | 1 to 4 `questions`, each with `header` (max 12 chars) and 2 to 4 `options` (`label` 1 to 5 words), `multiSelect` | `answers` keyed by question text (multi-select comma-joined), `response`, `annotations`, `afkTimeoutMs` set when the dialog auto-resolved after user inactivity |
| `ExitPlanMode` | `plan` | `plan`, `isAgent`, `filePath`, `planWasEdited`, `awaitingLeaderApproval`, `requestId` |
| `ListMcpResourcesTool` | `server` | result is a list |
| `ReadMcpResourceTool` | `server`, `uri` | `contents` with `blobSavedTo` for binary saved to disk |
| `TaskStop` | `task_id` (`shell_id` deprecated) | `task_type`, `command` |

Task tools: `TaskCreate` (`subject`, `description`, `activeForm`, `metadata`), `TaskUpdate` (`taskId`, `status` of `pending`, `in_progress`, `completed`, `deleted`; `addBlocks`, `addBlockedBy`, `owner`), `TaskGet`, `TaskList`; `TodoWrite` (`todos` with `content`, `status`, `activeForm`).

# Limits and defaults

`TodoWrite`, `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList` are available by default only on Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.5 and earlier; on other models (including unrecognized ids) they need opt-in (see the todo-tracking page). This default applies from Claude Code 2.1.268 (TypeScript Agent SDK bundles it from 0.3.268). Where available, the four Task tools are provided, or `TodoWrite` instead when `CLAUDE_CODE_ENABLE_TASKS=0`.
