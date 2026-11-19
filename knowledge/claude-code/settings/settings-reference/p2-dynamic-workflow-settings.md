---
type: "Reference"
title: "Dynamic workflow settings"
description: "Settings to turn dynamic workflows on or off, disable the ultracode keyword trigger and set a size guideline for agent count."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, workflows, agents, cost]
kind: "setting"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli]
requires: ""
identifiers:
  - "disableWorkflows"
  - "enableWorkflows"
  - "workflowKeywordTriggerEnabled"
  - "workflowSizeGuideline"
  - "CLAUDE_CODE_DISABLE_WORKFLOWS"
  - "ultracode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four any-file settings that govern dynamic workflows (multi-agent scripts Claude writes).

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `disableWorkflows` | Boolean | `false` | `true` turns off dynamic workflows and bundled workflow commands for everyone the settings reach (use in managed settings for an org). `CLAUDE_CODE_DISABLE_WORKFLOWS` turns them off for one session; whichever turns them off, the other cannot turn them back on |
| `enableWorkflows` | Boolean | unset: on, except off on the Pro plan | Personal on/off. `/config` row Dynamic workflows writes it to user settings and removes it when toggled back to the plan default. Cannot override `disableWorkflows`, `CLAUDE_CODE_DISABLE_WORKFLOWS` or org policy; row hidden if another source sets it or `disableWorkflows` is `true` |
| `workflowKeywordTriggerEnabled` | Boolean | `true` | Whether typing `ultracode` in a prompt triggers a dynamic workflow. The `ultracode` effort setting, `/workflows` and saved workflow commands are unaffected. `/config`: Ultracode keyword trigger |
| `workflowSizeGuideline` | `"unrestricted"`, `"small"`, `"medium"`, `"large"` | `"medium"`; `"small"` on Pro with v2.1.271+ | Advice to Claude, not an enforced cap: small is fewer than 5 agents, medium fewer than 10, large fewer than 50. Beats the `/config` Dynamic workflow size choice (stored in `~/.claude.json`) |

# Notes

Choose `"small"` to bound what a workflow spends.
