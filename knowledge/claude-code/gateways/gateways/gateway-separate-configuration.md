---
type: "Reference"
title: "What a gateway does not control"
description: "Model choice, non-gateway network traffic, client telemetry, corporate proxies and telemetry destinations are configured outside the gateway."
resource: "https://code.claude.com/docs/en/gateways"
tags: [gateway, telemetry, proxy, model-selection]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/model"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_TELEMETRY"
  - "HTTPS_PROXY"
  - "NO_PROXY"
  - "availableModels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gateways"
    resource: "https://code.claude.com/docs/en/gateways"
    title: "Run Claude Code through a gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A gateway routes model API requests only. These things are configured elsewhere.

# How to use it

| Topic | What the page says |
| - | - |
| Which model answers | Chosen with `/model` or model environment variables; the gateway decides where requests go, not which model. Claude apps gateway can bound the choice with per-group `availableModels`. |
| Other network traffic | Version checks and downloads go straight to Anthropic. Allow the required domains, or set `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` to stop the optional streams. |
| Client telemetry (Claude apps gateway) | Anthropic-bound client analytics are disabled once a session signs in. To also stop pre-sign-in startup analytics, deliver `DISABLE_TELEMETRY` in client-side managed settings on each device. |
| Client telemetry (other gateways) | Depends on the provider; see the data-usage telemetry defaults table. |
| Telemetry destinations | Depend on how the session signed in. |
| Corporate HTTP proxies | Requests, including to the gateway, go through `HTTPS_PROXY`. For a self-hosted Claude apps gateway behind the proxy, sign-in needs the proxy hostname to resolve to private addresses, or the gateway host in `NO_PROXY`. |
