---
type: "Limit"
title: "Ultrareview pricing and free runs"
description: "Ultrareview is billed as usage credits after 3 one-time free runs on Pro, Max and Ultra."
resource: "https://code.claude.com/docs/en/ultrareview"
tags: [pricing, usage-credits, free-runs, cost]
kind: "limit"
maturity: "research-preview"
since: ""
surfaces: [cli, cloud]
requires: "Pro, Max or Ultra plan; usage credits turned on for paid runs"
identifiers:
  - "/usage-credits"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "ultrareview"
    resource: "https://code.claude.com/docs/en/ultrareview"
    title: "Find bugs with ultrareview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ultrareview is a premium feature billed against usage credits, not the plan's included usage.

# How to use it

| Plan | Free runs | After |
| - | - | - |
| Pro | 3 | usage credits |
| Max | 3 | usage credits |
| Ultra | 3 | usage credits |

Run `/usage-credits` to check or change the usage-credits setting. If credits are off, Claude Code blocks a paid launch and links to billing settings if the user can manage billing.

# Limits and defaults

- The 3 free runs are a one-time allotment per account and do not refresh.
- After free runs: typically $5 to $25 per review depending on change size, matching the launch dialog estimate.
- A run counts once the cloud session starts. A review stopped early or failed still uses a free run; a paid review bills only for the portion that ran.
- Billing confirmation is asked once per conversation; `/clear` starts a new conversation and asks again.
