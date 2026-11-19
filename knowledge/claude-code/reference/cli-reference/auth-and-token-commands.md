---
type: "Reference"
title: "Authentication and token commands"
description: "claude auth login, logout, status, setup-token and MCP login/logout subcommands for signing in, including CI tokens."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [auth, oauth, ci, mcp]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli]
requires: "setup-token needs a Claude subscription"
identifiers:
  - "claude auth login"
  - "claude auth logout"
  - "claude auth status"
  - "claude setup-token"
  - "claude mcp"
  - "claude mcp login <name>"
  - "claude mcp logout <name>"
  - "--email"
  - "--sso"
  - "--console"
  - "--text"
  - "--no-browser"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subcommands that sign in or out of an Anthropic account, report auth state as JSON, mint a long-lived CI token, and run MCP server OAuth from the shell.

# How to use it

| Command | What it does |
| :- | :- |
| `claude auth login` | Sign in. `--email` pre-fills the email, `--sso` forces SSO, `--console` signs in with Anthropic Console for API usage billing. With managed settings requiring a Claude apps gateway sign-in, run with no flags in a terminal (v2.1.316+) |
| `claude auth logout` | Log out |
| `claude auth status` | Auth status as JSON; `--text` for human-readable. Exit code 0 if logged in, 1 if not. JSON has `authMethod` (one of `none`, `claude.ai`, `oauth_token`, `api_key`, `api_key_helper`, `third_party`) and `configDirectory` (v2.1.268+) |
| `claude setup-token` | Generate a long-lived OAuth token for CI and scripts; prints it without saving it. Requires a Claude subscription |
| `claude mcp` | Configure MCP servers |
| `claude mcp login <name>` | Run a server's OAuth flow without the `/mcp` panel; works for HTTP, SSE and claude.ai connector servers. `--no-browser` over SSH prints the URL; paste the redirect URL back for HTTP/SSE servers |
| `claude mcp logout <name>` | Clear stored OAuth credentials for a server |

# Notes

If `claude auth login` points you to `/login`, run that inside `claude`.
