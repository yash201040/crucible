---
type: "Reference"
title: "Endpoint override, custom headers and beta headers"
description: "Variables that route Claude Code requests through a proxy or gateway and add custom or anthropic-beta headers."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [gateway, headers, base-url, beta]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "ANTHROPIC_BETAS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Request-level routing controls for the Anthropic API.

# How to use it

| Variable | What it does |
| :- | :- |
| `ANTHROPIC_BASE_URL` | Override the API endpoint to use a proxy or gateway. As of v2.1.196, Remote Control is disabled when it points at a host other than `api.anthropic.com` (as on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry). See "Tool search through an LLM gateway" in the MCP page. |
| `ANTHROPIC_CUSTOM_HEADERS` | Extra request headers in `Name: Value` format, newline-separated. A name or value with a character HTTP headers cannot carry (curly quote, zero-width space) fails the request with an error naming the pair by position (requires v2.1.227+). Credential, org/tenant, routing or API-behavior headers such as `Authorization` or `Host` count as a setting needing approval when server-managed settings deliver them. |
| `ANTHROPIC_BETAS` | Comma-separated extra `anthropic-beta` header values, to opt into an API beta before native support. Unlike the `--betas` flag (API key auth only), it works with all auth methods including claude.ai subscription. |
