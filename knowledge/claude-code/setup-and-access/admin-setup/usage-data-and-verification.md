---
type: "Guide"
title: "Usage visibility, data handling and verification"
description: "Monitoring, analytics and spend controls by plan, data-retention options, and how to verify managed settings with /status."
resource: "https://code.claude.com/docs/en/admin-setup"
tags: [monitoring, analytics, spend-limits, data-retention, verification]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/status"
  - "Setting sources"
  - "Enterprise managed settings"
  - "/logout"
  - "/login"
  - "claude update"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "admin-setup"
    resource: "https://code.claude.com/docs/en/admin-setup"
    title: "Set up Claude Code for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How an admin tracks spend and adoption, what data policy applies, and how to confirm policy reached a machine.

# How to use it

| Capability | What you get | Availability |
| :- | :- | :- |
| Usage monitoring | OpenTelemetry export of sessions, tools, tokens | all providers |
| Analytics dashboard | adoption metrics (Teams/Enterprise, claude.ai/analytics); per-user usage and spend (Console, platform.claude.com/claude-code) | plan-dependent |
| Programmatic reporting | per-user usage/cost API: Enterprise Analytics API (Enterprise), Claude Code Analytics API (Console) | plan-dependent |
| Spend controls | spend and rate limits: org settings (Teams/Enterprise), workspace limits (Console); cloud budget controls or a Claude apps gateway with per-user spend limits on third-party clouds | plan-dependent |

On Teams/Enterprise, per-user spend numbers come from the spend report in analytics settings, not the dashboard. Cloud spend is in AWS Cost Explorer, GCP Billing or Azure Cost Management.

Verify enforcement: run `/status`; the `Setting sources` line shows `Enterprise managed settings` followed by the winning source in parentheses.

# Limits and defaults

- Team, Enterprise, API and cloud-provider plans: Anthropic does not train on your code or prompts.
- Zero Data Retention is available to qualified Claude for Enterprise accounts. A HIPAA configuration turns some local-mode features off.
- Request-level audit logging or routing by sensitivity: place a gateway (self-hosted Claude apps gateway logs per-request with IdP identity, or another LLM gateway). Gateway sessions are not eligible for the HIPAA configuration.
- Login fixes: `/logout` then `/login`; `claude update` if the enterprise auth option is missing. "You haven't been added to your organization yet" means the seat lacks Claude Code access.
