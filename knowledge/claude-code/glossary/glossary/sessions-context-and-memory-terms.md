---
type: "Reference"
title: "Glossary: sessions, context, memory"
description: "Definitions of session, transcript, checkpoint, compaction, context window, CLAUDE.md, AGENTS.md, auto memory, rules and system prompt terms."
resource: "https://code.claude.com/docs/en/glossary"
tags: [glossary, sessions, context, memory, compaction]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.277"
surfaces: [cli]
requires: ""
identifiers:
  - "AGENTS.md"
  - "CLAUDE.md"
  - "~/.claude/CLAUDE.md"
  - ".claude/rules/"
  - "paths:"
  - "MEMORY.md"
  - "~/.claude/projects/"
  - "claude -c"
  - "--fork-session"
  - "/rewind"
  - "/compact"
  - "/context"
  - "/clear"
  - "/resume"
  - "--append-system-prompt"
  - "--system-prompt"
  - "additionalContext"
  - "<system-reminder>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "glossary"
    resource: "https://code.claude.com/docs/en/glossary"
    title: "Glossary"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Glossary terms about session state, context and persistent instructions.

# How to use it

| Term | Definition |
| :- | :- |
| Session | A conversation tied to the current directory with its own context window. Resume with `claude -c`, fork with `--fork-session` (new session ID, history kept), or run in parallel. `/clear` starts a new session; the old one stays available via `/resume`. Transcripts live under `~/.claude/projects/`. |
| Transcript | The conversation stored as a file, by default `~/.claude/projects/<project>/<session-id>.jsonl`; read back on resume. |
| Checkpoint | A restore point at each prompt that starts a turn; files are snapshotted before every edit. `Esc` twice or `/rewind` restores code, conversation or both, or summarizes from a message. Saved with the conversation. Bash-command file changes are not undone unless Claude had already used its edit tools on that file. |
| Compaction | Automatic summarization when the context window nears its limit; project-root CLAUDE.md and auto memory survive, conversation-only instructions may not. `/compact` triggers it, optionally with a focus. |
| Context window | A session's working memory (history, file contents, command output, CLAUDE.md, auto memory, loaded skills, system instructions); inspect with `/context`. |
| CLAUDE.md | Persistent instructions you write, loaded at session start as a user message after the system prompt; at `./CLAUDE.md` or `./.claude/CLAUDE.md`, `~/.claude/CLAUDE.md`, or managed policy; all discovered files are concatenated, broadest scope first. Project-root file is re-read from disk after compaction. |
| AGENTS.md | Project instructions for AI coding agents; read when no CLAUDE.md exists. The `Project instructions` setting in `/config` can read both or only CLAUDE.md. Reading it directly needs v2.1.277 or later; in some sessions it cannot be read and should be imported from a CLAUDE.md. |
| Auto memory | Notes Claude writes for itself, stored per git repository under `~/.claude/projects/`; all worktrees of a repo share one directory; the first 200 lines or 25 KB of the `MEMORY.md` index load each session. |
| Rules | Modular files in `.claude/rules/`; YAML `paths:` frontmatter path-scopes a rule so it loads only when a matching file is read, written or edited. |
| System prompt | Instructions sent before the conversation on every request and the first layer of the prompt cache; add with `--append-system-prompt`, replace with `--system-prompt`. CLAUDE.md and output-style instructions are not part of it. |
| System reminder | A message the harness adds to the conversation (wrapped in `<system-reminder>` tags). Carries CLAUDE.md files, output-style instructions, hook `additionalContext`, the skills list, notes that an edited file changed on disk, and commit and PR attribution lines. |
| `.claude` directory | Project-scoped config at `.claude/` (settings, hooks, skills, subagents, rules, auto memory); user defaults at `~/.claude/`. |
