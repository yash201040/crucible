---
type: "Feature"
title: "Turning telemetry off for an organization"
description: "Deliver DISABLE_TELEMETRY through managed env to stop Anthropic operational telemetry, with side effects on analytics and feature flags."
resource: "https://code.claude.com/docs/en/managed-settings#turn-telemetry-off-for-your-organization"
tags: [telemetry, env, privacy, managed-settings]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "DISABLE_TELEMETRY"
  - "env"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "managed-settings"
    resource: "https://code.claude.com/docs/en/managed-settings"
    title: "Deploy managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code sends Anthropic operational telemetry by default on sessions using the Anthropic API (direct, through an LLM gateway, or custom `ANTHROPIC_BASE_URL`).

# How to use it

```json
{ "env": { "DISABLE_TELEMETRY": "1" } }
```

Applied without the approval dialog when the value is `1`.

# Limits and defaults

- Turning it off stops the usage data feeding the organization's analytics dashboard for affected developers, and also turns off feature-flag fetching.
- Customer-managed-encryption-key orgs routing through a gateway need this variable (see third-party-integrations).
