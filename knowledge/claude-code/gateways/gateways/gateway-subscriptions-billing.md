---
type: "Concept"
title: "Gateway credentials versus claude.ai subscriptions"
description: "Gateway credential traffic bills at API rates to the provider account; setting only ANTHROPIC_BASE_URL keeps the claude.ai login and its limits."
resource: "https://code.claude.com/docs/en/gateways"
tags: [gateway, billing, subscription, credentials]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gateways"
    resource: "https://code.claude.com/docs/en/gateways"
    title: "Run Claude Code through a gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With a gateway credential, usage is billed to the organization's provider account at API rates and developers' claude.ai subscriptions are neither used nor charged.

# Limits and defaults

- Exception: setting only `ANTHROPIC_BASE_URL` with no gateway credential. Requests still route through the gateway, but a saved claude.ai login stays the active credential, so subscription limits and billing apply.
