---
type: "Feature"
title: "Match rules by input parameter"
description: "Deny and ask rules can match one scalar input parameter of a built-in tool, such as Agent(model:opus)."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, deny-rules, subagents, parameters]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Agent(model:opus)"
  - "Agent(isolation:worktree)"
  - "Bash(run_in_background:true)"
  - "Agent(isolation:*)"
  - "Skill(skill:<name>)"
  - "--disallowedTools"
  - "--verbose"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Deny and ask rules (not allow) can match a top-level input parameter of any built-in tool with `Tool(param:value)`. The rule matches when Claude calls the tool with exactly that value.

# How to use it

| Rule | Matches |
| :- | :- |
| `Agent(model:opus)` | Agent calls requesting the Opus tier |
| `Agent(isolation:worktree)` | Agent calls requesting a git worktree |
| `Bash(run_in_background:true)` | Bash calls run in the background |

Matching rules:
- The parameter must be a direct field of the tool input; nested fields are not matchable.
- One parameter per rule. To gate on `model` and `isolation`, write two rules.
- `*` is a wildcard: `Agent(isolation:*)` matches any explicit isolation value. Without `*` the match is exact.
- An omitted parameter is never matched: `Agent(model:*)` does not match a call with `model` unset.
- The value is compared to the literal input before normalization: `Agent(model:opus)` matches the alias `opus`, not a full model ID.
- `Skill(skill:<name>)` deny matches the skill under any of its names (alias, display name).
- Whitespace around the colon is ignored. Run with `--verbose` to see exact parameter names and values.

# Limits and defaults

- Primary content fields cannot be matched: `command` (Bash, PowerShell), `file_path` (Read, Edit, Write), `path` (Grep, Glob), `notebook_path` (NotebookEdit), `url` (WebFetch). `Bash(command:rm *)` is ignored with a startup warning; use `Bash(rm *)`, `Read(./path)` or `WebFetch(domain:host)`.
- MCP tools: settings-file rules with parentheses on an `mcp__` name are skipped (listed in the invalid-settings dialog and `claude doctor`). To match a parameter on an MCP tool pass a deny rule with `--disallowedTools`.
