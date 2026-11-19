---
type: "Reference"
title: "Inspect what loaded: /context, /doctor and friends"
description: "Commands that show what Claude Code actually loaded: context contents, memory, skills, hooks, MCP servers, permissions, settings sources and diagnostics."
resource: "https://code.claude.com/docs/en/debug-your-config"
tags: [debugging, context, doctor, settings, diagnostics]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/context"
  - "/context all"
  - "/memory"
  - "/skills"
  - "/hooks"
  - "/mcp"
  - "/permissions"
  - "/doctor"
  - "claude doctor"
  - "/debug"
  - "/status"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "debug-your-config"
    resource: "https://code.claude.com/docs/en/debug-your-config"
    title: "Debug your configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When an instruction is ignored or a configured feature is missing, the cause is usually that the file did not load, loaded from another place, or was overridden. These commands show what was actually loaded.

# How to use it

| Command | Shows |
| :- | :- |
| `/context` | Everything in the context window by category: system prompt, system tools, MCP tools, custom subagents (with source), memory files, skills (including bundled skills that `/skills` omits), messages. In fullscreen mode the per-item breakdown is collapsed; use `/context all`. |
| `/memory` | Memory file locations across user and project scopes, open in editor, auto memory folder and toggle |
| `/skills` | Skills from project, user and plugin sources |
| `/hooks` | Active hook configuration, grouped by event |
| `/mcp` | Connected MCP servers and status |
| `/permissions` | Resolved allow and deny rules in effect |
| `/doctor` | Setup checkup: install health, invalid settings files, unused extensions, duplicate subagent names in one directory, checked-in `CLAUDE.md` content derivable from the code; proposes fixes and asks before applying |
| `claude doctor` | Terminal command: read-only installation and settings diagnostics without starting a session |
| `/debug [issue]` | Turns on debug logging for the session and has Claude diagnose from the log and settings paths |
| `/status` | Active settings sources, including whether managed settings apply |

# Limits and defaults

- Settings precedence: managed settings first when present; otherwise local over project over user. Command-line flags and environment variables are another override layer.
- Subdirectory `CLAUDE.md` files load on demand, so they do not appear in `/context` at start.
- `CLAUDE.md` is guidance; permissions and hooks enforce limits regardless of what Claude decides.

# Notes

If a file is shown loaded but not followed, the problem is the instruction (vague, conflicting, or too long a file), not loading.
