---
type: "Reference"
title: "Essential shell and session commands"
description: "The basic claude shell invocations and in-session slash commands from the quickstart, with shortcuts."
resource: "https://code.claude.com/docs/en/quickstart"
tags: [commands, cli, quickstart, shortcuts]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude"
  - "claude \"task\""
  - "claude -p"
  - "claude -c"
  - "claude -r"
  - "/clear"
  - "/help"
  - "/exit"
  - "Shift+Tab"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "quickstart"
    resource: "https://code.claude.com/docs/en/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The quickstart's list of daily commands.

# How to use it

Shell commands:

| Command | What it does |
| - | - |
| `claude` | Start interactive mode |
| `claude "task"` | Interactive mode with an initial prompt, e.g. `claude "fix the build error"` |
| `claude -p "query"` | One-off query, then exit, e.g. `claude -p "explain this function"` |
| `claude -c` | Continue the most recent conversation in the current directory |
| `claude -r` | Resume a previous conversation |

Session commands:

| Command | What it does |
| - | - |
| `/clear` | Start a new conversation; resume the previous one with `/resume` |
| `/help` | Show available commands |
| `/exit` or Ctrl+D twice | Exit |

Shortcuts: type `/` to list commands and skills; Tab completes commands; Up arrow shows history; `Shift+Tab` cycles permission modes.

# Notes

Full lists are in the CLI reference and commands reference. The page's workflow steps are plain-language prompts (explore, edit, git, bug fix, refactor, tests); Claude reads project files as needed, so no manual context is needed.
