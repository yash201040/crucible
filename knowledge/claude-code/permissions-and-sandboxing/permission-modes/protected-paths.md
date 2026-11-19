---
type: "Reference"
title: "Protected paths"
description: "Directories and files whose writes are gated per permission mode, with the per-mode outcome table and exceptions."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [protected-paths, permissions, security, git, config]
kind: "file"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: ""
identifiers:
  - ".git"
  - ".config/git"
  - ".vscode"
  - ".idea"
  - ".husky"
  - ".cargo"
  - ".devcontainer"
  - ".yarn"
  - ".mvn"
  - ".claude"
  - ".gitconfig"
  - ".gitmodules"
  - ".bashrc"
  - ".bash_profile"
  - ".bash_login"
  - ".bash_aliases"
  - ".bash_logout"
  - ".zshrc"
  - ".zprofile"
  - ".zshenv"
  - ".zlogin"
  - ".zlogout"
  - ".profile"
  - ".envrc"
  - ".npmrc"
  - ".yarnrc"
  - ".yarnrc.yml"
  - ".pnp.cjs"
  - ".pnp.loader.mjs"
  - ".pnpmfile.cjs"
  - "bunfig.toml"
  - ".bunfig.toml"
  - ".bazelrc"
  - ".bazelversion"
  - ".bazeliskrc"
  - ".pre-commit-config.yaml"
  - "lefthook.yml"
  - "lefthook.yaml"
  - ".lefthook.yml"
  - ".lefthook.yaml"
  - "gradle-wrapper.properties"
  - "maven-wrapper.properties"
  - ".devcontainer.json"
  - ".ripgreprc"
  - "pyrightconfig.json"
  - ".mcp.json"
  - ".claude.json"
  - "remote-settings.json"
  - "~/.claude/dev-mods/"
  - "--plugin-dir"
  - "plansDirectory"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A small set of paths holding repository state and Claude's own configuration. Each mode has its own rule for writes to them.

| Mode | Protected-path writes |
| :- | :- |
| `default`, `acceptEdits` | Prompted |
| `plan` | Allowed in interactive terminal sessions with bypass available; otherwise routed to the classifier when auto is available during planning, prompted when not |
| `auto` | Routed to the classifier |
| `dontAsk` | Denied |
| `bypassPermissions` | Allowed |

# How to use it

Protected directories: `.git`, `.config/git`, `.vscode`, `.idea`, `.husky`, `.cargo`, `.devcontainer`, `.yarn`, `.mvn`, `.claude`. Exceptions inside `.claude`: Claude's worktrees under `.claude/worktrees/`; the current session's plan files in `~/.claude/plans/` or the `plansDirectory`; a background session's scratch directory `~/.claude/jobs/<id>/tmp/`; Markdown files in the project's auto-memory directory (`~/.claude/projects/<project>/memory/`) and in a subagent memory directory (`.claude/agent-memory/`), both only in sessions started without `--restricted`. Also protected: a directory loaded with `--plugin-dir`; `~/.claude/dev-mods/` (or `dev-mods/` under `CLAUDE_CONFIG_DIR`).

Protected files: `.gitconfig`, `.gitmodules`; shell rc files (`.bashrc`, `.bash_profile`, `.bash_login`, `.bash_aliases`, `.bash_logout`, `.zshrc`, `.zprofile`, `.zshenv`, `.zlogin`, `.zlogout`, `.profile`, `.envrc`); package-manager files (`.npmrc`, `.yarnrc`, `.yarnrc.yml`, `.pnp.cjs`, `.pnp.loader.mjs`, `.pnpmfile.cjs`, `bunfig.toml`, `.bunfig.toml`); `.bazelrc`, `.bazelversion`, `.bazeliskrc`; hook configs (`.pre-commit-config.yaml`, `lefthook.yml`, `lefthook.yaml`, `.lefthook.yml`, `.lefthook.yaml`); `gradle-wrapper.properties`, `maven-wrapper.properties`; `.devcontainer.json`; `.ripgreprc`, `pyrightconfig.json`; `.mcp.json`, `.claude.json`; `remote-settings.json` and its signature/sync/consent files in `~/.claude` or `CLAUDE_CONFIG_DIR`; files passed to `--settings`, `--mcp-config` or `--agents`; the target of a user/project/local settings file that is itself a symlink (in classifier-routing modes it prompts even with an allow rule, unless that path is also a settings file path).

# Limits and defaults

- `permissions.allow` rules in settings do not pre-approve protected-path writes: the safety check runs before settings allow rules, so `Edit(.claude/**)` changes nothing. In prompting modes the prompt can offer session-scoped options: **Yes, and allow Claude to edit files in this project's .claude folder for this session** and **Yes, and allow Claude to edit files in its ~/.claude folder for this session**.
- In a `--restricted` session (v2.1.248+) the classifier cannot approve protected-path writes.
- While `permissions.blockWritesOutsideWorkingDirectories` is on, `Write`/`Edit`/`NotebookEdit` writes to settings files are refused in every mode.
- In classifier-routing modes, a write the symlink check resolves to a protected path prompts when the requested path is not itself protected.
