---
type: "Release Digest"
title: "Hooks, 2.1.261 to 2.1.295"
description: "Release-note entries for hook events, hook types, hook output handling and plugin/mod hook APIs from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [hooks, release-notes, prompt-hooks, permissions]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "onFailure"
  - "Stop"
  - "SubagentStop"
  - "PermissionRequest"
  - "PreToolUse"
  - "UserPromptSubmit"
  - "SessionStart"
  - "SessionEnd"
  - "TeammateIdle"
  - "WorktreeCreate"
  - "mcp_tool"
  - "hook_execution_complete"
  - "tool.check"
  - "turn.step"
  - "agent.spawn"
  - "serverToolUses"
  - "ceiling"
  - "agentId"
  - "/hooks"
  - "CLAUDE_PLUGIN_ROOT"
  - "claude plugin validate"
  - "gatingHooks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about hooks configured in settings, plugin hooks and the mod hook sites (`tool.check`, `turn.step`, `agent.spawn`). Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | `onFailure: "block"` on command and HTTP hooks: a hook that cannot start, times out or exits unexpectedly blocks the action instead of letting it through. | `onFailure` |
| 2.1.294 | 2026-10-08 | `prompt` hooks on Stop and SubagentStop written as instructions are judged better, so Claude is less likely to stop early. | `Stop`, `SubagentStop` |
| 2.1.292 | 2026-10-06 | `<system-reminder>` tags in a hook's output are escaped before reaching Claude. | |
| 2.1.292 | 2026-10-06 | Workflow agents go through the `agent.spawn` mod hook so a mod can refuse them. | `agent.spawn` |
| 2.1.290 | 2026-10-05 | `serverToolUses` added to the result of a mod's `turn.step` hook (API-run tool calls such as the advisor). | `turn.step`, `serverToolUses` |
| 2.1.290 | 2026-10-05 | `agentId` added to the `tool.check` plugin-hook event to tell subagent checks from the main session's. | `tool.check`, `agentId` |
| 2.1.290 | 2026-10-05 | `ceiling` added to the question and verdict a mod's `tool.check` hook reads (the approval an organization requires). | `tool.check`, `ceiling` |
| 2.1.290 | 2026-10-05 | `claude plugin validate` lists each gating hook a mod registers and whether it has a `.catch` (`gatingHooks` under `--json`). | `claude plugin validate`, `gatingHooks` |
| 2.1.290 | 2026-10-05 | Plugin hooks clip and log long text instead of refusing or dropping it silently. | |
| 2.1.290 | 2026-10-05 | TeammateIdle hooks no longer fire from an in-process teammate's subagents or forks. | `TeammateIdle` |
| 2.1.289 | 2026-10-03 | One agent id across plugin hook events; `agent.spawn` for teammates. | `agent.spawn` |
| 2.1.287 | 2026-10-01 | Whole-tool `Bash` allow rules and allowing hooks prompt for, not run, shell writes to files the file tools refuse outright (Anthropic profile store, host credentials file). | `Bash` |
| 2.1.286 | 2026-09-30 | `/hooks` opens on one list of configured hooks grouped by event. | `/hooks` |
| 2.1.284 | 2026-09-28 | A non-interactive first turn waits up to 2 s for MCP servers named by an `mcp_tool` hook. | `mcp_tool` |
| 2.1.281 | 2026-09-23 | Plugin hook-failure errors name the offending plugin; `claude plugin validate` warns when a shell-form hook leaves `${CLAUDE_PLUGIN_ROOT}` unquoted. | `${CLAUDE_PLUGIN_ROOT}`, `claude plugin validate` |
| 2.1.281 | 2026-09-23 | `/hooks` detail screen says the hook's kind and where to change it; notices for hooks-disabled, safe mode, managed-hooks-only clarified. | `/hooks` |
| 2.1.280 | 2026-09-22 | `PermissionRequest` hooks: an agent-type hook no longer runs there (it cannot allow or deny); an error points to command or http hooks. | `PermissionRequest` |
| 2.1.280 | 2026-09-22 | `hook_execution_complete` OpenTelemetry event gains output sizes and number of oversized outputs saved to file. | `hook_execution_complete` |
| 2.1.280 | 2026-09-22 | UserPromptSubmit hook timeout notice and debug log name the hook command that timed out. | `UserPromptSubmit` |
| 2.1.271 | 2026-09-14 | Spinner says a SessionStart, UserPromptSubmit, PreToolUse or SessionEnd hook is running with elapsed time; Esc cancels a prompt waiting on SessionStart. | `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `SessionEnd` |
| 2.1.268 | 2026-09-10 | `--continue` / `--resume` show the conversation immediately instead of waiting for SessionStart hooks. | `SessionStart` |
