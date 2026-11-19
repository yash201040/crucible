---
type: "Feature"
title: "Fast mode overview"
description: "A faster configuration of supported models, up to 2.5x faster at higher per-token cost, toggled with /fast."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, models, latency, cost]
kind: "slash_command"
maturity: "research-preview"
since: ""
surfaces: [cli, ide, cloud]
requires: "Fable 5.2, Opus 5.5, Opus 5 or Opus 4.8; subscription with usage credits, Console, or Agent Platform"
identifiers:
  - "/fast"
  - "fastMode"
  - "↯"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fast mode is the same model with an API configuration that prioritizes speed over cost: up to 2.5x faster, higher per-token price, same quality and capabilities. Supported on the Anthropic API: Fable 5.2, Opus 5.5, Opus 5, Opus 4.8. Not Sonnet, Haiku or others. Fast mode for Fable 5.2 and Opus 5.5 is available; for Opus 5 and Opus 4.8 it is a research preview (may change; availability, pricing and the underlying configuration subject to change).

# How to use it

Best for interactive work where latency matters more than cost: rapid iteration, live debugging, tight deadlines. Standard mode is better for long autonomous tasks, batch or CI/CD, and cost-sensitive work. Combine with a lower effort level for maximum speed on easy tasks (fast mode keeps quality and cuts latency; lower effort trades thinking time, possibly quality).

# Limits and defaults

- Opus 4.8 fast mode was deprecated October 30, 2026 and will be removed November 30, 2026; afterwards the API rejects requests with fast mode on Opus 4.8. Switch to Opus 5.5 with `/model` (needs v2.1.280+; fast mode stays on) or run `/fast off`.
- Opus 4.7 does not support fast mode (switching to it turns it off); its fast mode was deprecated June 25, 2026 and removed July 24, 2026.
- Fast mode usage on subscription plans is via usage credits only, not included in plan rate limits.
- Details: [toggling](./toggle-fast-mode.md), [cost](./fast-mode-cost.md), [requirements](./fast-mode-requirements.md).
