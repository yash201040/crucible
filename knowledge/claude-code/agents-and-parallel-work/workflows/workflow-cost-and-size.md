---
type: "Feature"
title: "Workflow cost, warnings and size guideline"
description: "Large workflow warning thresholds, model choice per agent and the workflowSizeGuideline setting."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, cost, tokens, size, model]
kind: "setting"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "workflowSizeGuideline"
  - "/config workflowSizeGuideline=small"
  - "Large workflow"
  - "unrestricted"
  - "small"
  - "medium"
  - "large"
  - "availableModels"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A run can use far more tokens than the same task in conversation and counts toward plan usage and rate limits. Gauge by running on a small slice first. `/workflows` shows per-agent token usage; stopping usually keeps completed work. Runtime agent caps bound a runaway script.

# How to use it

`Large workflow` warning: shown in the task panel progress line when a run schedules more than 25 agents or its projected token total passes 1.5 million. Advisory only; it does not pause or limit. A chosen size guideline's agent count replaces the 25 threshold (the built-in default leaves it at 25). Not shown with ultracode on.

Size guideline (advice to Claude when writing a workflow, not a cap):

| Value | Agent count aimed for |
| :- | :- |
| `unrestricted` | No guideline |
| `small` | Fewer than 5 |
| `medium` | Fewer than 10 |
| `large` | Fewer than 50 |

Default `medium`, or `small` on a Pro plan with v2.1.271 or later. Change via the Dynamic workflow size setting in `/config`, `/config workflowSizeGuideline=small`, or the `workflowSizeGuideline` key in any settings file (which wins and hides the `/config` row). Takes effect on the next prompt.

# Limits and defaults

Each agent's model follows the subagent model order; a model the script names for a stage counts as the per-invocation model; otherwise the session model. Blocked by `availableModels`: substituted per the subagent allowlist rules. To control cost check `/model` before a large run or ask Claude to use a smaller model for easy stages.
