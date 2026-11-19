---
type: "Feature"
title: "WorktreeCreate hook event"
description: "Replaces Claude Code's default git worktree creation; the hook must return the new worktree path."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, worktree, isolation, vcs]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "WorktreeCreate"
  - "name"
  - "worktreePath"
  - "--worktree"
  - "--tmux"
  - "EnterWorktree"
  - "isolation: \"worktree\""
  - ".worktreeinclude"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when Claude Code creates a worktree: `claude --worktree`; the `EnterWorktree` tool; a subagent with `isolation: "worktree"`; a workflow agent run in its own worktree; isolation of a background session; `claude remote-control` in `worktree` mode. Configuring this hook replaces the default `git worktree` behavior entirely, so you can use SVN, Perforce, Mercurial and so on. Because it replaces default behavior, `.worktreeinclude` is not processed; copy files like `.env` inside your hook.

# How to use it

Input adds `name` (slug, user-specified or generated, e.g. `bold-oak-a3f2`).

The hook must return the worktree directory path (it becomes the session's working directory):
- Command hooks: print the path as the last non-empty line of stdout (ANSI escapes stripped first, so shell banners are ignored); send other output to stderr.
- HTTP hooks: return `{ "hookSpecificOutput": { "hookEventName": "WorktreeCreate", "worktreePath": "/absolute/path" } }`.

Example: a command hook running `svn checkout ... "$DIR" >&2 && echo "$DIR"` with `NAME=$(jq -r .name)`.

# Limits and defaults

- Success/failure decides the outcome (no allow/block model); a failing hook or missing path makes creation fail. `systemMessage` and `continue` discarded.
- A relative path resolves against the hook's directory with `.`/`..` collapsed; if it is not an enterable directory the session prints an error naming the path and exits with code 1. An absolute path with `.` or `..` segments is refused, as is any path through a symlink below the repository root.
- Does not run for `git worktree add` through Bash (use a `PreToolUse` Bash hook). A plugin's hook does not run for `--worktree` with `--tmux` (worktree is created before plugins load); define it in a settings file instead. Before v2.1.300 a plugin's hook did not run with `--worktree` alone either.
