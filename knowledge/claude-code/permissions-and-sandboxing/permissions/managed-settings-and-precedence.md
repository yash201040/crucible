---
type: "Concept"
title: "Managed settings and permission precedence"
description: "Managed settings override everything; a deny at any level cannot be allowed elsewhere, and --allowedTools cannot override managed deny."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, managed-settings, precedence, enterprise]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk, desktop]
requires: ""
identifiers:
  - "allowManagedPermissionRulesOnly"
  - "disableBypassPermissionsMode"
  - "--allowedTools"
  - "--disallowedTools"
  - "managedSettings"
  - "allowManaged*Only"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Administrators deploy managed settings that user and project settings cannot override, apart from a few security-sensitive keys. Permission rules follow normal settings precedence with managed highest: no other level, including command-line arguments, overrides a managed permission rule.

# How to use it

- If a tool is denied at any level no other level can allow it: a managed deny cannot be overridden by `--allowedTools`, while `--disallowedTools` can add restrictions beyond managed settings. A user-level deny blocks a project-level allow and vice versa, since deny rules from every scope are evaluated before allow rules.
- `allowManagedPermissionRulesOnly` makes managed settings the only source of permission rules; its settings-reference entry lists every ignored source.
- `disableBypassPermissionsMode` is typically in managed settings but works from any scope (a user can lock themselves out of bypass mode).
- Embedding hosts can supply extra managed policy via the SDK `managedSettings` option, including allow rules, unless the admin sets the `allowManaged*Only` locks.

# Notes

Settings-versus-CLI precedence is separate from whether a deny holds over an installed mod; see [precedence of hooks, rules and mods](./hooks-rules-mods-precedence.md).
