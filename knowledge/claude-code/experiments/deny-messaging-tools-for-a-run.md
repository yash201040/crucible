---
type: "Experiment"
title: "One launch flag takes the messaging tools away from every agent of a run"
description: "Started with --disallowedTools SendMessage,ListAgents, a session's workflow agents cannot list or message other agents. Crucible does not set it by default."
tags: [isolation, workflows, messaging]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "--disallowedTools"
  - "SendMessage"
  - "ListAgents"
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

Crucible's attacker must never see the solver's reasoning. Agents of a workflow have `SendMessage`, and in some sessions `ListAgents` ([cross-session messaging](/agents-and-parallel-work/cross-session-messaging/overview-and-requirements.md)), with which one agent could reach another outside the engine's control. Can the host forbid it?

# What was tried

A session started with `claude --disallowedTools SendMessage,ListAgents -- "<prompt>"`, then a workflow agent listing its tools.

# Result

Neither tool is reachable by the workflow agent, directly or from the script tool (44 other tools are). A deny given at launch applies to the agents of a run. Note that the flag takes several names: a prompt placed after it is read as one more tool name, so the prompt goes after `--`.

In the records of the first large run, no agent called either tool.

# Why crucible does not set it by default

It would also take the tools from the session's own agent, which uses `SendMessage` to continue a helper it started. The risk has not been observed. Set the flag yourself for a session that only runs crucible, and revisit this if a run's records ever show an agent messaging another.

The probe was a workflow script with one small agent per question, in an interactive terminal session with Code Mode on and permission prompts off, on Claude Code 2.1.329. A result holds for that release only.
