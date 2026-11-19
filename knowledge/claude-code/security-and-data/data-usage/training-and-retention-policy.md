---
type: "Reference"
title: "Data training and retention policies"
description: "Training policy by plan, Development Partner Program, retention periods, local transcript caching and cleanupPeriodDays."
resource: "https://code.claude.com/docs/en/data-usage"
tags: [data, retention, training, privacy, transcripts]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "cleanupPeriodDays"
  - "~/.claude/projects/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "data-usage"
    resource: "https://code.claude.com/docs/en/data-usage"
    title: "Data usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Policy summary by account type.

# How to use it

| Account type | Training | Retention |
| - | - | - |
| Consumer (Free, Pro, Max, Ultra) | Training happens when the setting is on, including Claude Code use | 5 years if data use allowed; 30 days if not; changeable at claude.ai/settings/data-privacy-controls |
| Commercial (Team, Enterprise, API, third-party platforms, Claude Gov) | No training on code or prompts under commercial terms unless the customer opts in (e.g. Developer Partner Program) | Standard 30 days; zero data retention available to qualified Claude for Enterprise accounts, enabled per organization by the account team |

- Development Partner Program: an org admin can opt in; first-party API only, not Amazon Bedrock or Google Cloud's Agent Platform.
- Local caching: clients store session transcripts in plaintext under `~/.claude/projects/` for 30 days by default to enable resume; adjust with `cleanupPeriodDays`. Transcripts of sessions started or last continued in Claude Desktop or Cowork are exempt from that limit by default.
- Cloud sessions can be deleted at any time, permanently removing the session's event data.
- `/feedback`, `/bug` and `/share` transcripts are retained 5 years.
