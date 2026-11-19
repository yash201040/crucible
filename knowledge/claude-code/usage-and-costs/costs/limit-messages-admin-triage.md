---
type: "Reference"
title: "Which limit a developer hit"
description: "How to tell session/weekly seat limits, usage-credit spend limits, gateway caps and context warnings apart, with remedies."
resource: "https://code.claude.com/docs/en/costs"
tags: [limits, errors, usage-credits, autocontinue, admin]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: ""
identifiers:
  - "/model"
  - "/usage-credits"
  - "/rate-limit-options"
  - "autoContinueAtUsageLimit"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Different messages mean different ceilings.

# How to use it

| Message | Meaning and remedy |
| - | - |
| "You've hit your session limit" / "weekly limit" | Seat-based usage window shared across all models; switching with `/model` does not help. Message shows reset time. Use `/usage-credits` if credits are on, or wait and continue automatically (v2.1.234+) |
| "You've hit your Opus limit" / "Sonnet limit" | Model-specific; switching to a model outside that family with `/model` keeps work going |
| "individual spend limit", "org's monthly spend limit", "team's shared budget" | Usage credits reached a spend limit; admin raises the limit in Organization settings > Usage; or wait for the plan reset time if named |
| Spend limit from a Claude apps gateway | Self-hosted gateway cap passed; blocked until raised, or until the cap resets if above $0 |
| Context or auto-compact warning | Not a usage limit; conversation is near the auto-compact window |
| Unexpectedly high API/cloud spend | Usually long uncleared sessions or Opus as default model |

On v2.1.234+ Claude Code can wait and auto-continue the interrupted task after the reset; it either starts the wait itself or the developer picks it from `/rate-limit-options`. Fleet admins control whether it starts on its own with the `autoContinueAtUsageLimit` managed setting.
