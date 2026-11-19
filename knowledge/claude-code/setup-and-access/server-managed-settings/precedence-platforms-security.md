---
type: "Reference"
title: "Server-managed precedence, platform availability and security"
description: "Per-key exceptions across managed sources, which credentials receive settings, skipped-fetch conditions and the security model."
resource: "https://code.claude.com/docs/en/server-managed-settings#platform-availability"
tags: [server-managed, availability, credentials, ci]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, ide, cloud, desktop]
requires: "user_oauth profile delivery needs v2.1.257 or later"
identifiers:
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "claude setup-token"
  - "ANTHROPIC_BASE_URL"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_MANTLE"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_USE_FOUNDRY"
  - "CLAUDE_CODE_USE_ANTHROPIC_AWS"
  - "apiKeyHelper"
  - "--bare"
  - "forceLoginGatewayUrl"
  - "gatewayInternalNetworks"
  - "otelHeadersHelper"
  - "ConfigChange"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "server-managed-settings"
    resource: "https://code.claude.com/docs/en/server-managed-settings"
    title: "Configure server-managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Which sessions receive server-managed settings, and exceptions to the no-merge rule across managed sources.

# How to use it

Delivery needs a direct connection to `api.anthropic.com` and one of: Team/Enterprise OAuth login; `CLAUDE_CODE_OAUTH_TOKEN`; a directly configured API key; a `user_oauth` Anthropic profile without a non-Anthropic `base_url` (v2.1.257+). Keys from `apiKeyHelper` and Workload Identity Federation credentials do not trigger the fetch.

A session gets the settings of the organization owning its credential. A Console API key belongs to a Console org, separate from your claude.ai org, so a CI job using it gets no claude.ai settings. Options: generate a token with `claude setup-token`, authorize for the Team/Enterprise org, set `CLAUDE_CODE_OAUTH_TOKEN` and remove higher-precedence credentials such as `ANTHROPIC_API_KEY` (not usable with `--bare`); or deploy a managed settings file on the job host.

Exporting any `CLAUDE_CODE_USE_*` provider variable or a non-default `ANTHROPIC_BASE_URL` in the shell skips the fetch; a managed `env` block cannot undo it (eligibility is checked first). Remove the export or set it to `""` in user settings `env`. Self-hosted Claude apps gateway gives the equivalent for Bedrock, Vertex, Foundry and Claude Platform on AWS; a gateway client that cannot reach the gateway exits, while the hourly refresh is fail-open on both channels.

# Limits and defaults

- Per-key exceptions to first-wins: cross-source lock keys; `env` merged per variable (v2.1.223+; before it only the selected source's block); telemetry unit (`OTEL_EXPORTER_OTLP_*`, `OTEL_LOG_*`, `OTEL_LOGS_EXPORTER`, `ENABLE_BETA_TRACING_DETAILED`, `BETA_TRACING_ENDPOINT`, `otelHeadersHelper`) follows the highest source as a unit; credential-paired routing variables count only when that source wins the slot; `allowedProviders` (v2.1.285+); first-party login keys (set in both until clients are v2.1.299+); gateway login keys (`forceLoginGatewayUrl`, `gatewayInternalNetworks`, `forceLoginMethod: "gateway"`) never read from server-managed settings.
- Cowork sessions in Desktop never fetch these settings.
- Security model: a client-side control, not a boundary. Edited cache lasts until the next fetch (except `model` or newly added `env` variables until relaunch); older versions and modified binaries ignore it; third-party provider variables bypass it; intercepted traffic can alter it. Cleared server config with fallback to MDM leaves cached settings in effect until next successful fetch. For stronger guarantees use MDM-managed endpoints.
