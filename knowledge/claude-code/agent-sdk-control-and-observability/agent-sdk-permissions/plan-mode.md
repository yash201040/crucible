---
type: "Feature"
title: "Plan mode and auto-mode review"
description: "In plan mode file edits and AskUserQuestion reach canUseTool; with auto mode available a classifier reviews other calls."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, plan, classifier, planning]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "plan"
  - "useAutoModeDuringPlan"
  - "allowDangerouslySkipPermissions"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude explores and produces a plan. During planning, edits via Claude's file tools outside protected paths reach `canUseTool` even when an allow rule matches or a `PreToolUse` hook returns `allow`. `AskUserQuestion` also reaches it.

# How to use it

When auto mode is available, calls with no approving allow rule go to the auto-mode classifier instead of your callback: shell commands, web fetches, web searches, MCP tools their server marks read-only. This review is on by default; set `useAutoModeDuringPlan` to `false` in the `settings` option of `query()` or in user settings to turn it off (then web searches and read-only MCP calls reach your callback).

| Call during planning | Review on | Review off / auto unavailable |
| :- | :- | :- |
| Read-only shell command (`ls`) | runs, no callback | runs, no callback |
| Other shell command, no allow rule, not a critical-path removal | classifier decides | callback |
| `WebFetch` to a preapproved documentation domain | runs | runs |
| Other `WebFetch` | classifier decides | callback |

# Limits and defaults

TypeScript: `allowDangerouslySkipPermissions: true` with `permissionMode: 'plan'` still sends file edits to the callback.
