---
type: "Concept"
title: "Zero data retention scope and routing"
description: "ZDR is per-organization on Claude for Enterprise, covers inference only, and needs sign-ins pinned to the ZDR org via forceLoginMethod and forceLoginOrgUUID."
resource: "https://code.claude.com/docs/en/zero-data-retention"
tags: [zdr, retention, enterprise, managed-settings]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "Claude for Enterprise, enabled per organization by Anthropic"
identifiers:
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "zero-data-retention"
    resource: "https://code.claude.com/docs/en/zero-data-retention"
    title: "Zero data retention"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With ZDR, prompts and responses in Claude Code sessions are processed in real time and not stored after the response, except as required by law or to combat misuse. Not in the standard Enterprise plan and not enableable from admin settings; Anthropic enables it after confirming eligibility, audit-logged. Gives per-user cost controls, analytics dashboard, server-managed settings and audit logs. Applies only to Anthropic's direct platform; Bedrock, Agent Platform and Foundry follow their own platform policies.

# How to use it

- Each new organization needs ZDR enabled separately by the account team.
- ZDR covers requests that authenticate into the ZDR organization. Personal accounts or API keys from another organization are not covered; deploy `forceLoginMethod` and `forceLoginOrgUUID` managed settings to require claude.ai logins from the ZDR org.
- Organizations with HIPAA configuration can bring the CLI and Code tab under the BAA without ZDR; without it, ZDR is still needed for BAA coverage of Claude Code.
- Pay-as-you-go API-key ZDR users can migrate to Claude for Enterprise to gain admin features.

# Limits and defaults

Not covered (standard retention): claude.ai chat, Cowork, Artifacts (kept until deleted unless a retention period is set; not available in Claude Code under ZDR), Claude in Chrome, Claude Code Analytics metadata (account emails, usage stats; no contribution metrics, usage metrics only), user and seat management data, third-party integrations and MCP servers. Policy-violation data may be retained up to 2 years.
