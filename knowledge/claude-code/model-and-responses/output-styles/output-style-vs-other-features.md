---
type: "Guide"
title: "Choose between an output style and other features"
description: "Maps needs to the right mechanism: style, CLAUDE.md, skill, hook, subagent or --append-system-prompt."
resource: "https://code.claude.com/docs/en/output-styles#choose-between-an-output-style-and-other-features"
tags: [output-styles, hooks, skills, claude-md, subagents]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--append-system-prompt"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An output style applies to every response and is an instruction, so nothing enforces it. Narrower or guaranteed needs fit other features.

# How to use it

| You want | Use |
| :- | :- |
| Every response in a certain voice, length, format, or a different role | An output style |
| Project conventions, commands, structure | CLAUDE.md (stays loaded whichever style) |
| Instructions for one kind of task | A skill (loaded only when invoked or matched) |
| Something every time without exception (formatting after each edit, blocking a command) | A hook (Claude Code runs it at a lifecycle event) |
| A helper with own instructions, model and tools | A subagent (separate context, returns a summary) |
| An addition to instructions at launch | `--append-system-prompt` (appends without removing anything) |

# Notes

The features combine: CLAUDE.md for knowledge, an output style for response form, a hook for guarantees.
