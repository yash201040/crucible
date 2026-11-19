---
type: "Concept"
title: "Dynamic workflows overview"
description: "A dynamic workflow is a JavaScript script Claude writes that a runtime executes in the background to orchestrate many subagents."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, orchestration, subagents, scripts]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, headless, sdk]
requires: "paid plan, Anthropic API access, Bedrock, Google Cloud Agent Platform or Microsoft Foundry; on Pro enable Dynamic workflows in /config"
identifiers:
  - "/workflows"
  - "Workflow"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude writes a JavaScript script for the task; a runtime executes it in the background while the session stays responsive. The script holds the loop, branching and intermediate results in script variables, so Claude's context holds only the final answer. Use it when a task needs more agents than one conversation can coordinate, or when you want the orchestration codified and rerunnable (bug sweeps, 500-file migrations, cross-checked research, plans drafted from several angles). A workflow can apply quality patterns such as adversarial review among agents.

# How to use it

Who holds the plan, by mechanism:

| | Subagents | Skills | Agent teams | Workflows |
| :- | :- | :- | :- | :- |
| Decides what runs next | Claude, turn by turn | Claude, following prompt | Lead agent, turn by turn | The script |
| Intermediate results live in | Claude's context | Claude's context | Shared task list | Script variables |
| Repeatable | Worker definition | Instructions | Team definition | The orchestration |
| Scale | A few tasks per turn | Same | A handful of long-running peers | Dozens to hundreds of agents per run |
| Interruption | Restarts the turn | Restarts the turn | Teammates keep running | Resumable in the same session |

# Limits and defaults

Available on all paid plans, with Anthropic API access, and on Amazon Bedrock, Google Cloud's Agent Platform and Microsoft Foundry. See [limits](./runtime-limits-and-concurrency.md).
