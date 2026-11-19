---
type: "Reference"
title: "Remote Control, deep link and cloud environment settings"
description: "Settings for Remote Control auto-connect and disabling, deep-link registration and the default cloud environment."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, remote-control, cloud, deep-links]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "disableRemoteControl"
  - "remoteControlAtStartup"
  - "remote.defaultEnvironmentId"
  - "disableDeepLinkRegistration"
  - "--remote-control"
  - "--environment"
  - "claude remote-control"
  - "claude --cloud"
  - "/remote-env"
  - "claude-cli://"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any-file keys for Remote Control, cloud sessions and deep links.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `disableRemoteControl` | Boolean | `false` | `true` makes Claude Code refuse `claude remote-control`, `--remote-control`, auto-start and the in-session toggle; use managed settings for MDM enforcement |
| `remoteControlAtStartup` | Boolean | unset (default auto-connect applies) | Connect Remote Control at start of each interactive session. `--remote-control` turns it on for one session even if `false`; no flag turns it off. A `true` in project or local settings is ignored (repo can turn it off, not on). `/config`: Enable Remote Control for all sessions; reads old `~/.claude.json` value |
| `remote.defaultEnvironmentId` | string `env_...` or `ccpool_...` | unset: Anthropic-hosted environment if in list, else the first non-bridge environment, else first | Default cloud environment for sessions created from the CLI such as `claude --cloud`; `/remote-env` writes it. `--environment` overrides for that one session. A self-hosted `ccpool_` ID is honored only from user settings, managed settings and `--settings`; project or local ones are ignored |
| `disableDeepLinkRegistration` | the string `"disable"` | unset | Stop registering the `claude-cli://` protocol handler with the OS |

# Notes

Deep links let external tools open a Claude Code session with a pre-filled prompt.
