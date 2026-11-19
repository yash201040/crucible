---
type: "Reference"
title: "What survives compaction"
description: "Per-mechanism table of what is re-injected, rebuilt, reloaded on demand or summarized when a conversation compacts, with the file and skill caps."
resource: "https://code.claude.com/docs/en/context-window"
tags: [compaction, context, skills, hooks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: ""
identifiers:
  - "/compact"
  - "paths:"
  - "SessionStart"
  - "compact"
  - "includeGitInstructions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "context-window"
    resource: "https://code.claude.com/docs/en/context-window"
    title: "Explore the context window"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a long session compacts, Claude Code summarizes the conversation history to fit the window.

# How to use it

| Mechanism | After compaction |
| - | - |
| System prompt and output style | Still apply |
| Project-root CLAUDE.md and unscoped rules | Re-injected from disk |
| Auto memory | Re-injected from disk |
| Skill descriptions | Rebuilt from current skills and re-injected (requires v2.1.304 or later) |
| Git status snapshot | If the session started with one, a fresh one is read |
| Plan written in plan mode | Re-injected from disk |
| Rules with `paths:` frontmatter | Reloaded on demand |
| Nested CLAUDE.md in subdirectories | Reloaded on demand |
| Files Claude read or edited | Re-reads up to five, most recently modified first |
| Invoked skill bodies | Re-injected, capped at 5,000 tokens per skill and 25,000 total; oldest dropped first |
| Background commands and background subagents | Keep running; Claude is reminded which are running to avoid duplicates |
| Context hooks added earlier | Summarized with the conversation |
| SessionStart hooks matching the `compact` source | Run, output added to the compacted context |

# Limits and defaults

- A re-read file over 5,000 tokens comes back as a path reference (shown as `Referenced file` rather than `Read`).
- Path-scoped rules and nested CLAUDE.md load into message history, so compaction summarizes them away. To persist a rule, drop `paths:` or move it to the project-root CLAUDE.md.
- Skill truncation keeps the start of the file, so put the most important instructions at the top of `SKILL.md`.
