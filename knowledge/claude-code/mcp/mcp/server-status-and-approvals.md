---
type: "Reference"
title: "Server status, approvals and discovery cache"
description: "Status labels in claude mcp list and /mcp, project-server approval under workspace trust, and the cached status and MCP_DISCOVERY_CACHE."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, status, trust, cache]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.221"
surfaces: [cli]
requires: ""
identifiers:
  - "disabledMcpjsonServers"
  - "enabledMcpjsonServers"
  - "enableAllProjectMcpServers"
  - "MCP_DISCOVERY_CACHE"
  - ".claude/settings.local.json"
  - "skipDangerousModePermissionPrompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude mcp list` shows a health status per server; a failure status means that server did not connect, not that the command failed.

# How to use it

Statuses that report a configuration decision (printed without connecting):

| Status | Meaning | Shown in |
|---|---|---|
| `⏸ Pending approval (run claude to approve)` | `.mcp.json` server not yet approved | list and get |
| `✘ Rejected (see disabledMcpjsonServers in settings)` | rejected by `disabledMcpjsonServers` | get only |
| `⊘ Disabled for this project (re-enable via /mcp)` | named in `disabledMcpServers` | list and get |
| `✘ Blocked by enterprise managed policy` | an org policy refuses it | list and get; servers blocked by an allowlist/denylist are hidden instead |

# Limits and defaults

- Approvals: `claude mcp list/get` read `.mcp.json` approvals only from non-repo settings until you trust the workspace. `enableAllProjectMcpServers` or `enabledMcpjsonServers` committed in project `.claude/settings.json` is ignored in an untrusted folder. Approvals from user `~/.claude/settings.json`, managed settings and `--settings` still apply. Untracked `.claude/settings.local.json` approvals apply only in a trusted folder (before v2.1.207 they applied even when untrusted). A `disabledMcpjsonServers` entry in any file still rejects.
- Cached status (needs v2.1.221): a remote HTTP/SSE server used before can show `cached 2h ago · connects on first use · 5 tools`; tools come from the discovery cache and the server connects on first tool call. The cache is off by default unless a gradual rollout enabled it; `MCP_DISCOVERY_CACHE=1` forces on, `0` forces off (before v2.1.238 it was on by default). Disable or Clear authentication in `/mcp` discards the entry; Reconnect discards it on a connected or failed server but keeps it on a cached one.
- Failure detail: `✘ Failed to connect` gets the HTTP status or error code plus server error text (on `claude mcp list` and an `Issue:` line in `claude mcp get`); credential-like text is redacted and the expanded URL never shown. `✘ Connection error` gets no detail. After a failed `/mcp` authentication, the code and URL origin (scheme, host, port) are shown, never path or query.
- A remote server with an empty `url` shows `not configured` and is not connected (a plugin may ship such a placeholder).
- Project-scoped servers load without any prompt in `claude -p`, Agent SDK sessions, cloud sessions outside a project, and in `bypassPermissions` mode when `skipDangerousModePermissionPrompt` is set. See [installation scopes](./installation-scopes-and-precedence.md).
