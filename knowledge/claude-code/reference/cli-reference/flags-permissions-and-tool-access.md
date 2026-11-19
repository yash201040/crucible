---
type: "Reference"
title: "Permission, tool and settings flags"
description: "Flags controlling permission modes, allowed and denied tools, extra directories, restricted and safe mode, and settings sources."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [permissions, tools, restricted, settings, unattended]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.259"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--permission-mode"
  - "--dangerously-skip-permissions"
  - "--allow-dangerously-skip-permissions"
  - "--enable-auto-mode"
  - "--permission-prompt-tool"
  - "--permission-prompts"
  - "--allowedTools"
  - "--allowed-tools"
  - "--disallowedTools"
  - "--disallowed-tools"
  - "--tools"
  - "--add-dir"
  - "--restricted"
  - "--safe-mode"
  - "CLAUDE_CODE_SAFE_MODE"
  - "--setting-sources"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Launch-time controls over what Claude may do and which configuration it reads, central to unattended runs.

# How to use it

| Flag | Version | What it does |
| :- | :- | :- |
| `--permission-mode` | `manual` alias v2.1.200+ | Start in `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`, or `manual` (alias for `default`). Overrides `defaultMode` in settings |
| `--dangerously-skip-permissions` | | Equivalent to `--permission-mode bypassPermissions`. For `--bg` sessions the mode persists when the supervisor restarts the session |
| `--allow-dangerously-skip-permissions` | | Adds `bypassPermissions` to the `Shift+Tab` cycle without starting in it |
| `--enable-auto-mode` | removed v2.1.111 | Auto mode is now in the `Shift+Tab` cycle; use `--permission-mode auto` |
| `--permission-prompt-tool` | restriction v2.1.199+ | MCP tool (`mcp__<server>__<tool>`) that handles prompts in non-interactive mode; Claude Code waits for its server up to `MCP_TIMEOUT` (30 s default). It cannot approve an MCP tool marked as requiring user interaction: `allow` becomes deny |
| `--permission-prompts` | v2.1.259+ | Who answers prompts in print mode: `host` (default, goes to the SDK host or prompt tool) or `none` (denied) |
| `--allowedTools`, `--allowed-tools` | | Tools that run without prompting (not for network-path reads). Naming a task-tracking tool also opts the session in |
| `--disallowedTools`, `--disallowed-tools` | | Deny rules. A bare name removes the tool from context (`"Edit"`, `"*"` for all, `"mcp__*"` for all MCP); a scoped rule like `Bash(rm *)` keeps the tool and denies matching calls. `EndConversation` cannot be removed while any other tool remains |
| `--tools` | | Restrict built-in tools: `""` disables all, `"default"`, or a list like `"Bash,Edit,Read"`. Default set omits `Glob` and `Grep` on macOS, Linux and WSL. Does not affect MCP tools. `EndConversation` is removed by `""` only when no MCP tools remain |
| `--add-dir` | | Extra working directories for file access; most `.claude/` config is not discovered from them; path must exist and be a directory; most network paths are rejected. Persist with `permissions.additionalDirectories` |
| `--restricted` | v2.1.248+ | For evaluation harnesses on shared machines: removes command- and code-running built-in tools and WebFetch unless named in `--tools`; confines file tools to working directories; loads only managed settings and `--settings`; refuses `bypassPermissions`; refuses to create cloud sessions |
| `--safe-mode` | | Disable all customizations (CLAUDE.md, skills, plugins, hooks, MCP, custom commands and agents, output styles, workflows, themes, keybindings, status line, LSP, auto memory); auth, model, built-in tools and permissions work. Managed policy hooks, status line and file-suggestion commands still apply. Sets `CLAUDE_CODE_SAFE_MODE` |
| `--setting-sources` | | Comma-separated `user`, `project`, `local`; sessions started from this one inherit the list |
| `--settings` | | Path to a settings JSON file (regular file, at most 2 MiB) or inline JSON; overrides same keys for the session |
