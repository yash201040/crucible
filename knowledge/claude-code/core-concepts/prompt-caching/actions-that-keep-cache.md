---
type: "Reference"
title: "Actions that keep the cache"
description: "Edits, permission mode, output style, skills, /recap, /rewind and subagent spawns that leave the cached prefix intact."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, output-style, rewind, recap, permission-mode]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli]
requires: ""
identifiers:
  - "/output-style"
  - "outputStyle"
  - "/recap"
  - "/rewind"
  - "/clear"
  - "/compact"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

These actions append to the conversation or do not touch the request.

# How to use it

| Action | Why the cache stays |
| - | - |
| Editing repository files Claude already read | The copy in the conversation does not change |
| Editing project-root or user CLAUDE.md mid-session | Read at session start and held in memory; reload with `/clear`, `/compact` or restart |
| Nested CLAUDE.md and `paths:` rules | Load on demand; editing before load takes effect, after load it is history |
| Changing permission mode | System prompt and tools unchanged; exception: `opusplan` is a model switch |
| Changing output style (`/output-style`, `/config`, `outputStyle`) | Style instructions delivered as a conversation message; applies from next message. Before v2.1.251 it did not apply until `/clear` or a new session |
| Invoking skills and commands | Instructions injected as user messages; a frontmatter `model` can still be a model switch |
| `/recap` | Appends the summary as output rather than replacing history |
| `/rewind` | Truncates to an earlier, already-cached prefix; every turn since kept the entry warm; restoring file checkpoints has no separate effect |
| Spawning a subagent | See [subagents and the cache](./subagents-and-cache.md) |
