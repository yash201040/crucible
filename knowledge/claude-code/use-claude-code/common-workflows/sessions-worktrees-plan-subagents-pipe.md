---
type: "Feature"
title: "Resume, worktrees, plan mode, subagents, piping"
description: "Short workflows: continue a session, parallel worktree sessions, plan mode, research subagents and piping into claude -p."
resource: "https://code.claude.com/docs/en/common-workflows"
tags: [resume, worktrees, plan-mode, subagents, headless]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: "Worktrees need a repository with at least one commit"
identifiers:
  - "claude --continue"
  - "claude --resume"
  - "/resume"
  - "claude --worktree"
  - "claude --permission-mode plan"
  - "Shift+Tab"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "common-workflows"
    resource: "https://code.claude.com/docs/en/common-workflows"
    title: "Common workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five short workflows that each link to a fuller page.

# How to use it

| Need | Command or action | Notes |
| - | - | - |
| Continue later | `claude --continue` | Resumes the most recent session in the current directory; if none, prints `No conversation found to continue` and exits. `claude --resume` picks from a list; `/resume` works in a running session |
| Parallel sessions | `claude --worktree feature-auth` | Each git worktree is a separate checkout on its own branch, created from an existing commit. Run another name in a second terminal. See Worktrees page for cleanup, `.worktreeinclude`, non-git VCS; background agents page to monitor from one screen |
| Plan before editing | `claude --permission-mode plan`, or `Shift+Tab` mid-session | Claude reads and proposes a plan, no edits until approved; status bar shows `⏸ plan mode on` |
| Research without clutter | "use a subagent to investigate how our auth system handles token refresh" | Subagent reads files in its own window and returns a summary |
| Pipe into scripts | `git log --oneline -20 \| claude -p "summarize these recent commits"` | Non-interactive for CI, pre-commit hooks, batch; see Non-interactive mode for output formats, permission flags and fan-out |
