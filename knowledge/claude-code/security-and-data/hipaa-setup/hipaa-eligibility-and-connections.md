---
type: "Reference"
title: "HIPAA configuration: eligible connections and requirements"
description: "The HIPAA configuration applies only to Claude Enterprise sign-ins connecting directly to the Claude API on v2.1.285 or later, plus required network hosts."
resource: "https://code.claude.com/docs/en/hipaa-setup"
tags: [hipaa, compliance, eligibility, network, enterprise]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, desktop]
requires: "Claude Enterprise plan, BAA with Anthropic, Claude Code v2.1.285+, Claude Desktop v2.19675.0+"
identifiers:
  - "claude --version"
  - "/status"
  - "claude doctor"
  - "api.anthropic.com"
  - "ANTHROPIC_BASE_URL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hipaa-setup"
    resource: "https://code.claude.com/docs/en/hipaa-setup"
    title: "Set up Claude Code (local mode) for a HIPAA-ready organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An organization setting on Claude Enterprise plans for organizations handling PHI with a BAA. It applies to Claude Code (local mode: terminal, Code tab in Claude Desktop) and Cowork (local mode), not cloud sessions. VS Code and JetBrains extensions keep working but are not covered by the BAA.

# How to use it

| How Claude Code connects | Eligible |
| - | - |
| Claude Enterprise account, directly to the Claude API | Yes |
| Bedrock, Agent Platform, Foundry, Claude Platform on AWS, Claude apps gateway | No |
| LLM gateway or any custom `ANTHROPIC_BASE_URL` | No |
| `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` with no Enterprise sign-in | No |
| Console API key or federation credentials | No (Console organization, own agreement) |

Check a computer with `/status`: `Login method`, `Organization`, `API provider` (only for cloud provider or Claude apps gateway), `Anthropic base URL`. A corporate HTTPS proxy is fine if it reaches the hosts below.

Hosts to allow (HTTPS 443, whole hosts): `api.anthropic.com` (API, telemetry, the organization policy), `claude.ai`, `claude.com`, `platform.claude.com` (sign-in, token refresh), `sso.claude.com` (SSO), `downloads.claude.ai` (installer and updates), `mcp-proxy.anthropic.com` (claude.ai connectors).

# Limits and defaults

- Minimum versions: Claude Code v2.1.285 and Claude Desktop v2.19675.0; Anthropic servers reject older versions (Claude Code shows an API Error, Desktop shows **Update required**).
- Claude Code fetches the organization policy at start and about hourly while in use.
