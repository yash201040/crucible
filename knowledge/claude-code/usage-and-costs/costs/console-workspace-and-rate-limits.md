---
type: "Reference"
title: "Console workspace and rate limit recommendations"
description: "The auto-created Claude Code workspace on the Console and recommended per-user TPM and RPM by team size."
resource: "https://code.claude.com/docs/en/costs"
tags: [console, workspace, rate-limits, tpm, rpm]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: "Claude Console account"
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

API organizations manage Claude Code spend through workspaces: set workspace spend limits on total Claude Code spend and view cost and usage reporting. On first authentication with a Console account, a workspace called "Claude Code" is created automatically; you cannot create API keys for it. Its traffic counts toward the organization's overall API rate limits; set a workspace rate limit on its Limits page to cap Claude Code's share.

# How to use it

Recommended per-user rate limits by team size:

| Team size | TPM per user | RPM per user |
| - | - | - |
| 1-5 users | 200k-300k | 5-7 |
| 5-20 users | 100k-150k | 2.5-3.5 |
| 20-50 users | 50k-75k | 1.25-1.75 |
| 50-100 users | 25k-35k | 0.62-0.87 |
| 100-500 users | 15k-20k | 0.37-0.47 |
| 500+ users | 10k-15k | 0.25-0.35 |

Example: 200 users at 20k TPM each is 4 million total TPM.

# Notes

Limits apply at organization level, so individuals can temporarily exceed their share. Per-user TPM falls as size grows because fewer users are concurrent. For unusually high concurrency (live training sessions) request more.
