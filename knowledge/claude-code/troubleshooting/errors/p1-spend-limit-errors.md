---
type: "Reference"
title: "Spend limit errors (plan and gateway)"
description: "Monthly, individual, org, channel and team spend-limit messages, gateway spend caps and pooled budgets, and failures changing a limit."
resource: "https://code.claude.com/docs/en/errors#youve-hit-your-monthly-spend-limit"
tags: [spend-limit, budget, gateway, usage-credits, errors]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.225"
surfaces: [cli, cloud]
requires: "Usage credits; Claude apps gateway for gateway caps"
identifiers:
  - "You've hit your monthly spend limit"
  - "You've hit your individual spend limit"
  - "You've hit your org's monthly spend limit"
  - "You've hit your channel's monthly spend limit"
  - "You've hit your team's shared budget"
  - "You've hit your individual usage limit"
  - "spend limit reached"
  - "spend limit unavailable"
  - "This request exceeds your group's budget"
  - "Could not update your spend limit"
  - "Could not remove your spend limit"
  - "x-should-retry: false"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The plan's included usage cannot cover the request and the usage credits that would pay for it hit a spend limit (for example a request to a model that bills to usage credits). Words before the `·` name the limit; text after says how to raise it (no URL in cloud sessions or Remote Control).

# How to use it

- Forms: monthly, individual, org's monthly, channel's monthly (one Slack channel's budget), team's shared budget (a pooled budget for an admin-assigned group), and `usage limit` wording on organizations with usage-based billing. When a plan window ran out, the message adds a reset time and access returns then.
- Fix: Pro, Max, Ultra raise it in claude.ai Settings > Usage or `/usage-credits`; Team and Enterprise billing managers use Organization settings > Usage, others ask an admin (`/usage-credits` sends the request); channel limits are raised by an org owner or channel manager.
- Gateway (Claude apps gateway): lowercase `spend limit reached · resets Dec 1` is the operator's cap. Blocked 429s carry `x-should-retry: false`, so no retry. A date means reset at 00:00 UTC; no date means a $0 cap or a gateway before v2.1.225. From v2.1.225 until v2.1.319 on the gateway server the message named period and reset time. `This request exceeds your group's budget` means the pooled group budget is used up. `spend limit unavailable` means spend records could not be read and the request was blocked as a precaution.
- `Could not update your spend limit: <reason>`: a server-given reason will fail again if retried; without a reason it reads `... Press Enter to retry.`. Removing a limit gives `Could not remove your spend limit` from v2.1.327. Before v2.1.216 only the generic form existed.

# Limits and defaults

Under `CLAUDE_CODE_RETRY_WATCHDOG` these spend-limit 429s fail at once instead of retrying (see [Retry tuning variables](./p1-retry-tuning-variables.md)).
