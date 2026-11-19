---
type: "Feature"
title: "loop.md default prompt file"
description: "A loop.md file replaces the built-in maintenance prompt used by a bare /loop."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [loop, prompt, files, scheduling]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/loop.md"
  - "~/.claude/loop.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plain Markdown file defining the single default prompt for bare `/loop` (not a list of tasks). It is ignored whenever you give a prompt on the command line.

# How to use it

| Path | Scope |
| :- | :- |
| `.claude/loop.md` | Project; wins when both exist |
| `~/.claude/loop.md` | User; applies where the project has none |

The first file found is used. No required structure: write it as if typing the `/loop` prompt. Edits take effect on the next iteration, so a running loop can be refined. With neither file, the built-in maintenance prompt runs.

# Limits and defaults

Content beyond 25,000 bytes is truncated. To schedule more prompts alongside it, use `/loop <prompt>` or ask Claude directly.
