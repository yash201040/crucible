---
type: "Feature"
title: "Usage credits row and usage-request failures"
description: "The /usage usage-credits row, the /usage-credits command by role, and how /usage behaves when the usage request is rate limited."
resource: "https://code.claude.com/docs/en/costs"
tags: [usage-credits, spend-limit, rate-limit, subscription, non-interactive]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: "claude.ai subscription sign-in via /login (not API key); v2.1.248+ for self-serve Enterprise, trials and AWS Marketplace Enterprise"
identifiers:
  - "/usage-credits"
  - "/usage"
  - "/login"
  - "-p"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Usage credits let you keep working past your plan's usage limit. `/usage` shows a usage-credits row while they are on; `/usage-credits` manages them.

# How to use it

Row contents: Pro/Max/Ultra show this month's spend against your monthly spend limit (or `Unlimited` with no spend figure if none set). Team/Enterprise show your own monthly spend against any limit that applies to you; an organization-wide limit is not shown; with usage credits off for you there is no row. A row with a spend limit shows 0% until first spend. Before v2.1.236 the row showed only on Pro, Max, Ultra and stayed hidden until you had spent something.

| Role | `/usage-credits` does |
| - | - |
| Pro, Max, Ultra | Opens Settings > Usage on claude.ai (toggle credits, balance, spend, limit) |
| Team/Enterprise with billing access | Opens Organization settings > Usage |
| Team/Enterprise without billing access | Asks to confirm, then sends request to admins (before v2.1.211 no confirmation) |

# Limits and defaults

- Not available with API key authentication. Earlier versions than v2.1.248 on the listed Enterprise setups reject it with `Unknown command: /usage-credits`.
- The confirmation exists only in interactive sessions: with `-p` and from Remote Control the command sends no request and says to use an interactive session.
- A repeat run while a request is pending says one was already sent; after an admin dismisses it a new one is sent (before v2.1.222 a dismissed request blocked new ones).
- On Pro/Max/Ultra at the spend limit with credits left, Claude Code prompts to raise or remove the limit in the CLI.
- If the usage request fails (often rate limited), `/usage` shows last-known bars loaded within the past 60 minutes with a `Showing last-known usage` note; press `r` to retry. With no snapshot it reports the endpoint is rate limited. A message like `rate limited until 3:14am` means the plan limits cannot be fetched until then, not that work is limited. Before v2.1.208 no bars were shown on such an error.
