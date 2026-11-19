---
type: "Feature"
title: "Agent and Cd permission rules"
description: "Agent(Name) rules gate subagents; Cd rules restrict the user-run /cd command and are not model-callable."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, subagents, cd, deny-rules]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Agent(Explore)"
  - "Agent(Plan)"
  - "Agent(my-custom-agent)"
  - "--disallowedTools"
  - "Cd"
  - "Cd(~/code/*)"
  - "Cd(~/code/**)"
  - "Cd(**/node_modules)"
  - "/cd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Agent(AgentName)` rules control which subagents Claude can use: `Agent(Explore)`, `Agent(Plan)`, `Agent(my-custom-agent)`. Put them in `deny` or pass `--disallowedTools`; for example `"deny": ["Agent(Explore)"]` disables Explore. See also [match by input parameter](./match-by-input-parameter.md).

`Cd` rules control where the `/cd` command can move the session. `Cd` is not a model-invocable tool; rules apply only when you run `/cd`.

# How to use it

- Bare `Cd` deny disables `/cd`. `Cd(<path-pattern>)` deny blocks matching targets, checking every spelling including each symlink hop.
- Any `Cd` allow rule switches `/cd` to allowlist mode: the resolved target must match an allow or `/cd` refuses. With no `Cd` rules, `/cd` prompts to trust an unfamiliar directory.
- Patterns share the `//`, `~/`, `/` anchors but match the whole directory path: `*` is exactly one segment, `**` crosses segments, trailing `/**` also matches the root.

| Rule | Matches | Not |
| - | - | - |
| `Cd(~/code/*)` | `~/code/app` | `~/code/app/src`, `~/code` |
| `Cd(~/code/**)` | `~/code` and anything under | outside `~/code` |
| `Cd(**/node_modules)` | any `node_modules` at any depth under cwd | `node_modules/pkg` |
