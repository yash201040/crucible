---
type: "Reference"
title: "Allow and deny rules options"
description: "How allowed_tools and disallowed_tools add to rule lists, glob support, and which calls never reach canUseTool."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permissions, allowed-tools, disallowed-tools, rules]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "allowedTools"
  - "allowed_tools"
  - "disallowedTools"
  - "disallowed_tools"
  - "setting_sources"
  - "settingSources"
  - ".claude/settings.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`allowedTools`/`disallowedTools` (TypeScript) and `allowed_tools`/`disallowed_tools` (Python) add entries to the allow and deny rule lists. Unlisted tools remain available; calls to them needing approval fall to the permission mode.

# How to use it

| Option | Effect |
| :- | :- |
| `allowed_tools=["Read", "Grep"]` | Auto-approved (except reads from network paths). |
| `disallowed_tools=["Bash"]` | `Bash` tool definition removed from the request. |
| `disallowed_tools=["Bash(rm *)"]` | Matching calls (as written) denied in every mode incl. `bypassPermissions`; `/bin/rm` falls to mode. |
| `disallowed_tools=["*"]` | Deny-rule globs: `"*"` matches all tools, `"mcp__*"` all MCP tools. |

Allow-rule globs only after a literal `mcp__<server>__` prefix: `mcp__puppeteer__*`, `mcp__github__get_*`. An unanchored `allowed_tools=["*"]` or `["mcp__*"]` is ignored.

Locked-down agent:
```typescript
const options = { allowedTools: ["Read", "Glob", "Grep"], permissionMode: "dontAsk" };
```

# Limits and defaults

- Auto-approved calls never reach `canUseTool`; checks there are silently bypassed. Use a `PreToolUse` hook (runs for those calls too; its deny applies even in `bypassPermissions`).
- `allowed_tools` does not constrain `bypassPermissions`: with `allowed_tools=["Read"]` plus bypass, `Bash`, `Write`, `Edit` are still approved. Use `disallowed_tools` to block.
- Calls needing no approval in `default` (read-only Bash, `Agent`, reads in working directories) run whether listed or not. To hide a built-in tool entirely, add its bare name to `disallowedTools`.
- Bare name entry (`Read`, `mcp__github__get_issue`) approves every call except actions no mode auto-approves and network-path reads; scoped entry (`Bash(npm test *)`) approves only matches.
- Declarative allow/deny/ask rules in `.claude/settings.json` apply when the `project` setting source is enabled (default for `query()`); if you set `setting_sources`/`settingSources` explicitly, include `"project"`.

# Notes

Path pattern rules are in [path patterns](./path-patterns-in-rules.md).
