---
type: "Reference"
title: "Check whether mods can load"
description: "Run claude plugin test from a directory with no mod to learn from its message whether settings, policy or a rollout switch block mods."
resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
tags: [mods, troubleshooting, rollout, policy]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "no hooks module to load"
  - "hooks modules are turned off here"
  - "hooks modules are turned off in this process: the rollout switch served off"
  - "hooks modules are turned off in this process: the rollout switch was saved off by an earlier session"
  - "disableAllHooks"
  - "allowManagedModsOnly"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-troubleshoot"
    resource: "https://code.claude.com/docs/en/plugins/mods/troubleshoot"
    title: "Troubleshoot a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Run `claude plugin test` in your shell from a directory that holds no mod; no session is needed. The printed message gives the state.

# How to use it

| Message includes | Meaning |
| :- | :- |
| `no hooks module to load` | Mods can load; no mod to test here |
| `hooks modules are turned off here` | A setting blocks mods: `disableAllHooks` in your own settings, or organization policy |
| `hooks modules are turned off in this process: the rollout switch served off` | Anthropic turned installed mods off remotely |
| `hooks modules are turned off in this process: the rollout switch was saved off by an earlier session` | Uses a value an earlier session saved, possibly stale; start `claude` once to refresh, then rerun |

# Notes

An organization can set `allowManagedModsOnly` to allow only its own mods; this command does not report that. Claude Code then refuses a mod you install and a message says why (see [built-in guard messages](./built-in-guard-messages.md)).
