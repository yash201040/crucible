---
type: "Feature"
title: "DirectoryAdded hook event"
description: "Runs in the background after /add-dir or an SDK register_repo_root request adds a working directory."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, directoryadded, working-directories, sdk]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "DirectoryAdded"
  - "/add-dir"
  - "--add-dir"
  - "register_repo_root"
  - "slash_command"
  - "directory"
  - "source"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs after a working directory is added mid-session with `/add-dir` or by an SDK client with the `register_repo_root` control request. Use to prepare a new repo (e.g. install dependencies). Fires after sandbox and permission state refresh, so sandboxed tools already see the directory; hook commands themselves run unsandboxed.

# How to use it

Matcher filters on how it was added: `slash_command` or `register_repo_root`. Input adds `directory` (absolute path) and `source` (same two values).

# Limits and defaults

- Does not fire for the `--add-dir` startup flag (SessionStart covers those), a directory added on the `/permissions` Workspace tab, or one already a working directory or inside one.
- Claude Code does not wait: the add completes immediately and the hook runs in the background with the 600-second default timeout. No decision control; `continue` discarded.
- `slash_command`: the hook's `systemMessage` goes to Claude as context on the next turn, not shown to you; a count of failed hooks appears in the transcript, full failure output in the debug log. `register_repo_root`: `systemMessage` and failure output go to the debug log only.
