---
type: "Reference"
title: "Gateway admin, enforcement and pricing settings"
description: "gateway.yaml keys that enable the spend-limit Admin API, fail-open or fail-closed enforcement, pooled budgets and contracted-rate pricing."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, spend-limits, admin, pricing, enforcement]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "gateway with Postgres store"
identifiers:
  - "admin.write_keys"
  - "admin.read_keys"
  - "admin.admin_groups"
  - "admin.blocked_message"
  - "admin.audit_retention_days"
  - "admin.spend_retention_months"
  - "admin.identity_retention_days"
  - "admin.group_limit_mode"
  - "admin.pooled_conflict_rule"
  - "admin.pooled_priority_order"
  - "enforcement.fail_closed_on_error"
  - "pricing.multiplier"
  - "pricing.overrides"
  - "modelPricing"
  - "login_notice"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The optional `admin` block enables `/v1/organizations/spend_limits` and per-developer spend enforcement on `/v1/messages`. `enforcement` sets behavior when the store is down. `pricing` makes the spend meter use contracted rates. See [spend limits](../claude-apps-gateway-spend-limits/spend-limits-and-admin-api.md) for how caps work.

# How to use it

| Key | Default | What it does |
| - | - | - |
| `admin.write_keys` | none | array of `{id, key}`; `x-api-key` may list, set, delete caps; key at least 32 chars; ids unique |
| `admin.read_keys` | none | read-only keys for every GET endpoint |
| `admin.admin_groups` | none | IdP groups with full admin via normal gateway JWT (audits as `oidc:<sub>`) |
| `admin.blocked_message` | none | appended verbatim to the `429 billing_error` |
| `admin.audit_retention_days` | `365` | `admin_audit` sweep |
| `admin.spend_retention_months` | `13` | `spend` counter sweep |
| `admin.identity_retention_days` | `90` | `principal_emails` (PII) last-seen TTL |
| `admin.group_limit_mode` | `min` | `min` or `max` across several group caps |
| `admin.pooled_conflict_rule` | `default_order` | or `priority_list`; v2.1.319 or later |
| `admin.pooled_priority_order` | none | up to 50 group names, with `priority_list` |
| `enforcement.fail_closed_on_error` | `false` | `true` blocks inference when the store is unreachable; needs an `admin:` block |
| `pricing.multiplier` | `1` | above 0 and at most 10; above 1 is a markup (v2.1.271 or later) |
| `pricing.overrides` | none | rows `{upstream, model, input, output, cache_read, cache_write}` in USD per million tokens, each above 0 and at most 10000, all four required |

Pooled budget: one monthly limit a group spends against, set with `pooled_budget` in the cap request (for example `"pooled_budget": {"amount": "500000"}`). A developer in several pooled groups spends against the first budget under its limit; `default_order` is largest limit first, `priority_list` follows `pooled_priority_order`.

Pricing needs v2.1.227 or later and an `admin:` block, or from v2.1.268 a `managed:` block with a policy. From v2.1.268 the gateway also pushes the rates to matched clients as the `modelPricing` managed setting (clients v2.1.242 or later); a policy can opt out with `modelPricing: {}`. Overrides match the most specific row; web search stays at the 0.01 USD list price (multiplier still applies); unknown upstream names fail boot.

`login_notice` (up to 500 characters, v2.1.319 or later on gateway and client) shows text at sign-in.

# Limits and defaults

A gateway older than the version noted refuses to start when it finds a newer key; upgrade every replica before adding a key and remove it before rolling back.
