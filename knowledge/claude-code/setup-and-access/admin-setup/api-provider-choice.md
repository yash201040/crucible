---
type: "Concept"
title: "Choosing an API provider"
description: "Which provider Claude Code authenticates through (Teams/Enterprise, Console, Bedrock, Vertex, Foundry) and which features need a claude.ai account."
resource: "https://code.claude.com/docs/en/admin-setup"
tags: [admin, providers, billing, claude-ai-account]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "admin-setup"
    resource: "https://code.claude.com/docs/en/admin-setup"
    title: "Set up Claude Code for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The provider decides billing, authentication, inherited compliance posture and which Claude Code features developers get.

# How to use it

| Provider | Choose when |
| :- | :- |
| Claude for Teams / Enterprise | One per-seat subscription, no infrastructure; the default recommendation |
| Claude Console | API-first, pay-as-you-go |
| Amazon Bedrock | Inherit AWS compliance and billing |
| Google Cloud's Agent Platform | Inherit GCP compliance and billing |
| Microsoft Foundry | Inherit Azure compliance and billing |

A single endpoint in front of several providers, or centralized request logging, is done with an LLM gateway. Network/proxy rules apply regardless of provider.

# Limits and defaults

- Cloud sessions, cloud scheduled tasks, Code Review, Remote Control and the Chrome extension are not available through Console API keys or cloud-provider credentials alone; they need a claude.ai account (Teams/Enterprise seats if deploying on Bedrock, Vertex or Foundry).
- Each feature page lists its own plan requirements.
