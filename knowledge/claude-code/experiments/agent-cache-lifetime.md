---
type: "Experiment"
title: "Agents of a run keep their cache five minutes; a longer command makes them pay for their context again"
description: "In the first large run 57% of all cache writes were rebuilds after a command of 5 to 30 minutes. The one-hour lifetime is switched on by one variable or per agent type."
tags: [prompt-caching, cost, workflows]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"
  - "subagentPromptCacheTtl"
  - "experimental.cacheTtl"
  - "ephemeral_1h_input_tokens"
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

Agents of a workflow are outside the main conversation's cache bucket and get the five-minute lifetime even on a subscription ([lifetimes](/core-concepts/prompt-caching/cache-lifetime-ttl-buckets.md)). What does that cost a run, and do the controls ([reference](/core-concepts/prompt-caching/cache-ttl-controls-reference.md)) reach workflow agents?

# What the first large run shows

From the transcripts of 302 agents (20,800 model calls):

| Figure | Value |
| --- | --- |
| Tokens read from the cache | 4,098 M |
| Tokens written to the cache | 149.9 M, all with the five-minute lifetime |
| Calls that came more than five minutes after the agent's previous call and wrote most of the context again | 318 |
| Tokens written in those rebuilds | 85.0 M, 57% of all writes |
| Silence before a rebuild | 5 to 10 minutes: 225 times; 10 to 30 minutes: 93 times; never over an hour |
| What the agent did before the silence | a shell command (a build or a test run) in 317 of 318 cases |
| Whose rebuilds | solvers 67.6 M, attackers 9.6 M, repairs 4.5 M |

# What was tried

| Setting | Cache writes of a workflow agent |
| --- | --- |
| Nothing set | all at five minutes |
| `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL=1h` before the session starts | all at one hour |
| `experimental: { cacheTtl: 1h }` in the agent type's file | all at one hour |

# Result

Both controls work for workflow agents. With one hour every rebuild of that run would have been a read. A one-hour write is billed higher than a five-minute one (on the API twice the input price instead of 1.25 times; a read is a tenth), so the saving is the rebuilds minus the dearer first writes: by API prices about 7% of that run's token cost. How a subscription counts the two kinds of write is not published.

# What it means for crucible

`bin/crucible-claude` starts a session with the one-hour lifetime for agents. The run digest reports the share of cache writes that were rebuilds; the expectation is that it falls from 0.57 to under 0.1.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
