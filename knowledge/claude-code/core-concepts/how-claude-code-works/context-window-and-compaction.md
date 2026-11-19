---
type: "Feature"
title: "Context window and compaction"
description: "What fills the context window, automatic compaction into a summary, how to steer it, the thrashing stop, and attribution settings."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [context, compaction, compact, system-reminder]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/context"
  - "/compact"
  - "attribution"
  - "includeGitInstructions"
  - "disable-model-invocation: true"
  - "skillOverrides"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The window holds conversation history, file contents, command outputs, CLAUDE.md, auto memory, loaded skills and system instructions. Claude Code compacts automatically near the limit into a summary that keeps requests and key code snippets; detailed early instructions may be lost, so persistent rules go in CLAUDE.md.

# How to use it

- `/context` shows what is using space.
- Add a "Compact Instructions" section to CLAUDE.md, or run `/compact focus on the API changes`, to steer what is kept.
- Skills load on demand (descriptions at start, content on use); `disable-model-invocation: true` keeps descriptions out; `skillOverrides` does the same from settings.
- Subagents have their own window; a fork starts with a copy of the conversation. Their tool calls stay out of your context and a summary returns.
- MCP tool definitions are deferred by default via tool search, so only names and server instructions use context.
- Claude Code adds context itself: CLAUDE.md files, output style instructions, notes that an edited file changed on disk, and commit and PR attribution lines. Change attribution with `attribution`; remove built-in commit and PR instructions with `includeGitInstructions` set to `false`.

# Limits and defaults

If one file or tool output refills context immediately after each summary, auto-compaction stops after a few attempts and shows an error instead of looping (see the "Auto-compaction stops with a thrashing error" troubleshooting entry).
