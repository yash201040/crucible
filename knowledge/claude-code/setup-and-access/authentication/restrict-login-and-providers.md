---
type: "Feature"
title: "Restricting login method, organization and provider"
description: "forceLoginMethod, forceLoginOrgUUID and allowedProviders in managed settings, and which login paths enforce them."
resource: "https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization"
tags: [managed-settings, login, organization, providers]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, ide, sdk]
requires: "v2.1.212+ for method enforcement on all paths; v2.1.285+ for allowedProviders"
identifiers:
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "allowedProviders"
  - "customEndpoint"
  - "claude setup-token"
  - "/install-github-app"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "apiKeyHelper"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "authentication"
    resource: "https://code.claude.com/docs/en/authentication"
    title: "Authentication"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`forceLoginMethod` (`"claudeai"`, `"console"`, `"gateway"`) and `forceLoginOrgUUID` (org ID or array) govern which account a session uses; `allowedProviders` lists services a managed machine may reach Claude through.

# How to use it

```json
{ "forceLoginMethod": "claudeai",
  "forceLoginOrgUUID": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"],
  "allowedProviders": ["anthropic", "bedrock"] }
```

- Terminal, VS Code extension and Agent SDK logins verify `forceLoginOrgUUID` for claude.ai logins; `claude setup-token` and `/install-github-app` enforce only `forceLoginMethod`. Gateway sign-in is selected by `forceLoginMethod: "gateway"` and not org-checked.
- The terminal login screen only pre-selects the method, so a Console login can still complete there.
- Console logins: `forceLoginOrgUUID` only pre-selects the org when a single ID is set; no credential org check.
- An LLM gateway or proxy: list `"customEndpoint"` and pin the URL in managed `env`.
- Deploy login keys through device management; server-managed settings arrive only after login, so they cannot redirect a first login. Set both keys in server-managed settings as well until every client is v2.1.299+.

# Limits and defaults

- With either key set: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` sessions are blocked at startup. Cloud-provider sessions are blocked only while one of those or a saved Console key exists. Profile/federation credentials are not org-checked.
- `allowedProviders`: unlisted providers are refused at startup and on the next request. A list set only in server-managed settings reaches only sessions that fetch settings, so it is not enforcement.
- Keep these keys out of settings a gateway serves.
