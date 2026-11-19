---
type: "Reference"
title: "Dialog timeouts and usage-limit auto-continue"
description: "Settings that let unanswered dialogs expire and let a session wait out a claude.ai usage limit and resume by itself."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, timeouts, unattended, usage-limit]
kind: "setting"
maturity: "unlabelled"
since: "2.1.224"
surfaces: [cli]
requires: ""
identifiers:
  - "askUserQuestionTimeout"
  - "autoContinueAtUsageLimit"
  - "dialogExpiry"
  - "CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three user-or-managed scope settings decide what happens when nobody answers a prompt, or when a claude.ai usage limit stops a session.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `askUserQuestionTimeout` | string: `"60s"`, `"5m"`, `"10m"`, `"never"` | `"never"` | An unanswered `AskUserQuestion` dialog auto-continues after this idle time, submitting the options already selected. `/config` row: Question auto-continue timeout |
| `autoContinueAtUsageLimit` | Boolean | `true` | After a claude.ai usage limit stops the session, wait in the open session and continue after the reset. Needs v2.1.234+. `false` means no automatic wait; a wait can still be started from the usage-limit menu |
| `dialogExpiry` | string: `"60s"`, `"5m"`, `"10m"`, `"never"` | `"5m"` | Deadline for dialogs forwarded to a remote client (Remote Control or SDK host) and for the approval dialog of a held cross-session message. From v2.1.236 it also bounds the mid-session Fable usage-credits consent prompt. At expiry the dialog is cancelled and the no-action default applies. Needs v2.1.224+ |

# Limits and defaults

- `autoContinueAtUsageLimit` is read from user settings, `--settings` and managed settings only; if none sets it, a project or local file that sets it turns the feature off.
- `dialogExpiry` is overridden for one session by `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`. It does not govern permission prompts or `AskUserQuestion` questions, which have their own flows. `/config` row Dialog expiry needs v2.1.232+.
- `/config` hides these rows while managed settings or `--settings` set the key.
