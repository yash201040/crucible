---
type: "Feature"
title: "allowedProviders"
description: "Managed allowlist of model providers a machine may use, refused at startup, login and next API contact."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, providers, managed, policy]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, sdk, desktop]
requires: "Managed settings"
identifiers:
  - "allowedProviders"
  - "anthropic"
  - "bedrock"
  - "vertex"
  - "foundry"
  - "anthropicAws"
  - "anthropicGoogleCloud"
  - "mantle"
  - "customEndpoint"
  - "gateway"
  - "AWS_ENDPOINT_URL"
  - "AWS_ENDPOINT_URL_BEDROCK"
  - "AWS_ENDPOINT_URL_BEDROCK_RUNTIME"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope array of strings (default unset: any provider). A session on an unlisted provider is refused at startup, at login and on next API contact, so mid-session switching is refused too. Needs v2.1.285+.

# How to use it

`{ "allowedProviders": ["anthropic", "bedrock"] }`

| Value | Provider |
| :- | :- |
| `"anthropic"` | Anthropic API on Anthropic's host (claude.ai or Console sign-in or API key); Desktop's Cowork on the user's machine counts as this when signed in to claude.ai |
| `"bedrock"` | Amazon Bedrock |
| `"vertex"` | Google Cloud's Agent Platform (formerly Vertex AI) |
| `"foundry"` | Microsoft Foundry |
| `"anthropicAws"` | Claude Platform on AWS |
| `"anthropicGoogleCloud"` | Claude Models on Google Cloud (Anthropic managed) |
| `"mantle"` | Amazon Bedrock Mantle endpoint; list `"bedrock"` and `"mantle"` together for a session running both |
| `"customEndpoint"` | Anthropic or cloud API sent to another host such as an LLM gateway (`ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`); admitted only for the exact value a managed `env` block pins |
| `"gateway"` | Cloud gateway sign-in |

# Limits and defaults

- Unrecognized entries are dropped and reported; with an empty list or all entries unrecognized, every provider is refused and Claude Code does not start.
- Machine admin sources (MDM, managed files) keep applying when server-managed settings also deliver a list: only providers on both lists work (server-managed can narrow, never widen).
- Pins: custom endpoints, Bedrock `AWS_ENDPOINT_URL`, `AWS_ENDPOINT_URL_BEDROCK`, `AWS_ENDPOINT_URL_BEDROCK_RUNTIME` pointing outside Bedrock, and a gateway URL (`forceLoginGatewayUrl` counts as pin) must equal a value set in a managed `env` block. If a machine admin source sets the list, only machine admin `env` blocks count; if only server-managed settings set it, their `env` counts too.
- The list does not judge credentials, tenancy variables or network path (`HTTPS_PROXY`, certificates); set those in managed `env`.
