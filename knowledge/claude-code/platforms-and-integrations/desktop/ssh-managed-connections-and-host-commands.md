---
type: "Reference"
title: "SSH host commands, sshConfigs and allowlist"
description: "Settings that create or distribute SSH connections: sshHostCommands, sshConfigs, sshHostAllowlist and related controls."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, ssh, managed-settings, host-commands, allowlist]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "sshHostCommands: Desktop v3.6556.0+ (macOS/Linux) or v4.16336.0+ (Windows), Claude account"
identifiers:
  - "sshHostCommands"
  - "sshConfigs"
  - "sshHostAllowlist"
  - "disableDesktopLocalSessions"
  - "disableSshSavedPasswords"
  - "strictPluginOnlyCustomization"
  - "allowManagedHooksOnly"
  - "disableAllHooks"
  - "startDirectory"
  - "sshIdentityFile"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`sshHostCommands` lets Desktop run your own command to create a machine on demand (for example a dev-box tool); the host the command prints is saved as an SSH connection. `sshConfigs` pre-defines connections; `sshHostAllowlist` restricts hosts.

# How to use it

| Setting | Fields / behavior |
| - | - |
| `sshHostCommands` (array) | `id` (up to 64 ASCII chars, unique), `name` (up to 200), `command` (required); optional `sshIdentityFile`, `startDirectory`. User file `~/.claude/settings.json`; managed copy only in the managed settings file or MDM, ignored in server-managed settings |
| `sshConfigs` (array) | `id`, `name`, `sshHost` required; `sshPort`, `sshIdentityFile` optional; users may add their own; managed entries editable only for Worktree folder |
| `sshHostAllowlist` (array) | Case-insensitive patterns on resolved hostname (`*`, `*.example.com`); empty array disables SSH; managed only; jump hosts must match; Desktop only, not CLI or Bash `ssh` |
| `disableDesktopLocalSessions` | `true` turns off on-device Code sessions (v1.37937.0+) |
| `disableSshSavedPasswords` | `true` stops saved SSH passwords (v1.49585.0+) |

Command rules: on macOS/Linux started directly with no shell, no terminal, no input; bare name found on login-shell `PATH`; allowed characters `+,-./:=@_~` and spaces outside quotes; quotes need v4.16336.0+; 10 minute time limit. On Windows use the full path of an `.exe`, `.cmd` or `.bat`. Must exit 0 and print only `host`, `user@host`, or JSON `{"sshHost": ..., "sshPort": ..., "startDirectory": ...}`.

# Limits and defaults

Desktop never stops or deletes machines the command makes; archive sessions to stop auto-reconnects. After several runs within an hour each further run asks confirmation; **Create another** is gray for one minute after saving a host. Users' own entries behave like hooks: `strictPluginOnlyCustomization: ["hooks"]`, `allowManagedHooksOnly` or `disableAllHooks` gray them out. Server-managed `sshHostAllowlist` must also be kept on each machine because Desktop caches nothing; it reads only the highest-ranked managed source that delivers a policy key.
