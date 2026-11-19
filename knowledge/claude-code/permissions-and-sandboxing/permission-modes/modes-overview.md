---
type: "Reference"
title: "Permission modes overview"
description: "The six permission modes, what each runs without asking, the Manual/default naming, and how rules layer on top."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, modes, default, auto, bypass]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "default"
  - "manual"
  - "acceptEdits"
  - "plan"
  - "auto"
  - "dontAsk"
  - "bypassPermissions"
  - "--permission-mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A permission mode sets which actions Claude can take in a session without asking first. In Manual mode Claude Code stops before most file edits, shell commands and network access. In auto mode a second model, the classifier, reviews actions instead of the user. A running session's mode can be changed at any time.

# How to use it

| Mode | Runs without asking | Best for |
| :- | :- | :- |
| `default` (Manual) | Reads only | Reviewing every action, sensitive work |
| `acceptEdits` | Reads, file edits, common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) | Iterating on code you review |
| `plan` | Reads, plus classifier-approved commands when auto mode is available | Exploring before changing |
| `auto` | Everything, with background safety checks | Long tasks, fewer prompts |
| `dontAsk` | Reads inside working directories and pre-approved tools; anything that would prompt is denied (an installed mod can still approve some) | Locked-down CI and scripts |
| `bypassPermissions` | Everything | Isolated containers and VMs only |

The mode that reviews every action is shown as **Manual** in the CLI, `claude --help`, VS Code, JetBrains and desktop; its config value is `default`, which hooks and SDK integrations use. The CLI accepts the alias `manual` wherever the value is typed: `claude --permission-mode manual`, `"defaultMode": "manual"`.

# Limits and defaults

- Deny rules block in every mode, including `bypassPermissions`. Allow rules have no effect in `bypassPermissions`.
- Deny and ask rules do not apply to the `EndConversation` tool while Claude still has at least one other tool.
- Each mode has its own rule for writes to [protected paths](./protected-paths.md).
- Layer permission rules on top of a mode to pre-approve or block specific tools.
