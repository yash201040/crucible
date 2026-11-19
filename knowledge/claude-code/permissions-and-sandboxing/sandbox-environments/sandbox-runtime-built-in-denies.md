---
type: "Limit"
title: "Sandbox runtime built-in denies and start-up behavior"
description: "The runtime denies risky writes by default, differs between macOS and Linux on nested paths, and refuses to start on a bad settings file."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, sandbox-runtime, denywrite, limits]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "denyWrite"
  - "allowWrite"
  - "filesystem.allowGitConfig"
  - "mandatoryDenySearchDepth"
  - ".git/hooks"
  - ".git/config"
  - ".mcp.json"
  - ".claude/commands"
  - ".claude/agents"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Without configuration the runtime blocks the highest-risk writes. `denyWrite` takes precedence over `allowWrite`. At the project root it denies `.git/hooks`, `.git/config` (unless `filesystem.allowGitConfig: true`), `.mcp.json`, `.claude/commands`, `.claude/agents` and shell startup files.

# Limits and defaults

- macOS: denies are checked at write time, covering nested files and repositories created during the session.
- Linux and WSL2: the deny list is built once at launch. It reliably covers the project root, does a best-effort shallow scan for existing nested copies (`mandatoryDenySearchDepth` in the README), and does not cover things created later such as `git init`, `git clone` or scaffolding.
- If `~/.srt-settings.json` does not exist and no `--settings` is passed, the runtime still starts, blocking the network and confining writes to built-in paths such as `/tmp/claude`, `~/.npm/_logs`, `~/.claude/debug`. A clean start is not proof the settings loaded.
- If the settings file exists but is empty, unreadable or invalid, the runtime refuses to start; it also refuses if the `--settings` file does not exist.

# Notes

Your write grants still include other paths Claude Code loads configuration from; deny those with `denyWrite`. A sandboxed session able to write them can persist hooks, permission rules or MCP servers that run unsandboxed on the next launch. After unattended runs, review the paths you kept writable, and on Linux and WSL2 anything the session created.
