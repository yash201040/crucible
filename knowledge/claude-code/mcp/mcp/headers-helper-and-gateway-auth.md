---
type: "Feature"
title: "headersHelper dynamic headers and gateway sign-in"
description: "headersHelper command generates auth headers at connect time; trust, working directory and env rules; OAuth behind header-requiring proxies."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, headers, auth, security]
kind: "setting"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "headersHelper"
  - "headers"
  - "CLAUDE_CODE_MCP_SERVER_NAME"
  - "CLAUDE_CODE_MCP_SERVER_URL"
  - "CLAUDE_PLUGIN_ROOT"
  - "projects[\"<path>\"].hasTrustDialogAccepted"
  - "${user_config.*}"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For Kerberos, short-lived tokens or internal SSO, set `headersHelper` to a command that prints a JSON object of string key-value pairs; the output merges into the headers and overrides static `headers` of the same name. Example: `"headersHelper": "/opt/bin/get-mcp-auth-headers.sh"` (or inline shell).

# How to use it

- Runs in a shell, given up after 10 seconds, fresh on each connection (session start and reconnect), never cached. On `401` or `403` from a tool call it is re-run, the server reconnected and the call retried once; needs-auth only if that fails. If it returns `Authorization`, that is the credential and there is no OAuth fallback; a rejection at connect is reported as failed.
- Env vars set for the helper: `CLAUDE_CODE_MCP_SERVER_NAME`, `CLAUDE_CODE_MCP_SERVER_URL`, `CLAUDE_PLUGIN_ROOT` (only for plugin servers).
- Working directory by where the server is configured:

| Configured in | Working directory |
|---|---|
| plugin | plugin root |
| project `.mcp.json` or local scope | the project directory declaring it |
| project agent file, SDK `mcpServers` / `setMcpServers()`, `--mcp-config` | session primary working directory |
| user scope, managed MCP, claude.ai connector, agent file from outside project (incl. `--add-dir`) | config directory (`~/.claude` unless `CLAUDE_CONFIG_DIR`) |

`/cd` moves it only for servers running from the primary directory; a Bash `cd` does not. Before v2.1.238 the others ran from the start directory.

# Limits and defaults

- Credential variables are stripped from the helper's environment for servers from a project `.mcp.json`, a plugin, or an inline agent-file server from your project or an `--add-dir` directory (names containing `TOKEN`, `SECRET`, `PASSWORD`, `KEY`, `AUTH` in any case, plus a fixed list such as `ANTHROPIC_CUSTOM_HEADERS`; Git's `GIT_CONFIG_KEY_<n>` excepted). Not stripped for user/local scope, managed MCP, claude.ai connectors, SDK or `--mcp-config` servers, and `~/.claude/agents/`, managed or `--agents` inline servers. A URL embedding such a value gets `REDACTED` in `CLAUDE_CODE_MCP_SERVER_URL`.
- Trust: for project `.mcp.json` or local-scope servers the helper runs only after you accept the trust dialog for the declaring project directory (a parent's trust and the automatic trust of `claude -p`/SDK for settings hooks do not count; before v2.1.238 `-p` and SDK skipped the check). Until then the server connects with static `headers` only and `claude -p`/SDK print one `headersHelper not run` line per server to stderr. Trust without a dialog: set `projects["<path>"].hasTrustDialogAccepted` to `true` in `~/.claude.json`. Inline agent-file servers are not loaded at all until their project or directory is trusted.
- A plugin `headersHelper` cannot use `${user_config.*}` (shell-run; reported as misconfigured; before v2.1.207 it substituted). Use `headers`, which is not shell-parsed, or a config file.
- OAuth behind a proxy that needs its own header (v2.1.299 or later): configure the header via `--header`, `headers` or `headersHelper` but keep `Authorization` out, then `claude mcp login <name>`. Configured headers except `Authorization` are sent to sign-in, refresh and revocation requests to the server's origin (scheme, host, port). The browser authorization page, or an authorization server on another origin behind its own gateway, still needs the gateway operator to let requests through. For managed or plugin servers, ask the admin or author to add the header.
