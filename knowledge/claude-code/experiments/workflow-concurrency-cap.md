---
type: "Experiment"
title: "The cap on agents working at once holds a run back, and the setting lifts it"
description: "Twelve agents started together: six worked at once with the default on an 8-core machine, twelve with the variable set to 12. The first large run sat at six for 78% of its time."
tags: [workflows, concurrency, speed]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS"
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

A workflow runs 16 agents at once by default, "fewer when fewer CPUs are available" ([runtime limits](/agents-and-parallel-work/workflows/runtime-limits-and-concurrency.md)). How much does that bind, and does `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` lift it?

# What was tried

Twelve agents, each running one command that sleeps 25 seconds, started together.

| Session | Most agents alive at once | Time for all twelve |
| --- | --- | --- |
| Default (8-core machine) | 6 | two waves, 56 s |
| Variable set to 12 before the session started | 12 | one wave, 28 s |

In the records of the first large crucible run (302 agents, 31 hours) exactly six agents were alive for 78% of the time, and one or two for 12%.

# Result

On a laptop the default cap is the number of CPUs minus two, and a wide run spends most of its time at it. Agents wait for the model far more than for the CPU, so the cap is not protecting anything there. The variable is read when the session starts.

# What it means for crucible

`bin/crucible-claude` starts a session with 12. The run digest reports the share of time spent at the peak, so a cap that binds shows. A build whose agents all run heavy test suites can still overload a small machine: that is the one reason to set it lower.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
