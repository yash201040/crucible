---
type: "Reference"
title: "How Claude Code enforces worktree isolation"
description: "Four checks blocking edits, command directories, git redirects and unverifiable command shapes aimed at the main checkout."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, isolation, enforcement, security, subagents]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "git -C"
  - "--git-dir"
  - "GIT_DIR"
  - "GIT_WORK_TREE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While a session is isolated in a worktree (via `--worktree`, `EnterWorktree` or a resume), Claude Code blocks tool calls that fail four checks. The same enforcement covers every subagent spawned from the isolated session, interactive or background, and subagents in their own worktree.

# How to use it

| Check | Blocks |
| :- | :- |
| File edits | `Edit`, `Write`, `NotebookEdit` targeting a path in the main checkout |
| Command working directory | Bash, PowerShell or Monitor command whose cwd resolves to the main checkout or cannot be verified to stay outside it |
| Git redirects | Bash or Monitor command redirecting git into the main checkout via `git -C`, `--git-dir`, `GIT_DIR`/`GIT_WORK_TREE`, or `cd` into it before git |
| Command shape | Bash or Monitor command when it cannot be verified from text that any git stays in the worktree (computed command names, unparsable syntax, expansions like `${!name}` or `${ command; }`); Claude is told how to rewrite it; cannot be turned off |

# Limits and defaults

- The checks read the edit target path, command cwd and command text only; they do not track which files a command writes, so `cp` or a shell redirect into the main checkout without running git there is not refused (it follows normal permissions and sandboxing).
- Applies to the repository you launched from and the main checkout a linked worktree links to. PowerShell gets only the working-directory check.
- Claude sees each refusal as a tool error naming the worktree and how to proceed.
