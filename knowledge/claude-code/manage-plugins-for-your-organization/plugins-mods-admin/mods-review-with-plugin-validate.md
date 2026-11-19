---
type: "Feature"
title: "Review a mod with claude plugin validate"
description: "claude plugin validate prints the hooks and mods API calls a mod's code uses, so admins can review it without running it."
resource: "https://code.claude.com/docs/en/plugins/mods/admin"
tags: [mods, validate, review, security, cli]
kind: "tool"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: "Claude Code v2.1.323 or later for long lists to continue on more lines"
identifiers:
  - "claude plugin validate"
  - "$.fs.read"
  - "$.fs.write"
  - "$.process.run"
  - "$.process.spawn"
  - "$.http.fetch"
  - "$.env.get"
  - "$.env.set"
  - "$.settings.read"
  - "$.mcp.call"
  - "$.model.complete"
  - "$.prompt.submit"
  - "$.session.send"
  - "tool.call"
  - "prompt.submit"
  - "tool.check"
  - "ui.render{component=AskUserQuestion}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-admin"
    resource: "https://code.claude.com/docs/en/plugins/mods/admin"
    title: "Manage mods for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

`claude plugin validate ./some-mod` prints `hooks:` (events the mod receives; a `default matcher key: plugin` note means the hook skips other mods' controls and drawings) and `calls:` (mods API methods its code calls), plus `env reads:` / `env writes:` lines naming variables. Claude Code refuses to load a mod that uses the mods API in a way this command cannot read. Do not approve a mod that fails the command; read every `hooks:` and `calls:` line.

| Call | Meaning |
|---|---|
| `$.fs.read`, `$.fs.write` | files anywhere the user can |
| `$.process.run`, `$.process.spawn` | starts programs as the user |
| `$.http.fetch` | network requests |
| `$.env.get`, `$.settings.read` | environment variables and settings (may hold API keys) |
| `$.env.set` | sets an environment variable for Claude Code and every command and MCP server it starts |
| `$.mcp.call` | calls a connected MCP server tool with no permission prompt |
| `$.model.complete` | uses the user's plan or API key for model calls |
| `$.prompt.submit` | submits a prompt, can pass as the user's words |
| `$.session.send` | sends a message another session, subagent or teammate reads |

Hook signals: `tool.call` and `prompt.submit` mean the mod sees and can change every tool call and prompt; `session.append` can rewrite stored rows; `ui.render{component=AskUserQuestion}` can redraw the question dialog; `tool.check` can approve or deny a tool call before a prompt.

User access by plugin control: no controls, any marketplace, any `--plugin-dir`, or in-session Claude-written; with a marketplace allowlist, allowed marketplaces plus `--plugin-dir` (session-written needs the allowlist to include `skills-dir`); allowlist plus `disableSideloadFlags`, allowed marketplaces only.
