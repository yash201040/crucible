---
type: "Experiment"
title: "Custom agent types work in a workflow, and crucible does not use them"
description: "A workflow agent can run as a custom agent type: its tool list and cache lifetime apply. The type must exist when the session starts. Nothing it gives crucible is worth an install step."
tags: [subagents, workflows, agent-types]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "agentType"
  - "tools"
  - "disallowedTools"
  - "autoCompactWindow"
  - "experimental.cacheTtl"
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

`agent()` in a workflow script takes an agent type. Would crucible's roles gain from being agent types of their own ([frontmatter fields](/agents-and-parallel-work/sub-agents/frontmatter-fields.md)): a tool list per role, a context cap, a cache lifetime, the helper tool?

# What was tried

Three agent types in `~/.claude/agents/`, used from a workflow.

| Check | Result |
| --- | --- |
| Type defined after the session started (app) | not found: "agent type ... not found. Available agents: ..." |
| Type defined before the session started (terminal) | found |
| `tools: Read, Bash` | the agent has exactly those and the result tool |
| `tools` without `REPL` in a Code Mode session | no script tool |
| `tools` naming `Agent` | no helper tool (see [nesting](/experiments/workflow-agents-cannot-start-helpers.md)) |
| `experimental: { cacheTtl: 1h }` | cache writes at one hour |

# Result

They work. What they would give crucible: a tool list per role (an attacker that cannot edit, no messaging tools), a cache lifetime per role, a cap on context.

# Why crucible does not use them

- The cache lifetime is set for the whole session by one variable.
- A context cap is not wanted: see [context growth](/experiments/context-growth-without-compaction.md).
- They need files installed outside the framework folder before the session starts, and the same engine must run where they do not exist (the standalone runner, Codex).
- Messaging between agents never happened in 302 agents, and a session can deny those tools with one flag.

This is the decision to revisit if a run shows an attacker changing a solver's files, or agents messaging each other.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
