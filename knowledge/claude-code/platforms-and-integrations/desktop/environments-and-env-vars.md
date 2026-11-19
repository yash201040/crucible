---
type: "Guide"
title: "Environments and environment variables"
description: "Saved local, SSH and cloud environments, how to set variables for sessions and dev servers, and variables Desktop sets itself."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, environments, env-vars, thinking, timeout]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Current layout (Desktop v2.37337.0 or later) for saved environments"
identifiers:
  - "API_TIMEOUT_MS"
  - "ANTHROPIC_BASE_URL"
  - "MAX_THINKING_TOKENS"
  - "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_TMPDIR"
  - "PATH"
  - "env"
  - "disableDesktopLocalSessions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The environment selector picks where Claude runs: Local, Cloud, SSH, WSL. A saved environment records where and (local, SSH) which folders; Desktop creates up to eight from the most-used folders of the last month on first open of the current layout.

# How to use it

- **Local session variables**: edit a saved local environment > **Environment variables**, one `KEY=value` per line; only sessions from that environment get them. Every local session: `env` key in `~/.claude/settings.json` (ignored if the variable is already in the environment Desktop starts with).
- **Dev server secrets**: shell profile (macOS/Linux), Windows user/system variables, or the local environment editor (stored encrypted); restart Desktop. Saved environments and settings `env` do not reach dev servers.
- **Set by Desktop itself**: `API_TIMEOUT_MS` = `900000` (15 min) in local sessions (use the CLI for longer); `ANTHROPIC_BASE_URL` is Anthropic's host when signed in with a Claude account (use Desktop's third-party inference configuration for gateways).
- **Extended thinking**: on by default; set `MAX_THINKING_TOKENS` to `0` to turn off (not on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable models, which always think; on Opus 5 also select effort `high` or lower). On adaptive-reasoning models a positive value's number is ignored; Opus 4.6 and Sonnet 4.6 can use `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` for a fixed budget.
- `PATH`: on Windows Desktop does not read PowerShell profiles; set user/system variables. `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`: set where dev-server variables go, then restart.

# Limits and defaults

Before Claude Code v2.1.304, exported shell variables are not passed to commands. Managed devices: `disableDesktopLocalSessions` grays out Local; new sessions default to the first SSH connection. Cloud environments: add/edit/archive from the selector; see the cloud-environments page.
