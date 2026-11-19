---
type: "Experiment"
title: "No agent of the first large run compacted; capping context earlier would save little"
description: "Agents grew to 677K tokens at most and never compacted. Only 4% of all cache reads happened above a context of 400K, so an earlier cap is not worth what compaction loses."
tags: [context, compaction, cost]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "autoCompactWindow"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "compact_boundary"
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

Models with a one-million-token window compact at about 967K by default ([auto-compact window](/model-and-responses/model-config/set-auto-compact-window.md)). Every model call re-reads the context. Would capping an agent's context at 300K or 400K ([per subagent](/agents-and-parallel-work/sub-agents/subagent-auto-compaction.md)) save much?

# What the first large run shows

| Figure | Value |
| --- | --- |
| Largest context per agent | median 193K, 90th percentile 412K, maximum 677K |
| Agents over 300K | 67 of 302 |
| Agents that compacted | none |
| Share of all cache reads above a context of 200K / 300K / 400K | 24% / 10% / 4% |
| Model calls per agent | median 60, 90th percentile 122, maximum 393 |

# Result

A cap at 400K could save at most 4% of the reading, less what the compaction itself costs, and a compacted solver has lost detail it worked for. Not adopted.

# What it means for crucible

Context is kept small by how a plan sizes its parts, which is measured as the share of solvers over 300K. If that share stays high after the planning rule, the cap is the next thing to try, and this page says what it can and cannot save.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
