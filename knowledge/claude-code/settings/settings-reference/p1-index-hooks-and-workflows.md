---
type: "Reference"
title: "Index: hooks and workflow keys"
description: "Settings keys for hooks, HTTP hook limits, disabling hooks, and dynamic workflows (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [hooks, workflows, automation, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "hooks"
  - "allowedHttpHookUrls"
  - "allowManagedHooksOnly"
  - "disableAllHooks"
  - "httpHookAllowedEnvVars"
  - "disableWorkflows"
  - "enableWorkflows"
  - "workflowKeywordTriggerEnabled"
  - "workflowSizeGuideline"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from the "Hooks and automation" topic. Detailed sections are in other parts of the page.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `hooks` | Any file | Run your own commands as hooks at points in the lifecycle |
| `allowedHttpHookUrls` | Any file | Limit which URLs HTTP hooks can target |
| `allowManagedHooksOnly` | Managed | Run only the hooks the organization deploys |
| `disableAllHooks` | Any file | Turn off hooks, a custom status line and a custom `@` file suggestion command at once |
| `httpHookAllowedEnvVars` | Any file | Limit which env vars HTTP hooks can put in headers |
| `disableWorkflows` | Any file | Turn dynamic workflows off for everyone (use `enableWorkflows` for yourself) |
| `enableWorkflows` | Any file | Turn dynamic workflows on or off against the plan's default |
| `workflowKeywordTriggerEnabled` | Any file | Let the word `ultracode` in a prompt start a workflow; `false` types it without starting one |
| `workflowSizeGuideline` | Any file | Agent count Claude aims for in dynamic workflows |
