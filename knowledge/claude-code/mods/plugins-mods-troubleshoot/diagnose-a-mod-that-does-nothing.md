---
type: "Guide"
title: "Diagnose a mod that does nothing"
description: "When a mod's module or hook fails Claude Code skips it and continues; validate the mod, then read the one line naming it in the transcript, stderr or debug log."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, troubleshooting, validate, debug]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin validate"
  - "claude --debug"
  - "--plugin-dir"
  - "claude -p"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a mod's module or one of its hooks fails, Claude Code skips it and the session continues, so a broken mod looks like one that does nothing. `claude plugin validate ./first-mod` catches a misspelled event, a bad manifest and an unreadable module without starting a session.

# How to use it

When a module does not load, a hook is skipped, or another mod refuses yours, Claude Code writes one line naming the mod. Where to read it:

| Session | Where the line appears |
| :- | :- |
| Interactive session that hot-reloads a plugin directory (started with `--plugin-dir`, or hot reloading on for mods Claude wrote) | A dim line in the transcript |
| Any other interactive session (e.g. mod installed from a marketplace) | The debug log; start with `claude --debug` |
| `claude -p` run with `--plugin-dir` | stderr in the default text output format; a refusal by another mod goes to the debug log |

# Notes

See [reading the debug log](./read-the-debug-log.md) and [checking whether mods can load](./check-whether-mods-can-load.md).
