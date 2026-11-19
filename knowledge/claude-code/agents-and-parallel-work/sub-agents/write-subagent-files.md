---
type: "Feature"
title: "Writing subagent files and hot reload"
description: "Subagent file format, live reload of agent directories, prompt contents, working directory behavior and worktree isolation checks."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, files, hot-reload, isolation, cwd]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--disable-slash-commands"
  - "isolation: worktree"
  - "~/.claude/agents/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A subagent file is YAML frontmatter plus a Markdown body that becomes the system prompt. Subagents receive only that prompt plus basic environment details like the working directory, not the Claude Code system prompt.

# How to use it

Claude Code watches `~/.claude/agents/` and `.claude/agents/`; adds or edits (including by Claude) are detected within a few seconds and used by the next delegation without a restart.

Restart is still needed when: the `agents` directory did not exist at session start; the agents live in a directory added with `--add-dir` / `/add-dir` (not watched); the session was started with `--disable-slash-commands` (no watching at all).

# Limits and defaults

- A subagent starts in the main conversation's working directory; `cd` in Bash/PowerShell does not persist between calls and does not affect the main conversation.
- With `isolation: worktree`, Bash and PowerShell commands run in the worktree; a command whose working directory resolves to the main checkout (for example the worktree was removed mid-run) fails.
- The check covers the whole repository you launched from, and the main checkout when your session runs in a linked worktree.
- For Bash, Claude Code also blocks commands that redirect git into the main checkout and commands whose git usage cannot be verified from the text (for example a command name computed at runtime). PowerShell gets only the working-directory check. Monitor commands get the same checks as Bash.
- If the main conversation itself is isolated in a worktree, the same checks apply to the session and every subagent it spawns, including those without `isolation: worktree`.
