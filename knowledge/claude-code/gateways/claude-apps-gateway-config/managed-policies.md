---
type: "Feature"
title: "Gateway managed policies by IdP group"
description: "The managed block serves per-user Claude Code settings and a Claude Desktop overlay, chosen by IdP group or email domain."
resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
tags: [gateway, managed-settings, policies, permissions, desktop]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk, ide, desktop]
requires: "gateway sign-in via /login"
identifiers:
  - "managed.policies"
  - "managed.policy_mode"
  - "match"
  - "match.groups"
  - "match.email_domain"
  - "cli"
  - "code"
  - "settings"
  - "desktop"
  - "serve_to_desktop"
  - "availableModels"
  - "enforceAvailableModels"
  - "deniedModels"
  - "availableModelsMatch"
  - "permissions.deny"
  - "permissions.allow"
  - "permissions.disableBypassPermissionsMode"
  - "allowManagedPermissionRulesOnly"
  - "managedMcpServers"
  - "promptCacheTtl"
  - "subagentPromptCacheTtl"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "parentSettingsBehavior"
  - "allowedProviders"
  - "/managed/settings"
  - "/user/bootstrap"
  - "bootstrapUrl"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway-config"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway-config"
    title: "Claude apps gateway configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`managed.policies` is an ordered list of role policies, each with a `match` and a settings block. The gateway serves the matched policy per user at `GET /managed/settings` (ETag/304 caching). Each `cli` or `code` value is a full Claude Code `managed-settings.json` document in YAML, applied at the managed tier above user and project settings, and to every Claude Code invocation on the machine including `claude -p` and Agent SDK sessions. If the gateway is unreachable at startup, signed-in sessions exit rather than running without their policy.

# How to use it

Matchers: `match: {}` (everyone, the base layer), `{groups: [...]}` (any listed group, case-sensitive), `{email_domain: example.com}` (one bare domain), or both. By default the first matching policy wins and is merged onto the `match: {}` catch-all. `policy_mode: layered` (v2.1.316 or later) applies every matching policy.

Merge rules: allow-lists (`availableModels`, `permissions.allow`) are replaced whole; deny-lists and hook arrays are unioned; `env`, `modelOverrides`, `skillOverrides` merge by key.

`availableModels` is also enforced server-side at `/v1/messages` (a denied model gets `400`; an empty list denies all). Set `enforceAvailableModels: true` so the Default model resolves inside the list, and set `model` if the list holds no alias or built-in id. `deniedModels` and `availableModelsMatch` need v2.1.299 or later on the gateway and v2.1.283 or later on clients. The gateway also rejects a missing/empty `model` (`model is required`, v2.1.228+) or non-string (`model must be a string`, v2.1.221+).

Choose key `code` (recommended, v2.1.296 or later) or legacy `cli`/`settings`; mixing them stops boot. `code` reaches Claude Desktop's Code tab only if the policy has a `desktop` key, Desktop is 2.9939.2 or later, and client managed settings name the gateway over HTTPS.

Other policy features: `managedMcpServers` (http and sse remote servers, v2.1.259 or later; `mcpServers` is rejected); one-hour cache TTL via `promptCacheTtl: 1h` and `subagentPromptCacheTtl: 1h` (v2.1.242 or later; an upstream that rejects it fails the request with no retry; v2.1.286 needed for spend limits to price 1h writes); `CLAUDE_CODE_AUTO_COMPACT_WINDOW: "200000"` or `CLAUDE_CODE_DISABLE_1M_CONTEXT: "1"` in `env` (terminal sessions use the 1M window for Opus 4.7+, Sonnet 5+, Fable models, compacting near 967K).

Security approval dialog: interactive clients prompt before applying hooks, proxy/base-URL env vars, `apiKeyHelper`, `statusLine`, certain sandbox settings and `OTEL_EXPORTER_OTLP_ENDPOINT`. Non-interactive runs apply the settings for that run only without recording approval. Declining exits the session.

Client side (set on each machine via managed settings, not in the payload): `forceLoginMethod: "gateway"`, `forceLoginGatewayUrl`, `parentSettingsBehavior: "merge"`, optional `allowedProviders: ["gateway"]` (v2.1.285 or later; `claude gateway` refuses to run on a machine that sets it).

Desktop overlay (v2.1.203 or later): `/user/bootstrap` returns 404 unless the matched policy carries a `desktop` key (empty `desktop: {}` suffices). Set Claude Desktop's `bootstrapUrl` to `<listen.public_url>/user/bootstrap`. The gateway derives the model list, disabled tools and egress allowlist, and rejects keys it computes itself.

# Limits and defaults

A user matching no policy gets every catalog model and no managed settings. Empty `groups`, empty `email_domain` or entries stop the gateway at boot (before v2.1.232 they matched silently). `layered` mode refuses to start on a `!` pattern in Read/Edit rules and on hook limits outside the catch-all. Policy content changes reach clients on the next managed-settings poll (within an hour); group membership changes on the next silent refresh (bounded by `session.ttl_hours`). There is no SCIM endpoint.

# Notes

Test a policy against a throwaway Postgres database; boot connects to Postgres before checking policy contents. The `desktop` block rejects keys beginning `selfHosted` from v2.1.300. Gateway-delivered settings outrank MDM and local `managed-settings.json`.
