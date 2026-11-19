---
type: "Reference"
title: "Built-in tool input schemas"
description: "Input types for built-in tools exported from sdk-tools: Agent, Bash, Monitor, Workflow, tasks, cron, worktree, MCP resources, Artifact and more."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [tools, tool-input, agent-tool, workflow, scheduling, worktree]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Types exported from @anthropic-ai/claude-agent-sdk/sdk-tools"
identifiers:
  - "@anthropic-ai/claude-agent-sdk/sdk-tools"
  - "ToolInputSchemas"
  - "Agent"
  - "Task"
  - "AskUserQuestion"
  - "Bash"
  - "Monitor"
  - "TaskOutput"
  - "Edit"
  - "Read"
  - "Write"
  - "Glob"
  - "Grep"
  - "TaskStop"
  - "NotebookEdit"
  - "WebFetch"
  - "WebSearch"
  - "Workflow"
  - "TodoWrite"
  - "TaskCreate"
  - "TaskUpdate"
  - "TaskGet"
  - "TaskList"
  - "ExitPlanMode"
  - "EnterPlanMode"
  - "ListMcpResourcesTool"
  - "ReadMcpResourceTool"
  - "ReadMcpResourceDirTool"
  - "RefreshMcpTools"
  - "EnterWorktree"
  - "ExitWorktree"
  - "CronCreate"
  - "CronDelete"
  - "CronList"
  - "ScheduleWakeup"
  - "RemoteTrigger"
  - "PushNotification"
  - "ReportFindings"
  - "Artifact"
  - "Projects"
  - "ShowOnboardingRolePicker"
  - "REPL"
  - "CLAUDE_CODE_ENABLE_TASKS"
  - "CLAUDE_CODE_ENABLE_REFRESH_MCP_TOOLS"
  - "CLAUDE_CODE_REPL"
  - "run_in_background"
  - "isolation"
  - "resumeFromRunId"
  - "scriptPath"
  - "dangerouslyDisableSandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Input schemas (`ToolInputSchemas`) for Claude Code's built-in tools, useful for typing hook inputs and `canUseTool` calls. The `StructuredOutput` tool has no fixed type; its schema is built from `outputFormat`.

# How to use it

| Tool | Input fields and notes |
| :- | :- |
| `Agent` (alias `Task`, still accepted; init `tools` lists it as `Task`) | `description`, `prompt`, `subagent_type?`, `model?` (`sonnet|opus|haiku|fable`), `effort?`, `run_in_background?`, `name?`, `isolation?` (`worktree|remote`). `team_name` deprecated and ignored; `mode` deprecated and ignored from v2.1.212 (subagent runs in parent mode or its definition's `permissionMode`) |
| `Bash` | `command`, `timeout?` ms (foreground capped at 600000; with `run_in_background` on v2.1.285+: default 1800000, cap 7200000), `description?`, `run_in_background?`, `dangerouslyDisableSandbox?`. Working directory persists between commands; shell env state does not |
| `Monitor` | `description`, `timeout_ms` (default 300000, accepts up to 3600000, effective max 1800000), exactly one of `command` (one event per stdout line) or `ws` `{ url, protocols? }` (one event per text frame; v2.1.195+). Command follows Bash permission rules |
| `TaskOutput` | Removed in v2.1.277 with its type; a `disallowedTools` or deny rule naming it is silently ignored |
| `Edit` | `file_path`, `old_string`, `new_string`, `replace_all?` |
| `Read` | `file_path`, `offset?`, `limit?`, `pages?`, `allow_large?` (v0.3.296+ / v2.1.296) |
| `Write` | `file_path`, `content` |
| `Glob` / `Grep` | `pattern`, `path?`; Grep adds `glob`, `type`, `output_mode` (`content|files_with_matches|count`), `-i`, `-o`, `-n`, `-B`, `-A`, `-C`, `context`, `head_limit`, `offset`, `multiline` |
| `TaskStop` | `task_id?`, `shell_id?` (deprecated); from v2.1.198 accepts teammate or named background agent ID or name |
| `NotebookEdit` | `notebook_path`, `cell_id?`, `new_source`, `cell_type?`, `edit_mode?` (`replace|insert|delete`) |
| `WebFetch` / `WebSearch` | `url`, `prompt`, `offset?` (v0.3.290+); `query`, `allowed_domains?`, `blocked_domains?` |
| `Workflow` | `script`, `name`, `scriptPath` (at least one; `scriptPath` wins, errors if session tools lack `Read`), `args`, `resumeFromRunId` (same session only), `title`/`description` ignored. Available in SDK v0.3.149+. Script begins with literal `export const meta = { name, description }` and uses `agent()`, `parallel()`, `pipeline()`, `phase()` |
| `TodoWrite`, `TaskCreate`, `TaskUpdate`, `TaskGet`, `TaskList` | Task tracking. `TaskUpdate` status `pending|in_progress|completed|deleted`, `addBlocks`, `addBlockedBy`, `owner`, `metadata` |
| `ExitPlanMode` / `EnterPlanMode` | `allowedPrompts` deprecated and ignored (before v2.1.205 requested Bash prompt permissions) |
| `ListMcpResourcesTool`, `ReadMcpResourceTool`, `ReadMcpResourceDirTool` | `server?`; `server`+`uri`. Directory listing is non-recursive and not enabled in every session |
| `RefreshMcpTools` | `server?`; registered only with `CLAUDE_CODE_ENABLE_REFRESH_MCP_TOOLS=1` in `env` and at least one MCP server; v2.1.211+ |
| `EnterWorktree` / `ExitWorktree` | `name?` or `path?` (mutually exclusive; path must be a registered worktree, or under `.claude/worktrees/` from within a worktree session); `action` `keep|remove`, `discard_changes?` required `true` to remove with uncommitted files or unmerged commits |
| `CronCreate` / `CronDelete` / `CronList` | `cron` (5-field, local time), `prompt`, `recurring?`, `durable?` (persists to `.claude/scheduled_tasks.json`; silently session-only when unavailable, read output `durable`); `id` |
| `ScheduleWakeup` | `delaySeconds` (clamped 60 to 3600), `reason`, `prompt`, `noop`, `stop` (v2.1.202+); backs self-paced `/loop` |
| `RemoteTrigger` | `action` `list|get|create|update|run|create_webhook_trigger|list_runs|get_run_log`, `trigger_id`, `session_id`, `cursor`, `body`. Manages cloud scheduled tasks (formerly routines), backs `/schedule`. `create_webhook_trigger` v2.1.225+; `list_runs`/`get_run_log` v2.1.227+. Only with a claude.ai account on a plan with cloud scheduled tasks; absent when org policy disables cloud sessions |
| `PushNotification` | `message` (under 200 chars), `status: "proactive"`; not available on Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform or Foundry |
| `ReportFindings` | `level?`, `findings[]` (max 32 per call; `file`, `line?`, `summary`, `failure_scenario`, `short_summary?` (60 chars, v2.1.212+), `category?` (v2.1.199+), `verdict?`, `outcome?`); v2.1.196+ |
| `Artifact` | `action` `publish|list`, `file_path`, `icon`, `title`, `url`, `force`, `capabilities`, `contract` (v0.3.235+), `limit` (1-200; above 50 needs v0.3.292+, default 25), `scope`. Off by default in SDK sessions; not publishable with API-key auth |
| `Projects` | `method` `project_info|project_read|project_search|project_write|project_delete`, `path`, `content`, `local_path`, `present_to_user`, `query`, `n` (default 5) |
| `ShowOnboardingRolePicker` | No arguments (Cowork onboarding) |
| MCP tools | `mcp__<server>__<tool>`, open object |

# Limits and defaults

`TodoWrite` and the four Task tools are available by default only on Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.5 and earlier models; on other models (including unrecognized IDs) opt in. Where available Claude Code provides the four Task tools, or `TodoWrite` when `CLAUDE_CODE_ENABLE_TASKS=0`. Applies from Claude Code v2.1.268 (SDK v0.3.268). `REPL` was removed in v2.1.275 (earlier enabled with `CLAUDE_CODE_REPL=1`, experimental).
