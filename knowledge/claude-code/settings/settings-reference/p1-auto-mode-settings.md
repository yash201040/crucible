---
type: "Reference"
title: "Auto mode settings"
description: "autoMode rules and classifyAllShell, disableAutoMode, useAutoModeDuringPlan, skipAutoPermissionPrompt and skipDangerousModePermissionPrompt."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [auto-mode, permissions, classifier, bypass-permissions]
kind: "setting"
maturity: "unlabelled"
since: "2.1.193"
surfaces: [cli, headless, ide]
requires: "classifyAllShell v2.1.193; useAutoModeDuringPlan left-out-file rule v2.1.314"
identifiers:
  - "autoMode"
  - "autoMode.environment"
  - "autoMode.allow"
  - "autoMode.soft_deny"
  - "autoMode.hard_deny"
  - "autoMode.classifyAllShell"
  - "disableAutoMode"
  - "permissions.disableAutoMode"
  - "useAutoModeDuringPlan"
  - "skipAutoPermissionPrompt"
  - "skipDangerousModePermissionPrompt"
  - "$defaults"
  - "--setting-sources"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that tune the auto mode classifier (which reviews actions instead of prompting) and the prompts around auto and bypass modes.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `autoMode` | User or managed | object with `environment`, `allow`, `soft_deny`, `hard_deny` arrays of prose rules, plus `classifyAllShell` | unset | Add rules to classifier defaults. Include the literal `"$defaults"` in every array to add to built-ins rather than replace them. Arrays concatenate across files |
| `autoMode.classifyAllShell` | User or managed | Boolean | `false` | `true`: while auto mode is active every Bash and PowerShell command goes through the classifier and shell allow rules are suspended (rules still apply outside auto mode). `false`: only arbitrary-code allow rules (`Bash(*)`, `Bash(python *)`) are suspended; other matching allow rules such as `Bash(npm test)` skip the classifier unless they carry per-command allowed domains. Works differently in a Code Mode session |
| `disableAutoMode` | Any file (also `permissions.disableAutoMode`) | the string `"disable"` | unset | Removes auto mode from the `Shift+Tab` cycle; sessions that would start in auto start in `default` |
| `useAutoModeDuringPlan` | User, local or managed | Boolean | `true` | `true`: classifier reviews shell commands in plan mode (except critical-path removals). `false`: permission prompt for every command outside the built-in read-only set. `/config` label **Use auto mode during plan** |
| `skipAutoPermissionPrompt` | User or managed | Boolean | unset | Skips the one-time auto-mode notice shown when you enter auto mode yourself (not via built-in default) |
| `skipDangerousModePermissionPrompt` | User, local or managed, and `--settings` | Boolean | unset | Skips the confirmation before `bypassPermissions` mode; written to user settings when you accept once. Background sessions count only user and managed settings |

```json
{ "autoMode": { "soft_deny": ["$defaults", "Never run terraform apply"] } }
```

# Notes

- For `useAutoModeDuringPlan`, a `false` in any listed file or `--settings` turns it off unless that user or local file is left out with `--setting-sources` (ignoring left-out files needs v2.1.314).
- A repository cannot set `skipAutoPermissionPrompt`, `skipDangerousModePermissionPrompt` (untrusted) or `useAutoModeDuringPlan` for you.
