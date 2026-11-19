---
type: "Feature"
title: "Block reads and writes outside working directories"
description: "permissions.blockReadsOutsideWorkingDirectories and blockWritesOutsideWorkingDirectories make file tools refuse outside paths in every mode."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [permissions, isolation, working-directories, sandbox]
kind: "setting"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, headless, ide, cloud]
requires: "reads v2.1.257; writes v2.1.314"
identifiers:
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "EnterWorktree"
  - "ExitWorktree"
  - "NotebookEdit"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two Boolean keys, scope `Any file`, default unset. A `true` in any file applies, so a repository can turn the block on but cannot lift yours; `false` equals unset. Both work in every permission mode including `bypassPermissions`.

# How to use it

| Key | Tools it refuses | Version |
| :- | :- | :- |
| `permissions.blockReadsOutsideWorkingDirectories` | `Read`, `Grep`, `Glob`, `LSP` outside working directories; Claude is told to ask for `/add-dir` | v2.1.257 |
| `permissions.blockWritesOutsideWorkingDirectories` | `Write`, `Edit`, `NotebookEdit`; also removes or refuses `EnterWorktree` and `ExitWorktree` | v2.1.314 |

```json
{ "permissions": { "blockWritesOutsideWorkingDirectories": true } }
```

To let one directory through, add it as a working directory: `/add-dir <dir>`, `--add-dir <dir>`, or `additionalDirectories` in user or managed settings. No allow rule lets file tools through. To lift a block, remove the key from every file and restart.

# Limits and defaults

- Reads: files Claude Code itself needs (skills, plugins, rules, agents, commands, `~/.claude/` `CLAUDE.md`) stay readable. Shell commands are not refused the same way; an untraceable Bash command (multiple `cd`, subshell) prompts even in auto and `bypassPermissions`, unless it runs in the sandbox that enforces the block. Directories added only in repository settings (`.claude/settings.json`, or `.claude/settings.local.json` unless git reports it untracked) do not count as working directories. `autoMemoryDirectory` from repository settings loads and saves no auto memory.
- With sandboxing on, the read block also covers sandboxed commands: home and `/Users`, `/home`, `/root`, `/Volumes`, `/mnt`, `/media`, `/run/media`, `/srv` are denied, then working directories, session-created worktrees, session temp dir and needed `~/.claude` parts are reopened; repository `allowRead`/`allowWrite` entries do not count. A linked worktree keeps its common `.git` read/write. Global git config files (`~/.gitconfig`, `$XDG_CONFIG_HOME/git` `config`, `ignore`, `attributes`, files from `[include]`, `[includeIf]`, `core.excludesFile`, `core.attributesFile`) are reopened; `~/.git-credentials` stays blocked; a `denyRead` entry wins. The block does not reach sandboxed commands when `sandbox.filesystem.disabled`, `allowManagedReadPathsOnly` is set, or the start path contains `*`, `?` or `[`.
- Writes: default is also on while Claude Code cannot read the managed `permissions` object. In cloud sessions the key might not apply. Writes to Claude Code settings files are refused even inside working directories. Plan files, the scratchpad, a background session's `tmp` and `.md` files in the project's auto memory stay writable. Refused: directories only repository settings add, a subagent's `isolation: worktree` worktree outside the working directories (add the repo's `.claude/worktrees`), and auto memory in a repository-chosen directory.
