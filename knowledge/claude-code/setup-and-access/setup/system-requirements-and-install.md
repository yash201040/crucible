---
type: "Guide"
title: "System requirements and installation"
description: "Supported platforms, hardware, install commands for native, Homebrew, WinGet, Windows and Alpine setup."
resource: "https://code.claude.com/docs/en/setup"
tags: [install, requirements, windows, wsl]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "macOS 13.0+, Windows 10 1809+ or Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; 4 GB+ RAM"
identifiers:
  - "curl -fsSL https://claude.ai/install.sh | bash"
  - "irm https://claude.ai/install.ps1 | iex"
  - "brew install --cask claude-code"
  - "claude-code@latest"
  - "winget install Anthropic.ClaudeCode"
  - "CLAUDE_CODE_GIT_BASH_PATH"
  - "CLAUDE_CODE_USE_POWERSHELL_TOOL"
  - "claude --version"
  - "claude doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "setup"
    resource: "https://code.claude.com/docs/en/setup"
    title: "Advanced setup"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Requirements: macOS 13.0+, Windows 10 1809+/Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; 4 GB+ RAM; x64 or ARM64; internet; shell Bash, Zsh, PowerShell or CMD; supported country. ripgrep usually bundled. Git optional (2.31+ needed for `claude plugin eval` and for uploading a local repo to a cloud session).

# How to use it

| Method | Command | Auto-update |
| :- | :- | :- |
| Native macOS/Linux/WSL | `curl -fsSL https://claude.ai/install.sh \| bash` | yes |
| Native Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` | yes |
| Native Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` | yes |
| Homebrew | `brew install --cask claude-code` (stable) or `claude-code@latest` | no |
| WinGet | `winget install Anthropic.ClaudeCode` | no |
| apt, dnf, apk | see [package managers](./linux-packages-npm-integrity.md) | no |

Windows: native (no sandboxing), WSL 2 (sandboxing supported), WSL 1 (no sandboxing). Git for Windows is optional; with it, the Bash tool uses Git Bash (set `CLAUDE_CODE_GIT_BASH_PATH` in `env` if not found), without it the PowerShell tool is the shell. With Git for Windows the PowerShell tool is on by default for claude.ai and Console accounts; set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` for Bedrock/Vertex/Foundry, `0` to turn off. Alpine needs `apk add bash curl`. Verify with `claude --version` and `claude doctor`.

# Limits and defaults

Requires a Pro, Max, Ultra, Team, Enterprise or Console account (the free plan has no Claude Code) or a third-party provider.
