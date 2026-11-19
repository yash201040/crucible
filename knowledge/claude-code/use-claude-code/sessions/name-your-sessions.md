---
type: "Feature"
title: "Naming sessions"
description: "Ways to name a session, plus the default display name and generated title that Claude Code assigns to unnamed ones."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, naming, resume, title]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.221"
surfaces: [cli, desktop]
requires: "Claude Code v2.1.221 or later to rename from claude.ai or the Claude app"
identifiers:
  - "claude -n <name>"
  - "-n"
  - "--name"
  - "/rename"
  - "CLAUDE_CODE_DISABLE_TERMINAL_TITLE"
  - "claude agents --json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Names make sessions findable in the picker and resumable by name, especially when running several tasks in parallel.

# How to use it

| When | How |
| :- | :- |
| Startup | `claude -n auth-refactor` |
| During a session | `/rename auth-refactor` (also shown on the prompt bar) |
| Picker | Highlight and press `Ctrl+R` |
| Plan accept | Accepting a plan in plan mode gives a generated title based on the plan unless already named |
| claude.ai or Claude app | Rename a Remote Control session; the CLI applies it (v2.1.221+) |
| Desktop app | Rename there; resumes in the desktop app |

Unnamed sessions get two labels. Only the generated title works as a resume handle:
- Default display name: working-directory name plus a two-character suffix (e.g. `my-app-3f`), shown in agent view and `claude agents --json`. It is not a resume handle.
- Generated title: a short summary of the first prompt written by a background request to the small/fast model (normally Haiku-class). A `claude -p` run started directly from a shell or script gets none. With `CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1`, terminal and Agent SDK sessions do not get it. A plan accept replaces it. Either title resolves like a name in `claude --resume` and `/resume`.
