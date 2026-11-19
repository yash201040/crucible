---
type: "Feature"
title: "Worktree isolation of background edits"
description: "Dispatched background sessions move into their own git worktree before editing; setting and exceptions."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, worktrees, isolation, git]
kind: "setting"
maturity: "research-preview"
since: "2.1.143"
surfaces: [cli]
requires: ""
identifiers:
  - "worktree.bgIsolation"
  - "isolation: worktree"
  - "WorktreeCreate"
  - "WorktreeRemove"
  - ".claude/worktrees/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session dispatched from agent view or with `claude --bg` starts in your working directory and, before editing files, moves into an isolated git worktree under `.claude/worktrees/`, so parallel sessions read the same checkout but write separately. Worktree isolation is then enforced for the session and its subagents. Inside a git repository, until that move the session cannot use `Edit`, `Write` or `NotebookEdit` on the shared checkout.

# How to use it

Turn isolation off per repository in `.claude/settings.json`:

```json
{ "worktree": { "bgIsolation": "none" } }
```

Sessions then edit the working copy directly. Without git, configure a `WorktreeCreate` hook to isolate other VCSs.

# Limits and defaults

No worktree is made when: the session was already open and backgrounded with `←` or `/background`; it is already inside a linked git worktree; the edited file is in a linked worktree; the directory is not a git repository and no `WorktreeCreate` hook exists (a failing hook there skips isolation); or the write is outside the working directory. Outside git without a hook, parallel sessions are not isolated.

Subagents inherit the session's working directory (so land in its worktree); for a separate worktree set `isolation: worktree` in frontmatter or pass `isolation: "worktree"` when spawning.

Preserving work: after code changes in a worktree Claude entered, Claude commits without asking, pushes the branch if a remote exists, and opens a draft pull request when the task calls for it. Never pushes to `main`/`master`, force-pushes, or merges. Your git instructions in the task, `CLAUDE.md` or memory take precedence. A session editing an unisolated checkout still asks before committing or switching branches. Claude ends the job with a report of what it did and where the work is. To find a session's worktree, attach and check the working directory.
