---
type: "Feature"
title: "Commands in SDK sessions"
description: "Send /<name> in a prompt to run built-in commands, bundled skills, your skills or command files; slash_commands in the init message lists them."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [commands, slash-commands, dispatch, sdk]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [sdk, headless]
requires: ""
identifiers:
  - "/<name>"
  - "slash_commands"
  - "user-invocable: false"
  - "maxTurns"
  - "max_turns"
  - ".claude/commands/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A command is anything run by sending `/<name>` in a prompt. Four kinds back it: built-in commands (logic in the Claude Code process, e.g. `/compact`), bundled skills (e.g. `/code-review`), your skills (a directory with `SKILL.md`), and custom command files (older form, flat Markdown in `.claude/commands/`; skills are the recommended successor).

# How to use it

- Discover: the `system/init` message `slash_commands` field lists commands that work without an interactive terminal. Commands needing one (`/theme`, `/terminal-setup`) are not listed. Skills with `user-invocable: false` are not listed. MCP prompts can also appear as commands.
- Dispatch: put `/<name>` in the prompt string. Dispatch does not depend on the `skills` option: it runs a user-invocable skill even if `skills` omits it.
- By default both you and Claude can invoke any skill; restrict either path with the skill's frontmatter.
- `/<name>` matching nothing does not fail the query: it goes to Claude as an ordinary message with a note that the command did not run, costing a model turn. Before v2.1.274 it returned `Unknown command: /<name>` without a model turn.
- `/<name>` matching a built-in unavailable in the session (e.g. `/theme`) returns `/theme isn't available in this environment.` without a model turn.

# Limits and defaults

When a command hits `maxTurns`/`max_turns`, the query ends with an error result instead of `success`; set it high enough or wrap the loop in try/catch (TypeScript) or try/except (Python).

# Notes

A `.claude/commands/code-review.md` (or `verify`) file shadows the bundled skill of that name; `slash_commands` lists it once. Command files in `.claude/commands/` and `~/.claude/commands/` load from the same two scopes as skills.
