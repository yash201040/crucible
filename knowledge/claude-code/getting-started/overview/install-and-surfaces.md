---
type: "Guide"
title: "Install Claude Code and choose a surface"
description: "Install commands per platform, update behavior by install method, and the terminal, VS Code, JetBrains, desktop and web surfaces."
resource: "https://code.claude.com/docs/en/overview"
tags: [install, surfaces, terminal, updates]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop, web, mobile]
requires: "Claude subscription or Anthropic Console account for most surfaces; desktop app needs a paid subscription"
identifiers:
  - "curl -fsSL https://claude.ai/install.sh | bash"
  - "irm https://claude.ai/install.ps1 | iex"
  - "brew install --cask claude-code"
  - "claude-code@latest"
  - "winget install Anthropic.ClaudeCode"
  - "claude --version"
  - "ANTHROPIC_API_KEY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "overview"
    resource: "https://code.claude.com/docs/en/overview"
    title: "Overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code is an agentic coding tool that reads a codebase, edits files, runs commands and integrates with dev tools. It runs on the terminal CLI, VS Code (and Cursor), JetBrains IDEs, a desktop app and the web (claude.ai/code, also in the Claude iOS/Android app). Each surface uses the same engine, so a repo's CLAUDE.md files, settings and MCP servers work across all of them. The Terminal CLI, VS Code and JetBrains also support third-party providers.

# How to use it

| Install method | Command | Auto-update |
| - | - | - |
| Native (recommended), macOS/Linux/WSL | `curl -fsSL https://claude.ai/install.sh \| bash` | Yes, in background |
| Native, Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` | Yes |
| Native, Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` | Yes |
| Homebrew | `brew install --cask claude-code` (stable channel, about a week behind) or `claude-code@latest` (latest channel) | No; `brew upgrade claude-code` or `brew upgrade claude-code@latest` |
| WinGet | `winget install Anthropic.ClaudeCode` | No; `winget upgrade Anthropic.ClaudeCode` |

Also available via apt, dnf, apk (Debian, Fedora, RHEL, Alpine). Verify with `claude --version`, then run `claude` in a project. On first use it prompts for login; if `ANTHROPIC_API_KEY` is set and you approve the key, the login prompt is skipped.

# Limits and defaults

- Git for Windows is recommended on native Windows so Claude Code can use the Bash tool; without it Claude Code uses PowerShell as the shell tool. WSL needs no Git for Windows.
- The JetBrains plugin requires the CLI installed separately. The desktop app includes Claude Code and needs a paid subscription; on Ubuntu/Debian the desktop app is in beta (apt install).
- Desktop app: review diffs visually, run multiple sessions side by side, schedule recurring tasks, start cloud sessions.
