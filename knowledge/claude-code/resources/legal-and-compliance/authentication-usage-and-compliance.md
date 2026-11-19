---
type: "Concept"
title: "Authentication rules, BAA/HIPAA and usage policy"
description: "Which credentials developers may use, usage-limit assumptions, HIPAA and Zero Data Retention coverage, and security reporting."
resource: "https://code.claude.com/docs/en/legal-and-compliance"
tags: [legal, authentication, hipaa, zero-data-retention, usage-policy]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud, mobile]
requires: "HIPAA configuration needs Claude for Enterprise with HIPAA enabled and a BAA"
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "legal-and-compliance"
    resource: "https://code.claude.com/docs/en/legal-and-compliance"
    title: "Legal and compliance"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules on credentials and compliance for Claude Code and the Agent SDK.

# How to use it

- Acceptable use: the Anthropic Usage Policy applies. Advertised usage limits for Pro, Max and Ultra assume ordinary, individual use of Claude Code and the Agent SDK.
- OAuth authentication is only for purchasers of Claude Free, Pro, Max, Ultra, Team and Enterprise plans, for ordinary use of Claude Code and other native Anthropic apps.
- Developers building products or services (including with the Agent SDK) should use API key authentication via Claude Console or a supported cloud provider. Third parties may not offer Claude.ai login in their apps, route requests through Free/Pro/Max/Ultra plan credentials for their users, or collect, store or intermediate Claude.ai credentials or session tokens. Anthropic may enforce without notice.
- Allowed: customers provisioning their own API keys or 3P credentials (dev environment, secrets manager, machine image) for their own authorized users, if usage is billed to the key owner and not resold; end users signing in to the unmodified binary with their own subscription, including on a hosting platform.

# Limits and defaults

BAA coverage when a customer has a BAA: (1) HIPAA configuration: Claude Code CLI or the Code tab in Claude Desktop with a Claude for Enterprise account, HIPAA enabled and applied to Claude Code (local mode) and Cowork (local mode); (2) Zero Data Retention (ZDR) enabled for the organization (not available to all). Under the HIPAA configuration, cloud sessions, Remote Control, Claude Code in the Claude mobile app, and Claude Code routed through a third-party cloud provider or gateway are not covered.

# Notes

Security issues are reported through HackerOne; see the Anthropic Trust Center and Transparency Hub.
