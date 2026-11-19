---
type: "Reference"
title: "Feature availability by model provider"
description: "Which Claude Code features work on each provider: subscription, Console, Bedrock, Claude Platform on AWS, Google Cloud (two kinds) and Foundry."
resource: "https://code.claude.com/docs/en/feature-availability"
tags: [providers, availability, bedrock, foundry]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_MANTLE"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "ANTHROPIC_BASE_URL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "feature-availability"
    resource: "https://code.claude.com/docs/en/feature-availability"
    title: "Feature availability"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The CLI and everything local work on every provider. Columns map to the variable you set: Claude subscription (claude.ai Pro, Max, Ultra, Team, Enterprise login), Anthropic Console, Amazon Bedrock (`CLAUDE_CODE_USE_BEDROCK`, Mantle included), Claude Platform on AWS (`CLAUDE_CODE_USE_ANTHROPIC_AWS`), Google Cloud Anthropic managed (`CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD`), Google Cloud Google managed / Agent Platform (`CLAUDE_CODE_USE_VERTEX`), Microsoft Foundry (`CLAUDE_CODE_USE_FOUNDRY`).

# How to use it

Available on every provider: CLI and Agent SDK, VS Code and JetBrains extensions, subagents, hooks, commands, skills, CLAUDE.md memory, plugins, MCP servers, checkpoints, sandboxing, Workflows, OpenTelemetry metrics, managed settings file.

| Feature | Sub | Console | Bedrock | Platform on AWS | GCP Anthropic mgd | GCP Google mgd | Foundry |
|---|---|---|---|---|---|---|---|
| Web search | yes | yes | no | yes | yes | partial (Opus 4, Sonnet 4, Haiku 4.5 and later) | yes |
| Fast mode | yes (owner-enabled on Team/Ent) | yes (Opus 5 and 4.8 need provisioning) | no | no | no | Fable 5.2 with conditions | no |
| Auto mode | yes | yes | partial | yes | yes | partial | partial |
| Advisor | yes | yes | no | yes (v2.1.300+) | yes (v2.1.300+) | no | no |
| Code Mode (experimental) | yes, requirements apply | yes | no | no | no | no | no |
| Cross-session messaging | yes | same machine | same machine | same machine | same machine | same machine | same machine |
| Channels | yes | yes | no | no | no | no | no |
| GitHub Actions | yes | yes | yes | no | no | yes | yes |
| GitLab CI/CD | yes | yes | yes | yes | yes | yes | no |
| Analytics dashboard and API | Team/Ent (API: Ent) | yes (dashboard and API only) | no | no | no | no | no |
| Server-managed settings | Team/Ent | see platform availability | no | no | no | no | no |
| Zero Data Retention | qualified Ent | qualified | per AWS agreement | qualified | on request | per Google agreement | per Azure agreement |

"Partial" auto mode means only Claude Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5 and Fable models. Cross-session messaging needs v2.1.224+ on macOS/Linux/WSL 2, v2.1.234+ on native Windows, and v2.1.248+ on cloud providers (same machine only); finding cloud or other-machine sessions needs a Remote Control connection.

Provider-specific differences: claude.ai MCP connectors load only when the claude.ai subscription is the active auth; MCP tool search is not supported on Foundry deployments hosted on Azure, nor on Google Cloud (Google managed) models earlier than Opus 4.5, Sonnet 4.5, Haiku 4.5. When the parent runs Fable, the built-in Explore subagent runs on Opus with a subscription, Console, or LLM gateway via `ANTHROPIC_BASE_URL`, and on Fable on other providers. `/design-sync` and `/import` (and `claude import`) are unavailable on cloud providers and through a Claude apps gateway; `/voice` needs a claude.ai account; `/list-agents` and `/peers` need cross-session messaging.

# Limits and defaults

- Via an LLM gateway, availability matches the underlying provider except features Claude Code turns off itself: when `ANTHROPIC_BASE_URL` points away from `api.anthropic.com`, Remote Control is off; Advisor works only if the gateway forwards requests intact.
- On Bedrock, Google Cloud Agent Platform, Foundry and Claude Platform on AWS, error reporting and telemetry to Anthropic are off by default.
- Alternatives named: `/loop` instead of `/schedule`; GitHub Actions or GitLab CI/CD instead of cloud sessions; WebFetch with a URL instead of web search on Bedrock.
- Prompt caching works the same on most providers; on Bedrock support varies by model. Vision, PDF and extended thinking are model capabilities.
