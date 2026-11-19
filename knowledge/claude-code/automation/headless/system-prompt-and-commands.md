---
type: "Reference"
title: "System prompt flags and commands in -p mode"
description: "Appending or replacing the system prompt, and which slash commands and forms work non-interactively."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, system-prompt, slash-commands, skills]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [headless]
requires: "/output-style needs v2.1.269+"
identifiers:
  - "--append-system-prompt"
  - "--system-prompt"
  - "/model"
  - "/effort"
  - "/fast"
  - "/color"
  - "/rename"
  - "/mcp"
  - "/config"
  - "/output-style"
  - "/login"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--append-system-prompt` adds instructions while keeping the default behavior, e.g. `gh pr diff "$1" | claude -p --append-system-prompt "You are a security engineer. Review for vulnerabilities." --output-format json`. `--system-prompt` fully replaces the default; a replaced prompt also starts the run without the git status snapshot.

# How to use it

Command support in `-p`:

| Command | Behavior |
| --- | --- |
| User-invoked skills and custom commands | Work; include `/skill-name` in the prompt and it is expanded |
| Terminal-only built-ins such as `/login` | Not available |
| `/model`, `/effort`, `/fast`, `/color`, `/rename` | Accept a value argument, e.g. `/model sonnet` |
| `/mcp` with no argument | Prints a text summary of server status |
| `/config key=value` | Changes a setting, e.g. `/config verbose=true` |
| `/output-style <style>` / `/output-style` | Switches / lists output styles (v2.1.269+) |

# Notes

Build-script pattern: `git diff main | claude -p "you are a typo linter..."` in a `package.json` script, so Claude needs no Bash permission to read the diff.
