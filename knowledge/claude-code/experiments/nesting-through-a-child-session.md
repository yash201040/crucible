---
type: "Experiment"
title: "An agent of a workflow can nest by starting a child session from the shell"
description: "A workflow agent has no Agent tool, but it can run a headless claude from Bash, and that child nests its own subagents: three levels ran under one agent of a run."
tags: [workflows, nesting, subagents, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Agent"
  - "claude -p"
  - "--output-format json"
  - "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
verified:
  - { by: "process:crucible-probe", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "probe"
    resource: "/experiments/"
    title: "Probe runs on Claude Code 2.1.329, 2026-11-20"
stale_after: "2027-01-19T00:00:00Z"
---

# Question

[An agent of a workflow gets no Agent tool](/experiments/workflow-agents-cannot-start-helpers.md). Is there another way for it to hand work to helpers of its own, to any depth?

# What was tried

A workflow with one agent (Haiku). The agent ran one shell command: a headless child session (`claude -p --model haiku --output-format json "<task>"`, with the parent session's marker variables unset). The child's task was to start a subagent with its Agent tool, which was to start another.

| Level | What it was | Had the `Agent` tool |
| --- | --- | --- |
| 1 | agent of the workflow | no (it has Bash) |
| 2 | headless child session started from Bash | yes |
| 3 | subagent of the child | yes |
| 4 | subagent of that subagent | yes (it did not use it) |

The child's transcript confirms it: one `Agent` call in the child, one in its subagent, two subagent transcripts. The same child started straight from a shell behaved the same.

# Result

- Nesting works this way, three levels below the agent of the run without any setting. Each level can be given its own model through the `model` field of the Agent call, and the child through `--model` and `--effort`.
- The child answers in about 15 seconds for a trivial task and costs about a cent or less by API prices on Haiku. Most of that is its own system prompt (about 46K tokens written, 75K read), paid once per child whatever the task.
- `--output-format json` returns `result`, `session_id`, `total_cost_usd` and tokens per model, so a wrapper can record what each child used.
- A headless child never has Code Mode. With the variable set it prints "Code Mode (experimental) isn't available: for now it only works in the interactive terminal" and starts with the ordinary tools.

# What the run does not see

A child session is outside the workflow. It does not count against the cap on agents at once, the run's ceiling of agents, or the workflow's count of tokens. Its transcript is filed under its own working directory, not under the run. The workflow's waiting on a usage limit does not cover it. It runs in the permission mode of the user's settings, with no prompt anybody can answer.

# What it means for crucible

A hierarchy can be made two ways, and they suit different work.

- **Split by the engine**: parts that carry a claim someone must check. Each has its own solver and checker, and the cap, the ceiling and the records hold. This is what the planner, the restructuring pass and the layers already do.
- **A helper under one agent**: work with no claim of its own (reading a large body of files, a wide search, a long test run) whose result the owner checks anyway. It keeps the owner's context small.

Built in v5.5 as `scripts/crucible_helper.py`: see [helper sessions, counted and closed](/experiments/helper-sessions-counted-and-closed.md). In the first large run 67 of 302 agents grew past 300K tokens of context and 24% of all cache reads happened above 200K ([context growth](/experiments/context-growth-without-compaction.md)); that is the most a helper rule could act on, before the cost of the helpers.

The probe ran as a workflow inside an app built on the Agent SDK, on Claude Code 2.1.329. A result holds for that release only: run the probe again after an update.
