---
type: "Feature"
title: "FileChanged hook event and watch list"
description: "Fires on filesystem changes to watched files regardless of who changed them; matcher builds the watch list."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, filechanged, file-watcher, environment]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "FileChanged"
  - "file_path"
  - "event"
  - "change"
  - "add"
  - "unlink"
  - "watchPaths"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a watched file changes on disk. Claude Code uses a filesystem watcher, not tool-call inspection, so it fires whether an `Edit`/`Write` call, a `Bash` script or an outside process changed the file. Typical use: reload environment variables when config files change. Has access to `CLAUDE_ENV_FILE` (variables persist until the next CwdChanged event).

# How to use it

The `matcher` has two roles. (1) Watch list: split on `|`, each segment registered as a literal filename in the working directory, so `".envrc|.env"` watches those two files; regex is not useful (`^\.env` would watch a file named `^\.env`). (2) Filter: when a watched file changes, the value filters hook groups with standard matcher rules against the file's basename.

Input adds `file_path` (absolute) and `event`: `"change"`, `"add"` or `"unlink"`.

Output: `watchPaths` (absolute paths) replaces the dynamic watch list; matcher paths are always watched. `systemMessage` is read; `continue` discarded.

Dynamic watching: Claude Code starts the watcher only when something names a file, so seed it with a FileChanged group whose matcher names at least one file, or a SessionStart or CwdChanged hook returning `watchPaths`. A group with an omitted matcher matches every watched file and adds nothing to the list; a `"*"` matcher matches every file but is registered as a literal file named `*`.

# Limits and defaults

- No decision control; cannot block the change.
- A hook that rewrites its own watched file re-triggers itself: Claude Code reruns the hook after every rewrite, so guard it (the page's example tests for CR with `grep -q $'\r$'` before `perl -pi`). `systemMessage` shows as a terminal notification in interactive sessions, not in the SDK stream.
