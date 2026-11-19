---
type: "Release Digest"
title: "Hooks, 2.1.296 to 2.1.328"
description: "Release-note changes to hook behaviour, hook events, onFailure, decisions, limits and HTTP hooks between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [hooks, pretooluse, permissionrequest, posttooluse, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "onFailure"
  - "mcp_tool"
  - "PostToolUse"
  - "PostToolBatch"
  - "PreToolUse"
  - "PermissionRequest"
  - "UserPromptSubmit"
  - "updatedToolOutput"
  - "updatedInput"
  - "decision"
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
  - "headers"
  - "FileChanged"
  - "watchPaths"
  - "SessionStart"
  - "Setup"
  - "setMode"
  - "if"
  - "Monitor"
  - "WorktreeCreate"
  - "--debug"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Added onFailure block for mcp_tool hooks, as for command and HTTP hooks: a hook whose call fails blocks the action. | `onFailure`, `mcp_tool` |
| 2.1.328 | 2026-11-19 | Code Mode no longer runs UserPromptSubmit hooks (managed ones too) on scripts' output; redact with a PostToolUse hook using updatedToolOutput. | `UserPromptSubmit`, `PostToolUse`, `updatedToolOutput` |
| 2.1.328 | 2026-11-19 | Managed PostToolUse hooks no longer fire for calls refused before they ran; PostToolBatch gets most, not marked as refused. | `PostToolUse`, `PostToolBatch` |
| 2.1.328 | 2026-11-19 | A shell command rewritten by a PermissionRequest hook to a sandbox-excluded command runs outside the sandbox. | `PermissionRequest` |
| 2.1.327 | 2026-11-17 | /status lists hook matchers that never match. | `/status` |
| 2.1.326 | 2026-11-16 | A hook's decision block holds in more cases, so a hook that always prints one may start blocking calls. | `decision` |
| 2.1.326 | 2026-11-16 | A PreToolUse hook's updatedInput is kept when more than one hook answers a call; exit 127 error says the check may not have run; failures show red, stops yellow in the transcript. | `PreToolUse`, `updatedInput` |
| 2.1.326 | 2026-11-16 | allowedHttpHookUrls and httpHookAllowedEnvVars apply differently to hooks from managed settings; HTTP hooks ignore Content-Length and Transfer-Encoding in headers. | `allowedHttpHookUrls`, `httpHookAllowedEnvVars`, `headers` |
| 2.1.326 | 2026-11-16 | Commands rewritten by a permission hook or SDK host while approving stay in the sandbox if the original was checked as sandboxed; the approver can add dangerouslyDisableSandbox true. | `dangerouslyDisableSandbox` |
| 2.1.323 | 2026-11-12 | If a tool's permission check fails after a PreToolUse hook returned allow, Claude Code decides as if no hook had answered. | `PreToolUse` |
| 2.1.323 | 2026-11-12 | If the permission check fails on input a PermissionRequest hook rewrote, Claude Code asks again or refuses where nobody can answer. | `PermissionRequest` |
| 2.1.323 | 2026-11-12 | Progress heartbeat every 30 seconds while hooks run long in claude -p and SDK sessions. | |
| 2.1.323 | 2026-11-12 | Cloud scheduled tasks: a PostToolUse hook from your settings can no longer replace the plan in ExitPlanMode's result. | `PostToolUse`, `ExitPlanMode` |
| 2.1.321 | 2026-11-09 | Cowork cloud sessions: a PostToolUse hook can no longer replace the answer to AskUserQuestion or ExitPlanMode's plan. | `PostToolUse`, `AskUserQuestion` |
| 2.1.321 | 2026-11-09 | Windows: FileChanged hooks no longer stop for watchPaths after the first shell command with a lowercase drive letter (fix). | `FileChanged`, `watchPaths` |
| 2.1.319 | 2026-11-06 | PostToolUse hooks run, with up to 10 seconds, on tool calls that finish after a new message interrupts the turn. | `PostToolUse` |
| 2.1.317 | 2026-11-03 | Added onFailure block for Agent SDK hook callbacks so a failing callback blocks the action. | `onFailure` |
| 2.1.314 | 2026-10-30 | Hook if conditions such as Monitor(tail *) match the Monitor tool's shell commands as Bash(tail *) matches Bash's. | `if`, `Monitor` |
| 2.1.314 | 2026-10-30 | Cowork cloud sessions: a hook's allow of an MCP tool call counts as no answer. | |
| 2.1.312 | 2026-10-27 | Prompt and agent hooks run at most 24 at a time per session plus 12 that waited longer than their event's timeout; timeout under 1 second counts as 1. | |
| 2.1.310 | 2026-10-23 | Windows: PreToolUse and PermissionRequest hooks no longer let a call through when Git Bash is missing and the command is only quoted strings. | `PreToolUse`, `PermissionRequest` |
| 2.1.305 | 2026-10-20 | VS Code shows a Running start-up hooks status while SessionStart or Setup hooks run. | `SessionStart`, `Setup` |
| 2.1.302 | 2026-10-16 | At most 12 prompt and agent hooks of one event run at a time; the rest wait. | |
| 2.1.300 | 2026-10-14 | updatedInput from PreToolUse and PermissionRequest hooks is validated like Claude's own input: unknown keys dropped, input the tool rejects denies the call. | `updatedInput` |
| 2.1.300 | 2026-10-14 | Cowork cloud sessions: a setMode update in a PermissionRequest hook's allow is ignored. | `setMode` |
| 2.1.299 | 2026-10-14 | UserPromptSubmit hooks run before a skill or custom slash command expands, so a blocking hook also stops its embedded shell commands; a skill's own frontmatter UserPromptSubmit hook first runs on the next prompt. | `UserPromptSubmit` |
| 2.1.299 | 2026-10-14 | Actions a plugin hook can block are refused when the hook cannot be handed them or cannot answer; Windows hooks with no shell block when Git for Windows is missing. | |
| 2.1.299 | 2026-10-14 | Plugin hooks and workflow scripts refuse values nested deeper than 28,000 levels (workflow scripts allowed 100,000). | |
| 2.1.296 | 2026-10-09 | --debug logs command, plugin, outcome and duration for command hooks on tool calls, prompts, SessionStart and Stop. | `--debug` |
