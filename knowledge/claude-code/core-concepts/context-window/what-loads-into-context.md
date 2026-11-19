---
type: "Concept"
title: "What enters the context window"
description: "What loads before the first prompt and as Claude works, with the page's illustrative token counts for each step."
resource: "https://code.claude.com/docs/en/context-window"
tags: [context, tokens, startup, subagents]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/context"
  - "/memory"
  - "--append-system-prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "context-window"
    resource: "https://code.claude.com/docs/en/context-window"
    title: "Explore the context window"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The context window holds the instructions, files read, Claude's own responses and content never shown in the terminal. Before you type: CLAUDE.md, auto memory, MCP tool names and skill descriptions load (AGENTS.md can replace CLAUDE.md; an output style or `--append-system-prompt` text may add more). As Claude works: each file read adds tokens, path-scoped rules load alongside matching files, and PostToolUse hooks fire after edits. A subagent does research in its own separate context window; only a summary and a small metadata trailer return.

# How to use it

Run `/context` for a live breakdown by category with optimization suggestions (including which CLAUDE.md and auto memory files loaded). Run `/memory` to open and edit them.

Illustrative token counts (they vary with CLAUDE.md size, MCP servers and file lengths):

| Phase | Item | Tokens |
| - | - | -: |
| Before you type | System prompt | 4,200 |
| Before you type | Auto memory (`MEMORY.md`) | 680 |
| Before you type | Environment info | 280 |
| Before you type | MCP tool names | 120 |
| Before you type | Skill descriptions | 450 |
| Before you type | `~/.claude/CLAUDE.md` | 320 |
| Before you type | Project CLAUDE.md | 1,800 |
| As Claude works | File reads 2,400 / 1,100 / 1,800 / 1,600 | 6,900 total |
| As Claude works | Rules 380 and 290; search 600; edits 400 and 600; Prettier hook output 120 and 100; `npm test` output 1,200 | various |
| Follow-up | Subagent call 80; subagent summary 420 | small |
| End | `!git status` 180; `/commit-push` skill body 620 | |

Before `/compact`: 22,225 tokens in use; the subagent uses another 9,890 tokens in its own window. After `/compact`: 17,095 tokens (startup rows, a 1,725-token summary, the four files read, and the skill body).

# Notes

Tip from the page: send large reads to a subagent so file contents stay out of your context.
