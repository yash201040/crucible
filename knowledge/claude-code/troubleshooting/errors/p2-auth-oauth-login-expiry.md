---
type: "Reference"
title: "OAuth, login expiry and sign-in errors"
description: "Errors for revoked, expired or unsaved claude.ai logins, token refresh contention, held accounts, profile logins and the structured error codes."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, authentication, oauth, login, headless]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop, cloud]
requires: ""
identifiers:
  - "authentication_failed"
  - "server_error"
  - "account_on_hold"
  - "claude setup-token"
  - "claude auth login"
  - "claude auth logout"
  - "CLAUDE_CONFIG_DIR"
  - "ANTHROPIC_PROFILE"
  - "~/.claude.json"
  - "/login"
  - "/logout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors that arise when the saved claude.ai login is revoked, expired, cannot be refreshed or cannot be saved. For unattended `claude -p` and Agent SDK runs the docs give structured error codes.

# How to use it

| Message | Structured code (`-p` / SDK) | Notes |
|---|---|---|
| `OAuth token revoked · Please run /login`; `API Error: 401 OAuth token has expired` | `authentication_failed` | Non-interactive text: `Failed to authenticate: OAuth token revoked...`. If `CLAUDE_CODE_OAUTH_TOKEN` is set, Claude Code keeps sending it after a 401 (before v2.1.225 it could swap in a stored login token). Use `claude setup-token` for a fresh long-lived token. |
| `API Error: 401 Invalid authentication credentials` | | Credential revoked, org disabled, or account deactivated. An approved `ANTHROPIC_API_KEY` outranks the login. Behind a gateway, the text after 401 is the gateway's. Since v2.1.304 tool search fields (`defer_loading`, `tool_reference`) are sent through gateways by default; before that `ENABLE_TOOL_SEARCH` was needed. |
| `Login expired · Please run /login` | `authentication_failed` | Refresh token rejected, stored credentials cleared. `-p` text: `Failed to authenticate: OAuth session expired and could not be refreshed`; says `reached its time limit` on v2.1.318+. |
| `Could not refresh your login because another Claude Code process is refreshing it` | `server_error` | Shared refresh lock held by another process; transient, retry in a minute; `/login` does not wait on the lock. |
| `Could not refresh your login: the disk that holds the Claude Code config directory ... is full` | | Config dir is `~/.claude` unless `CLAUDE_CONFIG_DIR`. Also caused by quota or inode exhaustion. Re-login does not help. |
| `Couldn't save your login` | | Credential store failure; macOS locked keychain. |
| `Your account is on hold ...` | `account_on_hold` | Account suspended, appeal at claude.ai/restricted. Before v2.1.235 shown as Login expired. |
| `Anthropic profile login expired` / `Login expired · Run /login ... or re-authenticate your Anthropic profile` | | Profile selected via `ANTHROPIC_PROFILE`, discovered in the Anthropic config directory, or written by keyless Console sign-in. Requests stop locally with no retry. |
| `OAuth token does not meet scope requirement: user:profile` | | Token predates a scope; `/login` again. |
| `Claude login not accepted · Run /login, then try again` | | Cloud session creation refused with 401. |
| `Artifacts need a claude.ai login` | | Select "Claude account with subscription", not Console account. |
| `Couldn't start the local listener that receives the browser sign-in` | | Port on `127.0.0.1` unavailable (sandbox, piped input). Fallback: paste code, or `claude setup-token` plus `CLAUDE_CODE_OAUTH_TOKEN`, or `ANTHROPIC_API_KEY`. Before v2.1.305 sign-in simply stopped. |
| `Sign in again to take your previous account or API key off the config file` / `Your account or API key may still be in the config file` | | Run `claude auth login` / `claude auth logout`; success prints `Successfully logged out from your Anthropic account.` |

# Notes

For automation that cannot sign in interactively the docs recommend `ANTHROPIC_API_KEY` or `claude setup-token`. Before v2.1.318, `claude -p` jobs could lose the stored login when someone signed in again to the same account.
