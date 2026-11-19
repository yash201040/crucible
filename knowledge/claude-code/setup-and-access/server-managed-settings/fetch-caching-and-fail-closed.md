---
type: "Feature"
title: "Fetch, caching and fail-closed startup"
description: "How server-managed settings are fetched, cached for 24 hours, withheld env categories, and forceRemoteSettingsRefresh."
resource: "https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior"
tags: [server-managed, caching, fail-closed, env]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.223"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "forceRemoteSettingsRefresh"
  - "~/.claude/remote-settings.json"
  - "modelPricing"
  - "managedMcpServers"
  - "allowedProviders"
  - "HTTPS_PROXY"
  - "claude --debug-file <path>"
  - "claude auth login"
  - "companyAnnouncements"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "server-managed-settings"
    resource: "https://code.claude.com/docs/en/server-managed-settings"
    title: "Configure server-managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code fetches at startup and polls hourly during active sessions, sending `Cache-Control: no-cache`. Gateway-signed-in clients fetch from the gateway and wait before the session starts; a failed gateway fetch exits (a `401` on an attended interactive launch without the force setting prints `Cloud gateway session expired — run /login to reconnect.` and opens signed out).

# How to use it

- First launch without cache: waits up to five seconds when signing in at startup; otherwise opens while the fetch continues (brief unrestricted window). Fetch failure: continues without remote settings and warns (interactive and Desktop Code tab); endpoint-managed settings still apply.
- Later launches: cached settings apply immediately, except cached `modelPricing` (cost figures at list price until confirmed), cached `managedMcpServers` (waits up to 30 seconds for confirmation; failure starts without them), withheld `env` categories, and plugin-guard changes. Cache expires 24 hours after last successful fetch.
- Withheld cached `env` categories until server confirms: proxy/TLS (`HTTPS_PROXY`, `NODE_EXTRA_CA_CERTS`, `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`), routing/provider (`ANTHROPIC_BASE_URL`, `CLAUDE_CODE_USE_*`, provider endpoint URLs), credentials (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`), `CLAUDE_CONFIG_DIR`, and from v2.1.223 federation variables, `ANTHROPIC_PROFILE`, `ANTHROPIC_CONFIG_DIR`, `HOME`, `XDG_CONFIG_HOME`, `APPDATA`, `USERPROFILE`. Federation/profile selectors are read only at startup, so deliver them through endpoint-managed settings. If the fetch needs a proxy, set `HTTPS_PROXY` in endpoint-managed `env` (v2.1.223+), shell, or user settings.
- Fail closed: `"forceRemoteSettingsRefresh": true` blocks startup until a fresh fetch and exits on failure; `claude auth` subcommands are exempt; needs connectivity to `api.anthropic.com`. Also honored from any admin source (MDM/file) for first-launch enforcement; a server-delivered value is read from cache on later startups.

# Limits and defaults

- Anthropic can require settings before a session starts (sign-in expired, or no settings and no recent cache); message contains `before a session can start` or `Your Claude session has expired`.
- Updates applying only at next launch include OpenTelemetry exporter config, `model`, and removal of a `env` variable.
- Invalid entries (v2.1.169+): valid remainder applies; if every setting fails and none falls back to stricter, nothing applies, cache unchanged, failure reported as `no setting in the server response could be applied as written`. Debug: `claude --debug-file <path>` and search `Remote settings`.
- If the selected source is an MDM/file source with a `policyHelper`, the helper is not consulted while server-managed settings deliver a policy key; it runs immediately if a later fetch finds them removed.
- `apiKeyHelper` in machine policy is not in effect when server-managed is selected; refusal `Claude Code didn't send your claude.ai login` needs v2.1.314+.
