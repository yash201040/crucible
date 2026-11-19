---
type: "Reference"
title: "Gateway enforcement, visibility and limitations"
description: "What the Claude apps gateway enforces on signed-in sessions and the table of supported and unsupported features and server limits."
resource: "https://code.claude.com/docs/en/claude-apps-gateway"
tags: [gateway, enforcement, limits, availability]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "Claude Code v2.1.195 or later"
identifiers:
  - "availableModels"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "telemetry.forward_to"
  - "admin.admin_groups"
  - "revocation_endpoint"
  - "CLAUDE_CODE_ENABLE_AUTO_MODE"
  - "/logout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway"
    title: "Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Guarantees on every `/login` session, and what the gateway does and does not support.

# How to use it

Enforced:
- Model access: ungranted models return 400; `/model` is filtered to the policy's `availableModels`.
- Telemetry: OTLP/HTTP exports go to the gateway rather than a locally set `OTEL_EXPORTER_OTLP_ENDPOINT` unless a policy names your collector; the gateway relays to `telemetry.forward_to` and discards signals with no destination. Embedded Desktop sessions export to the configured endpoint and attach the session token only when it points at the gateway.
- Credentials: the gateway token is the only credential; Anthropic profiles and earlier claude.ai logins are ignored.
- Managed settings: applied at startup, refreshed on an hourly poll (some changes apply at next launch). Signed-in sessions exit at startup after about 10 seconds if the gateway is unreachable.
- Deprovisioning: a disabled IdP user expires within `ttl_hours` when refresh fails. `/logout` deletes the credential locally and, on v2.1.275+, calls the discovery document's `revocation_endpoint` if it is on the gateway's own origin; the built-in server advertises none (see JWT secret rotation in the deployment guide to force sessions out).
- Visibility: usage telemetry carries identity, token counts, model and latency; prompt and completion content is not logged or stored.

| Feature | Status |
|---|---|
| Inference to Bedrock, Claude Platform on AWS, Google Cloud (Anthropic managed and Agent Platform), Foundry, Anthropic API | Available, per-upstream model translation and failover |
| 1M context window | Available; Fable, Sonnet 5+, Opus 4.7+ default (v2.1.287+ on client) |
| Per-group model access and managed settings | Available |
| Claude Desktop | Available with `desktop` key opt-in (server v2.1.203+) |
| Telemetry fan-out OTLP/HTTP | Available (protobuf and JSON) |
| Per-user and per-group spend limits | Available |
| Prompt caching | Available; `cache_control` forwarded |
| 1-hour cache TTL | Opt-in via policy only; default is 5 minutes; request fails if an upstream rejects it |
| Auto mode | Available under third-party rules (before v2.1.207 needed `CLAUDE_CODE_ENABLE_AUTO_MODE=1`) |
| Server-side web search | Not available (WebSearch disabled) |
| Remote Control | Not available |
| `/design-sync`, `/design-login` | Not available |
| Feature-flag-dependent features (`/import`, `claude import`) | Not available |
| First-party-only optimizations (global cache scope, token-efficient tools) | Not available |
| OTLP/gRPC | Not supported (HTTP only) |
| SAML, LDAP | Not supported (OIDC only) |
| Multiple OIDC issuers | Not supported (one per gateway) |
| Windows server | Not supported |
| Helm chart | Not available |
| Admin UI | Spend limits only (Claude Desktop 4.23118.0+; `admin.admin_groups`) |

# Notes

The gateway forwards `anthropic-beta` values to every upstream; for Bedrock it moves them into the request body `anthropic_beta` field. Companion pages cover the configuration reference, deployment guide, spend limits and worked AWS and GCP examples.
