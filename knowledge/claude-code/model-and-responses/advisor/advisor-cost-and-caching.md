---
type: "Concept"
title: "Advisor cost and prompt caching"
description: "Advisor tokens bill at the advisor model's rates; toggling the advisor does not invalidate the main model's prompt cache."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, cost, prompt-caching, usage]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/usage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each advisor call has the advisor model read the whole conversation, consuming tokens at the advisor's rates on top of the main model's usage.

# Limits and defaults

- API billing: advisor model's input and output rates.
- Subscription plans: counts toward plan usage limits, except a Fable advisor bills to usage credits on plans where Fable usage does.
- Advisor usage counts in the session totals shown by `/usage`. API responses report advisor tokens as described in the Claude API advisor-tool docs ("Usage and billing").
- Claude calls the advisor at decision points, so a faster main model with a stronger advisor typically costs less than the stronger model throughout.
- Caching: enabling or disabling the advisor mid-session does not invalidate the main model's prompt cache (unlike switching models); the advisor's guidance is cached as part of the transcript on later turns. The advisor's own read of the conversation is not cached: each call processes the full transcript anew.
