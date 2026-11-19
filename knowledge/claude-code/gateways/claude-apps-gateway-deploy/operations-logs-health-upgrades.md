---
type: "Reference"
title: "Gateway operations: logs, health, outages, upgrades"
description: "Audit events, log formats, probes, upstream concurrency, drain on SIGTERM, outage behavior, JWT rotation and Postgres tables."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
tags: [gateway, operations, logs, upgrades, postgres]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_GATEWAY_LOG_LEVEL"
  - "CLAUDE_GATEWAY_LOG_FORMAT"
  - "CLAUDE_GATEWAY_DRAIN_TIMEOUT_MS"
  - "BUN_CONFIG_MAX_HTTP_REQUESTS"
  - "store.readiness_grace_seconds"
  - "store.max_connections"
  - "session.jwt_secret"
  - "/healthz"
  - "/readyz"
  - "/.well-known/oauth-authorization-server"
  - "config.load"
  - "session.mint"
  - "session.refresh"
  - "device.authorize"
  - "device.verify"
  - "device.callback"
  - "auth.denied"
  - "access.denied"
  - "access.public_client"
  - "inference"
  - "managed.serve"
  - "desktop_bootstrap.serve"
  - "desktop_bootstrap.denied"
  - "spend.blocked"
  - "admin.denied"
  - "admin.limit.upsert"
  - "admin.limit.delete"
  - "guardrail.trace"
  - "x-cc-gateway-version"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-deploy"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-deploy"
    title: "Claude apps gateway deployment and operations"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Day-to-day operation of a gateway: two stderr streams (single-line JSON audit events and `[gateway]` operational lines), health endpoints, a concurrency cap on upstream requests, graceful shutdown, outage behavior and the Postgres schema.

# How to use it

- Audit events: `config.load`, `session.mint`, `session.refresh`, `device.authorize`, `device.verify`, `device.callback`, `auth.denied`, `access.denied`, `access.public_client`, `inference` (which upstream served and status), `managed.serve`, `desktop_bootstrap.serve`, `desktop_bootstrap.denied`, `spend.blocked`, `admin.denied` (reasons `invalid_key`, `bearer_rejected`, `no_credentials`), `admin.limit.upsert`, `admin.limit.delete`, plus `guardrail.trace`.
- `CLAUDE_GATEWAY_LOG_LEVEL`: debug, info (default), warn, error. `CLAUDE_GATEWAY_LOG_FORMAT=json` (v2.1.319 or later) gives `severity`, `time`, `message`; audit events keep `ts` and `evt`.
- Probes: `GET /healthz` (liveness), `GET /readyz` (readiness, checks store; `store.readiness_grace_seconds` keeps it ready after Postgres stops answering). Both exempt from `access_control.allow_cidrs`. `/.well-known/oauth-authorization-server` returns 200 only after the whole boot succeeds. Gateway version is on `/` and in the `x-cc-gateway-version` header of `/managed/settings`.
- Concurrency: each replica sends at most 256 upstream requests at once (a stream counts until it ends); extras wait inside the gateway. Raise with `BUN_CONFIG_MAX_HTTP_REQUESTS` (1-65535) or add replicas. A warning containing `client requests are open` logs at most once a minute. Memory grows with open requests.
- Drain (v2.1.274 or later): on `SIGTERM` or `SIGINT` the gateway stops accepting and waits 25 s by default (`CLAUDE_GATEWAY_DRAIN_TIMEOUT_MS`, positive integer ms; other forms ignored). Keep the orchestrator grace period (`terminationGracePeriodSeconds`, ECS `stopTimeout`) at least 5 s longer. Fargate `stopTimeout` max 120 s; Cloud Run stops 10 s after `SIGTERM`.
- JWT rotation: prepend new secret to `session.jwt_secret` array, roll, wait `ttl_hours` plus margin, drop old. No per-session revocation; replacing the secret outright invalidates all sessions.
- Upgrades: rolling restart loses no state; migrations run at boot under a Postgres advisory lock and are append-only, so rollback is safe but a config using a newer key fails on the older binary.

# Limits and defaults

Postgres outage: existing sessions keep working (tokens validate locally); new sign-ins fail; spend enforcement fails open by default; `/readyz` goes not-ready at once unless a grace period is set. IdP outage: sessions work until `ttl_hours`.

Postgres tables: `kv` (device grants 10-minute TTL, rate counters), `spend` (13 months), `spend_limits`, `admin_audit` (365 days), `principal_emails` (PII, 90 days), plus `_migrations`. Pool sizing: replicas (including rolling-update extras) times `store.max_connections` (default 5) must fit within database `max_connections` minus reserved (default `superuser_reserved_connections` 3). Only real PostgreSQL is supported.

Retry tuning on developer machines: keep `API_TIMEOUT_MS` above gateway time to first byte; `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` (v2.1.307 or later) sets a first-byte deadline, debug line `[first-byte] no response headers`.
