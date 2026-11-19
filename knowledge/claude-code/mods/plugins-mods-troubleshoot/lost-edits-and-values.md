---
type: "Reference"
title: "Lost edits and values, settings.read"
description: "Why edits to installed plugins do not apply, why module variables and $.state reset, and how to debug settings.read hook answers."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, settings, state, reload]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "settings.read"
  - "classic.SessionStart"
  - "$.state"
  - "$.store"
  - "$.env.set"
  - "--debug-file"
  - "settings.read hook skipped"
  - "settings.read bypassed by cc-plugin-sec-default"
  - "settings.read: the answer for <key> is no value the key can hold"
  - "settings.read: the merge never settles for <key>"
  - "answered settings.read without next()"
  - "settings.read: refused to the engine"
  - "next.origin"
  - "{ deny: reason }"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cases where the mod runs but a change or kept value is missing.

# How to use it

- **Edits do not take effect**: you edited an installed plugin; Claude Code runs the cached copy. Develop with `claude --plugin-dir ./first-mod`, which reloads on save.
- **Value resets on module reload**: module-level variables reinitialize each reload. Keep values in `$.state` or `$.store`.
- **Value resets after `/clear`, `/resume`, or `/branch`**: each resets `$.state` to defaults and `session.start` does not fire again. Reload the saved value in a `classic.SessionStart` hook.
- **A `settings.read` key does not take effect**: permission rules or `env` returned on Claude Code's own read are not checked on tool calls and `env` entries do not become environment variables. Use a settings file, or `$.env.set` for `env`.

Debug log lines for `settings.read`:

| Log line | Meaning and step |
| :- | :- |
| `settings.read hook skipped` after your mod's name | Your hook failed; fix the error |
| `settings.read bypassed by cc-plugin-sec-default` on a line naming your mod | The built-in guard skipped your hook; ask the administrator to install it as an organization mod |
| `settings.read: the answer for <key> is no value the key can hold` | Value refused for that key alone (type or range); the settings' own value stands. Return a value the settings reference allows, or find the other mod that returned it |
| `settings.read: the merge never settles for <key>` | Keys keep the settings sources' values; set them in a settings file |
| `answered settings.read without next()` after a mod's name | If that mod runs before yours, your hook did not run on that read; turn that mod off or ask the admin |
| `settings.read: refused to the engine (engine: $.settings.read: <reason>); the settings' own values stand` | Claude Code's own read was refused and every hook's value dropped. If your code has the reason, return `{ value }` when `next.origin` shows the engine read; otherwise turn other mods off one at a time, each time starting `claude --debug-file ./settings-read-2.log` (new path each time) with the same flags and searching for `refused to the engine` |

# Notes

If no other mod is left, set the keys in a settings file; its values hold while the read is refused.
