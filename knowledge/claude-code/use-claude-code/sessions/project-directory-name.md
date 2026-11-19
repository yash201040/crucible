---
type: "Feature"
title: "Pinning the project directory name"
description: "CLAUDE_CODE_PROJECT_DIR_NAME fixes the transcript and auto memory directory name for hosts that embed Claude Code."
resource: "https://code.claude.com/docs/en/sessions"
tags: [embedding, transcripts, config-dir, multi-tenant]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli, sdk]
requires: "Claude Code v2.1.234 or later"
identifiers:
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Set alongside `CLAUDE_CONFIG_DIR`, it stores that session's transcripts and auto memory under a name you choose instead of one derived from the working directory. Suited to a host that embeds Claude Code and gives each session its own config directory.

# How to use it

```
CLAUDE_CONFIG_DIR=/srv/tenant-a CLAUDE_CODE_PROJECT_DIR_NAME=work claude
```

This writes transcripts to `/srv/tenant-a/projects/work/` and auto memory to `/srv/tenant-a/projects/work/memory/` whatever the working directory.

# Limits and defaults

- Set `CLAUDE_CONFIG_DIR` too: Claude Code ignores `CLAUDE_CODE_PROJECT_DIR_NAME` when it is unset (under default `~/.claude` all projects would merge).
- Value: 1-64 letters, digits, hyphens or underscores; no Windows device name such as `con`. Any other value is ignored and the derived name used.
- Set it in the shell environment that starts `claude`; it is read once at startup, so an `env` block in a settings file cannot set it.
- Keep launching with it: without it, the same config dir reads and writes the derived directory again. Sessions under your name stay on disk; `Ctrl+A` in the picker lists every project directory under the config dir, and `claude --resume <session-id>` finds a session under either name.
