---
type: "Reference"
title: "Glossary: effort, bare and non-interactive modes"
description: "Definitions of effort level, extended thinking, bare mode, non-interactive mode and the deprecated or renamed terms table."
resource: "https://code.claude.com/docs/en/glossary"
tags: [glossary, effort, headless, bare-mode, renamed-terms]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--bare"
  - "--add-dir"
  - "-p"
  - "--print"
  - "--no-session-persistence"
  - "MAX_THINKING_TOKENS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "glossary"
    resource: "https://code.claude.com/docs/en/glossary"
    title: "Glossary"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Glossary terms about reasoning settings and run modes, plus the table of renamed terms.

# How to use it

| Term | Definition |
| :- | :- |
| Effort level | Controls adaptive reasoning (the model decides whether and how much to think per step); higher is deeper and costlier, lower is faster and cheaper. Supported on Fable models, Opus 4.6 and later, Sonnet 4.6 and later, and Haiku 5.5. |
| Extended thinking | Visible step-by-step reasoning before responding; adjust with effort level, or cap with `MAX_THINKING_TOKENS` on models with a fixed thinking budget. Shown in gray italic text. |
| Bare mode | `--bare` starts without hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory or CLAUDE.md, apart from skills in a directory passed with `--add-dir`. Recommended for CI and scripted calls for the same result on every machine. |
| Non-interactive mode | Runs a single prompt and exits, with `-p` or `--print`; for CI, scripts and piping. The run is still saved as a resumable session unless `--no-session-persistence` is passed. The Agent SDK is the Python and TypeScript equivalent. Formerly headless mode. |

Deprecated and renamed terms:

| Old term | Now called | Notes |
| :- | :- | :- |
| Headless mode | Non-interactive mode | same `-p` flag and behavior |
| Web session; "Claude Code on the web" for any cloud session | Cloud session | "Claude Code on the web" now names only the browser surface at claude.ai/code |
| Custom commands | Skills | `.claude/commands/` files still work |
| Slash commands | Commands | "Slash" dropped from product copy |

# Notes

The glossary also states that "tool" means an action Claude can take (read a file, edit code, run a shell command, search the web, spawn a subagent); see [tools reference](../../reference/tools-reference/tools-agents-and-sessions.md).
