---
type: "Reference"
title: "SDK authentication and third-party providers"
description: "How the SDK reads ANTHROPIC_API_KEY and which environment variables select Bedrock, Vertex, Foundry or Claude Platform on AWS."
resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
tags: [authentication, api-key, providers, environment]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ANTHROPIC_API_KEY"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "ANTHROPIC_AWS_WORKSPACE_ID"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_USE_FOUNDRY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-quickstart"
    resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK reads its credentials from the environment of the process that runs the agent. It does not load `.env` files automatically; load them yourself (for example with the `dotenv` package) before calling the SDK.

# How to use it

| Variable | Kind | What it does |
| - | - | - |
| `ANTHROPIC_API_KEY` | env_var | API key from the Claude Console |
| `CLAUDE_CODE_USE_BEDROCK=1` | env_var | Use Amazon Bedrock; configure AWS credentials |
| `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` plus `ANTHROPIC_AWS_WORKSPACE_ID` | env_var | Use Claude Platform on AWS; configure AWS credentials |
| `CLAUDE_CODE_USE_VERTEX=1` | env_var | Use Google Cloud's Agent Platform; configure Google Cloud credentials |
| `CLAUDE_CODE_USE_FOUNDRY=1` | env_var | Use Microsoft Foundry; configure Azure credentials |

# Limits and defaults

Unless previously approved, Anthropic does not allow third-party developers to offer claude.ai login or rate limits in their products, including agents built on the Agent SDK. Use the API key methods above. Authentication errors such as `Not logged in` or `Invalid API key` usually mean the key is not set in the shell running the agent.
