---
type: "Feature"
title: "Checkpoints and permission modes"
description: "File snapshots before edits (Esc twice to rewind) and the four permission modes cycled with Shift+Tab, including Auto as the starting mode."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [checkpoints, rewind, permissions, auto-mode, plan-mode]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, ide]
requires: "Auto as built-in starting mode: Claude Code v2.1.283 or later; earlier versions only on Pro, Max, Ultra and Team plans"
identifiers:
  - "Shift+Tab"
  - "Esc"
  - ".claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Before Claude edits a file it snapshots the contents; press `Esc` twice to rewind or ask Claude to undo. Checkpoints are separate from git and survive resume. They cover file changes only, a restore skips symlinked and hard-linked files, and actions on remote systems (databases, APIs, deployments) cannot be checkpointed.

# How to use it

`Shift+Tab` cycles permission modes:

| Mode | Behavior |
| - | - |
| Auto | A classifier reviews most actions in the background and blocks risky ones instead of asking |
| Manual | Asks before file edits and shell commands |
| Accept edits | Edits files and runs common filesystem commands such as `mkdir` and `mv` without asking; asks for other commands |
| Plan | Explores and proposes a plan without editing source files |

Specific commands can be allowed in `.claude/settings.json`, scoped from organization policy down to personal preference.

# Limits and defaults

Auto is the built-in starting mode for interactive terminal and VS Code sessions from v2.1.283; on earlier versions only on Pro, Max, Ultra and Team plans.
