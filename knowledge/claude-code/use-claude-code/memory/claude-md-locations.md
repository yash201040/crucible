---
type: "Reference"
title: "CLAUDE.md file locations and scopes"
description: "Where managed, user, project and local CLAUDE.md files live, in load order from broadest to most specific."
resource: "https://code.claude.com/docs/en/memory"
tags: [claude-md, scopes, managed-policy, paths]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/Library/Application Support/ClaudeCode/CLAUDE.md"
  - "/etc/claude-code/CLAUDE.md"
  - "C:\\Program Files\\ClaudeCode\\CLAUDE.md"
  - "~/.claude/CLAUDE.md"
  - "./CLAUDE.md"
  - "./.claude/CLAUDE.md"
  - "./CLAUDE.local.md"
  - "/init"
  - "CLAUDE_CODE_NEW_INIT"
  - "/context all"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

CLAUDE.md files can live in several locations. The table is in load order, broadest first, so a project instruction appears in context after a user instruction.

# How to use it

| Scope | Location | Shared with |
| - | - | - |
| Managed policy | macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`; Linux and WSL `/etc/claude-code/CLAUDE.md`; Windows `C:\Program Files\ClaudeCode\CLAUDE.md` | All users in the organization |
| User | `~/.claude/CLAUDE.md` | Only you, all projects |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team via source control |
| Local | `./CLAUDE.local.md` (add to `.gitignore`) | Only you, current project |

- Run `/init` to generate a starting CLAUDE.md from the codebase; if one exists it suggests improvements instead of overwriting.
- Set `CLAUDE_CODE_NEW_INIT=1` before `/init` for an interactive multi-phase flow: it asks which artifacts to set up (CLAUDE.md files, skills, hooks), explores with a subagent, asks follow-up questions and shows a reviewable proposal before writing. The variable only changes how `/init` runs; set it in the shell or the `env` block of a settings file.
- Confirm a file loaded with `/context all` and look under **Memory files**. In fullscreen mode, `/context` alone collapses that list.
- Add to CLAUDE.md when Claude repeats a mistake, a review catches something it should know, you retype the same correction, or a new teammate would need the same context. Multi-step procedures or single-area rules belong in a skill or path-scoped rule.

# Notes

Files above the working directory load at launch; subdirectory files load on demand. See [how files load](./how-claude-md-files-load.md).
