---
type: "Concept"
title: "Agent terminated early due to an API error"
description: "A subagent's terminal API failure ends it with this message; partial output handling and how to resume."
resource: "https://code.claude.com/docs/en/errors#agent-terminated-early-due-to-an-api-error"
tags: [subagents, errors, resume, partial-output]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.199"
surfaces: [cli]
requires: ""
identifiers:
  - "Agent terminated early due to an API error: <error detail>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A subagent's API request failed terminally (for example a usage limit reached or server-error retries exhausted), so it stopped before finishing. Requires v2.1.199 or later; before then the API error text was returned to Claude as if it were the subagent's result.

# How to use it

Match the detail after the colon to its section (Usage limits, Server errors) and follow it. Once the cause clears, ask Claude to retry the task or resume the subagent.

When a rate limit, overload or server error interrupts a foreground subagent that already produced text, Claude receives that partial output marked incomplete instead of this error. A subagent whose only output was tool calls gets this error (v2.1.199 returned an empty partial result in that case).

# Notes

Related behavior: a cut-off subagent response with text but no tool calls is prompted to continue (see [The response above may be incomplete](./p1-response-incomplete.md)).
