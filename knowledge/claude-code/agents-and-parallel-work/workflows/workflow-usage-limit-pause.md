---
type: "Feature"
title: "Workflow pause at a usage limit"
description: "When an agent hits a claude.ai usage limit the run waits for reset and continues, under conditions listed."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, usage-limits, pause, unattended]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, desktop]
requires: "claude.ai subscription without usage-based billing"
identifiers:
  - "autoContinueAtUsageLimit"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On hitting a claude.ai usage limit the run pauses instead of failing the agent: affected agents wait for the reset, no new agents start, and shortly after the reset they run again. Requires v2.1.271 or later (v2.1.319 or later in the Desktop Code tab). Earlier versions fail the agents. The task panel and `/workflows` header show the reset time; the Code tab shows e.g. `Paused at usage limit · continues after 3:45 PM if the app stays open`.

# How to use it

It pauses only when all hold; otherwise the agent fails:
- Signed in with a claude.ai subscription without usage-based billing, in an interactive terminal session or a local Code tab session. No pause in `claude -p`, the Agent SDK, a background session, Remote Control or agent team teammate sessions; none in SSH, WSL, Dispatch, scheduled task, Remote Control-started or corporate-launcher Code tab sessions, nor when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set.
- `autoContinueAtUsageLimit` is on (turning it off during a wait ends the wait and fails waiting agents).
- In the Code tab, the "Auto-continue when limits reset" checkbox on the session-limit card is checked (default); unchecking stops pausing unless managed settings set `autoContinueAtUsageLimit` to `true`.
- The limit resets within 24 hours (a weekly limit can reset further out).
- The run has not already waited twice; the third time the agent fails.

To finish a run whose agents failed at a limit, relaunch the workflow after the reset.
