---
type: "Reference"
title: "Background session and agent view variables"
description: "Variables that turn off agent view and background sessions, control hand-off of in-flight work and wrap the processes Claude Code launches."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [agent-view, background-sessions, supervisor, wrapper]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.196"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_AGENT_VIEW"
  - "CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF"
  - "CLAUDE_CODE_DISABLE_BG_STABLE_PATH"
  - "CLAUDE_CODE_DISABLE_WINDOWS_SHELL_LAUNCHER"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches for background sessions (`claude agents`, `--bg`, `/background`) hosted by a supervisor process.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_AGENT_VIEW` | `1` turns off background agents and agent view (`claude agents`, `--bg`, `/background`, the on-demand supervisor). Same as the `disableAgentView` setting. |
| `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF` | `1` stops a background session's in-flight work (running background shells, plus background subagents as of v2.1.198) when the supervisor stops, restarts or updates its process, instead of handing it to the next process. Backgrounding with the left arrow or `/background` still carries work over. Requires v2.1.196+. |
| `CLAUDE_CODE_DISABLE_BG_STABLE_PATH` | macOS native installer: `1` runs each background session's host from the installed binary, not `~/.local/share/claude/ClaudeCode.app`; macOS may re-ask for folder access, including after updates. Set in the `env` block of user or managed settings or an MDM policy, not the shell. Requires v2.1.295+. |
| `CLAUDE_CODE_DISABLE_WINDOWS_SHELL_LAUNCHER` | `1` starts PowerShell tool commands on Windows directly instead of via the `cmd.exe` launcher; a backgrounded PowerShell command then stops when the session process exits. Bash unaffected. Requires v2.1.269+. |
| `CLAUDE_CODE_PROCESS_WRAPPER` | Launches processes Claude Code starts from its own binary (such as the agent view background service) through a corporate launcher given as an argv prefix like `/opt/corp/launcher`. Set in user or managed settings `env`, not a shell export; project and local settings cannot set it. Equivalent to the `processWrapper` setting (v2.1.210+); the variable wins. The VS Code extension uses its own `claudeProcessWrapper` setting. Ignored on Windows. Requires v2.1.208+. |
