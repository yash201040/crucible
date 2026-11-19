---
type: "Feature"
title: "Restricting a subagent's tools"
description: "Use tools as an allowlist and disallowedTools as a denylist, including MCP server wildcards and double-underscore server names."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, tools, allowlist, denylist, mcp]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "tools"
  - "disallowedTools"
  - "mcp__github__*"
  - "mcp__github"
  - "mcp__*"
  - "permissions.deny"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`tools` is an allowlist; `disallowedTools` a denylist. If both are set, `disallowedTools` is applied first, then `tools` resolves against what remains; a tool in both is removed.

# How to use it

```yaml
tools: Read, Grep, Glob, Bash      # only these; no edit, write or MCP
disallowedTools: Write, Edit        # inherit everything else
```

| Goal | Field | Entry |
| :- | :- | :- |
| All tools of one MCP server | `tools` | `mcp__github__*` |
| Withhold one server | `disallowedTools` | `mcp__github` or `mcp__github__*` |
| Withhold every MCP tool | `disallowedTools` | `mcp__*` |

To keep Bash but block commands, add a Bash deny rule such as `Bash(git push *)` to `permissions.deny`; it applies to the main conversation and subagents. A `disallowedTools` entry with a specifier removes the whole tool.

# Limits and defaults

- If nothing in `tools` resolves (misspelled or unavailable entries), the launch usually fails with the error `Agent would be spawned with zero tools`, naming the entries.
- Servers whose name contains `__` (e.g. `reports__v2`): in `tools` write `mcp__reports__v2__*`; in `disallowedTools`, `mcp__reports` or `mcp__reports__*` also removes `reports__v2` tools, so list the `reports` tools one by one (e.g. `mcp__reports__run_query`).
