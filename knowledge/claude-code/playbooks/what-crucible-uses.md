---
type: "Playbook"
title: "What crucible uses of the host, what it leaves, and why"
description: "The decision for each host feature that could matter to crucible, with the evidence behind it. Read this before proposing to use or drop one."
tags: [crucible, decisions, feature-map]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "crucible-claude"
  - "crucible_run.py host"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "probe"
    resource: "/experiments/"
    title: "Probe runs on Claude Code 2.1.325 and 2.1.329, 2026-11-19 and 2026-11-20"
stale_after: "2027-01-19T00:00:00Z"
---

# How to read this

One row per host feature that bears on running many agents. "Evidence" links to a test or names the run that showed it. A row is a decision made on 2026-11-20 for Claude Code 2.1.328; it stands until evidence changes, and the last column says what would change it.

# Used

| Feature | How crucible uses it | Evidence |
| --- | --- | --- |
| [Dynamic workflows](/agents-and-parallel-work/workflows/dynamic-workflows-overview.md) | The engine is one workflow script: code starts every agent and decides when a part is settled. | two large runs |
| [Structured output per agent](/agents-and-parallel-work/workflows/workflow-script-format.md) | Every role returns a checked object. | suite |
| [Model and effort per agent](/agents-and-parallel-work/sub-agents/choose-subagent-model.md) | The routing table gives each role a model by the difficulty of its part. | calibration |
| [Replay of finished agents](/agents-and-parallel-work/workflows/resume-after-pause.md) | Continue never redoes finished work. The replay stops at the first agent whose prompt changed, so prompts are built the same every time. | suite |
| [Cap on agents at once](/agents-and-parallel-work/workflows/runtime-limits-and-concurrency.md) | `bin/crucible-claude` starts the session with 12 instead of the machine's default. | [test](/experiments/workflow-concurrency-cap.md) |
| [Cache lifetime for agents](/core-concepts/prompt-caching/cache-ttl-controls-reference.md) | `bin/crucible-claude` starts the session with one hour. | [test](/experiments/agent-cache-lifetime.md) |
| [Headless runs](/automation/headless/print-mode-basics.md) | The standalone runner starts one headless session per agent on hosts without the workflow tool. | suite, one small run |
| Agent transcripts | The save step reads them for tokens, model calls, cache rebuilds and time. | [counting](/experiments/code-mode-reaches-workflow-agents.md) |
| [Nested subagents](/agents-and-parallel-work/sub-agents/nested-subagents.md), through [a headless child session](/automation/headless/index.md) | A workflow's agents get no tool that starts agents, so a solver hands bulk work with no claim of its own (a large body of reading, a wide search, a long build or test run) to a helper session started by `scripts/crucible_helper.py`, which may start another. The launcher caps how many work at once and how deep they go, holds them to an allowance inside the run's ceiling, records each and ends each. Solvers only. | [no tool](/experiments/workflow-agents-cannot-start-helpers.md), [the child session](/experiments/nesting-through-a-child-session.md), [counted and closed](/experiments/helper-sessions-counted-and-closed.md). Not yet measured on a real run. |

# Recorded, not relied on

| Feature | Why only recorded | What would change it |
| --- | --- | --- |
| [Code Mode](/model-and-responses/code-mode/code-mode-overview.md) | It reaches a run's agents in a terminal session, breaks nothing, and saved nothing on five small tasks. | [a real run](/experiments/code-mode-model-calls-on-small-tasks.md) with fewer model calls per agent than one without it |
| [Waiting out a usage limit](/agents-and-parallel-work/workflows/workflow-usage-limit-pause.md) | The host does it only in a terminal session; elsewhere crucible's own pause and continue applies. | nothing: both paths stay |

# Left out, with reasons

| Feature | Why not | What would change it |
| --- | --- | --- |
| [Custom agent types per role](/agents-and-parallel-work/sub-agents/frontmatter-fields.md) | Work, but give nothing a session setting does not, and need an install step. | [an attacker changing a solver's files](/experiments/custom-agent-types-in-workflows.md) |
| [Earlier compaction](/agents-and-parallel-work/sub-agents/subagent-auto-compaction.md) | At most 4% of the reading to save, against lost detail. | [solvers over 300K](/experiments/context-growth-without-compaction.md) staying common |
| [Agent teams](/agents-and-parallel-work/agent-teams/agent-teams-overview-and-enable.md) | Agents decide between themselves and talk freely: the opposite of code deciding and of an attacker who never sees the solver's reasoning. | nothing foreseeable |
| [Denying messaging tools](/experiments/deny-messaging-tools-for-a-run.md) | Works, never needed so far, and it would bind the session's own agent too. | a run in which one agent messages another |
| Starting a run in a hidden terminal session from an app (so that app users get Code Mode and the launcher's settings) | It works in a test, but the session can hang on a prompt nobody sees, and the two settings that matter can be had from the user's own settings. | [Code Mode](/experiments/code-mode-model-calls-on-small-tasks.md) showing a real saving on a run. |
| [Advisor](/model-and-responses/advisor/advisor-tool-overview.md) | A stronger model advises a lighter one at moments the lighter one picks; no cap, experimental. Crucible already has a second look that code controls. | a calibration in which a light model with an advisor matches a stronger model on the role probes at lower cost |
| [Fallback model chain](/model-and-responses/model-config/fallback-model-chains.md) | An agent would carry on with a weaker model, and a weaker model must never check a stronger one. | a way to see the switch in code and discard that agent's verdict |
| [/goal](/automation/goal/goal-command.md), [hooks that judge](/automation/hooks-guide/prompt-and-agent-hooks.md) | A model decides when work is done; in crucible code does. | nothing foreseeable |
| [A terminal session driven from an app](/experiments/code-mode-reaches-workflow-agents.md) | It would give app users the launcher's settings and Code Mode, at the price of a hidden session that can hang on a prompt. The two settings can be had by starting the session with them. | Code Mode showing a real saving, or users who cannot start their own sessions with the settings |
| [Plugin packaging](/plugins/plugins-overview/index.md) | Install is already one clone and one command; a review commits in the clone, which a plugin cache would hide. | several users asking for it |
| [Background sessions](/agents-and-parallel-work/agent-view/dispatch-from-shell.md) | A running workflow does not move to a background session by itself. | the host carrying workflows over |

# Not yet looked at closely

Scheduled reviews ([routines](/platforms-and-integrations/routines/index.md)), usage figures from telemetry ([monitoring](/usage-and-costs/monitoring-usage/index.md)) instead of transcripts, the permission setting that denies instead of asking (`permissions.denyInsteadOfPrompting`) for sessions that are not in bypass mode, and everything about the Agent SDK as a host.
