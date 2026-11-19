---
type: "Reference"
title: "What worktrees share with the main checkout"
description: "Shared .git, plugins, permission approvals and untracked skills/agents/commands; desktop-app configuration source."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, sharing, permissions, plugins, skills]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.277"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - ".claude/settings.local.json"
  - ".claude/skills"
  - ".claude/agents"
  - ".claude/commands"
  - ".mcp.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A worktree has its own files and branch but shares these with the main checkout (whether created by `--worktree` or `git worktree add`):

| Shared item | Detail |
| :- | :- |
| Repository `.git` directory | Git commands write to the shared `.git`. With the sandbox enabled `git commit` works from the worktree root (where `--worktree` starts); by default it fails with an `index.lock` error if you run `claude` in a worktree subdirectory |
| Plugins | Plugins installed at project scope load in all worktrees of the repository |
| Permission approvals | "Yes, and don't ask again" for a Bash command saves to the main checkout's `.claude/settings.local.json`, applying to the main checkout and every worktree and surviving the worktree's removal. On Windows and other cases where Claude Code does not use the repository root, the rule stays with that worktree |
| Untracked skills, agents, commands | If the worktree has no `.claude/skills` at its root (e.g. gitignored), the main checkout's project skills load; a worktree with its own `.claude/skills` uses only that. Same read-through for `.claude/agents` and `.claude/commands`; skills read-through needs v2.1.277 or later |

# Notes

Desktop-app worktree sessions read settings, hooks, skills, agents, commands and `.mcp.json` servers from the main checkout's root; hook commands run there and `${CLAUDE_PROJECT_DIR}` points at it (use the hook input `cwd` for the worktree path). `CLAUDE.md` and `.claude/rules/` still load from the worktree.
