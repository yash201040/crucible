---
type: "Guide"
title: "HIPAA sample managed settings keys"
description: "Sample managed settings (forceLoginMethod, forceLoginOrgUUID, allowedProviders, cleanupPeriodDays) and sessions they do not block."
resource: "https://code.claude.com/docs/en/hipaa-setup"
tags: [hipaa, managed-settings, login, allowed-providers]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, desktop]
requires: "allowedProviders needs v2.1.285; requiredMinimumVersion needs v2.1.163"
identifiers:
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "allowedProviders"
  - "cleanupPeriodDays"
  - "requiredMinimumVersion"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hipaa-setup"
    resource: "https://code.claude.com/docs/en/hipaa-setup"
    title: "Set up Claude Code (local mode) for a HIPAA-ready organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A recommended starting sample that applies whether or not the HIPAA configuration is in effect:

```json
{ "forceLoginMethod": "claudeai",
  "forceLoginOrgUUID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "allowedProviders": ["anthropic"],
  "cleanupPeriodDays": 30 }
```

A fuller `managed-settings.json` (sandboxing, network allowlist, credential protections) is `settings-hipaa.json` with `README-hipaa.md` in the settings examples of the claude-code repository.

# How to use it

| Key | Value | Enforcement |
| - | - | - |
| `forceLoginMethod` | `"claudeai"` | Directs sign-in to claude.ai instead of Console |
| `forceLoginOrgUUID` | Org ID | Exits at startup when the claude.ai sign-in is another organization (a wrong value exits for every claude.ai developer) |
| `allowedProviders` | `["anthropic"]` | Refuses to start on a cloud provider or gateway |
| `cleanupPeriodDays` | days | Every computer deletes old session data after that many days; managed value overrides the developer's |

# Limits and defaults

- With `forceLoginMethod` or `forceLoginOrgUUID`, sessions using `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` are also refused.
- Not blocked: Console sign-ins and federation credentials (`forceLoginOrgUUID` checks only claude.ai); server-managed settings need the same keys added by an Owner; versions before v2.1.285 ignore `allowedProviders` (v2.1.163 to v2.1.284 can be made to refuse with `requiredMinimumVersion` `"2.1.285"`; before v2.1.163 ignore both).
- Verify: `/status` `Setting sources` lists `Enterprise managed settings`, and `Allowed providers` reads `Anthropic API (managed allowedProviders)`.
- Claude Desktop sign-in restriction is configured separately in the Desktop policy.
