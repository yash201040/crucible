---
type: "Reference"
title: "Glossary: agents, subagents, loop, harness"
description: "Definitions of agent teams, subagent, agentic loop, harness, turn, verification loop, worktree isolation, bundled skills and related terms."
resource: "https://code.claude.com/docs/en/glossary"
tags: [glossary, agents, subagents, worktree, verification]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "-w"
  - "isolation: worktree"
  - ".claude/worktrees/"
  - "/goal"
  - "/batch"
  - "/code-review"
  - "/debug"
  - "/loop"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "glossary"
    resource: "https://code.claude.com/docs/en/glossary"
    title: "Glossary"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Glossary terms about agents and how work is run.

# How to use it

| Term | Definition |
| :- | :- |
| Agent teams | Multiple independent Claude Code sessions coordinated by a team lead, with a shared task list and peer-to-peer messaging; each teammate has its own context window and you can talk to any. Experimental and disabled by default. |
| Subagent | A specialized assistant in its own context window with custom system prompt, tool access and independent permissions; returns a summary to the parent. Stays inside the spawning session (use cross-session messaging to pass findings between separate sessions). Built-ins: Explore, Plan, general-purpose. |
| Agentic coding | The AI reads files, runs commands and edits autonomously, as opposed to chat that only returns text. |
| Agentic harness | The tools, context management and execution environment around the model; Claude Code is the harness, Claude the model. It supplies file access, shell, permission gating, memory loading and the loop. |
| Agentic loop | Gather context, act, verify, repeat; hooks, skills and MCP plug into phases of it. |
| Turn | One complete response from a message to the end of Claude's reply, with any number of tool calls; Stop hooks fire at the end of each turn. |
| Verification loop | Giving Claude a runnable check (tests, build, screenshot comparison) so it iterates until the check passes; the prerequisite for `/goal`, unattended runs and dynamic workflows. |
| Worktree isolation | Runs Claude in a separate git worktree under `.claude/worktrees/`, enabled with `-w` or `isolation: worktree` in subagent config, so parallel agents edit their own copy on a separate branch. |
| Bundled skills | Prompt-based playbooks shipped with Claude Code such as `/batch`, `/code-review`, `/debug`, `/loop`; unlike built-in commands they can spawn agents and adapt to the codebase. |
| Cloud session | A session that keeps running on cloud infrastructure (Anthropic-managed or a self-hosted environment); started from claude.ai/code, the mobile app, the Desktop app with Cloud selected, `claude --cloud`, or a cloud scheduled task. |
| Channel | An MCP server that pushes events into a running session, optionally two-way; Telegram, Discord and iMessage are in the research preview. |
| Dispatch | A phone-initiated router that spawns a Claude Code session in the Desktop app from the mobile app; Pro, Max and Ultra plans. |
| Remote Control | Continue a local session from phone or browser via claude.ai; code and files stay on your machine (unlike a cloud session). |
| Teleport | `/teleport` pulls a cloud session into the local terminal (fetches branch, loads history); the reverse is `--cloud`. |
| Surface | Any place Claude Code is accessed (CLI, VS Code, JetBrains, Desktop, claude.ai); all share one engine; cloud sessions start from a fresh clone and do not read local `~/.claude/`. Slack and the Chrome extension are integrations, not surfaces. |
