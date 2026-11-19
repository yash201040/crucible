---
type: "Reference"
title: "Fast mode pricing and where spend shows"
description: "Per-MTok fast mode rates by model, the uncached-context charge when first enabled, and where to see the spend."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, pricing, cost, prompt-caching]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "/status"
  - "/usage"
  - "/usage-credits"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fast mode has higher per-token pricing than standard speed. Pricing is flat across the full 1M-token context window.

# How to use it

| Model | Input (MTok) | Output (MTok) |
| - | - | - |
| Fable 5.2 | $16 | $80 |
| Opus 5.5 | $8 | $40 |
| Opus 5 | $10 | $50 |
| Opus 4.8 | $10 | $50 |

Where spend appears (run `/status`: a `Login method` row means subscription; an `API key` row means a Console organization):
- Pro, Max, Ultra: paid from usage credits; Settings > Usage on claude.ai shows total credit spend (fast mode not broken out).
- Team, Enterprise: the organization pays from its usage credits; `/usage` shows your own spend.
- Claude Console: billed with other API usage; on the Usage and Cost pages choose **Speed** in **Group by** (shown only when the range includes fast mode usage).

# Limits and defaults

The first time you enable fast mode in a conversation you pay the full uncached fast input price for the whole context, so enabling early is cheapest. Fast mode and standard speed keep separate prompt caches, so each later switch reads some or all of the conversation uncached again.
