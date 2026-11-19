---
type: "Reference"
title: "Login restriction and gateway settings"
description: "Settings that force a login method, organization or cloud gateway and declare internal gateway address blocks."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, authentication, gateway, managed]
kind: "setting"
maturity: "unlabelled"
since: "2.1.212"
surfaces: [cli, sdk, ide]
requires: "Managed settings for enforcement"
identifiers:
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "forceLoginOrgUUID"
  - "gatewayInternalNetworks"
  - "claudeai"
  - "console"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys that restrict how people sign in. All default to unset.

# How to use it

| Name | Scope | Type | What it does |
| :- | :- | :- | :- |
| `forceLoginMethod` | any file; `"gateway"` honored only from the same sources as `forceLoginGatewayUrl` | `"claudeai"`, `"console"`, `"gateway"` | Restricts login kind. `"claudeai"` in any file also stops the keyless Console sign-in offer. Applies to every first-party login path (VS Code extension, Agent SDK, `claude setup-token`, `/install-github-app`) except the terminal's interactive login screen, which only pre-selects (before v2.1.212 only terminal logins applied it). With `"gateway"` from a machine managed source, leftover logins, API keys or `apiKeyHelper` credentials are not used (before v2.1.261 a leftover login was used); a `CLAUDE_CODE_USE_*` provider session does not need the gateway sign-in |
| `forceLoginGatewayUrl` | user or managed; read from managed source on the machine (`managed-settings.json`, macOS plist, Windows HKLM, policy helper); v2.1.295+ also reads user settings on a machine with none of those; ignored in HKCU and server-managed | string, full URL with scheme | URL the `/login` Cloud gateway screen connects to (Enter to connect). In managed settings this key or `forceLoginMethod: "gateway"` makes the machine gateway-only except `CLAUDE_CODE_USE_*` provider sessions. Invalid URL reported at sign-in; rest of file still applies |
| `forceLoginOrgUUID` | any file | string UUID or array of UUIDs | From a managed source, requires claude.ai logins to belong to that org (or any of several). In any file a single UUID pre-selects the org during login (an array pre-selects nothing), and the keyless Console sign-in is no longer offered (an API key is created instead). A managed empty array or wrong-type value blocks Anthropic-account users from starting or logging in. A `policyHelper` emitting a wrong type fails its run |
| `gatewayInternalNetworks` | managed, from a machine source only (not HKCU, not server-managed). Needs v2.1.268+ | array of at most 4 IPv4 CIDR blocks, `/8` to `/32`, non-overlapping and not overlapping private space | Lets `/login` accept a gateway inside a listed public block, direct connection only, with the machine's own address in the same block. Documentation ranges, VPN and NAT64 client ranges and reserved space (multicast) are refused. An invalid entry or non-list makes `/login` refuse every new gateway sign-in until fixed; existing sign-ins keep working |

# Limits and defaults

Without `gatewayInternalNetworks`, `/login` connects to a gateway only on a private address.
