---
type: "Reference"
title: "Index: agents, sessions and worktrees keys"
description: "Settings keys for starting as a subagent, agent view, cross-session messaging, teammate display, process wrapper and worktree creation (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [agents, worktrees, sessions, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "agent"
  - "crossSessionInbound"
  - "disableAgentView"
  - "isolatePeerMachines"
  - "processWrapper"
  - "teammateMode"
  - "worktree"
  - "worktree.baseRef"
  - "worktree.bgIsolation"
  - "worktree.location"
  - "worktree.sparsePaths"
  - "worktree.symlinkDirectories"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from the "Agents, sessions, and worktrees" topic. The detailed sections for these keys are in other parts of the page; this part has only the index row.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `agent` | Any file | Start every session as a named subagent with its prompt, tools and model |
| `crossSessionInbound` | Any file | Deliver messages from your other sessions, show a notice without delivering, or refuse them |
| `disableAgentView` | Any file | Turn off background agents and agent view |
| `isolatePeerMachines` | Any file | Ask before Claude messages one of your sessions on another machine |
| `processWrapper` | User or managed | Run Claude Code's background processes through a corporate launcher on macOS and Linux |
| `teammateMode` | Any file | Choose how agent team teammates are displayed |
| `worktree` | Any file | Configure how Claude Code creates git worktrees |
| `worktree.baseRef` | Any file | Branch new worktrees from the remote default branch or the local HEAD |
| `worktree.bgIsolation` | Any file | Let background sessions edit the working copy without a worktree |
| `worktree.location` | User | Where Desktop SSH sessions create worktrees on a remote machine |
| `worktree.sparsePaths` | Any file | Check out only needed directories in each worktree |
| `worktree.symlinkDirectories` | Any file | Symlink large directories into each worktree instead of duplicating them |
