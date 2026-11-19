---
type: "Feature"
title: "Connecting developers to a Claude apps gateway"
description: "Managed-settings keys for gateway sign-in, TLS fingerprint pinning, gatewayInternalNetworks, Desktop bootstrap and CI behavior."
resource: "https://code.claude.com/docs/en/claude-apps-gateway"
tags: [gateway, login, managed-settings, ci]
kind: "setting"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli, desktop, headless]
requires: "User-settings gateway URL needs v2.1.295+; gatewayInternalNetworks needs v2.1.268+; Desktop connection needs v2.1.203+ on the gateway server"
identifiers:
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "parentSettingsBehavior"
  - "gatewayInternalNetworks"
  - "forceLoginOrgUUID"
  - "NO_PROXY"
  - "bootstrapUrl"
  - "ANTHROPIC_API_KEY"
  - "ANTHROPIC_AUTH_TOKEN"
  - "apiKeyHelper"
  - "/login"
  - "/logout"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway"
    title: "Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Developers connect with one browser sign-in using their corporate account; no claude.ai account, API key or subscription needed. The CLI pins the gateway's TLS leaf certificate fingerprint per hostname on first connect and rechecks it on sign-in, silent refresh and managed-settings fetch (inference uses normal TLS validation). HTTPS-proxied requests skip the pin, so put the gateway host in `NO_PROXY` (and `no_proxy`). `/login` shows the first 16 hex characters of the SHA-256 fingerprint; certificate rotation re-prompts every developer (and re-shows any security approval dialog).

# How to use it

- Managed settings file (MDM or disk): `{"forceLoginMethod": "gateway", "forceLoginGatewayUrl": "https://<gateway>", "parentSettingsBehavior": "merge"}`. `forceLoginMethod` alone, without a URL, shows a "Contact your IT administrator" message. These keys belong in the pushed file; the gateway's `managed.policies[].cli` block only reaches already-connected clients.
- No managed settings: put `forceLoginMethod` and `forceLoginGatewayUrl` in `~/.claude/settings.json` (v2.1.295+; user settings only, not project or local; ignored once any managed source reaches the machine).
- `gatewayInternalNetworks`: managed-only setting listing public IPv4 blocks your organization owns (v2.1.268+). At most 4 blocks, each `/8` to `/32`, no overlaps, none overlapping private, VPN/NAT64, documentation, reserved or multicast ranges. A gateway in a listed block must resolve entirely inside that block, the client must connect from the same block (no NAT, container, WSL2 or outside-pool VPN) and directly (not via `HTTPS_PROXY`). Invalid lists refuse every new gateway sign-in. Pair with the gateway's `access_control.allow_cidrs` and `listen.trusted_proxies`.
- Desktop: set `bootstrapUrl` in Claude Desktop managed configuration to `<listen.public_url>/user/bootstrap` and opt the policy in with a `desktop` key. Desktop and CLI sign in separately.
- CI and remote machines: there is no service-token flow; gateway sign-in always uses the browser device flow, so CI cannot authenticate (configure CI against the provider directly and leave the login keys off runners). A session using `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` on a machine whose managed settings set the login keys exits at startup. Once a developer is signed in, `claude -p` and Agent SDK sessions on that machine use the gateway session and policy. A remote box works by running `/login` over SSH and opening the link on a laptop.

# Limits and defaults

An optional `email` field in the token response lets the developer confirm the account (v2.1.275+ client); the built-in server does not return it. Sessions refresh before `ttl_hours` expiry; failed refresh after deprovisioning prompts re-login.
