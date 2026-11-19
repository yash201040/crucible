---
type: "Concept"
title: "Gateway security model and data flow"
description: "What data the gateway sends where, its threat model and SSRF guard, device-code brute-force limits and compliance answers."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
tags: [gateway, security, ssrf, compliance, data-flow]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_GATEWAY_ALLOW_LOOPBACK"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_TELEMETRY"
  - "DISABLE_UPDATES"
  - "DISABLE_AUTOUPDATER"
  - "skipWebFetchPreflight"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-deploy"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
    title: "Claude apps gateway deployment and operations"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Security-review facts for the gateway. Inference goes CLI to gateway to your upstream (to Anthropic only if the Anthropic API is a configured upstream). Telemetry, identity, managed settings and audit logs never go to Anthropic.

# How to use it

Threat model: developers hold short-lived JWTs, not upstream keys; the CLI-to-gateway leg uses the RFC 8628 device grant and PKCE with the IdP. An SSRF guard on requests to the IdP, OTLP collectors and `provider: anthropic` upstreams resolves DNS, blocks link-local, cloud-metadata and loopback addresses, and pins the resolved IP; RFC 1918 ranges are allowed. `CLAUDE_GATEWAY_ALLOW_LOOPBACK=1` relaxes loopback for every operator URL and skips the metadata-reachability boot warning. With proxy-only egress the check moves to your proxy. Out of scope: a compromised gateway host (comparable to controlling your MDM) and a malicious OIDC provider.

User code: 8 characters from a 20-character alphabet (about 2.56e10 combinations), expires in 10 minutes, per-IP limited.

Client-side privacy facts: while signed in to a gateway the CLI disables its own analytics, error reporting and survey rating uploads; before first sign-in it still sends startup events unless `DISABLE_TELEMETRY` is delivered in client managed settings. WebFetch hostname checks and version checks continue unless `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` and `skipWebFetchPreflight: true`. Update control: `DISABLE_UPDATES` (all) vs `DISABLE_AUTOUPDATER` (background only). The official plugin marketplace first registration is not stopped by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`; use a `strictKnownMarketplaces`/`blockedMarketplaces` setting or `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` set to `"1"` in managed `env`, also in client-side managed settings.

# Limits and defaults

Gateway versions before v2.1.227 sent startup telemetry and a boot `HEAD` request to `api.anthropic.com`. Fixes in new Claude Code releases reach a gateway only when you update your pinned image.
