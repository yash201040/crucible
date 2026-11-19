---
type: "Reference"
title: "Gateway oidc, session and store settings"
description: "Identity provider sign-in options, certificate client auth, proxy egress, gateway bearer-token session and Postgres store settings."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, oidc, session, postgres, proxy]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "PostgreSQL; an OIDC identity provider"
identifiers:
  - "oidc.issuer"
  - "oidc.client_id"
  - "oidc.client_secret"
  - "oidc.allowed_email_domains"
  - "oidc.allowed_groups"
  - "oidc.groups_claim"
  - "oidc.google_groups"
  - "oidc.email_claim"
  - "oidc.scopes"
  - "oidc.scope_on_refresh"
  - "oidc.extra_auth_params"
  - "oidc.userinfo_fallback"
  - "oidc.use_pkce"
  - "oidc.clock_skew_seconds"
  - "oidc.token_endpoint_auth_method"
  - "private_key_jwt"
  - "oidc.client_assertion"
  - "oidc.id_token_signed_response_alg"
  - "oidc.additional_authorized_parties"
  - "oidc.discovery_url"
  - "oidc.use_proxy"
  - "oidc.form_action_origins"
  - "oidc.ca_cert_pem"
  - "CLAUDE_GATEWAY_ALLOW_LOOPBACK"
  - "CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY"
  - "HTTPS_PROXY"
  - "NO_PROXY"
  - "session.jwt_secret"
  - "session.ttl_hours"
  - "store.postgres_url"
  - "store.username"
  - "store.password"
  - "store.max_connections"
  - "store.connect_timeout_seconds"
  - "store.readiness_grace_seconds"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `oidc` block connects the gateway to the identity provider (IdP) and decides who may sign in. `session` shapes the HS256 bearer tokens the gateway mints. `store` points at the PostgreSQL database that holds device grants and rate-limit counters.

# How to use it

| Key | Default | What it does |
| - | - | - |
| `oidc.issuer`, `client_id` | required | discovery base (must serve `/.well-known/openid-configuration`) and OAuth client |
| `oidc.client_secret` | required unless `private_key_jwt` | leave out with certificate auth |
| `allowed_email_domains` | none | reject id_tokens outside these domains; `email_verified: false` is always rejected |
| `allowed_groups` | none | restrict sign-in to groups from `groups_claim`; exact, case-sensitive, no nested-group expansion |
| `groups_claim` | `groups` | flat key or RFC 6901 JSON Pointer (Entra: `roles`) |
| `google_groups` | none | Admin SDK Directory lookup via `service_account_json_path` and `admin_email` |
| `email_claim` | `email` | flat key, pointer, or list of fallbacks |
| `scopes` | `[openid, profile, email, offline_access]` | full override; must include `openid`; dropping `offline_access` disables refresh tokens |
| `scope_on_refresh` | `false` | resend `scope` on refresh; needs v2.1.260 or later |
| `extra_auth_params` | none | extra authorization query params; cannot override state, nonce, redirect_uri, PKCE, scope, response_type, response_mode, client_id |
| `userinfo_fallback` | `false` | fill missing email/groups from `/userinfo` |
| `use_pkce` | `true` | S256 challenge |
| `clock_skew_seconds` | `0` | tolerance for id_token time claims |
| `token_endpoint_auth_method` | auto | `client_secret_basic`, `client_secret_post`, or `private_key_jwt` |
| `client_assertion` | with `private_key_jwt` | `private_key_pem` and `certificate_pem` (PEM contents, use `${file:...}`); v2.1.284 or later |
| `id_token_signed_response_alg` | `RS256` | for ES256, PS256, EdDSA IdPs |
| `additional_authorized_parties`, `discovery_url`, `form_action_origins`, `ca_cert_pem` | none | Keycloak azp values, proxy-rewritten discovery, CSP form-action origins, private CA PEM |
| `use_proxy` | unset | send IdP requests through `HTTPS_PROXY`/`HTTP_PROXY`; v2.1.227 or later |
| `session.jwt_secret` | required | at least 32 bytes entropy; string or array (index 0 signs, all verify) for rotation |
| `session.ttl_hours` | `1` | bearer token life; raise to 8 or 12 if no refresh tokens |
| `store.postgres_url` | required | one host only; gateway runs its own migrations (needs create/alter rights) |
| `store.username`, `store.password` | none | override URL credentials |
| `store.max_connections` | `5` | pool per replica |
| `store.connect_timeout_seconds` | `5` | 1-60; v2.1.274 or later |
| `store.readiness_grace_seconds` | `0` | 0-3600; v2.1.282 or later |

Certificate client auth: create an unencrypted RSA key (at least 2048 bits, PKCS#8 or PKCS#1) and certificate, upload the certificate to the IdP, set `token_endpoint_auth_method: private_key_jwt` with `client_assertion`, restart and compare the SHA-1 thumbprint in the boot log. JWT is RS256 with `x5t` and `x5t#S256` headers. Rotate by uploading the new certificate first, replacing files and restarting, then removing the old certificate.

Proxy-only egress: set `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` next to `HTTPS_PROXY` (v2.1.277 or later). It stays off unless a proxy variable is set, `NO_PROXY` and `no_proxy` are empty, and `CLAUDE_GATEWAY_ALLOW_LOOPBACK` is off. The proxy then must itself refuse metadata, link-local and loopback destinations.

# Limits and defaults

A loopback issuer is rejected by the SSRF guard unless `CLAUDE_GATEWAY_ALLOW_LOOPBACK=1`. Gateways older than a key's stated version refuse to start when it is set. Session secret rotation: prepend new secret, wait `ttl_hours`, drop the old one.
