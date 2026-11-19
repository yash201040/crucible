---
type: "Guide"
title: "Team security practices and vulnerability reporting"
description: "Managed settings, shared permissions, OpenTelemetry monitoring, ConfigChange hooks, sandbox runtime or dev container isolation, and the HackerOne reporting path."
resource: "https://code.claude.com/docs/en/security"
tags: [team, managed-settings, hooks, monitoring, reporting]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ConfigChange"
  - "/permissions"
  - "/security-review"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security"
    resource: "https://code.claude.com/docs/en/security"
    title: "Security"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Recommended practices: use project-specific permission settings for sensitive repositories; for extra isolation run the whole Claude Code (local mode) process inside the sandbox runtime or a dev container; use managed settings to enforce organizational standards; share approved permissions via version control; monitor with OpenTelemetry metrics; audit or block settings changes during sessions with `ConfigChange` hooks.

# Notes

Vulnerabilities are reported through Anthropic's HackerOne program, not publicly. Related: the security guidance plugin and `/security-review` (on-demand pass over the current branch's changes). Certifications (SOC 2 Type 2, ISO 27001) are at the Anthropic Trust Center.
