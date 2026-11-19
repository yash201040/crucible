---
type: "Reference"
title: "Anthropic authentication and credential variables"
description: "Variables for API keys, bearer tokens, OAuth tokens, workload identity federation and credential helper refresh."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [auth, api-key, oauth, federation]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_PROFILE"
  - "ANTHROPIC_FEDERATION_RULE_ID"
  - "ANTHROPIC_ORGANIZATION_ID"
  - "ANTHROPIC_WORKSPACE_ID"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "CLAUDE_CODE_OAUTH_REFRESH_TOKEN"
  - "CLAUDE_CODE_OAUTH_SCOPES"
  - "CLAUDE_CODE_API_KEY_HELPER_TTL_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Credentials Claude Code reads for Anthropic-hosted access, headless and SDK runs included.

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_API_KEY` | Sent as `X-Api-Key`. Replaces a Pro/Max/Ultra/Team/Enterprise login. With `-p` the key is always used when present; interactively the user approves it once. `unset` it to use the subscription. |
| `ANTHROPIC_AUTH_TOKEN` | Custom `Authorization` header value, prefixed with `Bearer `. |
| `ANTHROPIC_PROFILE` | Anthropic profile name to authenticate with (for example from `ant auth login` or a Console sign-in without an API key). |
| `ANTHROPIC_FEDERATION_RULE_ID` | Rule ID for Workload Identity Federation; set together with `ANTHROPIC_ORGANIZATION_ID`. |
| `ANTHROPIC_ORGANIZATION_ID` | Organization ID for Workload Identity Federation; set with `ANTHROPIC_FEDERATION_RULE_ID`. |
| `ANTHROPIC_WORKSPACE_ID` | Workspace to target when the federation rule covers more than one workspace. |
| `CLAUDE_CODE_OAUTH_TOKEN` | claude.ai OAuth access token, an alternative to `/login` for SDK and automated environments. Takes precedence over keychain credentials; ignored in project and local settings. Generate with `claude setup-token`. Used for the whole session; to replace an expired token, generate a new one and restart. |
| `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` | claude.ai refresh token; `claude auth login` exchanges it directly instead of opening a browser. Requires `CLAUDE_CODE_OAUTH_SCOPES`. Works once (the exchange replaces it). Ignored in project and local settings. |
| `CLAUDE_CODE_OAUTH_SCOPES` | Space-separated scopes the refresh token was issued with, for example `"user:profile user:inference user:sessions:claude_code"`. Required with the refresh token. |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | Interval in ms at which credentials are refreshed when `apiKeyHelper` is used. |

# Notes

See the authentication page's "authentication precedence" for how these combine.
