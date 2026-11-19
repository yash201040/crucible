---
type: "Concept"
title: "Teams and Enterprise allowance and spend caps"
description: "Per-seat usage windows, spend report, usage credits and limits, and the Enterprise Analytics API for Claude for Teams and Enterprise."
resource: "https://code.claude.com/docs/en/costs"
tags: [teams, enterprise, seat-allowance, usage-credits, admin]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "Claude for Teams or Enterprise"
identifiers:
  - "read:analytics"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each member's usage draws from a per-seat allowance that resets on a rolling five-hour window and a weekly window. The allowance is shared with Claude chat and Cowork; its size depends on seat tier (Standard or Premium). Controls are in the claude.ai admin console, not the Claude Console.

# How to use it

- See spend: spend report in org analytics shows estimated spend per user and per model, CSV export, updated daily. It covers usage-credit spend and appears once usage credits are on; usage inside the seat allowance is not metered in dollars.
- See adoption: the analytics dashboard (daily active users, sessions, contribution metrics).
- Cap spend: the seat allowance is the default ceiling; turn on usage credits and set spend limits at organization, group or individual level.
- Per-user numbers: Enterprise Analytics API (Primary Owner creates a `read:analytics` key at claude.ai/analytics/api-keys); on Teams export the spend report CSV.

# Notes

The Claude Enterprise consumption guide is the admin planning reference; a coding seat needs more budget than a chat seat.
