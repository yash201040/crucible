---
type: "Reference"
title: "Artifact availability requirements"
description: "Plan, authentication, provider, policy and surface conditions that must all hold for artifacts, including SDK and -p exclusions."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, availability, plans, sdk]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli, desktop, headless, sdk]
requires: "See table"
identifiers:
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "claude remote-control"
  - "-p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every condition below must be met; otherwise Claude writes a local HTML file or says it cannot publish.

# How to use it

| Requirement | Available when |
| --- | --- |
| Plan | Pro, Max, Ultra, Team or Enterprise. Pro/Max/Ultra: private until shared, no admin management. Team/Enterprise: on by default; an Owner can turn off for the org |
| Authentication | Session backed by a claude.ai account (`/login`). Claude Tag sessions need no sign-in. API key, gateway token or cloud-provider credential sessions cannot publish |
| Model provider | Anthropic API only. Not Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry |
| Organization policy | CMEK, HIPAA and Zero Data Retention not enabled |
| Surface | Claude Code CLI, or Claude desktop app 1.13576.0+. Claude Tag sessions when both enabled. Sessions served by `claude remote-control` when you started the session yourself (Claude Code v2.1.281+). Off by default in the Agent SDK, the GitHub Action, MCP-server contexts, when running with `-p` from your own terminal or scripts, and when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set |

# Notes

Org policy is loaded from `api.anthropic.com`; if it cannot load, artifacts are unavailable and Claude says why. Behind a proxy, VPN or filter, have IT allow `api.anthropic.com`; Claude Code retries in the background and artifacts return once policy loads and allows them.
