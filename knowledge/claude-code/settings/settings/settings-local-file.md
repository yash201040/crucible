---
type: "Feature"
title: "Local settings file location and git handling"
description: "Where .claude/settings.local.json lives in a repo or worktree, how it stays out of git, and why its allow rules skip the trust step."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, local, git, worktrees, trust]
kind: "file"
maturity: "unlabelled"
since: "2.1.211"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - ".claude/settings.local.json"
  - "core.excludesFile"
  - "XDG_CONFIG_HOME"
  - "resolveSettings()"
  - "/cd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Project local settings override the committed `.claude/settings.json` for you only (e.g. team sets `claude-sonnet-5`, your local file sets `claude-opus-5-5`). Claude Code also writes to it when you choose "Yes, and don't ask again" for a Bash command.

# How to use it

- First write in a git repo that does not ignore it adds `**/.claude/settings.local.json` to your global git excludes: `core.excludesFile` if set to an absolute or `~` path, else `$XDG_CONFIG_HOME/git/ignore`, or `~/.config/git/ignore` when unset. A hand-created file needs your own `.gitignore` entry.
- Its `allow` rules apply without the workspace-trust step while the file stays untracked; if git tracks it, trust applies.
- Started in a repo subdirectory, the file is read and written at the repository root and the approval applies repo-wide. In a worktree it uses the main checkout's root.

# Limits and defaults

- The file stays with `.claude/settings.json` instead: outside a git repo, when the repo root is your home directory, on Windows, or when the root, its `.git` or `.claude` is not owned by your user.
- Permission rules starting with `/` or relative sandbox paths anchor at the session's primary working directory, not the repo root.
- Before v2.1.211 the file lived in the starting directory; it is still read alongside the root file, root wins on same keys, permission rules from both apply. The SDK's `resolveSettings()` always reads from the starting directory.
- Shared `.claude/settings.json` is read from the primary working directory; start at the repo root to use a root file. After `/cd`, both project files are read from the new directory (v2.1.246 or later).
