---
type: "Release Digest"
title: "Sessions, context and memory (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on resume, compaction, context windows, transcripts, memory and background sessions."
resource: "https://code.claude.com/docs/en/changelog"
tags: [sessions, context, memory, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT"
  - "/context"
  - "/compact"
  - "/resume"
  - "MEMORY.md"
  - "/rewind"
  - "language"
  - "/cd"
  - "CLAUDE_CODE_SESSION_ID"
  - "--continue"
  - "--resume"
  - "CLAUDE_CODE_ENABLE_AWAY_SUMMARY"
  - "/recap"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | Auto-compact on 1M-context Opus and Fable sessions fires shortly before the 1M limit; recovery compaction no longer times out at 10 minutes |  |
| 2.1.247 | 2026-08-26 | Sonnet 5 auto-compacts at about 967K tokens on the full 1M window (was about 934K) |  |
| 2.1.239 | 2026-08-21 | Post-compaction reminder no longer re-runs a skill's original arguments |  |
| 2.1.235 | 2026-08-18 | Context-limit error says when auto-compact is off and points to /config |  |
| 2.1.234 | 2026-08-17 | Claude Code continues the session automatically when a claude.ai usage limit resets ("Continue automatically at usage limit"); built-in claude-api skill context cost cut from 200k+ to about 25k tokens |  |
| 2.1.229 | 2026-08-12 | prompt is too long errors explain why automatic compaction could not recover |  |
| 2.1.224 | 2026-08-07 | Fullscreen mode keeps full pre-compaction history in scrollback across compactions |  |
| 2.1.223 | 2026-08-06 | Auto-compact keeps unrecognized model IDs inside the assumed window; CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1 restores old behavior | `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT` |
| 2.1.217 | 2026-07-21 | Warnings when transcript writes fail or session saving is off |  |
| 2.1.216 | 2026-07-20 | /context warns when the conversation exceeds the window; failed /compact shows as an error | `/context`, `/compact` |
| 2.1.214 | 2026-07-18 | Memory file frontmatter gets an ISO modified timestamp; SessionStart reports source fork |  |
| 2.1.212 | 2026-07-17 | Typing /resume in agent view opens a picker including deleted sessions; resumes as background session | `/resume` |
| 2.1.211 | 2026-07-15 | Memory index over-limit warning measures loaded content only |  |
| 2.1.210 | 2026-07-14 | Memory writes leaving MEMORY.md over its limit now error instead of silent truncation | `MEMORY.md` |
| 2.1.208 | 2026-07-14 | Session transcript size reduced up to 79x in edit-heavy sessions; file edit read cache bounded to 16 MB |  |
| 2.1.191 | 2026-06-24 | /rewind can resume a conversation from before /clear | `/rewind` |
| 2.1.186 | 2026-06-22 | Agent reminded to compact MEMORY.md near the size limit |  |
| 2.1.176 | 2026-06-12 | Session titles generated in the conversation language (language setting pins one) | `language` |
| 2.1.169 | 2026-06-08 | CLAUDE.md too long warning scales with context window; /cd moves a session without breaking the prompt cache | `/cd` |
| 2.1.144 | 2026-05-19 | /resume includes background sessions; resumed sessions keep their own model |  |
| 2.1.141 | 2026-05-13 | Rewind menu gains Summarize up to here |  |
| 2.1.139 | 2026-05-11 | Compaction prompt preserves sensitive user instructions; /context all per-skill estimates | `/context` |
| 2.1.132 | 2026-05-06 | CLAUDE_CODE_SESSION_ID in Bash tool environment, matching hooks session_id | `CLAUDE_CODE_SESSION_ID` |
| 2.1.118 | 2026-04-23 | --continue and --resume find sessions that added the current directory via /add-dir | `--continue`, `--resume` |
| 2.1.117 | 2026-04-22 | /resume offers to summarize stale large sessions first |  |
| 2.1.110 | 2026-04-15 | --resume and --continue resurrect unexpired scheduled tasks; session recap enabled with telemetry disabled (CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 opts out) | `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` |
| 2.1.108 | 2026-04-14 | Recap feature (/recap) gives context when returning to a session; /resume defaults to current directory, Ctrl+A shows all projects | `/recap` |
| 2.1.101 | 2026-04-10 | claude -p --resume accepts session titles |  |
