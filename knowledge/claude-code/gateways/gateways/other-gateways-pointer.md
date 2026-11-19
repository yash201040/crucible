---
type: "Concept"
title: "Using a gateway product you already run"
description: "Any existing LLM or API gateway can be used; Anthropic does not endorse, maintain or audit them and does not support routing to non-Claude models."
resource: "https://code.claude.com/docs/en/gateways"
tags: [gateway, third-party, support-policy]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gateways"
    resource: "https://code.claude.com/docs/en/gateways"
    title: "Run Claude Code through a gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

If the organization already runs an LLM or API gateway, Claude Code can use it instead of Claude apps gateway. Anthropic does not endorse, maintain or audit other gateway products, and does not support routing Claude Code to non-Claude models through any gateway. A separately maintained gateway needs its forwarding rules updated as they change with each release.
