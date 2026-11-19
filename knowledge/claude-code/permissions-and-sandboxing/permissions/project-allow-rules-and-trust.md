---
type: "Concept"
title: "Workspace trust and project allow rules"
description: "Project allow rules and additionalDirectories apply only after the workspace trust dialog, which is not shown in -p or SDK runs."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, workspace-trust, headless, security]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, ide]
requires: ""
identifiers:
  - "hasTrustDialogAccepted"
  - "~/.claude.json"
  - "claude --bg"
  - "claude -p"
  - "this workspace has not been trusted"
  - "Workspace not trusted"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`permissions.allow` rules and `permissions.additionalDirectories` entries in a project's `.claude/settings.json` grant capability, so Claude Code applies them only after you accept the workspace trust dialog for that folder (the dialog lists them). `deny` and `ask` rules are not affected.

# How to use it

Where trust is keyed:
- In a repository: the git repository root (the main checkout in a worktree), covering the whole repository except a nested repository such as a submodule.
- Outside a repository: the directory you started in, covering subdirectories except a nested repository such as a clone.
- In your home directory: trust is held for the current session only and not written to disk.

The dialog shows in interactive terminal sessions, not in `claude -p` or SDK sessions. The VS Code extension asks via `Trust this folder in Claude Code?`. Trusting a parent does not count for these rules.

Before starting or restarting a background session (`claude --bg`) Claude Code checks trust for the run directory: in an untrusted one the dialog appears first; where no dialog can appear (a script) the command exits with a `Workspace not trusted` error.

To trust a folder by hand set `projects["<path>"].hasTrustDialogAccepted` to `true` in `~/.claude.json` (path is the repository root, or the folder outside a repository). Debug logs and warnings print the exact key.

# Notes

`.claude/settings.local.json` is applied without the trust step normally. If it is tracked in git or `.claude` is a symlink, it is treated as repository-supplied and held until trusted. Claude Code runs git to tell only after the folder is trusted (accepted dialog, accepted parent, or `-p`/SDK which count as accepted). Before then: in your configuration home (home directory, or a `CLAUDE_CONFIG_DIR` directory) the file applies at once; if that `CLAUDE_CONFIG_DIR` directory is inside a git repository and settings are kept at the repo root, it is held like elsewhere. Anywhere else it is held like project settings until the check runs, after which an untracked file, or one outside any repository, applies. `~/.claude/settings.local.json` is still local scope and read only for sessions started in your home directory; for cross-project rules use user settings (`~/.claude/settings.json` or `$CLAUDE_CONFIG_DIR/settings.json`).
