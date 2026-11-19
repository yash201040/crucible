---
type: "Reference"
title: "Credential storage, helpers and precedence"
description: "Where credentials are stored, apiKeyHelper behavior, login expiry, and the ordered credential precedence list."
resource: "https://code.claude.com/docs/en/authentication#authentication-precedence"
tags: [credentials, precedence, apikeyhelper, oauth]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.261"
surfaces: [cli, ide, sdk, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "apiKeyHelper"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "ANTHROPIC_PROFILE"
  - "ANTHROPIC_FEDERATION_RULE_ID"
  - "ANTHROPIC_ORGANIZATION_ID"
  - "ANTHROPIC_IDENTITY_TOKEN_FILE"
  - "ANTHROPIC_BASE_URL"
  - "~/.claude/.credentials.json"
  - "forceLoginGatewayUrl"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "authentication"
    resource: "https://code.claude.com/docs/en/authentication"
    title: "Authentication"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How Claude Code stores credentials and picks one when several exist.

# How to use it

Precedence, highest first:

| # | Credential | Notes |
| - | - | - |
| 1 | Cloud provider (`CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY`) | |
| 2 | `ANTHROPIC_AUTH_TOKEN` | `Authorization: Bearer`; for gateways |
| 3 | `ANTHROPIC_API_KEY` | `X-Api-Key`; interactive mode asks once (toggle "Use custom API key" in `/config`); in `-p` mode always used when present |
| 4 | `apiKeyHelper` output | dynamic or rotating keys |
| 5 | `CLAUDE_CODE_OAUTH_TOKEN` | long-lived token for CI |
| 6 | Anthropic profile / federation credentials | `ant auth login` profile ranks here only if named in `ANTHROPIC_PROFILE` |
| 7 | Subscription OAuth from `/login` | default for Pro/Max/Ultra/Team/Enterprise |

A signed-in Claude apps gateway session sits outside the list and outranks cloud providers. With `forceLoginMethod: "gateway"` or `forceLoginGatewayUrl` set (and no cloud provider variable), only gateway sign-in is used (v2.1.261+, v2.1.265+ for `forceLoginGatewayUrl` alone).

# Limits and defaults

- Storage: macOS Keychain (falls back to `~/.claude/.credentials.json`, mode 0600, if the Keychain rejects the write); Linux `~/.claude/.credentials.json` (0600); Windows `%USERPROFILE%\.claude\.credentials.json`. `CLAUDE_CONFIG_DIR` moves the file and keys the Keychain entry.
- `apiKeyHelper` slower than 10 seconds shows a warning; failures give `Your apiKeyHelper script is failing` within three attempts.
- `apiKeyHelper`, `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` apply to the CLI and wrappers (VS Code, Agent SDK, GitHub Actions); not Claude Desktop or cloud sessions (OAuth). Cloud sessions always use subscription credentials.
- Warning `Your login expires in 3 days` appears at startup for claude.ai logins. Expired logins fail with `Login reached its time limit` or `Login expired`; `/status` shows `Login` row `Expired — log in again`. Remote Control sessions disconnect and background sessions in agent view stop progressing when the login expires with no other credential.
- Profiles: `~/.config/anthropic` (macOS/Linux) or `%APPDATA%\Anthropic`; modes `oidc_federation` or `user_oauth`. Sources in order: `ANTHROPIC_PROFILE`; `ANTHROPIC_FEDERATION_RULE_ID` + `ANTHROPIC_ORGANIZATION_ID`; active profile. Not read in bare mode, Claude Desktop or cloud sessions. Selecting one disables claude.ai connectors and `/schedule`.
