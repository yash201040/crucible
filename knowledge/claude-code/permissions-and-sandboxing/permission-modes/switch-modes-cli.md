---
type: "Feature"
title: "Switch modes in the CLI"
description: "Shift+Tab cycle order, status bar labels, which modes join the cycle, and the Bash-prompt switch to auto."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, shift-tab, cli, cycle, status-bar]
kind: "ui"
maturity: "unlabelled"
since: "2.1.247"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "Shift+Tab"
  - "--permission-mode"
  - "--allow-dangerously-skip-permissions"
  - "--dangerously-skip-permissions"
  - "/plan"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Shift+Tab` cycles modes during a CLI session (also the JetBrains plugin, which runs Claude Code in the IDE terminal; there `--permission-mode` also works at launch).

# How to use it

- From `auto`, first press goes to `default`, then `default` -> `acceptEdits` -> `plan`. Optional modes slot in after `plan`, `bypassPermissions` first and `auto` last.
- Status bar: gray `⏸ manual mode on`, `⏵⏵ accept edits on`, `⏸ plan mode on`, `⏵⏵ auto mode on`, `⏵⏵ don't ask on`, `⏵⏵ bypass permissions on`.
- `auto` joins the cycle when auto mode is available; cycling to it needs no confirmation.
- `bypassPermissions` joins after starting with `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`, `--allow-dangerously-skip-permissions`, or `permissions.defaultMode: "bypassPermissions"` in user, `--settings` or managed settings. The `--allow-` variant adds it to the cycle without activating it.
- `dontAsk` never appears in the cycle; use `--permission-mode dontAsk`.
- In Manual and `acceptEdits`, when auto is available, a Bash permission prompt adds **Yes, and switch to auto mode** (needs v2.1.247+). Not offered on PowerShell prompts, nor on prompts forced by an `ask` rule or a hook.
- `--permission-mode` also works with `-p`.
