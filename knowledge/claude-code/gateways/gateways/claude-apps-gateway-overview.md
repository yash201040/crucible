---
type: "Feature"
title: "Claude apps gateway (Anthropic's self-hosted gateway)"
description: "A gateway built into the claude binary with IdP sign-in, per-group model and managed-settings control, and OTLP usage metrics; no service-token flow for CI."
resource: "https://code.claude.com/docs/en/gateways"
tags: [gateway, sso, otlp, managed-settings, ci]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/login"
  - "availableModels"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gateways"
    resource: "https://code.claude.com/docs/en/gateways"
    title: "Run Claude Code through a gateway"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude apps gateway is Anthropic's self-hosted gateway, included in the `claude` binary. Upstream options: Amazon Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry or the Anthropic API. Developers sign in with the corporate identity provider through `/login`; the gateway enforces model access and managed settings by IdP group and emits OTLP usage metrics to the organization's own observability stack.

# Limits and defaults

- Built and tested with each Claude Code release, so it forwards the `anthropic-beta` values and request fields Claude Code sends; no forwarding list to maintain.
- The sign-in is a browser SSO step and there is no service-token flow. A CI pipeline with nobody to approve the sign-in cannot authenticate through it; configure those against the provider directly.
- Agent SDK sessions and `claude -p` runs on a machine where a developer has signed in use that machine's gateway session and are governed by its policies.
- A per-group `availableModels` allowlist can bound model choice; the developer still picks within it.
- A small set of features behave differently on a gateway session (see the Claude apps gateway page, not in this unit).

# Notes

Related page: claude-apps-gateway (deployment guide).
