---
type: "Release Digest"
title: "Sessions, context and memory, 2.1.296 to 2.1.328"
description: "Release-note changes to resume, compaction, transcripts, background sessions, tasks and context handling between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [sessions, resume, compaction, transcripts, context, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "--resume"
  - "--continue"
  - "fg"
  - "--bg"
  - "claude --bg"
  - "/resume"
  - "/teleport"
  - "claude --teleport"
  - "/rewind"
  - "/clear"
  - "/compact"
  - "/autocompact"
  - "/context"
  - "/tasks"
  - "/btw"
  - "CLAUDE_CODE_TRANSCRIPT_LOCAL_GC"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS"
  - "cleanupPeriodDays"
  - "CLAUDE_CODE_AUTOMOUNT_ROOTS"
  - "~/.claude.json"
  - "claude purge"
  - "SendMessage"
  - "CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | Faster resume of large sessions; less memory resuming sessions with many images; less memory and better response in long SDK and desktop sessions running slow commands. | |
| 2.1.328 | 2026-11-19 | Cross-session messaging explains that Remote Control is off when a cloud session or another computer is not listed. | |
| 2.1.327 | 2026-11-17 | Added a line when a resumed session's earlier messages cannot be loaded; a transcript read that ends early on a very long session is retried once. | |
| 2.1.327 | 2026-11-17 | Some pre-started background sessions are discarded after an account change; a workflow paused at a usage limit stays paused after a login until the earlier login returns or you type a prompt. | |
| 2.1.327 | 2026-11-17 | Most prompts ignore answers other than Esc briefly after resuming with fg; transcript search finds text in edits and written files. | `fg` |
| 2.1.326 | 2026-11-16 | Claude's instructions keep wanted files out of its temporary scratchpad folder, which can be cleared (2.1.325). | |
| 2.1.323 | 2026-11-12 | Messages each session can send other sessions on the machine without a user prompt raised from about 20 to 100,000 (Desktop Code tab sessions from 20 to 100,000; 2.1.321 had raised 10 to 20). | |
| 2.1.323 | 2026-11-12 | /logout in a background session now signs out every session on the computer, deletes stored MCP logins and plugin secrets, and ends the session. | `/logout` |
| 2.1.321 | 2026-11-09 | Sessions with more images than fit in a request: Claude is told whether it saw a dropped image and repeat reads of an unchanged image are limited. | |
| 2.1.319 | 2026-11-06 | Added an "Earlier in this session" row to /tasks listing finished subagents. | `/tasks` |
| 2.1.318 | 2026-11-04 | ~/.claude.json, settings files and the stored login survive saves on shared network home directories better; unattended runs stop rewriting ~/.claude.json when unchanged. | `~/.claude.json` |
| 2.1.318 | 2026-11-04 | Removed the 2.1.288 fix that kept earlier thinking when resuming a conversation started on 2.1.286 or earlier. | |
| 2.1.314 | 2026-10-30 | Idle compaction for VS Code and Desktop Code tab; --resume faster on damaged transcripts; /context faster with 10,000+ MCP tools. | `--resume`, `/context` |
| 2.1.311 | 2026-10-26 | /teleport and claude --teleport warn when a compacted cloud session loads from its last compaction; background session exit messages say how to resume. | `/teleport`, `claude --teleport` |
| 2.1.311 | 2026-10-26 | Compaction asks again once for a summary when the reply has none; shell commands that reach their timeout show output so far and say the command still runs in the background. | |
| 2.1.304 | 2026-10-19 | Compaction summary in the transcript view lists names of tools called earlier; compaction resends the skill list; auto-mode classifier context no longer stored with every request; faster resume of large compacted sessions in SDK and headless. | |
| 2.1.300 | 2026-10-14 | Local session transcripts also record each API request's system prompt, tools and parameters; background sessions resume a carried workflow through the Workflow tool's approval. | |
| 2.1.299 | 2026-10-14 | Exit resume command names the session by ID and uses -w and -r if long flags do not fit; PDFs @-mentioned no longer have bytes kept in the transcript. | |
| 2.1.296 | 2026-10-09 | A large transcript file is no longer rewritten by CLAUDE_CODE_TRANSCRIPT_LOCAL_GC when that frees under 10% of it. | `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` |

# Not found in the documentation pages

- `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`
