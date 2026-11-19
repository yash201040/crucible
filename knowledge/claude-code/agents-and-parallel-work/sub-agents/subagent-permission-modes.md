---
type: "Feature"
title: "Subagent permission modes"
description: "How the permissionMode field interacts with the main conversation's mode, including auto, plan, dontAsk and bypassPermissions."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, permissions, auto-mode, unattended]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.267"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "permissionMode"
  - "default"
  - "acceptEdits"
  - "auto"
  - "dontAsk"
  - "bypassPermissions"
  - "plan"
  - "manual"
  - "disableAutoMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`permissionMode` sets the mode a subagent runs in; unset means inheriting the main conversation's mode. The main conversation's mode decides whether the value is used.

# How to use it

| Mode | Behavior |
| :- | :- |
| `default` (alias `manual`) | Prompts for permission |
| `acceptEdits` | Auto-accepts file edits and common filesystem commands in the working directory or `additionalDirectories` |
| `auto` | Background classifier reviews commands and protected-directory writes |
| `dontAsk` | Auto-denies calls that would prompt; explicitly allowed tools still work; `AskUserQuestion`, MCP tools marked `requiresUserInteraction`, network-path reads and org-`ask` connector tools are denied even if allowed (a mod can still approve some calls) |
| `bypassPermissions` | Skips prompts; a subagent runs in it only when the main conversation does |
| `plan` | Read-only exploration |

# Limits and defaults

- Main conversation in `bypassPermissions`, `acceptEdits` or auto mode: the subagent runs in that same mode and the field is ignored. Under auto mode the classifier evaluates the subagent's tool calls with the main conversation's rules and reviews its work and final report before delivery.
- Main conversation in `plan`: subagent stays in plan mode (unless an agent team teammate); with `dontAsk` it denies rather than prompts.
- Main conversation in `default` or `dontAsk`: the field is used, except when it is `bypassPermissions` (v2.1.267 or later), or `auto` where auto mode is unavailable (e.g. `disableAutoMode` setting or unsupported model).
