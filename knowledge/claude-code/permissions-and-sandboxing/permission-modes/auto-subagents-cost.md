---
type: "Concept"
title: "Auto mode with subagents; cost and latency"
description: "Classifier checks at subagent spawn, run and finish, and which accounts pay for classifier calls."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, subagents, cost, latency, classifier]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "permissionMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The classifier checks subagent work at three points:
1. Before it starts: the delegated task description is evaluated, so a dangerous-looking task is blocked at spawn.
2. While it runs: each action uses the same decision order, block and allow rules as the parent. Any `permissionMode` in the subagent's frontmatter is ignored.
3. When it finishes: the classifier reviews its work and final report before the parent reads it. If flagged (or a separate API safety check refuses the review) the report is still delivered, prefixed with a security warning. If the classifier is unavailable, the report arrives with a note to verify before acting.

# Limits and defaults

- Cost: classifier calls count toward token usage on Enterprise plans and on Claude API, Claude Platform on AWS, Bedrock, Agent Platform and Foundry accounts. Each check sends part of the transcript plus the pending action, adding a round trip before execution. With server-side review there are no separate calls to count.
- Sandboxed network access adds no per-connection classifier requests: hosts a command names are judged once with the command, and connections are checked against the approved list.
