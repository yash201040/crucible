---
type: "Reference"
title: "What a subagent loads at startup"
description: "Initial context of a non-fork subagent: system prompt, task message, CLAUDE.md, git status, skills and sibling roster, plus what never reaches it."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, context, claude-md, startup]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "omitClaudeMd"
  - "includeGitInstructions"
  - "SendMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each subagent starts with a fresh isolated window and does not see conversation history, invoked skills or files already read. A fork is the exception (it inherits the parent conversation).

# How to use it

A non-fork subagent's initial context:

| Item | Detail |
| :- | :- |
| System prompt | The agent's own prompt plus appended environment details, not the Claude Code prompt |
| Task message | The delegation prompt Claude writes |
| CLAUDE.md files | Whole hierarchy incl. `~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy files, `AGENTS.md`; Explore and Plan skip them; `omitClaudeMd` loads only managed policy files (none for managed-settings definitions) |
| Git status | Snapshot at start (the worktree's branch for isolated subagents); absent outside a repo or when `includeGitInstructions` is off; Explore and Plan skip it |
| Preloaded skills | Full content of `skills` field entries |
| Sibling roster | System reminder listing `main` and other named agents (valid `SendMessage` `to` values); only when tools include `SendMessage` and another agent has a name; snapshot at start |

Subdirectory CLAUDE.md and path-scoped rules still load when Explore, Plan or `omitClaudeMd` subagents work with files there.

# Limits and defaults

- Never reaches a non-fork subagent: output style, the main conversation's auto memory, and the parent's context window size (the window is sized by the subagent's own model).
- You cannot change which subagents receive git status; only Explore and Plan skip it.
- The main conversation still has full CLAUDE.md when reading results; restate a needed rule in the delegation prompt.
