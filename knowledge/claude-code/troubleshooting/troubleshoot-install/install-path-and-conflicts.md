---
type: "Guide"
title: "Install locations, PATH and conflicting installs"
description: "Where the native installer puts files, how to fix a missing claude command, and how to find and remove duplicate installations."
resource: "https://code.claude.com/docs/en/troubleshoot-install"
tags: [install, path, native-installer, diagnostics]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.local/bin/claude"
  - "%USERPROFILE%\\.local\\bin\\claude.exe"
  - "~/.local/share/claude/"
  - "~/.local/state/claude/"
  - "~/.cache/claude/"
  - "~/.claude/downloads/"
  - "~/.claude/local/"
  - "~/.claude.json"
  - "XDG_DATA_HOME"
  - "XDG_STATE_HOME"
  - "XDG_CACHE_HOME"
  - "CLAUDE_CONFIG_DIR"
  - "claude --version"
  - "claude doctor"
  - "which -a claude"
  - "where.exe claude"
  - "npm uninstall -g @anthropic-ai/claude-code"
  - "brew uninstall --cask claude-code"
  - "winget uninstall Anthropic.ClaudeCode"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshoot-install"
    resource: "https://code.claude.com/docs/en/troubleshoot-install"
    title: "Troubleshoot installation and login"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Diagnostics for the case where `claude` is not found after install, or several installations coexist. The page opens with a "Find your error" table mapping each error text (for example `command not found: claude`, `Native installation exists but ... is not in your PATH`) to a fix section.

# How to use it

- The native installer places the launcher at `~/.local/bin/claude` (macOS/Linux) or `%USERPROFILE%\.local\bin\claude.exe` (Windows). The installer reports a missing PATH entry under `Setup notes:` but does not change PATH itself.
- The VS Code extension bundles a private CLI copy and does not put `claude` on PATH; run the standalone install to get it.
- Zsh: `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc` then `source ~/.zshrc`. Bash on Linux uses `~/.bashrc`; Bash on macOS uses `~/.bash_profile` (first of `~/.bash_profile`, `~/.bash_login`, `~/.profile` that exists). Windows PowerShell: add `;$env:USERPROFILE\.local\bin` to the User PATH with `[Environment]::SetEnvironmentVariable`.
- A terminal inside an editor takes its PATH from the editor; reopen the editor.
- Find duplicates with `which -a claude` / `where.exe claude`. Sources: native `~/.local/bin/claude`, legacy local npm install `~/.claude/local/`, npm global (`npm -g ls @anthropic-ai/claude-code`), Homebrew cask, WinGet. Keep only the native one.
- A native install is a symlink into `~/.local/share/claude/versions/`; a custom script or symlink at that path is a custom launcher that auto-update leaves in place.

# Limits and defaults

Install write locations on macOS/Linux: `~/.claude/downloads/` (downloaded binary), `~/.local/bin/` (launcher), `~/.local/share/claude/` (versions), `~/.local/state/claude/` (lock files), `~/.cache/claude/` (staged downloads), `~/.claude.json` (global config, records install method). `XDG_DATA_HOME`, `XDG_STATE_HOME`, `XDG_CACHE_HOME` replace the `~/.local/share`, `~/.local/state`, `~/.cache` bases; `CLAUDE_CONFIG_DIR` moves the global config file under that directory.

# Notes

On Windows an older Claude Desktop can register a `Claude.exe` in `WindowsApps` that wins PATH priority, so `claude` opens the Desktop app; updating Desktop fixes it.
