---
type: "Reference"
title: "Desktop permission modes and auto mode"
description: "The five Desktop permission modes with their settings keys, defaults, cloud limits and auto mode availability."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, permissions, auto-mode, bypass]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Auto mode: Anthropic API and Opus 4.6+, Sonnet 4.6+, Haiku 5.5 or a Fable model"
identifiers:
  - "permissions.defaultMode"
  - "default"
  - "acceptEdits"
  - "plan"
  - "auto"
  - "bypassPermissions"
  - "dontAsk"
  - "disableAutoMode"
  - "permissions.disableBypassPermissionsMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The mode selector under the prompt box sets how much autonomy Claude has. It can change during a session. Earlier names: Ask permissions, Auto accept edits, Plan mode.

# How to use it

| Mode | Settings key | Behavior |
| - | - | - |
| Manual | `default` | Asks before editing files or running commands; diff to accept or reject |
| Accept edits | `acceptEdits` | Auto-accepts file edits and common filesystem commands (`mkdir`, `touch`, `mv`); asks for other commands |
| Plan | `plan` | Explores and proposes a plan without editing source |
| Auto | `auto` | No routine prompts; a background classifier checks shell commands and network requests align with the request; no separate Settings toggle |
| Bypass permissions | `bypassPermissions` | No prompts except actions no mode auto-approves, external-site safety classifiers and desktop actions such as deleting a session; equals `--dangerously-skip-permissions` |

Default for new local sessions: `permissions.defaultMode` in settings. A mode picked in a local session is remembered per folder and outranks a project `.claude/` `defaultMode`; a `defaultMode` from `~/.claude/settings.json` or managed settings can still apply to a new session. Plan applies to the current session only.

# Limits and defaults

- `dontAsk` is CLI only.
- Cloud sessions (also self-hosted environments) offer Accept edits (maps to `default`), Plan and Auto; no Bypass permissions.
- Bypass: on Pro, Max and Ultra enable "Allow bypass permissions mode" in Settings > Code; on Team and Enterprise there is no toggle and organization policy decides. Use only in sandboxed containers or VMs.
- Auto mode is available to all users on the Anthropic API and needs Claude Opus 4.6 or later, Sonnet 4.6 or later, Haiku 5.5, or a Fable model. Admins turn it off with `disableAutoMode`. Enterprise Desktop routed to Google Cloud's Agent Platform also gets it by default.
- Managed `permissions.disableBypassPermissionsMode: "disable"` and `disableAutoMode: "disable"` also work in user and project settings; in an SSH session the local managed setting removes the mode regardless of the remote host.
