---
type: "Feature"
title: "Ultrareview overview and availability"
description: "Ultrareview is a cloud multi-agent code review launched with /code-review ultra, with account and provider restrictions."
resource: "https://code.claude.com/docs/en/ultrareview"
tags: [code-review, cloud, multi-agent, research-preview]
kind: "slash_command"
maturity: "research-preview"
since: ""
surfaces: [cli, cloud]
requires: "claude.ai account sign-in; not Bedrock, Google Cloud Agent Platform, Foundry, ZDR, HIPAA or CMEK"
identifiers:
  - "/code-review ultra"
  - "/ultrareview"
  - "/tasks"
  - "/login"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "ultrareview"
    resource: "https://code.claude.com/docs/en/ultrareview"
    title: "Find bugs with ultrareview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A deep code review that runs as a cloud session on Anthropic infrastructure. `/code-review ultra` launches a fleet of reviewer agents in a cloud sandbox; each reported finding is independently reproduced and verified. Labelled research preview: feature, pricing and availability may change. `/ultrareview` is an alias when available to the account. It runs only when the user invokes it; Claude never starts one on its own.

# How to use it

Compared with local `/code-review`:

| | `/code-review` | `/code-review ultra` |
| - | - | - |
| Target | working diff, PR, branch or path | working diff or PR |
| Runs | locally | cloud sandbox |
| Depth | scales with effort argument | multi-agent fleet with verification |
| Duration | seconds to minutes | about 5 to 15 minutes |
| Cost | normal usage | free runs, then about $5 to $25 usage credits |

The review runs as a background task: use `/tasks` to list, open or stop reviews. Stopping archives the cloud session and returns no partial findings. When done, verified findings arrive as a notification with file location and explanation.

# Limits and defaults

- Needs claude.ai authentication (run `/login` if API-key only).
- Not available with Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry, Zero Data Retention or HIPAA configuration: `/code-review ultra` then runs a local review instead. CMEK organizations cannot run it.
- If the cloud session is stopped or archived, Claude reports it stopped; if deleted or the account/org changed, "session wasn't found". After switching accounts, sign back in and `claude --resume` to re-attach a still-running review.
