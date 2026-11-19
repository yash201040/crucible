---
type: "Guide"
title: "Gateway IdP registration and deployment"
description: "Register an OIDC client, build the gateway container and run it on Kubernetes or Cloud Run behind an L7 proxy, then push the URL to clients."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
tags: [gateway, deployment, kubernetes, cloud-run, oidc]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "private-network address, PostgreSQL, OIDC IdP"
identifiers:
  - "CLAUDE_CONFIG_DIR"
  - "claude gateway --config /etc/claude/gateway.yaml"
  - "/oauth/callback"
  - "/readyz"
  - "/healthz"
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "parentSettingsBehavior"
  - "gatewayInternalNetworks"
  - "skipWebFetchPreflight"
  - "rate_limits"
  - "listen.trusted_proxies"
  - "CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS"
  - "API_TIMEOUT_MS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-deploy"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
    title: "Claude apps gateway deployment and operations"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The gateway is a single stateless Linux binary (part of the `claude` binary, no separate license or per-seat fee) that coordinates through Postgres. At sign-in Claude Code refuses a gateway whose hostname resolves to a public IP, so plan a private address (RFC 1918 or CGNAT `100.64.0.0/10`) or declare an owned public IPv4 block in the `gatewayInternalNetworks` managed setting (gateway and user machine must both be in the block).

# How to use it

1. IdP: register a confidential OIDC web app with the single redirect URI `https://<gateway>/oauth/callback`. IdP must serve `/.well-known/openid-configuration`, support authorization-code flow (PKCE default on), and return `email` (and optionally `groups`) or serve them via userinfo. Okta org server needs `userinfo_fallback: true`; Entra emits group Object IDs (or use `groups_claim: roles`); Google has no groups claim (use `oidc.google_groups`) and needs `scopes: [openid, profile, email]` with `extra_auth_params: { access_type: offline, prompt: consent }` for refresh tokens.
2. Container: download a pinned Linux build, verify the GPG-signed `manifest.json`, use a glibc image (musl needs the `linux-x64-musl` or `linux-arm64-musl` build), set `CLAUDE_CONFIG_DIR` to a writable path such as `/tmp/.claude`, command `claude gateway --config /etc/claude/gateway.yaml`, listen port 8080.
3. Kubernetes: Deployment, config from ConfigMap, secrets via env or `${file:...}`, TLS at the Ingress, readiness `GET /readyz`, liveness `GET /healthz`. Cloud Run: port 8080 (or `port: ${PORT}`), config as secret volume, `min-instances: 1`. Lambda and Cloud Functions do not work.
4. Push `forceLoginMethod`, `forceLoginGatewayUrl`, `parentSettingsBehavior: "merge"` to developer machines via MDM or `managed-settings.json`.

# Limits and defaults

- Set `listen.trusted_proxies` to the L7 proxy ranges, or all requests share the proxy IP's rate-limit bucket.
- Do not redirect the device-authorization and token endpoints; Claude Code does not follow redirects there.
- Proxy idle timeout must exceed the keepalive: non-`anthropic` upstreams get an SSE `ping` after about 15 s of silence.
- The gateway does not enforce that it is the only route to a model; block provider egress by network policy. Blocking `api.anthropic.com` breaks the WebFetch domain check unless `skipWebFetchPreflight: true`.
- Each gateway is a separate deployment; one OIDC issuer per instance.
- Large rollouts: defaults are 30 sign-in starts and 10 code submissions per IP per 10 minutes; size `rate_limits` by developers per egress address, doubled. Claude Code v2.1.274 or later shows `The gateway is limiting sign-in attempts right now`.
