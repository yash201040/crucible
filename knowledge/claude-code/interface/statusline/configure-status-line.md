---
type: "Feature"
title: "Configure a custom status line"
description: "The statusLine setting runs a shell command that receives session JSON on stdin and shows its output in a bar at the bottom of Claude Code."
resource: "https://code.claude.com/docs/en/statusline"
tags: [statusline, settings, interface, scripts]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "statusLine"
  - "statusLine.type"
  - "statusLine.command"
  - "statusLine.padding"
  - "statusLine.refreshInterval"
  - "statusLine.hideVimModeIndicator"
  - "/statusline"
  - "footerLinksRegexes"
  - "disableAllHooks"
  - "allowManagedHooksOnly"
  - "~/.claude/statusline.sh"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "statusline"
    resource: "https://code.claude.com/docs/en/statusline"
    title: "Customize your status line"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The status line is a bar at the bottom of Claude Code that runs any shell script you configure. The script gets JSON session data on stdin and whatever it prints to stdout is shown. It renders in its own row above the built-in footer badges. It runs locally and uses no API tokens. It hides temporarily during some UI interactions, such as the help menu and permission prompts.

With a custom status line set, Claude Code stops showing some footer hints such as `? for shortcuts` and the `hold space to speak` voice hint. For clickable footer link badges without a script, use `footerLinksRegexes` instead.

# How to use it

Run `/statusline <natural language>` to have Claude write a script into `~/.claude/` and update settings. To remove it, run `/statusline delete` (or clear/remove) or delete the `statusLine` field.

Manual setup in `~/.claude/settings.json` or project settings:

```json
{ "statusLine": { "type": "command", "command": "~/.claude/statusline.sh", "padding": 2 } }
```

| Field | Default | What it does |
| - | - | - |
| `type` | none | Set to `"command"` |
| `command` | none | Script path or inline shell command |
| `padding` | `0` | Extra horizontal spacing in characters |
| `refreshInterval` | unset | Re-run every N seconds, minimum `1`; for clocks, or when background subagents change git state while the main session is idle |
| `hideVimModeIndicator` | false | `true` hides the built-in `-- INSERT --` text when your script renders `vim.mode` |

Output can be several lines (each print is a row), ANSI colors, and OSC 8 links (iTerm2, Kitty, WezTerm; Terminal.app does not support them; set `FORCE_HYPERLINK=1` to override detection). Claude Code captures output, so `tput cols` does not work: read the `COLUMNS` and `LINES` environment variables, which Claude Code sets before running the script.

# Limits and defaults

The script runs once at session start (including resume), then on: a new assistant message, `/compact` finishing, permission mode change, vim mode toggle, a change to `command`, a `refreshInterval` tick, a rate-limit window reaching its `resets_at`, or a warm prompt cache reaching its `expires_at`. Updates are debounced at 300ms; a change to `command` skips the debounce. A new trigger cancels a still-running script.

Output is shown only after the script exits with code 0. A non-zero exit or empty output blanks the status line.

# Notes

- The status line stays blank until the workspace trust dialog is accepted (same rule as hooks in settings files); `claude --debug` logs `Status line command skipped: workspace trust not accepted`.
- If `disableAllHooks` is true outside managed settings, only a managed `statusLine` runs; with none, the status line is disabled. If `allowManagedHooksOnly` is set in managed settings, only a managed `statusLine` works.
- `claude --debug` logs the script's stderr on each run and its exit code on the first run of a session.
- On Windows, Claude Code uses Git Bash if installed, else PowerShell; use forward slashes in the `command` path. To run a PowerShell script use `powershell -NoProfile -File C:/Users/username/.claude/statusline.ps1`.
- Notifications share the status line row outside fullscreen rendering; verbose mode adds a token counter there.
- Cache slow work (git) keyed on `session_id`, not process ID; the page's example refreshes every 5 seconds.
