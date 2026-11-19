---
type: "Reference"
title: "Cloud provider selection and auth-skip switches"
description: "Variables that choose Bedrock, Foundry, Vertex, Mantle or the AWS and Google Cloud Anthropic platforms, and skip client-side auth for gateways."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [providers, bedrock, vertex, foundry]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "CLAUDE_CODE_USE_MANTLE"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH"
  - "CLAUDE_CODE_SKIP_ANTHROPIC_GOOGLE_CLOUD_AUTH"
  - "CLAUDE_CODE_SKIP_BEDROCK_AUTH"
  - "CLAUDE_CODE_SKIP_FOUNDRY_AUTH"
  - "CLAUDE_CODE_SKIP_MANTLE_AUTH"
  - "CLAUDE_CODE_SKIP_VERTEX_AUTH"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches that pick the model provider, and switches that drop client-side authentication when a gateway signs requests itself.

# How to use it

| Variable | Selects / skips |
| :- | :- |
| `CLAUDE_CODE_USE_ANTHROPIC_AWS` | Use Claude Platform on AWS |
| `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD` | Use Claude Models on Google Cloud (Anthropic managed) |
| `CLAUDE_CODE_USE_BEDROCK` | Use Amazon Bedrock |
| `CLAUDE_CODE_USE_FOUNDRY` | Use Microsoft Foundry |
| `CLAUDE_CODE_USE_MANTLE` | Use the Amazon Bedrock Mantle endpoint |
| `CLAUDE_CODE_USE_VERTEX` | Use Google Cloud's Agent Platform |
| `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH` | Skip client auth for Claude Platform on AWS (gateway signs requests) |
| `CLAUDE_CODE_SKIP_ANTHROPIC_GOOGLE_CLOUD_AUTH` | Skip Google Cloud auth for Claude Models on Google Cloud (gateway attaches credentials) |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Skip AWS auth for Bedrock (for example behind an LLM gateway) |
| `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` | Skip Azure auth for Foundry; preserves a supplied `Authorization` header. Ignored when `ANTHROPIC_FOUNDRY_API_KEY` or `ANTHROPIC_FOUNDRY_AUTH_TOKEN` is set. Before v2.1.203 the client could not send requests unless an API key was also set. |
| `CLAUDE_CODE_SKIP_MANTLE_AUTH` | Skip AWS auth for Bedrock Mantle |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH` | Skip Google auth for Google Cloud's Agent Platform |

# Notes

A stale `USE_*` variable from a shell profile can be neutralized with an empty string in the settings `env` block (see precedence). `CLAUDE_CODE_ENABLE_AUTO_MODE` and `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` are covered elsewhere.
