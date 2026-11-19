---
type: "Reference"
title: "Desktop versus CLI comparison"
description: "What carries over from the CLI, flag equivalents, moving sessions with /desktop and claude --desktop, and what Desktop lacks."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, cli, comparison, resume, headless]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [desktop, cli]
requires: "/desktop: macOS or x64 Windows with a Claude subscription"
identifiers:
  - "/desktop"
  - "claude --desktop"
  - "--continue"
  - "--resume"
  - "/resume"
  - "--print"
  - "--output-format"
  - "--add-dir"
  - "--allowedTools"
  - "--disallowedTools"
  - "--dangerously-skip-permissions"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Desktop runs the same engine as the CLI with a graphical interface. Both can run on the same project; each keeps its own session list. Shared: CLAUDE.md and `CLAUDE.local.md`, MCP servers in `~/.claude.json` or `.mcp.json`, hooks, skills, `~/.claude.json` and `~/.claude/settings.json` (permission rules apply). The Code tab runs its own copy of Claude Code; check its version with `/status` in a local session.

# How to use it

- `/desktop` in the CLI saves the session and opens it in Desktop; `claude --desktop` (Claude Code v2.1.285+) does it from the shell, with `--continue` or `--resume <session-id>` (names do not work). Not available with API key auth, Bedrock, Agent Platform or Foundry. Does not move a session open in another terminal or running in background.
- In Desktop, `/resume` lists CLI sessions on this computer (local sessions only; not SSH, WSL or cloud). The same session continues, not a copy.

| CLI | Desktop |
| - | - |
| `--model` | model picker |
| `--resume`, `--continue` | sidebar or `/resume` |
| `--permission-mode` | mode selector |
| `--dangerously-skip-permissions` | Bypass permissions mode |
| `--add-dir` | Add folder, or several repositories in cloud |
| `--allowedTools`, `--disallowedTools` | no per-session equivalent; settings rules apply |
| `--print`, `--output-format` | not available (Desktop is interactive only) |

# Limits and defaults

Not in Desktop: scripting and the Agent SDK, `dontAsk` mode, agent teams (use dynamic workflows), inline code suggestions, third-party providers by default (gateway or Desktop on 3P instead), Computer Use on Linux. Dispatch and the iOS Simulator pane are Desktop-only; CLI uses computer use via `/mcp` on macOS.
