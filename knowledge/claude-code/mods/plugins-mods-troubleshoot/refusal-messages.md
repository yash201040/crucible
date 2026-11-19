---
type: "Reference"
title: "Hooks module refusal messages"
description: "Reasons that follow 'hooks module <name> not loaded:' in the debug log or stderr, with their meaning."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, troubleshooting, refusal, policy]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "not loaded:"
  - "disableAllHooks in managed settings"
  - "only managed plugins and built-in plugins run"
  - "allowManagedHooksOnly"
  - "--bare"
  - "installed plugins that are not managed load no hooks module in this mode (--bare)"
  - "another plugin of that name loads first"
  - "hooks module first-mod@inline not loaded: disableAllHooks in managed settings"
  - "mods active"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If nothing the mod adds appears and the `mods active` line in `/plugin` does not name it, the hooks module did not load. When Claude Code refused it, the debug log has a line starting `hooks module`, the mod's name and `not loaded:`. A `claude -p` run prints `hooks module not loaded` to stderr (no transcript). Read the reason after the colon.

# How to use it

| Message starts with | Meaning |
| :- | :- |
| `hooks modules are turned off for installed plugins in this process: the rollout switch served off` | Anthropic turned installed mods off remotely |
| `hooks modules are turned off for installed plugins in this process: the rollout switch was saved off by an earlier session` | Value saved by an earlier session, maybe stale; restart Claude Code |
| `disableAllHooks in managed settings` | Organization turned off hooks from installed plugins |
| `only managed plugins and built-in plugins run` | `allowManagedHooksOnly` is set, or `disableAllHooks` is set in a settings file other than managed settings |
| `installed plugins that are not managed load no hooks module in this mode (--bare)` | Claude Code started with `--bare` |
| `another plugin of that name loads first` | Another enabled plugin holds the same name, so the hooks module does not load |

# Notes

Some settings stop a mod and leave the rest of its plugin working. If the log has no `not loaded:` line, work through the [load errors](./module-load-errors.md).
