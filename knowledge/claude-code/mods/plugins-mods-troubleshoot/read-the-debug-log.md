---
type: "Guide"
title: "Read the mod debug log"
description: "Start Claude Code with --debug or --debug-file to get a line for every module loaded or refused, hook failure and refused result."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, debug-log, debugging]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--debug"
  - "--debug-file <path>"
  - "$.ui.log"
  - "{ to: 'debug' }"
  - "@inline"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The debug log has a line for every module Claude Code loads or refuses, every hook that fails and every result it refuses; use it when the transcript shows nothing.

# How to use it

```bash
claude --debug-file ./mod-debug.log --plugin-dir ./first-mod
tail -f ./mod-debug.log | grep first-mod
```

A loaded mod has a line naming it and its events; a mod loaded with `--plugin-dir` appears as `<name>@inline`:
`hooks module first-mod@inline loaded (worker, environment 2, tier user); events: session.start,tool.call,command.run,ui.render`.

To write your own lines call `$.ui.log('message', { to: 'debug' })`. Without the second argument `$.ui.log` adds a dim line to the transcript.

# Notes

Related: [diagnosing a mod](./diagnose-a-mod-that-does-nothing.md).
