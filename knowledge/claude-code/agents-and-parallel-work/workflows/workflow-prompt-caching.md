---
type: "Feature"
title: "Prompt caching in a workflow fan-out"
description: "Agents with matching config share a cache prefix; a stagger hold and 5-minute default TTL apply."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, prompt-cache, cost, fan-out]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "subagentPromptCacheTtl"
  - "CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agents in one run can read each other's prompt cache. Two agents with the same model, effort level, agent type, tools, output schema and working directory build the same tools-and-system-prompt prefix, so an agent starting after a matching sibling's response has begun reads that sibling's cache on its first request.

# How to use it

| Name | Default | Effect |
| :- | :- | :- |
| `subagentPromptCacheTtl` (setting) | 5 minutes | Set `1h` to keep workflow agents' cache an hour (API bills 1-hour cache writes higher) |
| `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS` | `5000` | Cap in ms on holding matching agents until the first one's response begins; `0` disables the hold |

# Limits and defaults

Workflow agent requests fall outside the main conversation's cache TTL bucket, so the default holds five minutes even on a Claude subscription. When a fan-out starts several matching agents at once, all but the first are held, then released together.
