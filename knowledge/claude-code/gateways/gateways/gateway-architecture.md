---
type: "Concept"
title: "How a gateway sits between Claude Code and the provider"
description: "A gateway is an organization-run proxy that holds the provider credential, so developers authenticate to it and usage, budgets and audit live in one place."
resource: "https://code.claude.com/docs/en/gateways"
tags: [gateway, proxy, credentials, architecture]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gateways"
    resource: "https://code.claude.com/docs/en/gateways"
    title: "Run Claude Code through a gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A gateway is a proxy the organization runs between Claude Code and a model provider. Claude Code sends API traffic to the gateway; the gateway forwards it with a credential the organization holds. Authentication, usage tracking, budgets and audit logging then happen in one place.

# How it works

- Two credentials are involved: a per-developer credential issued by the gateway (authenticates and identifies the developer in usage tracking) and one provider credential held by the gateway and shared by all forwarded traffic.
- The upstream can be the Anthropic API or a cloud provider (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry); the gateway configuration decides.
- With Claude apps gateway, or another gateway exposing a single Anthropic-format endpoint, changing provider needs no change on developer machines.

# Notes

The page links onward to [Claude apps gateway](./claude-apps-gateway-overview.md), [other gateways](../llm-gateway/other-gateways-overview.md) and the admin setup guide.
