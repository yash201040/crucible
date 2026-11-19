---
type: "Feature"
title: "Claude apps gateway overview and quickstart"
description: "Self-hosted gateway built into the claude binary (claude gateway) giving IdP sign-in, per-group model access, managed settings and OTLP telemetry in front of cloud upstreams."
resource: "https://code.claude.com/docs/en/claude-apps-gateway"
tags: [gateway, sso, oidc, managed-settings, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.195"
surfaces: [cli, desktop]
requires: "Claude Code v2.1.195+ on server and clients; OIDC IdP; PostgreSQL 11+; Linux server; private-network HTTPS address"
identifiers:
  - "claude gateway --config gateway.yaml"
  - "gateway.yaml"
  - "listen.public_url"
  - "listen.tls"
  - "oidc.issuer"
  - "session.ttl_hours"
  - "store.postgres_url"
  - "upstreams"
  - "auto_include_builtin_models"
  - "access_control.allow_cidrs"
  - "managed.policies"
  - "telemetry.forward_to"
  - "/.well-known/oauth-authorization-server"
  - "/oauth/device_authorization"
  - "/oauth/callback"
  - "/oauth/token"
  - "/device"
  - "/protocol"
  - "/user/bootstrap"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway"
    title: "Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A self-hosted service between developers' Claude Code clients and the model provider, run with the same `claude` binary: `claude gateway --config gateway.yaml`. Developers sign in with the corporate IdP (device flow in a browser) and receive short-lived bearer tokens (session default one hour); the upstream credential stays in your infrastructure. It enforces model access server-side (requests for non-granted models return 400), selects managed settings per IdP group (applied at the managed settings tier), forwards OTLP metrics (token counts, model, user identity, latency; logs and traces opt-in per destination), and translates the Anthropic Messages API for each upstream (Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Foundry, Anthropic API) with failover. The gateway's data plane sends nothing to Anthropic unless the Anthropic API is an upstream. A gateway sign-in replaces a Claude for Teams or Enterprise login, and gateway sessions do not fetch claude.ai server-managed settings; use the gateway's `managed` block.

# How to use it

Prerequisites: Claude Code v2.1.195+ on the server and each developer machine (Claude Platform on AWS upstream needs v2.1.198+ on the server; Mantle upstream v2.1.283+; Google Cloud Anthropic managed upstream v2.1.307+); OIDC IdP (Okta, Entra ID, Google Workspace, Keycloak, Dex, others; SAML and LDAP unsupported); PostgreSQL 11+ (11 to 13 need v2.1.290+ on the server); HTTPS with `listen.tls` or a TLS ingress and `listen.public_url`; native Linux binary (macOS for local development only, Windows unsupported); a hostname that resolves only to private addresses (RFC 1918, link-local, `100.64.0.0/10`, ULA `fc00::/7`, loopback). Plain `http://` is accepted at `/login` only for loopback hosts.

Steps:
1. Register an OIDC web app with redirect URI `https://<gateway>/oauth/callback`.
2. Provision Postgres (role must create and alter tables; schema migrations run at boot).
3. Write `gateway.yaml` with `listen`, `oidc` (`issuer`, `client_id`, `client_secret`, `allowed_email_domains`, `userinfo_fallback`), `session` (`jwt_secret`, `ttl_hours`), `store.postgres_url`, `upstreams` (e.g. `provider: bedrock`, `region`, `auth: {}`), `auto_include_builtin_models`. Secrets use `${ENV_VAR}` expansion.
4. Run it (Docker Compose example with a container around the `claude` binary, or directly). Boot is fail-closed for config, Postgres, OIDC discovery and upstream construction; inference credentials resolve on first request. It warns when `access_control.allow_cidrs` is empty.
5. Verify: `curl .../.well-known/oauth-authorization-server`, `POST /oauth/device_authorization`, then open `verification_uri_complete`. The audit log records auth rejections.
6. Developer: set `forceLoginMethod` `"gateway"`, `forceLoginGatewayUrl`, `parentSettingsBehavior` `"merge"` in managed settings, then `/login` and press Enter on **Cloud gateway**.

A running gateway serves its protocol reference at `GET /protocol`. Breaking protocol changes are announced in advance, not guaranteed backward compatible. A gateway token identifies the developer, not the program; `User-Agent` is not proof of Claude Code.
