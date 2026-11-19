---
type: "Limit"
title: "Memory and instruction size limits"
description: "Per-file and combined size limits for CLAUDE.md, rules and MEMORY.md, and the 200K/1M context-window character limits for on-demand files."
resource: "https://code.claude.com/docs/en/memory"
tags: [limits, claude-md, context-window, rules]
kind: "limit"
maturity: "unlabelled"
since: "2.1.309"
surfaces: []
requires: ""
identifiers:
  - "/status"
  - "wc -m"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Size limits that decide how much instruction text Claude actually receives.

# Limits and defaults

| Item | Limit |
| :- | :- |
| Recommended CLAUDE.md size | under 200 lines |
| CLAUDE.md loaded at launch | whole file if 4 MiB or smaller; a larger file is skipped and none of it loads |
| MEMORY.md at session start | first 200 lines or 25KB |
| On-demand files (subdirectory CLAUDE.md / CLAUDE.local.md and their imports, subdirectory `.claude/rules/`, path-scoped rules in project `.claude/rules/` or `~/.claude/rules/`), 200K context window | 40,000 characters per file |
| Same, 1M context window | 200,000 characters on Claude Opus 4.6 and Claude Sonnet 4.6; 150,000 on later models |
| Import depth | 4 hops |
| Brace-expansion budget per `paths` list | 1,000 patterns and 4 MiB |

# How to use it

An on-demand file over its limit delivers only its start, ending with a note to read the rest with the Read tool; later instructions are not in context until Claude does. Check with `wc -m path/to/CLAUDE.md` (Bash or Zsh); trim or move part into rules files, each counting separately. Before v2.1.309 this limit was not applied to on-demand files.

An over-length instruction file produces a warning at startup and in `/status`; a warning also appears when files each within length add up past a combined limit at session start. Each CLAUDE.md, rules file and `@path` import counts as a separate file.
