---
type: "Guide"
title: "Turn on the sandbox and verify it"
description: "Steps to enable the sandbox with /sandbox, the panel tabs, where choices are saved, per-session enabling, and a probe that confirms commands are sandboxed."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, setup, verification, settings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/sandbox"
  - "--settings"
  - "sandbox.enabled"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.failIfUnavailable"
  - ".claude/settings.local.json"
  - "~/.claude/settings.json"
  - "--add-dir"
  - "/add-dir"
  - "permissions.additionalDirectories"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The sandbox is built in. macOS uses the built-in Seatbelt framework; Linux and WSL2 need `bubblewrap` and `socat` (see [Linux and WSL2 setup](./linux-wsl2-setup.md)).

# How to use it

1. Run `/sandbox`. The panel has tabs: **Mode** (how sandboxed commands are approved), **Overrides** (the `allowUnsandboxedCommands` setting, shown as Strict sandbox mode), **Config** (resolved settings), plus a **Dependencies** tab on Linux when the optional seccomp filter is missing. If Dependencies is the only tab, the sandbox cannot start yet.
2. Choose auto-allow or regular permissions on the Mode tab (see [sandbox modes](./sandbox-modes.md)).
3. Ask Claude to run a Bash command. The first time a command needs a new network domain Claude Code prompts; in auto mode Claude names the hosts on the command itself instead.

A mode chosen in the panel is saved to `.claude/settings.local.json` (project-local; added to your global gitignore). To enable it in all projects, set `sandbox.enabled` to `true` in `~/.claude/settings.json`. For one session without writing a file:

```
claude --settings '{"sandbox": {"enabled": true, "allowUnsandboxedCommands": false}}'
```

Verify by asking Claude (not by typing at `!`) to run:

| Command | Expected result inside the sandbox |
| - | - |
| `touch ~/sandbox-probe` | `Operation not permitted` on macOS, `Read-only file system` on Linux/WSL2 |
| `curl --noproxy '*' https://example.com` | `Could not resolve host` |

If Claude asks to retry outside the sandbox, decline.

# Limits and defaults

Default: if the platform lacks support or the dependency check fails, commands run unsandboxed. Set `sandbox.failIfUnavailable` to `true` to exit at startup instead.
