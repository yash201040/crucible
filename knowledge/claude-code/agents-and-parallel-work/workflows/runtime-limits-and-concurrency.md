---
type: "Limit"
title: "Workflow runtime limits"
description: "Concurrency, item and total-agent caps, and constraints on scripts (no input, no module loading, no direct fs)."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, limits, concurrency, caps]
kind: "limit"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Constraints the runtime applies.

# How to use it

| Constraint | Detail |
| :- | :- |
| Concurrent agents | 16 by default, fewer when fewer CPUs are available (including a CPU-limited container); set `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` to 1-256 (v2.1.269 or later) |
| Items per `parallel()` / `pipeline()` | Up to 4,096; a longer list is rejected with an error |
| Agents per run | 1,000 total, to prevent runaway loops |
| Fan-out cache stagger | Agents sharing a prefix start up to 5 s after the first by default |
| Mid-run user input | None; a run pauses itself only for agent permission prompts and a usage-limit wait. For sign-off between stages run each stage as its own workflow |
| Filesystem/shell | Not available to the script itself; agents do the work |
| Modules | A script containing `import()` fails before the run starts |

# Notes

Runtime agent caps apply regardless of the size guideline setting.
