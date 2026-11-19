---
type: "Reference"
title: "Resume, transcript and session persistence variables"
description: "Variables for auto-resuming interrupted turns, resume prompts, skipping history, forcing persistence, transcript trimming and config directory choice."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [resume, sessions, transcripts, persistence]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS"
  - "CLAUDE_CODE_RESUME_PROMPT"
  - "CLAUDE_CODE_RESUME_SHOWS_CUT_OFF_CALLS"
  - "CLAUDE_CODE_RESUME_HINT_COMMAND"
  - "CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "CLAUDE_CODE_FORCE_SESSION_PERSISTENCE"
  - "CLAUDE_CODE_TRANSCRIPT_LOCAL_GC"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How sessions resume, where their state lives and whether it is stored at all. Useful for spawn scripts of long-running agents.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` | `1` auto-resumes when the previous session ended mid-turn, so the SDK need not resend the prompt (SDK mode). Unset or `0` turns it off. |
| `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` | Max age of the last transcript message for auto-continue; older sessions start idle. Unset or `0`: no bound, except some turns (such as one ended by an API error) resume only within six hours. Positive value bounds every turn; negative or non-numeric applies one hour. Claude Code itself uses one hour when restarting a crashed agent view session that inherited an interactive conversation. Requires v2.1.211+. |
| `CLAUDE_CODE_RESUME_PROMPT` | Continuation message sent when an interrupted turn continues, or when resuming a deferred tool call with `-p`. Default `Continue from where you left off.`; empty string uses the default. |
| `CLAUDE_CODE_RESUME_SHOWS_CUT_OFF_CALLS` | `1` keeps interrupted tool calls, marked cut off, in a continued turn; otherwise dropped. Calls to subagents, skills, workflows and tools waiting on a person stay dropped. Requires v2.1.309+. |
| `CLAUDE_CODE_RESUME_HINT_COMMAND` | Wrapper name shown at exit as `mytool --resume <session-id>` instead of `claude --resume <session-id>`. Must match `^\w[\w-]*$`; ignored in a settings `env` block. Requires v2.1.323+. |
| `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL` | `1` drops a deferred tool call whose tool is unavailable when resuming with `-p`; otherwise it stays pending and a prompt does not reach Claude. Requires v2.1.319+. |
| `CLAUDE_CODE_SKIP_PROMPT_HISTORY` | `1` writes no prompt history or session transcripts; such sessions are absent from `--resume`, `--continue` and up-arrow history. |
| `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE` | `1` forces transcript persistence, prompt history and `claude agents` registration even inside another Claude Code session (an inherited `CLAUDE_CODE_CHILD_SESSION` can misclassify a top-level session). Since v2.1.178 tmux is detected automatically. Honored on v2.1.169 and earlier; no effect on v2.1.170-v2.1.171. |
| `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` | `1` limits transcript growth of long `-p` or SDK sessions: after each compaction, once the file exceeds 5 MB, history before it is removed (from v2.1.296 skipped if it would shrink the file by under 10%). Resume restores the same conversation. Set in the launching environment; a settings `env` block cannot turn it on. Requires v2.1.287+. |
| `CLAUDE_CODE_PROJECT_DIR_NAME` | With `CLAUDE_CONFIG_DIR`, picks the `projects/` directory name for transcripts and auto memory, for example `CLAUDE_CONFIG_DIR=/srv/tenant-a CLAUDE_CODE_PROJECT_DIR_NAME=work claude` stores under `/srv/tenant-a/projects/work/`. Ignored without `CLAUDE_CONFIG_DIR`; read only from the launching environment. Requires v2.1.234+. |
| `CLAUDE_CONFIG_DIR` | Configuration directory (default `~/.claude`) holding settings, session history and plugins; useful for side-by-side accounts, for example `alias claude-work='CLAUDE_CONFIG_DIR=~/.claude-work claude'`. In a settings file write the absolute path. Ignored in project and local settings. |
