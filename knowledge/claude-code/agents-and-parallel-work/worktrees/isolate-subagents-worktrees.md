---
type: "Feature"
title: "Isolating subagents with worktrees"
description: "isolation: worktree gives a subagent its own temporary worktree; cleanup sweep by cleanupPeriodDays, locks and manual removal."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, subagents, isolation, cleanup, sweep]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "isolation: worktree"
  - "cleanupPeriodDays"
  - "git worktree lock"
  - "git worktree add"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ask Claude to "use worktrees for your agents", or set `isolation: worktree` in a custom subagent's frontmatter so parallel edits do not conflict. Each subagent gets a temporary worktree removed automatically if it finishes without changes; one with changes stays until the periodic sweep can remove it without losing work. Subagent worktrees use the same base branch as `--worktree` (default branch unless `worktree.baseRef` is `"head"`).

# How to use it

```markdown
---
name: refactorer
description: Applies mechanical refactors across many files
isolation: worktree
---
```

Instruction files: a subagent in its own worktree takes the files it starts with from the main conversation, not the worktree; for the default location under `.claude/worktrees/` it also does not load the worktree-root `CLAUDE.md` or `.claude/rules/` as it reads files there, even if they differ on that branch.

# Limits and defaults

Sweep: Claude Code periodically removes worktrees it created for subagents and background sessions once older than `cleanupPeriodDays`. A backgrounded `--worktree` session's worktree becomes sweepable. The sweep leaves a worktree when:
- it holds work (changed or untracked files, unpushed commits);
- a checked-out submodule has changes or cannot be inspected (v2.1.274 or later);
- one of the four filter-driver cases blocking creation applies;
- it belongs to a `--worktree` session you have not backgrounded, whatever its age;
- you created it with `git worktree add`, even if a `--worktree <name>` session ran in it and was backgrounded.

Claude Code writes a marker in the git metadata of every worktree it creates with git; worktrees without one (including `WorktreeCreate` hook ones) are kept.

Locks: while an agent runs Claude Code holds a `git worktree lock` on its worktree (and on a backgrounded session's worktree while it runs). The sweep releases a lock Claude Code set for an exited process, never one you set yourself. To remove a kept worktree: `git worktree remove` (add `--force` for uncommitted or untracked files; `git worktree unlock` first if locked).
