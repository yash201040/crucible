---
type: "Feature"
title: "Review and approve a plan"
description: "The approval prompt options in plan mode and what mode each one switches the session to."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [plan-mode, approval, permissions, editor]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+G"
  - "showClearContextOnPlanAccept"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a plan is ready Claude presents it. Approving exits plan mode and switches to the mode the chosen option describes.

# How to use it

- **Yes, and use auto mode**: approve and start in auto. If auto is unavailable, it reads **Yes, auto-accept edits**; if the session started with bypass enabled, it reads **Yes, and switch to BYPASS PERMISSIONS (no further prompts) for this session**.
- **Yes, manually approve edits**: review each edit.
- **No, keep planning**: stay in plan mode.
- With `showClearContextOnPlanAccept` enabled, a first option approves and clears the planning context.
- `Ctrl+G` opens the plan in the default editor.
- Accepting gives the session a generated title from the plan unless already named. To plan again, `Shift+Tab` or `/plan`.
