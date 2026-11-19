---
type: "Guide"
title: "Test with safe mode or a clean configuration"
description: "Bisect a configuration problem with claude --safe-mode or a fresh CLAUDE_CONFIG_DIR plus --setting-sources user."
resource: "https://code.claude.com/docs/en/debug-your-config"
tags: [safe-mode, config-dir, isolation, debugging]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --safe-mode"
  - "CLAUDE_CONFIG_DIR"
  - "--setting-sources user"
  - "~/.claude.json"
  - "~/.claude"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "debug-your-config"
    resource: "https://code.claude.com/docs/en/debug-your-config"
    title: "Debug your configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to start a session without your own customizations, to see whether a problem comes from configuration.

# How to use it

`claude --safe-mode` disables: `CLAUDE.md`, skills, plugins and hooks, MCP servers, custom commands and agents, custom output styles, custom keybindings. Authentication, model selection, built-in tools and permissions work normally. Managed hooks and settings policy still apply; managed plugins, skills, `CLAUDE.md` and MCP servers are turned off. If the problem disappears, one disabled item is the cause.

Fully clean session:
1. In an empty directory with no session running: `mkdir -p ~/claude-clean/empty && cd ~/claude-clean/empty`.
2. Launch: `CLAUDE_CONFIG_DIR=~/claude-clean/config claude --setting-sources user` (the variable applies to that one launch in Bash/Zsh; in PowerShell it stays set for the shell session until `Remove-Item Env:CLAUDE_CONFIG_DIR`). `--setting-sources user` turns off project configuration (`.claude/settings.json`, `CLAUDE.md`, `.mcp.json`).
3. Reproduce. If the problem is gone, copy `~/.claude.json` and files from `~/.claude` into the clean dir one at a time; then try the project directory without `--setting-sources user`. If it persists, check `/status` for managed settings and shell environment variables.

# Limits and defaults

First launch repeats the first-run setup screens, confirming the clean directory is used. Managed settings still apply, and claude.ai connectors still load if logged in with a claude.ai account.
