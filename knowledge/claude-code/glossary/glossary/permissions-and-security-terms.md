---
type: "Reference"
title: "Glossary: permissions and security"
description: "Definitions of permission mode, permission rule, auto mode, plan mode, sandboxing, project trust, managed settings and prompt injection."
resource: "https://code.claude.com/docs/en/glossary"
tags: [glossary, permissions, auto-mode, sandbox, security]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, ide, desktop, web]
requires: ""
identifiers:
  - "default"
  - "acceptEdits"
  - "plan"
  - "auto"
  - "dontAsk"
  - "bypassPermissions"
  - "manual"
  - "/plan"
  - "Shift+Tab"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "glossary"
    resource: "https://code.claude.com/docs/en/glossary"
    title: "Glossary"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Glossary terms about approval behavior and isolation.

# How to use it

| Term | Definition |
| :- | :- |
| Permission mode | Baseline approval behavior. Cycle with `Shift+Tab` in the CLI or the mode selector in VS Code, Desktop, claude.ai. Modes: `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. `default` is labeled Manual in the CLI, VS Code and JetBrains extensions and the desktop app; `manual` is accepted as an alias. |
| Permission rule | A settings entry that allows, asks or denies a tool call by tool name and argument pattern; evaluated deny, ask, allow with first match winning; layered on top of the mode. |
| Auto mode | A permission mode where a separate classifier reviews actions instead of you; explicit ask rules still prompt. The classifier blocks scope escalation, untrusted infrastructure and prompt injection. From v2.1.283 it is the built-in starting mode for interactive terminal and VS Code sessions; earlier versions only on Pro, Max, Ultra and Team plans. |
| Plan mode | A permission mode where Claude researches and proposes without editing source files, then presents a plan for approval. Enter with `/plan` or `Shift+Tab`. |
| Sandboxing | OS-level filesystem and network isolation for the Bash tool, separate from permission rules. |
| Project trust | A dialog accepting a directory before configuration loads. Saved per project directory, except the home directory (session only, prompt each launch). Until trusted, some repo-supplied content (project allow rules, marketplaces in `.claude/settings.json`) is held back; see the permissions page for what a `-p` session runs without a dialog. |
| Prompt injection | Hostile instructions in files, pages or tool results. Defenses: permission system, command injection detection, trust verification; in auto mode a server-side probe scans tool results and a classifier reviews actions. |
| Managed settings | Org-wide settings from the admin console or an OS-level path outside `~/.claude`; user and project settings cannot override them. |
| Settings layers | Precedence high to low: managed policy, `--settings` flag, `.claude/settings.local.json`, `.claude/settings.json`, `~/.claude/settings.json`. Most lists such as `permissions.allow` merge across files. |
