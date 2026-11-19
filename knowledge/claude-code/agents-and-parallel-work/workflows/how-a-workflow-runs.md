---
type: "Concept"
title: "How a workflow runs"
description: "The runtime executes the script in isolation, writes it under ~/.claude/projects/, and tracks agent results for resume."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, runtime, isolation, scripts]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "~/.claude/projects/"
  - "/add-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The runtime runs the script in an isolated environment separate from the conversation; intermediate results stay in script variables. Unless Claude starts from a script file path, the run's script is written under the session's directory in `~/.claude/projects/` and Claude receives its path, so you can read it, diff it against another run, or edit it and ask for a relaunch.

# How to use it

Claude can start a workflow only from a script file the session may already read. For a script outside the working directory, add its directory with `/add-dir` or a Read allow rule first. The runtime tracks each agent's result, which makes runs resumable within the same session.
