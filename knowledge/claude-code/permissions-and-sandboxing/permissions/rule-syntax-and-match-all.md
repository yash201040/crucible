---
type: "Reference"
title: "Permission rule syntax"
description: "Rules are Tool or Tool(specifier); a bare name matches all uses, and tool labels differ from canonical names."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, rule-syntax, specifiers]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Bash"
  - "Bash(*)"
  - "WebFetch"
  - "Read"
  - "Bash(npm run build)"
  - "Read(./.env)"
  - "WebFetch(domain:example.com)"
  - "TaskStop"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A permission rule is `Tool` or `Tool(specifier)`.

# How to use it

| Rule | Effect |
| :- | :- |
| `Bash` | All Bash commands |
| `WebFetch` | All web fetch requests |
| `Read` | All file reads |
| `Bash(*)` | Same as `Bash`; as a deny it also removes the tool from context |
| `Bash(npm run build)` | Exactly `npm run build` |
| `Read(./.env)` | Reading `.env` in the current directory |
| `WebFetch(domain:example.com)` | Fetches to example.com |

# Notes

The label shown in the transcript or dialog can differ from the canonical name (the tool labeled `Stop Task` is `TaskStop`). Rules and hook matchers match only canonical names; a rule written with the label does not match. For deny and ask rules a startup warning says so. Canonical names are in the tools reference.
