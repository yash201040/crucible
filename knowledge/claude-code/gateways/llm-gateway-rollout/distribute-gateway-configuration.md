---
type: "Guide"
title: "Distribute gateway configuration through managed settings"
description: "Table of variables to push (base URL, credential, hint headers, discovery, beta disabling, fast mode, model pins) and managed-settings delivery caveats."
resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
tags: [gateway, managed-settings, mdm, distribution, env]
kind: "setting"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli, desktop, headless]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "apiKeyHelper"
  - "ANTHROPIC_AUTH_TOKEN"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "CLAUDE_CODE_GATEWAY_HINT_HEADERS"
  - "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS"
  - "CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_AWS_BASE_URL"
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "forceLoginGatewayUrl"
  - "wslInheritsWindowsSettings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-rollout"
    resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
    title: "Roll out an LLM gateway for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Deliver variables in the `env` block of a managed settings file pushed by MDM, registry policy or configuration management, so developers configure nothing. Otherwise hand each developer the URL, their credential, which variable to use, and any conditional variables.

# How to use it

```json
{ "env": { "ANTHROPIC_BASE_URL": "https://llm-gateway.example.com" },
  "apiKeyHelper": "/usr/local/bin/get-gateway-key" }
```

| Variable or setting | Include when |
| - | - |
| `ANTHROPIC_BASE_URL` | Always |
| `apiKeyHelper`, `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY` | Always, one of the three (the helper command authenticates to the secrets store as the local developer, so each machine gets its own key) |
| `ANTHROPIC_CUSTOM_HEADERS` | Gateway requires a tenant or routing header |
| `CLAUDE_CODE_GATEWAY_HINT_HEADERS` | Gateway reads hint headers (v2.1.273 or later) |
| `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` | Gateway serves `/v1/models` |
| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` | Bedrock or Agent Platform upstream rejects beta fields |
| `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` / `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK` | Org uses fast mode but the direct `api.anthropic.com` check fails, is intercepted, or is skipped for lack of an Anthropic credential |
| `ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Gateway routes names that differ from defaults; route both override names and the built-in IDs, since some background sub-calls request a built-in ID regardless |
| `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, `ANTHROPIC_FOUNDRY_BASE_URL`, `ANTHROPIC_AWS_BASE_URL` | Gateway fronts that provider; Bedrock and Agent Platform switch to native formats |

# Limits and defaults

- Do not combine `forceLoginMethod`, `forceLoginOrgUUID` or `forceLoginGatewayUrl` with a gateway credential: developers cannot proceed (`This machine's managed settings require a first-party login`).
- Desktop reads routing from its third-party inference configuration (deploy via MDM alongside managed settings), not managed settings.
- CI runners need base URL and credential in the runner environment.
- WSL on managed Windows reads Windows managed settings only when `wslInheritsWindowsSettings` is `true`.
- Checkpoint: `claude` starts without a login screen; `/status` shows `Anthropic base URL` and a `Setting sources` line including managed settings.
