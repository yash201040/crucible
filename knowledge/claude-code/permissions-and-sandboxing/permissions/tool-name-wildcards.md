---
type: "Feature"
title: "Tool-name wildcards and MCP rules"
description: "Glob patterns in the tool-name position for deny/ask rules, anchored globs for allow, and how MCP server names map to rules."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, mcp, wildcards, deny-rules]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "mcp__*"
  - "mcp__<server>__*"
  - "mcp__<server>__<tool>"
  - "mcp__puppeteer__*"
  - "mcp__plugin_<plugin>_<server>__*"
  - "mcp__claude_ai_<server>__<tool>"
  - "mcp__workspace__bash"
  - "mcp__workspace__web_fetch"
  - "ruleContent"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Deny and ask rules accept glob patterns that must match the full tool name: `"*"` matches every tool, `"mcp__*"` every MCP tool on all servers. A bare-name glob deny removes matched tools from context (same `EndConversation` exception). Allow rules accept globs only after a literal `mcp__<server>__` prefix with a glob-free server segment.

# How to use it

- Deny all MCP tools: `"deny": ["mcp__*"]`.
- Allow: `mcp__puppeteer__*` (all tools of server `puppeteer`), `mcp__github__get_*`. Unanchored allow globs `"*"`, `"B*"`, `"mcp__*"` are skipped and approve nothing.
- MCP forms: `mcp__puppeteer` and `mcp__puppeteer__*` match all tools of that server; `mcp__puppeteer__puppeteer_navigate` matches one tool.
- Server-name mapping: characters like `.` or spaces become `_` (`my.server` -> `mcp__my_server__*`); plugin servers use `mcp__plugin_my-plugin_database-tools__*`; a server name containing `__` or ending `_` needs the wildcard form (`mcp__reports__v2__*`). As deny or ask, `mcp__reports__v2` and `mcp__reports` each also cover the `reports__v2` server's tools; as allow they do not.
- Write MCP allow rules without a specifier (`ruleContent`); an allow rule with a specifier matches no call.
- Connectors Claude Code fetches itself appear as `mcp__claude_ai_<server>__<tool>`.

# Limits and defaults

- A deny/ask rule matching no known tool gives a startup warning; names with `_` or `*` and removed tools (e.g. `TaskOutput`) are exempt.
- If your organization set a claude.ai connector tool to `ask` and that reaches the session, allow rules do not take effect: it prompts each time, even in `auto` and `bypassPermissions`; in `dontAsk` or a `-p` run with nobody to answer it denies.
- In Cowork sessions in Claude Desktop, shell runs through `mcp__workspace__bash` and fetches through `mcp__workspace__web_fetch`. Whole-tool `Bash`/`WebFetch` deny rules also apply to them; `Bash` allow rules never carry over. The denial reads `Permission to use mcp__workspace__bash has been denied.`
