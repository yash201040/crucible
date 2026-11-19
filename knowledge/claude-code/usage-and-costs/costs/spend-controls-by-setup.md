---
type: "Reference"
title: "Where to see and cap spend by setup"
description: "Table mapping Teams/Enterprise, Console and cloud-provider setups to spend visibility, caps and per-user reporting."
resource: "https://code.claude.com/docs/en/costs"
tags: [cost, spend-limits, organization, reporting, opentelemetry]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: ""
identifiers:
  - "read:analytics"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cost controls depend on how the organization accesses Claude Code. On Teams/Enterprise, usage draws from each member's seat allowance. On the Console and cloud providers, usage is billed per token. If sign-in methods are mixed, each developer is metered by the one they authenticated with. Reference averages: about $13 per developer per active day, $150-250 per developer per month, below $30 per active day for 90% of users.

# How to use it

| Setup | See spend | Cap spend | Per-user reporting |
| - | - | - | - |
| Claude for Teams or Enterprise | Spend report in org analytics | Spend limits in admin settings | Spend report CSV; Enterprise Analytics API (Enterprise) |
| Claude Console (API) | Console Cost page | Workspace spend limits | Console dashboard; Claude Code Analytics API |
| Bedrock, Google Cloud's Agent Platform, Microsoft Foundry | Cloud billing console | Cloud budget controls | OpenTelemetry or an LLM gateway |

OpenTelemetry export works on every setup and is the only option that streams per-user token and cost metrics into your own stack in near real time.

# Notes

Individual Pro/Max/Ultra users track their own usage-credit spend (including fast mode) via /usage.
