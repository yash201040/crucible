---
type: "Limit"
title: "HIPAA configuration behind a gateway"
description: "Sessions through a gateway are not eligible for the HIPAA configuration; managed keys can restrict features but do not replicate it."
resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
tags: [gateway, hipaa, compliance, managed-settings]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-rollout"
    resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
    title: "Roll out an LLM gateway for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Gateway sessions are not eligible for the HIPAA configuration (see [HIPAA setup](../../security-and-data/hipaa-setup/hipaa-eligibility-and-connections.md)). Admins can restrict features in managed settings using the keys in the monitoring-usage page's egress map, but those keys do not make a session eligible and do not cover everything.

# Limits and defaults

- Cloud sessions: no managed key turns them off (use Desktop admin console controls).
- Anthropic credentials in child processes: the HIPAA configuration removes them; no settings key does only that.
- Do not substitute `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`: it turns off the auto-updater and leaves WebFetch on.
