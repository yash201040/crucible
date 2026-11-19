---
type: "Limit"
title: "Features that need feature-flag fetching"
description: "Which sessions skip feature-flag fetching, which features stop working without it, and why the first session after an install may lack a flag-gated feature."
resource: "https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching"
tags: [feature-flags, limits, availability, offline]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Some features are switched on by feature flags Claude Code fetches from Anthropic. When the fetch is skipped those features are unavailable.

# How to use it

Fetching is skipped in:
- A session with `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`, `DISABLE_TELEMETRY`, `DO_NOT_TRACK` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set (see [opt-out variables](./telemetry-and-traffic-opt-out-variables.md)).
- A session on a third-party provider (Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry), unless a host sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`.
- A Claude apps gateway session.

Without fetching you cannot:
- Use Remote Control (with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`; for `DISABLE_TELEMETRY` and `DO_NOT_TRACK` see the Remote Control requirements).
- Message sessions beyond this machine when Remote Control is unavailable (messaging on this machine still works).
- Run `claude import` or `/import`.
- Run `/skill-doctor` or open its report in the `/plugin` Stats tab.
- Run `/restart` on Pro, Max and Ultra plans.
- Sync claude.ai skills and plugins into terminal sessions.
- Turn on the You should know mod.
- Use the advisor tool (except v2.1.300+ on Claude Platform on AWS or Claude Models on Google Cloud).
- Use MCP tasks.
- Turn on Code Mode.
- Read or reply to artifact comments, or have Claude read another organization's public artifact.
- Get the PowerShell tool by default for claude.ai and Console accounts on Windows with Git Bash (set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`; without Git Bash it stays on).
- Get Claude-drafted feedback.

# Limits and defaults

First session after an install or upgrade: a flag-gated feature can be missing; flags fetched during that session are saved on the machine, so the next session has them. Sessions after the first also start without fresh flags when:
- every run starts in a clean environment (CI container) with no saved flags, so each run is a first session;
- you authenticate with `ANTHROPIC_AUTH_TOKEN` and no API key while `ANTHROPIC_BASE_URL` points at a non-Anthropic host (LLM gateway): there is no credential to fetch flags with.
