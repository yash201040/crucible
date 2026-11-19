---
type: "Feature"
title: "PowerShell permission rules"
description: "PowerShell rules mirror Bash rules, with alias canonicalization, case-insensitive matching and AST-based compound splitting."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, powershell, windows]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "PowerShell"
  - "PowerShell(*)"
  - "PowerShell(Get-ChildItem *)"
  - "PowerShell(Remove-Item *)"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules have the same shape as Bash rules; bare `PowerShell` or `PowerShell(*)` matches every command. Example: allow `PowerShell(Get-ChildItem *)` and `PowerShell(git commit *)`, deny `PowerShell(Remove-Item *)`.

# How to use it

Common aliases are canonicalized, so a `Get-ChildItem` rule also matches `gci`, `ls`, `dir`. Matching is case-insensitive. Claude Code parses the PowerShell AST and checks each command of a compound independently; `|`, `;` and on PowerShell 7+ `&&` and `||` split it. Every subcommand must be allowed.
