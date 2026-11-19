---
type: "Reference"
title: "Route to a cloud provider through a gateway"
description: "Provider-specific base URL and skip-auth variables for Bedrock, Agent Platform, Foundry and Claude Platform on AWS gateways."
resource: "https://code.claude.com/docs/en/llm-gateway-connect"
tags: [gateway, bedrock, vertex, foundry, env]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.203"
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "CLAUDE_CODE_SKIP_BEDROCK_AUTH"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "AWS_BEARER_TOKEN_BEDROCK"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "CLAUDE_CODE_SKIP_VERTEX_AUTH"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLOUD_ML_REGION"
  - "VERTEX_REGION_CLAUDE_*"
  - "ANTHROPIC_FOUNDRY_BASE_URL"
  - "ANTHROPIC_FOUNDRY_API_KEY"
  - "ANTHROPIC_FOUNDRY_AUTH_TOKEN"
  - "CLAUDE_CODE_SKIP_FOUNDRY_AUTH"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "ANTHROPIC_AWS_BASE_URL"
  - "ANTHROPIC_AWS_WORKSPACE_ID"
  - "CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-connect"
    resource: "https://code.claude.com/docs/en/llm-gateway-connect"
    title: "Connect Claude Code to an LLM gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Use only when the gateway team names a provider. Bedrock and Agent Platform gateways accept those providers' native formats (Claude Code limits beta headers and fields to what they accept); Foundry and Claude Platform on AWS gateways accept the Anthropic Messages format. Skip skip-auth variables tell Claude Code not to sign with cloud credentials because the gateway holds them.

# How to use it

| Provider | Variables to set |
| - | - |
| Amazon Bedrock | `ANTHROPIC_BEDROCK_BASE_URL`, `CLAUDE_CODE_SKIP_BEDROCK_AUTH=1`, `CLAUDE_CODE_USE_BEDROCK=1`. Leave `AWS_BEARER_TOKEN_BEDROCK` unset, otherwise it is sent as `Authorization` instead of the gateway token. |
| Google Cloud's Agent Platform | `ANTHROPIC_VERTEX_BASE_URL`, `ANTHROPIC_VERTEX_PROJECT_ID`, `CLAUDE_CODE_SKIP_VERTEX_AUTH=1`, `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION`. Project and region go into each request path. Per-model regions via `VERTEX_REGION_CLAUDE_*` (for example `VERTEX_REGION_CLAUDE_4_6_SONNET`). |
| Microsoft Foundry | `ANTHROPIC_FOUNDRY_BASE_URL`, `ANTHROPIC_FOUNDRY_API_KEY` (sent as `x-api-key`) or `ANTHROPIC_FOUNDRY_AUTH_TOKEN` (bearer, wins when both set; v2.1.203 or later), `CLAUDE_CODE_USE_FOUNDRY=1`. For a gateway injecting its own `Authorization`: `CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1` with both credential variables unset. |
| Claude Platform on AWS | `ANTHROPIC_AWS_BASE_URL`, `ANTHROPIC_AWS_WORKSPACE_ID`, `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH=1`, `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` |

- For Bedrock, Agent Platform or Claude Platform on AWS, add `ANTHROPIC_AUTH_TOKEN` after the block for a bearer credential (keep the skip-auth variable, else Claude Code removes any `Authorization` header). Other schemes: `ANTHROPIC_CUSTOM_HEADERS`.
- Pin `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`; setting the Haiku one also moves background tasks such as session titles. Declare unknown pinned models' abilities with `ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES` and Sonnet/Haiku counterparts.
- `/status` shows rows such as `API provider: Amazon Bedrock`, `Bedrock base URL`, `AWS auth skipped` (`Vertex base URL`, `GCP auth skipped` for Agent Platform).
