---
type: "Feature"
title: "Gateway spend limits and Admin API"
description: "Per-developer, group or org spend caps by day, week or month, set through a REST Admin API and enforced live on every request."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-spend-limits"
tags: [gateway, spend-limits, admin-api, budgets, enforcement]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "admin: block in gateway.yaml"
identifiers:
  - "/v1/organizations/spend_limits"
  - "/v1/organizations/spend_limits/effective"
  - "/v1/organizations/spend_limits/audit"
  - "scope.type"
  - "scope.user_id"
  - "scope.rbac_group_id"
  - "rbac_group"
  - "amount"
  - "period"
  - "pooled_budget"
  - "admin.write_keys"
  - "admin.read_keys"
  - "admin.admin_groups"
  - "admin.blocked_message"
  - "admin.group_limit_mode"
  - "x-api-key"
  - "billing_error"
  - "x-should-retry"
  - "retry-after"
  - "anthropic-ratelimit-unified-*"
  - "spl_"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-spend-limits"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-spend-limits"
    title: "Claude apps gateway spend limits"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With the `admin:` block configured, the gateway serves `/v1/organizations/spend_limits` (mirroring Anthropic's public Admin API wire shapes) and enforces caps on every `/v1/messages` request. A group or organization cap is a per-seat default each member inherits, not a shared pool (except pooled budgets, see [admin settings](../claude-apps-gateway-config/admin-enforcement-pricing.md)). Caps are set only through the API, not `gateway.yaml`.

# How to use it

`POST /v1/organizations/spend_limits` with `{scope, amount, period}` creates or replaces a cap, for example `{"scope": {"type": "organization"}, "amount": "50000", "period": "monthly"}` (USD 500). Auth: `x-api-key` matching `admin.write_keys` (full) or `admin.read_keys` (GET only), audited as `admin-key:<id>`; or a gateway bearer token whose groups include `admin.admin_groups`, audited as `oidc:<sub>`.

| Field | Values |
| - | - |
| `scope.type` | `user` (OIDC `sub` in `scope.user_id`), `rbac_group` (name in `scope.rbac_group_id`), `organization` |
| `amount` | whole-number string of USD cents; `null` unlimited; `"0"` blocks every request |
| `period` | `daily`, `weekly`, `monthly`; one cap per period per scope, each enforced independently |

Effective cap per period: per-user override, then most restrictive group cap, then org default, then unlimited (`admin.group_limit_mode: max` flips to least restrictive).

| Endpoint | Purpose |
| - | - |
| `GET /v1/organizations/spend_limits` | list; query `limit`, `after_id`, `before_id`, `scope_type` |
| `POST /v1/organizations/spend_limits` | create or replace |
| `GET /v1/organizations/spend_limits/{id}` | one cap by `spl_` id |
| `DELETE /v1/organizations/spend_limits/{id}` | delete; returns `{type: "spend_limit_deleted", id}` |
| `GET .../effective` | resolved cap and spend per principal per period; params `user_ids[]`, `period[]`, `sort=spend_desc`, `q`, `limit` (1-1000, default 20), `page` |
| `GET .../audit` | mutation trail, newest first; `limit` default 100, `after_id` |

Only spend-limits endpoints exist; the `spend_limit_increase_requests` queue is not part of the gateway. Every mutation writes a before/after row to `admin_audit`.

# Limits and defaults

- Enforcement: over any cap, `/v1/messages` gets `429` with `error.type: billing_error`, `x-should-retry: false`, and a `retry-after` header; message shows the UTC reset date and appends `admin.blocked_message`. `"0"` caps show no date. `/v1/messages/count_tokens` is never blocked.
- Caps reset on UTC boundaries: daily 00:00, weekly Monday, monthly first.
- The pre-check queries Postgres with a 2-second timeout and fails open by default; `enforcement.fail_closed_on_error: true` returns `429` `spend limit unavailable`.
- Message format before v2.1.319 named the period and time; before v2.1.225 it had no period, reset time or `retry-after`. `<public_url>/protocol` lists headers and the `429` body (v2.1.227 or later).
- `q=` and `user_ids[]=` appear in proxy access logs.
