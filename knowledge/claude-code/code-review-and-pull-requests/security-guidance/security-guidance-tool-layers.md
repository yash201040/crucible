---
type: "Concept"
title: "Security guidance in the security tool stack"
description: "Where the in-session security guidance plugin sits relative to /security-review, the Claude Security plugin, Code Review and CI scanners."
resource: "https://code.claude.com/docs/en/security-guidance"
tags: [security, layers, code-review, comparison]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/security-review"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security-guidance"
    resource: "https://code.claude.com/docs/en/security-guidance"
    title: "Catch security issues as Claude writes code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Stage | Tool |
| :- | :- |
| In session | Security guidance plugin |
| On demand, single pass | `/security-review` (current branch only) |
| On demand, deep scan | Claude Security plugin |
| On pull request | Code Review (Team and Enterprise) |
| In CI | Your own static analysis and dependency scanners |

# Notes

To find issues in existing code rather than changes Claude is writing, ask Claude to review a file or directory, or use the Claude Security plugin. All of these read source in your checkout, not a running site or deployed service.
