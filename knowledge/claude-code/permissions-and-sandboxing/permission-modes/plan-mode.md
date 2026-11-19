---
type: "Feature"
title: "Plan mode"
description: "Research-and-propose mode that blocks edits until a plan is approved; shell commands go to the classifier or prompt."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [plan-mode, permissions, classifier, planning]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, ide]
requires: ""
identifiers:
  - "plan"
  - "/plan"
  - "--permission-mode plan"
  - "useAutoModeDuringPlan"
  - "Ctrl+G"
  - "showClearContextOnPlanAccept"
  - "plansDirectory"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude reads files, runs shell commands to explore and writes a plan but does not edit source. Edits stay blocked until the plan is approved, except in interactive terminal sessions where bypass permissions is available (see [bypassPermissions](./bypass-permissions-mode.md)).

Shell commands during planning, first matching case:
1. Interactive terminal with bypass available: neither classifier nor prompt applies.
2. Auto mode available and `useAutoModeDuringPlan` on (the default): the classifier reviews shell commands other than critical-path removals; approved run, rejected are blocked.
3. Auto unavailable or `useAutoModeDuringPlan` off: commands outside the built-in read-only set prompt, even with sandbox auto-allow on.

# How to use it

Enter with `Shift+Tab`, prefix one prompt with `/plan`, or `claude --permission-mode plan`. To leave with no approval prompt open press `Shift+Tab` again; at the approval prompt press `Esc` first because `Shift+Tab` there approves the plan. Make it a project default with `defaultMode: "plan"` in `.claude/settings.json` (VS Code: set `claudeCode.initialPermissionMode` to `plan`).

# Notes

Plan mode keeps its blocks in `-p`, Agent SDK and the VS Code chat panel. Protected-path writes in plan mode follow the [protected paths table](./protected-paths.md). Approval flow: [plan approval](./plan-approval.md).
