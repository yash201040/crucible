---
type: "Feature"
title: "Managed CLAUDE.md and claudeMdExcludes"
description: "Organization-wide CLAUDE.md via file or the claudeMd setting, and skipping unwanted CLAUDE.md files with claudeMdExcludes."
resource: "https://code.claude.com/docs/en/memory"
tags: [managed, policy, claudemdexcludes, monorepo]
kind: "setting"
maturity: "unlabelled"
since: "2.1.239"
surfaces: []
requires: ""
identifiers:
  - "claudeMd"
  - "claudeMdExcludes"
  - "permissions.deny"
  - "sandbox.enabled"
  - "env"
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Organizations can deploy a managed CLAUDE.md to all users on a machine (deploy via MDM, Group Policy, Ansible; paths in [locations](./claude-md-locations.md)). It loads before user and project CLAUDE.md and cannot be excluded with `claudeMdExcludes`. If a session starts with CLAUDE.md loading turned off altogether, it does not load the managed content either.

# How to use it

`claudeMd` puts the managed content directly in `managed-settings.json`, e.g. `{"claudeMd": "Always run `make lint` before committing.\nNever push directly to main."}`. It is honored only in managed and policy settings; in user, project or local settings it has no effect.

`claudeMdExcludes` is an array of glob patterns matched against absolute paths, e.g. `["**/monorepo/CLAUDE.md", "/home/user/monorepo/other-team/.claude/rules/**"]`. Configure at any settings layer (user, project, local, managed); arrays merge across layers. Put it in `.claude/settings.local.json` to keep it local.

| Concern | Configure in |
| :- | :- |
| Block tools, commands, paths | `permissions.deny` (managed settings) |
| Enforce sandbox | `sandbox.enabled` |
| Env vars, API provider routing | `env` |
| Login method, org restrictions | `forceLoginMethod`, `forceLoginOrgUUID` |
| Code style, compliance reminders, behavioral guidance | Managed CLAUDE.md |

Settings are enforced by the client; CLAUDE.md is guidance, not enforcement.

# Notes

For an excluded rules file reached via symlink, a pattern matching either the `.claude/rules/` path or the link target excludes it. Before v2.1.239 only the link target matched.
