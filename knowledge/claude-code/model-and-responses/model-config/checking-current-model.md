---
type: "Concept"
title: "Checking your current model"
description: "Where to see the active model: the status line and /status."
resource: "https://code.claude.com/docs/en/model-config#checking-your-current-model"
tags: [model, status, status-line]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/status"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The current model appears in the status line (if configured) and in `/status`, which also shows account information.

# Notes

For subprocess or unattended runs, the non-interactive result message carries the actual model in `modelUsage` (see [setting your model](./setting-your-model.md)).
