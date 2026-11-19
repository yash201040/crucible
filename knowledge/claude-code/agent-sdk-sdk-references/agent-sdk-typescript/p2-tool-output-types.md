---
type: "Reference"
title: "Built-in tool output schemas"
description: "Output types returned by built-in tools, notably AgentOutput, WorkflowOutput, BashOutput, Cron outputs, Read variants and git operation metadata."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [tools, tool-output, agent-output, workflow, bash]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ToolOutputSchemas"
  - "AgentOutput"
  - "WorkflowOutput"
  - "BashOutput"
  - "MonitorOutput"
  - "FileReadOutput"
  - "FileEditOutput"
  - "GrepOutput"
  - "GlobOutput"
  - "CronCreateOutput"
  - "CronListOutput"
  - "ScheduleWakeupOutput"
  - "PushNotificationOutput"
  - "ReportFindingsOutput"
  - "ArtifactOutput"
  - "ProjectsOutput"
  - "RefreshMcpToolsOutput"
  - "ExitWorktreeOutput"
  - "async_launched"
  - "remote_launched"
  - "resolvedModel"
  - "modelsUsed"
  - "worktreePath"
  - "worktreeBranch"
  - "backgroundTaskId"
  - "gitOperation"
  - "nextFireAt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Result shapes for built-in tools, available as `tool_use_result` on user messages. Matching input types are in [the input schemas](./p2-tool-input-types.md).

# How to use it

- `AgentOutput` is discriminated on `status`: `completed` (`agentId`, `content`, `resolvedModel` v2.1.174+, `modelsUsed` only when a mid-run swap happened, v2.1.212+, `totalToolUseCount`, `totalDurationMs`, `totalTokens`, `usage`, `toolStats`, `prompt`, `worktreePath`/`worktreeBranch` when a worktree was kept), `async_launched` (`agentId`, `description`, `outputFile`, `canReadOutputFile?`), `remote_launched` (`taskId`, `sessionUrl`, `outputFile`). `usage` and `totalTokens` come from the subagent's final API request only, not the whole run. `usage.output_tokens_details.thinking_tokens` needs v0.3.228+; `fallback_credit` needs v0.3.285+. Guard optional fields.
- `WorkflowOutput`: `status` `async_launched|remote_launched`, `taskId`, `taskType` (`local_workflow|remote_agent`), `workflowName`, `runId` (pass as `resumeFromRunId`; absent for remote runs, where the cloud session URL is the handle), `summary`, `transcriptDir`, `scriptPath` (edit and pass back to rerun), `sessionUrl`, `warning`, `error`. Returns immediately and the result arrives later as a task completion. A script failing its syntax check returns `async_launched` with `error` set and never runs: check `error`.
- `BashOutput`: `stdout` (stdout+stderr merged), `stderr` (tool notices only), `backgroundTaskId`, `timedOutAfterMs` and `backgroundCwdHint` (v2.1.210+), `backgroundEndsWithFinalResponse` (v2.1.227+; set when a foreground subagent owns the backgrounded command, which ends with that subagent's run), `gitOperation` (`commit`, `push`, `branch`, `pr` with actions including `created`, `merged`, `reopened` v0.3.234+, `auto-merge-enabled`).
- `MonitorOutput`: `taskId`, `timeoutMs`, `persistent?`; stop early with `TaskStop`.
- `CronCreateOutput` / `CronListOutput`: `id`, `humanSchedule`, `recurring`, `durable`, `nextFireAt` (epoch ms with jitter; v0.3.299+ and v2.1.299+; never earlier than the call). `ScheduleWakeupOutput`: `scheduledFor`, `clampedDelaySeconds`, `wasClamped`, `stopped` (v2.1.202+), `cancelledWakeups` (v2.1.206+; recurring `/loop` cron is not cancelled by `stop: true`).
- `PushNotificationOutput`: `pushSent`, `localSent`, `disabledReason` (`config_off|user_present|no_transport`), `sentAt`.
- `Read` variants by `type`: `text` (with `truncatedByTokenCap`), `image`, `notebook`, `pdf`, `parts` (page images as image blocks; before v0.3.242 PDF content came in a separate user message), `file_unchanged`. `Write` returns `originalFile` null and empty patch above about 10 MB. `Grep` totals: `totalFiles` (v2.1.208+), `totalLines` (v2.1.210+), `timedOut` (v2.1.317+, results may be incomplete). `Glob`: `totalMatches`, `countIsComplete` (v2.1.191+).
- `ExitWorktree` returns `action`, `originalCwd`, `worktreePath`, `worktreeBranch`, `tmuxSessionName`, `discardedFiles`, `discardedCommits`. `RefreshMcpTools` returns per-server `status` `refreshed|error|not_connected`. `ArtifactOutput` returns `url`, `path`, `updated`, `warnings` or an `artifacts` list with `total` (v0.3.292+).
- `AskUserQuestionOutput` adds `response` (freeform reply) and `afkTimeoutMs`. `WebFetchOutput.artifactRead.seeded` v0.3.239+.

# Limits and defaults

`TodoWriteOutput`, `TaskCreate/Update/Get/List` outputs, `ExitPlanModeOutput`, MCP resource outputs and `ReportFindingsOutput` (v2.1.196+) are also exported; `McpOutput` is a string, content-block array or object and may be `undefined` at runtime.
