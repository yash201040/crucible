---
type: "Limit"
title: "Permission modes under HIPAA configuration"
description: "How the HIPAA configuration changes the starting mode by version and which managed settings disable auto and bypass."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [hipaa, managed-settings, permissions, auto]
kind: "setting"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, ide]
requires: "HIPAA configuration applied by the organization"
identifiers:
  - "permissions.disableAutoMode"
  - "permissions.disableBypassPermissionsMode"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With the HIPAA configuration applied, terminal and VS Code sessions on v2.1.326 or later start in auto mode by default. On v2.1.285 through v2.1.325 an eligible session starts in Manual.

# How to use it

- Keep Manual: set a different `permissions.defaultMode` (see [starting mode](./start-in-different-mode.md)).
- Remove auto mode: `permissions.disableAutoMode` = `"disable"` in managed settings.
- Block bypass: `permissions.disableBypassPermissionsMode` = `"disable"` in managed settings.
