---
type: "Feature"
title: "Bare mode (--bare)"
description: "--bare skips hooks, skills, plugins, MCP, memory and CLAUDE.md discovery for fast, reproducible scripted runs."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, bare, ci, startup]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.286"
surfaces: [cli, headless, sdk]
requires: "ANTHROPIC_API_KEY or apiKeyHelper for the Anthropic API"
identifiers:
  - "--bare"
  - "--append-system-prompt"
  - "--append-system-prompt-file"
  - "--settings"
  - "--mcp-config"
  - "--agents"
  - "--plugin-dir"
  - "--plugin-url"
  - "--add-dir"
  - "--ide"
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--bare` reduces startup time by skipping auto-discovery of hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory and CLAUDE.md. Without it, `claude -p` loads them as an interactive session would, including anything in the working directory or `~/.claude`. The docs recommend `--bare` for scripted and SDK calls and say it will become the default for `-p` in a future release. Example: `claude --bare -p "Summarize README.md" --allowedTools "Read"`.

Without `--bare`, a `-p` session runs hooks from a project's `.claude/settings.json` and connects servers from its `.mcp.json` even in a never-trusted folder, with no trust dialog or per-server prompt.

# How to use it

In bare mode Claude has Bash, file read and file edit tools. Pass other context with flags:

| To load | Use |
| --- | --- |
| System prompt additions | `--append-system-prompt`, `--append-system-prompt-file` |
| Settings | `--settings <file-or-json>` |
| MCP servers | `--mcp-config <file-or-json>` |
| Custom agents | `--agents <file-or-json>` |
| A plugin | `--plugin-dir <path>`, `--plugin-url <url>` |

Authentication: bare mode never reads OAuth credentials or the system keychain. Set `ANTHROPIC_API_KEY` (a Console key) or supply `apiKeyHelper` in the `--settings` JSON. Bedrock, Google Cloud's Agent Platform and Foundry still read their own provider credentials.

# Limits and defaults

- Hooks still do not run in bare mode when passed via `--settings`, or in a flag-loaded plugin's `hooks/hooks.json` or manifest `hooks` key. Do not use bare mode for a run that needs hooks.
- A `--add-dir` directory: skills from its `.claude/skills/` load, but `.claude/commands/` and `.claude/agents/` do not.
- MCP: only servers supplied on the command line connect; interactive sessions skip the automatic IDE connection unless `--ide`.
- System reminders are not sent (no notice of files changed on disk, no skills list, including `--add-dir` skills).
- Background tasks are off: no background commands or subagents, other features that `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` disables are off, and a command hitting its timeout stops instead of moving to background.
- Before v2.1.286 these limits held only partly (interactive `--bare` connected normal MCP servers, system reminders were sent, background tasks stayed available).
