---
type: "Reference"
title: "Hook skipped and mod unloaded messages"
description: "Lines for skipped hooks, unanswered commands, worker crashes, repeated session.start, failed reloads and refused $.agent.register."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, hooks, worker, reload]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli]
requires: ""
identifiers:
  - "hook skipped"
  - "no command.run hook answered it"
  - "it crashed the hooks worker"
  - "its session.start ran again in a fresh copy"
  - "This mod's change didn't load, so the earlier version is still running"
  - "This mod didn't load, and the earlier version is no longer running"
  - "reload failed, the previous version stays loaded"
  - "reload failed"
  - "$.agent.register refused: the hooks module that made the call is no longer loaded"
  - "mods that run in the hooks worker are off for this session"
  - "focus: false"
  - "$.agent.spawn"
  - "$.prompt.submit"
  - "$.command.run"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages about hooks that fail after a mod loaded, and mods that get unloaded.

# How to use it

| Message | Meaning and fix |
| :- | :- |
| `<mod>: <event> hook skipped: <reason>` (e.g. `first-mod: tool.call hook skipped: threw Error: boom`) | A hook threw, exceeded its time limit, or returned the wrong shape. Shown once per event and failure kind until the mod reloads; the debug log has every occurrence |
| `<mod> registered /tally but no command.run hook answered it` | The command reached the end of the chain: no `command.run` hook, a filter naming a different command, the hook returned `next(e)`, or the hook was skipped (passing `focus: false` to `$.ui.open` is one way) |
| `<mod> was unloaded: it crashed the hooks worker` | Installed mods share one worker thread; it crashed or stopped responding and was traced to this mod (e.g. a loop that never awaits). Fix the hook |
| `<mod>: its session.start ran again in a fresh copy; the $.prompt.submit call it had already made was not made again` | Module reloaded (e.g. worker crash) and `session.start` reran; the named `$.prompt.submit`, `$.command.run` or `$.agent.spawn` call resolved with its first result instead of running again. Nothing to fix. Before v2.1.292 the call ran a second time |
| `This mod's change didn't load, so the earlier version is still running: <reason>.` / `This mod didn't load, and the earlier version is no longer running: <reason>.` | A change to a mod Claude wrote in this session failed. Claude does not see this line; paste it into your next message |
| `reload failed, the previous version stays loaded: <reason>` | Last working version keeps running; it unloads if the change still fails at the next reload of all plugins (e.g. `/reload-plugins`) |
| `reload failed: <reason>` | Run `/plugin`; if the `mods active` line names the mod the last working version is loaded, otherwise none is |
| `<mod>: $.agent.register refused: the hooks module that made the call is no longer loaded (it was reloaded or removed)` | Call came from code in the old copy after a reload; agent not registered. Make the call in the `session.start` hook, which reruns in each fresh copy |
| `hooks: mods that run in the hooks worker are off for this session: it crashed 3 times` | Worker stopped three times with no single mod to blame; every non-built-in mod (including organization-installed) is unloaded. Reaches the transcript in every interactive session. Run `/reload-plugins` |

# Notes

A hook that does not catch a rejection fails and is skipped. Mods can start subagents (`$.agent.spawn`) and register agents (`$.agent.register`).
