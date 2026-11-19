---
type: "Feature"
title: "Starting Claude in a worktree"
description: "claude --worktree <name> creates an isolated git worktree and branch; also EnterWorktree, trust rules and the blockWritesOutsideWorkingDirectories interaction."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, isolation, cli, parallel-sessions]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, desktop]
requires: "a git repository (or WorktreeCreate hook)"
identifiers:
  - "--worktree"
  - "-w"
  - ".claude/worktrees/<name>/"
  - "worktree-<name>"
  - "EnterWorktree"
  - "ExitWorktree"
  - "CLAUDE_PROJECT_DIR"
  - "permissions.blockWritesOutsideWorkingDirectories"
  - "claude --bg --worktree"
  - "worktree.bgIsolation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A worktree is a separate working directory with its own files and branch, sharing history and remote with the main checkout. `claude --worktree <name>` (or `-w`) creates `.claude/worktrees/<name>/` on a new branch `worktree-<name>` and starts Claude in it. Without a name Claude generates one such as `bright-running-fox`. A second terminal with another name gives a second isolated session. Worktrees isolate file edits; they differ from subagents and cross-session messaging.

# How to use it

```bash
claude --worktree feature-auth
```

- Interactive runs require workspace trust (run `claude` once in the directory, else `--worktree` exits with an error). Non-interactive `-p` skips the trust check.
- Add `.claude/worktrees/` to `.gitignore`. A worktree is a fresh checkout: install dependencies there; copy gitignored files with `.worktreeinclude`.
- During a session ask Claude to "work in a worktree": it uses the `EnterWorktree` tool and can switch directly to another worktree under `.claude/worktrees/` by path (previous one stays). Entering a path outside `.claude/worktrees/` asks for approval (the move carries working directory, write access and project config such as `CLAUDE.md` and settings); an `EnterWorktree` permission rule or "don't ask again" does not suppress it; only `bypassPermissions` does.
- Hook paths: `${CLAUDE_PROJECT_DIR}` stays at the project root where the session started; the `cwd` field in hook input JSON is the worktree root and follows `cd`.

# Limits and defaults

If `permissions.blockWritesOutsideWorkingDirectories` is on, Claude Code removes (or refuses) both `EnterWorktree` and `ExitWorktree`. Workarounds: interactive `claude --worktree`; for background sessions (whose edits in the main checkout are refused until they call `EnterWorktree`) use `claude --bg --worktree`, set `worktree.bgIsolation` to `"none"`, or have Claude edit in a worktree made with `git worktree add` under the starting directory. To restore the tools, check `/status` for setting sources, remove the key from every file, restart; managed settings need an administrator.
