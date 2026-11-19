---
type: "Experiment"
title: "Code Mode did not reduce model calls or tokens on five small tasks"
description: "The same five tool-heavy tasks, all solved correctly both ways: 15 model calls and 322K tokens read without Code Mode, 17 and 301K with it."
tags: [code-mode, cost, model-calls]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "REPL"
  - "Bash"
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

Does an agent that can write one script for many tool calls need fewer model calls than one that is told to work in few, large steps with the ordinary tools?

# What was tried

Sonnet 5.5 at medium effort, the same prompt both ways, including crucible's rule to work in few, large steps. Every answer was checked against a result computed by code, and the repairs by running the tests; all were right.

| Task | Without Code Mode (app): model calls, tokens read | With Code Mode (terminal): model calls, tokens read |
| --- | --- | --- |
| Count lines and functions in seven source files, name the three longest functions | 2, 29K | 2, 21K |
| Read frontmatter of 31 files and find the five most frequent names in 1,600 files | 4, 91K | 2, 21K |
| Write a module until 14 given tests pass | 3, 59K | 4, 69K |
| Find and fix 14 planted bugs in a four-module package (run 1) | 3, 62K | 5, 104K |
| The same (run 2) | 3, 81K | 4, 86K |
| Sum | 15, 322K | 17, 301K |

# Result

No measurable difference. Without Code Mode the agents already put many reads, edits and commands into one shell command or one short program, which is what the rule asks for. One run per cell, so single differences are noise.

# What is not known

Whether it differs on the long sessions of a real run, where a solver made 69 model calls on average before the rule existed. The first runs on the current version record model calls per agent and whether Code Mode was on, so they will show it.

# What it means for crucible

Code Mode is recorded, not required and not recommended. Nothing is built around it.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
