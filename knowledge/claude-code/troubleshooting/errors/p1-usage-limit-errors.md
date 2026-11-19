---
type: "Reference"
title: "Usage limit and throttle errors"
description: "Session, weekly, Opus and Sonnet limits, 1M context credits, 429 throttles and low credit balance, with recovery steps."
resource: "https://code.claude.com/docs/en/errors#usage-limits"
tags: [usage-limits, 429, rate-limits, credits, errors]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli, desktop]
requires: "Subscription plan for session and weekly limits"
identifiers:
  - "You've hit your session limit"
  - "You've hit your weekly limit"
  - "You've hit your Opus limit"
  - "You've hit your Sonnet limit"
  - "Usage credits required for 1M context"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "/usage"
  - "/usage-credits"
  - "/model"
  - "dialogExpiry"
  - "Server is temporarily limiting requests"
  - "Request rejected (429)"
  - "Credit balance is too low"
  - "the prompt to confirm went unanswered"
  - "ANTHROPIC_API_KEY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors tied to plan quota or API throttles.

# How to use it

| Message | Meaning and action |
| :- | :- |
| `You've hit your session limit` / `weekly limit` | Blocks requests until the reset time shown. Shared across all models. Usage counts against session and weekly allowances at once; a large workflow fanout can exhaust the weekly allowance before the session resets. Interactive claude.ai sessions can wait and auto-continue after reset (not offered before v2.1.234); the Desktop session-limit card has **Auto-continue when limits reset** (not on the weekly card), separate from the CLI setting **Continue automatically at usage limit** in `/config`. |
| `You've hit your Opus limit` / `Sonnet limit` | Applies to that family only; `/model` to another family keeps you working, but each model has its own prompt cache so the whole conversation is re-read with no cache hits. |
| `Usage credits required for 1M context` | Entitlement check, not exhausted quota. Use `/model` without `[1m]`, or `/usage-credits` then restart. Mid-conversation growth past 200K auto-compacts under the standard limit (before v2.1.172 it repeated on every request including `/compact`; use `/clear`). `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` removes 1M variants. |
| `the prompt to confirm went unanswered · nothing was sent` (from v2.1.324 table; Fable usage-credits consent prompt closed unanswered) | Happens in Remote Control, background sessions, agent team teammates and sessions hosted via the Agent SDK. Answer the prompt where the session runs, `/model` to a non-credit model, or raise `dialogExpiry` (or `"never"`). Before v2.1.236 Claude Code waited 60 seconds then continued on the default model. |
| `Server is temporarily limiting requests` | Short throttle unrelated to plan quota (no unified quota headers); retried automatically from v2.1.199 whichever way you authenticate. |
| `Request rejected (429)` | Rate limit on your API key, Bedrock project or Google Cloud project. Check `/status` for a stray `ANTHROPIC_API_KEY`, raise tier, and reduce concurrency (many parallel subagents) or use a smaller model for high-volume scripted runs. |
| `Credit balance is too low` | Console prepaid credits are out, or an approved `ANTHROPIC_API_KEY` is routing around a subscription; unset it and `/login`. |

Useful commands: `/usage` (plan limits and resets), `/usage-credits` (buy extra on Pro, Max, Ultra; request from admin on Team and Enterprise). A custom status line can show `rate_limits` fields; warnings such as `You've used 85% of your session limit` can appear first.

# Notes

Spend-limit variants are in [Spend limit errors](./p1-spend-limit-errors.md).
