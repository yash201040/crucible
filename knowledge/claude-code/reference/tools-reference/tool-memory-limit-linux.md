---
type: "Limit"
title: "Tool memory limit on Linux and WSL"
description: "A cgroup memory cap for Bash, PowerShell and Monitor commands, with optional exclusions for other process kinds."
resource: "https://code.claude.com/docs/en/tools-reference#memory-limit-on-linux-and-wsl"
tags: [memory, cgroup, linux, isolation, limits]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.233"
surfaces: [cli, headless]
requires: "Linux or WSL with memory cgroup support"
identifiers:
  - "CLAUDE_CODE_TOOL_MEMORY_LIMIT"
  - "CLAUDE_CODE_TOOL_MEMORY_CGROUP_EXCLUDE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Caps the memory that Bash, PowerShell and Monitor tool commands can use, so one runaway build cannot starve the session. All of a session's commands count against one cap. Monitor commands were outside the cap before v2.1.246.

# How to use it

- `CLAUDE_CODE_TOOL_MEMORY_LIMIT=4G`: bytes or a `K`, `M`, `G`, `T` suffix. `0`, `off`, `false`, `no`, `none` turn it off. Other unreadable values (such as `4e9`) are ignored.
- `CLAUDE_CODE_TOOL_MEMORY_CGROUP_EXCLUDE` (v2.1.246+): comma-separated kinds exempt from the cap. Kinds: `mcp` (local MCP servers), `lsp`, `hooks`, `plugin`, `helper` (Claude Code's own commands such as `git`), `agent` (child Claude Code processes such as agent teammates). `none` caps every kind; `all-new` caps only Bash, PowerShell and Monitor. Unknown names are ignored. When unset, the set of other capped kinds comes from server-delivered configuration and can change over time.

# Limits and defaults

- The cap is applied with a memory cgroup; if setup fails, commands run uncapped (see `claude --debug`). The first result (on, or off because of an off value or failed setup) is held until relaunch.
- When commands exceed the cap the kernel kills a command and its result does not mention the cap.
- Hooks that can block or change an action, and any MCP server such a hook calls, are always excluded from the cap, so a kill cannot allow the blocked action.
