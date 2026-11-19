---
type: "Concept"
title: "Sandbox protected paths"
description: "Files the sandbox keeps write-denied inside writable directories, including settings, hooks, git config, and the HEAD/objects/refs deletion behavior."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, protected-paths, git, security]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.307"
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/skills"
  - ".claude/agents"
  - ".claude/commands"
  - ".claude/hooks"
  - ".claude/workflows"
  - ".claude/scheduled_tasks.json"
  - ".mcp.json"
  - "~/.claude.json"
  - ".credentials.json"
  - "CLAUDE_CONFIG_DIR"
  - "sandbox.allowNestedUserNamespaces"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Inside writable directories the sandbox still denies writes to files Claude Code loads config and code from, so a command cannot grant itself permissions or add a hook or MCP server that runs outside the sandbox. The sandbox list applies to an already-running command; the permission system has its own protected paths. Four groups:

1. Working directory and directories above it: `.claude` settings files; `.claude/skills`, `.claude/agents`, `.claude/commands`, `.claude/hooks`; `.mcp.json`; files Claude Code runs itself such as `.claude/workflows` and `.claude/scheduled_tasks.json`.
2. Working directory only: shell startup files (`.bashrc`, `.zshrc`), `.gitconfig`, `.vscode`, `.idea`, and `hooks` and `config` inside `.git`.
3. Files that would make the working directory a bare git repo: top-level `HEAD`, `objects`, `refs`, plus existing `config` and `hooks` when a `HEAD` file or symlink sits beside them (a file named `config` is denied even with no `HEAD`). On Linux/WSL2 a sandboxed command can create one where none exists.
4. In `~/.claude` (or `CLAUDE_CONFIG_DIR`): most contents, plus `~/.claude.json` and `.credentials.json`.

# How to use it

An `allowWrite` entry or `Edit` allow rule covering these paths does not lift the protection; only `filesystem.disabled` does (and it disables the rest of filesystem isolation). `/sandbox` Config tab lists most under "Denied within allowed".

# Limits and defaults

- If a symlink appears at a protected settings file during the session, the file it points to is denied from the next command.
- After a sandboxed command ends, a newer top-level `HEAD`, `objects` or `refs` (not present when the sandbox last built its config) is deleted unless it is a folder with contents; a newer `objects`/`refs` folder with contents is also deleted when a `HEAD` file or symlink was present. Before v2.1.307 a folder was deleted even with contents and no `HEAD`.
- macOS: a denied path through a symlink (e.g. `~/.claude` linked to a dotfiles repo) also denies the real location, including `denyWrite` globs when a folder before the first `*`, `?` or `[` is a symlink.
- With `allowNestedUserNamespaces` true on Linux/WSL2, do not rely on protected paths.
