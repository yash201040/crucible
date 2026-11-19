---
type: "Feature"
title: "Auto memory"
description: "Claude saves its own notes across sessions into a per-repository memory directory with a MEMORY.md index loaded each session."
resource: "https://code.claude.com/docs/en/memory"
tags: [auto-memory, memory, storage, settings]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: ""
identifiers:
  - "autoMemoryEnabled"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "autoMemoryDirectory"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "CLAUDE_CONFIG_DIR"
  - "~/.claude/projects/<project>/memory/"
  - "MEMORY.md"
  - "cleanupPeriodDays"
  - "permissions.blockReadsOutsideWorkingDirectories"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude accumulates notes without being asked. Four kinds, recorded as a `type` field in the memory file's frontmatter: `user` (role, expertise, preferences), `feedback` (corrections and confirmed approaches), `project` (ongoing work, deadlines, decisions not derivable from code or git), `reference` (where to find outside information). It skips anything derivable from the codebase or already in CLAUDE.md, and does not save every session.

# How to use it

- On by default in local sessions. Outside Claude Tag sessions, a session in a self-hosted environment runs with it off by default.
- Toggle in `/memory` (saves `autoMemoryEnabled` to `~/.claude/settings.json`); per project set `"autoMemoryEnabled": false`; or set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.
- The toggle can turn it off but not back on in a background session or in a session another Claude Code session started (such as `claude` run via Bash). It then reads `off · can't be turned on here; use a session started outside Claude Code`.
- Directory: `~/.claude/projects/<project>/memory/`, derived from the git repository (all worktrees and subdirectories share it; outside git, the project root). Contains `MEMORY.md` plus topic files like `user_role.md`.
- `CLAUDE_CODE_PROJECT_DIR_NAME` (with `CLAUDE_CONFIG_DIR`) replaces `<project>` under `<config dir>/projects/`; needs v2.1.234 or later.
- `autoMemoryDirectory` relocates it (absolute path or starting `~/`); allowed in any scope (user, project, local, policy, `--settings`). Project-file values obey the same workspace trust rule as hooks. While `permissions.blockReadsOutsideWorkingDirectories` is on, no auto memory loads from or saves to a directory a repository-supplied settings file chose.

# Limits and defaults

- First 200 lines or 25KB of `MEMORY.md`, whichever comes first, load at session start; the rest does not. Topic files are read on demand, not at startup.
- After a write, Claude Code measures MEMORY.md against the limits: near the limit it reminds Claude to shorten; over it, the write succeeds but an error tells Claude to rewrite the index.
- The limit applies only to MEMORY.md; each launch CLAUDE.md loads fully up to 4 MiB (a larger file is skipped entirely).
- Machine-local: not shared across machines or cloud environments.
- Memory files are excluded from the `cleanupPeriodDays` transcript retention sweep.
- The main conversation's auto memory is not loaded into subagents, except a fork, which inherits the parent. A subagent's own memory (subagent `memory` field) is a separate directory.
- Writing a memory file that starts with YAML frontmatter makes Claude Code add a `modified` ISO 8601 timestamp field.
- UI shows "Saved N memories" / "Recalled N memories".

# Notes

Plain markdown, editable or deletable at any time. See [/memory](./memory-command.md).
