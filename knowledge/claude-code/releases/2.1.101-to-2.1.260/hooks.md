---
type: "Release Digest"
title: "Hooks (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on hook events, hook input and output fields and hook types."
resource: "https://code.claude.com/docs/en/changelog"
tags: [hooks, events, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "PreModelSwitch"
  - "PostModelSwitch"
  - "SessionStart"
  - "/cd"
  - "Setup"
  - "DirectoryAdded"
  - "register_repo_root"
  - "if"
  - "args"
  - "CLAUDE_PLUGIN_OPTION_<KEY>"
  - "Notification"
  - "agent_needs_input"
  - "agent_completed"
  - "Stop"
  - "SubagentStop"
  - "hookSpecificOutput.additionalContext"
  - "MessageDisplay"
  - "reloadSkills"
  - "hookSpecificOutput.sessionTitle"
  - "background_tasks"
  - "session_crons"
  - "/doctor"
  - "SubagentStart"
  - "terminalSequence"
  - "continueOnBlock"
  - "PostToolUse"
  - "effort.level"
  - "CLAUDE_EFFORT"
  - "hookSpecificOutput.updatedToolOutput"
  - "duration_ms"
  - "PostToolUseFailure"
  - "mcp_tool"
  - "hooks"
  - "PreCompact"
  - "allowManagedHooksOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.251 | 2026-08-28 | PreModelSwitch and PostModelSwitch hook events can block, confirm or annotate a model switch; SessionStart resume hooks receive session staleness and estimated re-cache cost | `PreModelSwitch`, `PostModelSwitch`, `SessionStart` |
| 2.1.246 | 2026-08-25 | /cd makes the new directory's project settings, hooks, .mcp.json servers, skills and agents take effect at once | `/cd` |
| 2.1.239 | 2026-08-21 | Remote sessions keep sending keep-alives during a long SessionStart or Setup hook | `SessionStart`, `Setup` |
| 2.1.229 | 2026-08-12 | Server-supplied Claude Code hooks supported for self-hosted runner sessions |  |
| 2.1.219 | 2026-07-24 | DirectoryAdded hook fires after /add-dir or SDK register_repo_root registers a working directory | `DirectoryAdded`, `register_repo_root` |
| 2.1.214 | 2026-07-18 | Single-segment dir/** hook if: conditions match only cwd/dir (use **/dir/** for any depth); SessionStart reports source fork for forked sessions | `if`, `SessionStart` |
| 2.1.207 | 2026-07-11 | Plugin hooks, monitors and headersHelper reject ${user_config.*} in shell-form commands; use exec-form args or $CLAUDE_PLUGIN_OPTION_<KEY> | `args`, `CLAUDE_PLUGIN_OPTION_<KEY>` |
| 2.1.198 | 2026-07-01 | Background agent notifications fire the Notification hook (agent_needs_input, agent_completed) | `Notification`, `agent_needs_input`, `agent_completed` |
| 2.1.163 | 2026-06-04 | Stop and SubagentStop hooks can return hookSpecificOutput.additionalContext to give feedback and keep the turn going | `Stop`, `SubagentStop`, `hookSpecificOutput.additionalContext` |
| 2.1.152 | 2026-05-27 | MessageDisplay hook event transforms or hides assistant text as displayed; SessionStart hooks can return reloadSkills: true and hookSpecificOutput.sessionTitle | `MessageDisplay`, `reloadSkills`, `hookSpecificOutput.sessionTitle` |
| 2.1.145 | 2026-05-19 | Stop and SubagentStop hook input includes background_tasks and session_crons | `background_tasks`, `session_crons` |
| 2.1.144 | 2026-05-19 | /doctor shows an exec-form example when a command hook lacks the command field | `/doctor` |
| 2.1.142 | 2026-05-14 | Prompt- or agent-type hooks on SessionStart, Setup or SubagentStart now give a clear use-a-command-hook error | `SessionStart`, `Setup`, `SubagentStart` |
| 2.1.141 | 2026-05-13 | terminalSequence field in hook JSON output emits notifications, titles and bells without a controlling terminal | `terminalSequence` |
| 2.1.139 | 2026-05-11 | Hook args: string[] exec form spawns the command without a shell; continueOnBlock for PostToolUse feeds the rejection reason back and continues | `args`, `continueOnBlock`, `PostToolUse` |
| 2.1.133 | 2026-05-07 | Hooks receive the effort level in effort.level and CLAUDE_EFFORT; Bash tool commands can read CLAUDE_EFFORT | `effort.level`, `CLAUDE_EFFORT` |
| 2.1.121 | 2026-04-28 | PostToolUse hooks can replace tool output for all tools via hookSpecificOutput.updatedToolOutput (was MCP-only) | `hookSpecificOutput.updatedToolOutput` |
| 2.1.119 | 2026-04-23 | PostToolUse and PostToolUseFailure hook inputs include duration_ms | `duration_ms`, `PostToolUseFailure` |
| 2.1.118 | 2026-04-23 | Hooks can invoke MCP tools directly with type mcp_tool | `mcp_tool` |
| 2.1.116 | 2026-04-20 | Agent frontmatter hooks fire when running as a main-thread agent via --agent | `hooks` |
| 2.1.105 | 2026-04-13 | PreCompact hooks can block compaction by exiting 2 or returning decision block | `PreCompact` |
| 2.1.101 | 2026-04-10 | An unrecognized hook event name in settings.json no longer discards the whole file; plugin hooks force-enabled by managed settings run under allowManagedHooksOnly | `allowManagedHooksOnly` |

# Not found in the documentation pages

These identifiers occur only in the release notes, not in the saved documentation pages:

- `hookSpecificOutput.sessionTitle`
- `hookSpecificOutput.updatedToolOutput`
