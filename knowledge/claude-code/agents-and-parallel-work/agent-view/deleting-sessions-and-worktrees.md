---
type: "Feature"
title: "Deleting sessions and their worktrees"
description: "What Ctrl+X twice and claude rm remove, when deletion is refused, and the retry flags."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, delete, worktrees, cleanup]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude rm <id>"
  - "--discard-unpushed"
  - "--force-remove-worktree"
  - "WorktreeRemove"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Delete with `Ctrl+X` twice in agent view or `claude rm <id>`. The transcript stays on your machine (`claude --resume`). For a worktree Claude created: agent view removes it including uncommitted changes (commit first); `claude rm` keeps it and the row when uncommitted changes exist. Deletion is refused for unpushed commits in the worktree (message names branch and count), or when another live session runs inside the worktree (`not deleted` / `kept <id>`, v2.1.227).

# How to use it

| Command | Effect |
| :- | :- |
| `claude rm <id> --discard-unpushed <commit>@<worktree-id>` | Retry deleting and discard the worktree after unpushed-commit refusal (v2.1.260+); copy from the refusal message |
| `claude rm <id> --force-remove-worktree <worktree-id>` | Retry and remove a worktree directory that git or the `WorktreeRemove` hook could not remove (v2.1.268+) |

A `Worktree not removed` message means git or `WorktreeRemove` did not finish; push commits and copy files out, then follow the message. The `files that weren't checked against a repository` message from `claude rm` concerns a directory outside any repo or managed by a `WorktreeCreate` hook: without a hook, press `Ctrl+X` twice in agent view to discard or remove it yourself then re-run `claude rm <id>`; with hook and `WorktreeRemove`, `Ctrl+X` twice tries your hook; with hook but no `WorktreeRemove`, remove it yourself.

# Limits and defaults

Some worktrees stay on disk: ones you created and started the session in, and directories whose `.git` file is gone (branch and commits remain). Unrecognised directories do not appear in `git worktree list`; remove by hand (`git worktree list`, `git worktree remove <path>`).
