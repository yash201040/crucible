---
type: "Reference"
title: "Where tool names are used and rule formats"
description: "The places that accept tool names and the ToolName(specifier) formats for permission rules."
resource: "https://code.claude.com/docs/en/tools-reference#configure-tools-with-permission-rules-and-hooks"
tags: [permissions, rules, tools, hooks, allowedtools]
kind: "setting"
maturity: "unlabelled"
since: "2.1.228"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "permissions.allow"
  - "permissions.deny"
  - "--allowedTools"
  - "--disallowedTools"
  - "allowedTools"
  - "disallowedTools"
  - "allowed-tools"
  - "Bash(npm run *)"
  - "PowerShell(Get-ChildItem *)"
  - "Read(~/secrets/**)"
  - "Edit(/src/**)"
  - "Skill(deploy *)"
  - "Agent(Explore)"
  - "WebFetch(domain:example.com)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool names are referenced in `permissions.allow` and `permissions.deny` and the `/permissions` UI, the CLI flags `--allowedTools` and `--disallowedTools`, the Agent SDK `allowedTools` and `disallowedTools` options, a skill's `allowed-tools` frontmatter, and a hook's `if` condition. All accept the rule format `ToolName(specifier)`.

# How to use it

| Rule | Applies to | Matching |
| :- | :- | :- |
| `Bash(npm run *)` | Bash, Monitor | command pattern |
| `PowerShell(Get-ChildItem *)` | PowerShell | command pattern |
| `Read(~/secrets/**)` | Read, Grep, Glob, LSP | path pattern |
| `Edit(/src/**)` | Edit, Write, NotebookEdit | path pattern |
| `Skill(deploy *)` | Skill | skill name |
| `Agent(Explore)` | Agent | subagent type |
| `WebFetch(domain:example.com)` | WebFetch | domain |
| `WebSearch` | WebSearch | no specifier |

Tools not listed (for example `ExitPlanMode`, `ShareOnboardingGuide`) accept only the bare name. Hook `matcher` fields use bare tool names, not the parenthesized form.

# Limits and defaults

An `Edit(...)` allow rule also grants read access to the path. A `Read(...)` deny rule also blocks Edit and Write on that path, including creating a file there (for Write, the check needs v2.1.228+).
