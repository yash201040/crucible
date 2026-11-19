---
type: "Feature"
title: "Desktop sessions in WSL"
description: "Run Code tab sessions inside a WSL 2 distribution on Windows, with what works, what does not, and managed-device limits."
resource: "https://code.claude.com/docs/en/desktop-wsl"
tags: [desktop, wsl, windows, sessions]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Windows 10 or 11 with WSL 2 (not WSL 1), a distribution, git installed inside it"
identifiers:
  - "\\\\wsl.localhost\\"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop-wsl"
    resource: "https://code.claude.com/docs/en/desktop-wsl"
    title: "Claude Code Desktop in WSL"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A WSL session runs Claude Code, its tools and git inside the distribution with native Linux paths. Use it when the repo lives in the distribution's filesystem (access from Windows is slow and breaks file watching).

# How to use it

Choose a distribution under **WSL** in the environment selector, pick a folder (Linux paths), trust the folder (trust is per distribution and folder). Opening a `\\wsl.localhost\...` folder reopens inside that distribution. Works: parallel sessions, side chats, diff review, branch and PR status, worktrees; "Open in editor" uses VS Code Remote - WSL.

# Limits and defaults

- Plugins are not available in WSL sessions.
- File pane is view-only; ask Claude to edit.
- Integrated terminal and connectors may be missing (rolling out separately for Claude accounts; never for third-party providers).
- **+** menu may show **Add image** only; @mention other files.
- On managed devices WSL sessions may be unavailable (administrator control).
