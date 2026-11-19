---
type: "Reference"
title: "Removed global config keys"
description: "Two ~/.claude.json keys that no longer do anything: permissionExplainerEnabled (removed v2.1.257) and teammateDefaultModel (removed v2.1.234)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [global-config, removed, agent-teams, permissions]
kind: "setting"
maturity: "deprecated"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "permissionExplainerEnabled"
  - "teammateDefaultModel"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two global config keys the docs list as removed. Setting them has no effect on current versions.

# How to use it

| Name | Removed in | Earlier behavior |
| - | - | - |
| `permissionExplainerEnabled` | v2.1.257 (together with the `Ctrl+E` command explanation on Bash and PowerShell permission prompts) | Boolean, default `true`. Through v2.1.256, `Ctrl+E` on a Bash or PowerShell permission prompt showed a model-generated explanation of the command; `false` turned the shortcut off. |
| `teammateDefaultModel` | v2.1.234 (with its `/config` row Default teammate model) | String (alias or full model ID) or `null`, default unset. Through v2.1.233 it set the model for agent team teammates the prompt did not name a model for; `null` followed the lead's model. |

# Notes

For the model Claude Code now picks for unnamed teammates, the docs point to "specify teammates and models" on the agent-teams page.
