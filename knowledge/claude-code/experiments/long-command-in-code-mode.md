---
type: "Experiment"
title: "A command of eleven minutes finishes inside a Code Mode agent of a workflow"
description: "A script that waits is stopped after ten minutes, but a long shell command moved to the background by itself and the agent collected its output: one attempt, no loss."
tags: [code-mode, workflows, long-running]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "REPL"
  - "Bash"
  - "BASH_DEFAULT_TIMEOUT_MS"
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

In Code Mode, code that waits is stopped after ten minutes unless it can run in the background ([long-running code](/model-and-responses/code-mode/long-running-code.md)). Solvers of a real run regularly start builds and test runs of 5 to 30 minutes. Does such a command survive in a workflow agent that works in Code Mode?

# What was tried

One agent was told to run `date +%s; sleep 660; echo long-done; date +%s` the way it would run a long test suite, and to report every obstacle.

# Result

One attempt. The first call came back with a running task and no output: the command had moved to the background at the default command timeout. The agent read the task's output until it held `long-done`; the two timestamps were 660 seconds apart. Nothing was stopped and nothing ran twice.

# What it means for crucible

Long builds and test runs are safe in a Code Mode session with permission prompts off. Not tested: a session in a mode that asks for permission, where the documentation says code cannot move to the background.

The probe was a workflow script with one small agent per question, in an interactive terminal session with Code Mode on and permission prompts off, on Claude Code 2.1.329. A result holds for that release only.
