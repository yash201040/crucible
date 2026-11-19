---
type: "Experiment"
title: "An agent of a workflow cannot start helpers of its own"
description: "Tested four ways on two surfaces: no agent started by a workflow script gets the Agent tool, so nesting is not available inside a run."
tags: [workflows, nesting, subagents]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Agent"
  - "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"
  - "agentType"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
verified:
  - { by: "process:crucible-probe", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "probe"
    resource: "/experiments/"
    title: "Probe runs on Claude Code 2.1.325 and 2.1.329, 2026-11-19 and 2026-11-20"
stale_after: "2027-01-19T00:00:00Z"
---

# Question

The documentation says a subagent can start its own subagents, three layers deep by default ([nested subagents](/agents-and-parallel-work/sub-agents/nested-subagents.md)). Does that hold for the agents a workflow script starts with `agent()`? It would let a solver hand bulk reading to a light helper.

# What was tried

| Agent started by the script | Session | Has the `Agent` tool |
| --- | --- | --- |
| Default workflow agent | app (SDK) | no (not loaded, not deferred) |
| Default workflow agent | terminal, Code Mode | no (not reachable from the script tool either) |
| `agentType: general-purpose` | app and terminal | no |
| Custom agent type whose `tools` list names `Agent` | terminal | no |
| All of the above with `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=5` | terminal | no |

# Result

Nesting is not available to a workflow's agents, whatever the agent type or the depth setting. The documentation does not say so; it lists `Workflow` among the tools every subagent loses, and `Agent` only "at the depth limit" ([available tools](/agents-and-parallel-work/sub-agents/subagent-available-tools.md)).

# What it means for crucible

A hierarchy inside a run has to be made by the engine: a part that is too large is split into owned parts by the script, which keeps the budget, the records and the isolation in code. A solver cannot delegate by itself.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
