---
type: "Feature"
title: "Forking the current conversation"
description: "A fork is a subagent that inherits the full conversation and prompt cache; start one with /subtask or let Claude fork in fork mode."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, fork, prompt-cache, subtask]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "/subtask"
  - "/fork"
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "Agent(fork)"
  - "isolation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A fork sees the same system prompt, tools, model and message history as its parent; its own tool calls stay out of the parent and only its final result returns. Claude can start forks itself while fork mode is on (default); `/subtask <task>` starts one whether or not fork mode is on, naming it from the first words of the task. It runs in the background in a panel below the prompt.

# How to use it

`/subtask draft unit tests for the parser changes so far`

| | Fork | Non-fork subagent |
| :- | :- | :- |
| Context | Full conversation history | Fresh context with the prompt |
| System prompt and tools | Same as parent | From definition, filtered for background |
| Model | Same as parent | Follows the model order |
| Prompt cache | Shared with parent | Separate cache |

Because system prompt and tools are identical, a fork's first request reuses the parent's prompt cache, so it costs less than a fresh subagent for same-context tasks. Claude can pass `isolation: "worktree"` on a fork so its edits go to a separate worktree.

Turn off: add `"Agent(fork)"` to `permissions.deny` (forks only), or set `CLAUDE_CODE_FORK_SUBAGENT` to `0` (fork mode off).

# Limits and defaults

- A fork cannot spawn further forks; at the depth limit its `Agent` tool errors.
- Fork mode is on by default from v2.1.302, and in an interactive terminal session from v2.1.232. While on, Claude cannot wait for a subagent in interactive terminal, VS Code or desktop sessions on your machine.
- When agent view is turned off, `/subtask` is unavailable and `/fork` starts the forked subagent; otherwise `/fork` copies the whole session into a new background session.
