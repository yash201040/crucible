---
type: "Reference"
title: "Switch modes in VS Code, Desktop, web"
description: "Mode selectors, labels and start-mode rules for VS Code, the desktop app, cloud sessions and Remote Control."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [vscode, desktop, web, remote-control, permissions]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [ide, desktop, web, mobile, cloud]
requires: ""
identifiers:
  - "claudeCode.initialPermissionMode"
  - "claudeCode.claudeProcessWrapper"
  - "claude remote-control --permission-mode"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each surface has its own switcher and its own way of choosing the starting mode.

# How to use it

VS Code labels: Manual = `default`, Edit automatically = `acceptEdits`, Plan = `plan`, Auto = `auto`, Bypass permissions = `bypassPermissions`. Set `claudeCode.initialPermissionMode` (user settings) to `default`, `manual`, `acceptEdits`, `plan` or `bypassPermissions` (not `auto`). New conversation start order: 1) that setting; 2) last mode picked in the indicator if Manual, Edit automatically or Auto (Plan or Bypass apply to that conversation only); 3) `permissions.defaultMode` from managed settings or `~/.claude/settings.json`; 4) the built-in default. The extension never reads project `.claude/settings.json` or `.claude/settings.local.json` for this. With `claudeCode.claudeProcessWrapper` set, items 3 and 4 do not apply (starts Manual). Bypass needs the **Allow dangerously skip permissions** toggle; without it a `bypassPermissions` value starts Manual. Before v2.1.283 item 3 applied only on Pro, Max, Ultra, Team with feature flags fetched.

Desktop: mode selector in the Code tab. Auto appears when available; Bypass needs **Allow bypass permissions mode** on Pro, Max, Ultra (Team/Enterprise: organization policy). Cowork has its own separate modes. Desktop reads the same settings files as the CLI. A mode picked in a local session is remembered per folder and outranks project `defaultMode`; Plan applies to that session only.

Web and mobile: dropdown on claude.ai/code; mobile: **+** then **Permission**.
- Cloud sessions: Accept edits, Plan, Auto. Accept edits corresponds to `default` (edits are pre-approved regardless); `defaultMode: "acceptEdits"` is honored; Bypass is not available; Auto is grayed out for unsupported models.
- Remote Control sessions: Manual, Accept edits, Plan, Auto; no Bypass from the app. Needs a claude.ai sign-in on the local machine (API keys unsupported). Launch: `claude remote-control --permission-mode acceptEdits`.
