---
type: "Experiment"
title: "Code Mode reaches the agents of a workflow, in a terminal session only"
description: "In a terminal session with Code Mode on, a workflow agent has only the script tool and the result tool directly; in an SDK app it has the ordinary tools."
tags: [code-mode, workflows, tools]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "REPL"
  - "StructuredOutput"
  - "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE"
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

[Code Mode](/model-and-responses/code-mode/code-mode-overview.md) works only in an interactive terminal session. The documentation does not say whether the agents a workflow starts get it.

# Result

| Session | Tools a workflow agent can call directly | Other tools |
| --- | --- | --- |
| Terminal, Code Mode on | `REPL`, `StructuredOutput` | everything else is called from inside a script (`tools.list()` showed Bash, Read, Edit, Write, Glob, Grep, the MCP tools and more) |
| App built on the Agent SDK | Bash, Read, Edit, Write and the rest, loaded or deferred | no script tool |
| Headless (`claude -p`), Code Mode set in the user's settings | the ordinary tools | none; it prints "Code Mode (experimental) isn't available: for now it only works in the interactive terminal" |

The main agent of a new terminal session started with nothing but `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1` in the `env` of `~/.claude/settings.json` has `REPL` and `Poll` as its only direct tools (checked on 2.1.329).

A custom agent type with a `tools` list gets the script tool only when `REPL` is in that list; without it the agent has the listed tools and no Code Mode.

A transcript of a Code Mode agent holds an entry for every tool call a script made, with `isVirtual: true` and `"model": "<synthetic>"` and no token usage. Those are tool calls, not model calls: counting assistant entries over-counts the model calls of such an agent several times.

# What it means for crucible

Whether a run's agents work in Code Mode is decided by where the session was started, not by anything in the run. The efficiency log counts only entries with a real model behind them.

Where a result says "here", the probe ran as a workflow inside an app built on the Agent SDK; "terminal" means an interactive `claude` session in a terminal with Code Mode on. Each probe was a workflow script with one small agent per question, on Claude Code 2.1.325 or 2.1.329. A result holds for that release only: run the probe again after an update.
