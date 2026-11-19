---
type: "Feature"
title: "Load settings files into a session"
description: "settingSources picks which filesystem settings load; settings passes a file path, inline JSON or object that outranks all but managed policy."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [settings, setting-sources, precedence, isolation]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "settingSources"
  - "setting_sources"
  - "settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings files supply configuration beyond the options object. Two options control loading.

# How to use it

| Option | What it does |
| - | - |
| `settingSources` / `setting_sources` | Which filesystem sources load: user, project, local. Settings files and CLAUDE.md arrive through these |
| `settings` | A settings file path or inline JSON string (both languages); TypeScript also accepts a settings object |

Whichever form of `settings` you pass overrides user, project and local filesystem settings; only managed policy settings rank higher. Pass `[]` to `settingSources` to disable user, project and local settings. Precedence is documented in the TypeScript and Python references under Settings precedence.
