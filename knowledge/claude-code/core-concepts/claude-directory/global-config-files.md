---
type: "Reference"
title: "Global ~/.claude files and when they load"
description: "User-scope files under ~/.claude and ~/.claude.json: CLAUDE.md, settings, keybindings, themes, rules, skills, agents, workflows, auto memory."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [claude-directory, global, memory, settings]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude.json"
  - "~/.claude/CLAUDE.md"
  - "~/.claude/settings.json"
  - "~/.claude/keybindings.json"
  - "~/.claude/themes/"
  - "~/.claude/projects/"
  - "~/.claude/projects/<project>/memory/MEMORY.md"
  - "~/.claude/rules/"
  - "~/.claude/skills/"
  - "~/.claude/commands/"
  - "~/.claude/output-styles/"
  - "~/.claude/agents/"
  - "~/.claude/workflows/"
  - "/keybindings"
  - "/theme"
  - "/output-style"
  - "outputStyle"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Global counterparts that apply in every project on the machine.

# How to use it

| File | When it loads | Notes |
| - | - | - |
| `~/.claude.json` | Session start; written back when you change a global config option in `/config` or trust a project folder | Account details, per-project trust decisions, personal MCP servers, UI toggles. Created at session start or by a subcommand such as `claude auth status`, not by `--version` or `--help` |
| `~/.claude/CLAUDE.md` | Session start, every project | Loaded alongside project CLAUDE.md; on conflict Claude may follow either |
| `~/.claude/settings.json` | Session start; most edits apply live | Same format as project; ranks below project settings, `--settings` and managed settings |
| `~/.claude/keybindings.json` | Session start, hot-reloaded | Create or open with `/keybindings` |
| `~/.claude/themes/` | Session start, hot-reloaded; listed in `/theme` | `.json` files: built-in `base` preset plus `overrides` map; selected custom theme stored as `custom:<slug>` |
| `~/.claude/projects/` | Current project's `memory/MEMORY.md` at session start while auto memory is on; topic files on demand | Auto memory, one directory per project keyed by repository path |
| `~/.claude/projects/<project>/memory/MEMORY.md` | First 200 lines, capped at 25KB | Index to topic files (e.g. `user_role.md`), created and updated by Claude; you can edit or delete |
| `~/.claude/rules/` | Same as project rules | Applies to every project |
| `~/.claude/skills/`, `~/.claude/commands/` | Same as project | Personal, all projects |
| `~/.claude/output-styles/` | Read at startup in the terminal | Select with `/output-style`, `/config` or the `outputStyle` key; a project style with the same name wins |
| `~/.claude/agents/` | Each subagent runs in its own context window | Available in all projects |
| `~/.claude/workflows/` | Loaded at startup when workflows are on | A project workflow of the same name in `.claude/workflows/` takes precedence |

# Limits and defaults

Auto memory loads first 200 lines, capped at 25KB.
