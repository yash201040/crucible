---
type: "Reference"
title: "Sandbox network settings"
description: "sandbox.network keys: allowedDomains, deniedDomains, strictAllowlist, allowManagedDomainsOnly, proxy ports, unix sockets, local binding, tlsTerminate."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [sandbox, network, proxy, domains]
kind: "setting"
maturity: "experimental"
since: "2.1.229"
surfaces: [cli, headless]
requires: "strictAllowlist v2.1.219; bracketed IPv6 v2.1.229"
identifiers:
  - "sandbox.network"
  - "sandbox.network.allowedDomains"
  - "sandbox.network.deniedDomains"
  - "sandbox.network.strictAllowlist"
  - "sandbox.network.allowManagedDomainsOnly"
  - "sandbox.network.httpProxyPort"
  - "sandbox.network.socksProxyPort"
  - "sandbox.network.allowUnixSockets"
  - "sandbox.network.allowAllUnixSockets"
  - "sandbox.network.allowLocalBinding"
  - "sandbox.network.allowMachLookup"
  - "sandbox.network.tlsTerminate"
  - "sandbox.network.tlsTerminate.caCertPath"
  - "sandbox.network.tlsTerminate.caKeyPath"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls which hosts, ports and sockets sandboxed commands reach. Outbound traffic goes through a proxy enforcing these lists. Array sub-keys merge across scopes unless a repository lock applies; `WebFetch(domain:...)` allow and deny rules feed the same lists. `tlsTerminate` is labelled experimental on the page.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `allowedDomains` | Any file (managed only when `allowManagedDomainsOnly`) | array of domain, `*.wildcard`, IP literal, optional `:port` | unset | Pre-allow so there is no prompt; no port means every port. IPv6 bracketed: `"[::1]"`, `"[::1]:443"` |
| `deniedDomains` | Any file | array, same syntax | unset | Blocked even if an allow entry matches; merges from all sources even under `allowManagedDomainsOnly`; trailing-dot FQDN equals plain name |
| `strictAllowlist` | User or managed | Boolean | `false` | Deny hosts outside the allowlist instead of prompting. When `false`, permission mode decides: auto checks per-command allowed domains; `dontAsk` denies; `bypassPermissions` (and interactive plan mode where bypass is available) allows; otherwise asks. Sandboxed commands only; `WebFetch` follows its own rules. Once any honored source sets `true` it stays on |
| `allowManagedDomainsOnly` | Managed | Boolean | `false` | Honor only managed `allowedDomains` and `WebFetch(domain:...)` allows; auto-block others; makes the sandbox admin-required; only managed settings can set a proxy port |
| `httpProxyPort` | Any file (subject to other limits) | number | unset | Use your own HTTP proxy; Claude Code stops applying its domain lists and prompts to traffic sent there |
| `socksProxyPort` | Any file | number | unset | Your own SOCKS5 proxy; with only one of the two set, Claude Code still runs its own proxy for the other protocol |
| `allowUnixSockets` | Any file | array of socket paths | unset (all blocked) | macOS only; ignored on Linux/WSL2. Broad grants (e.g. `/var/run/docker.sock`) let a command control the daemon |
| `allowAllUnixSockets` | Any file | Boolean | `false` | Allow every Unix socket. On Linux/WSL2 the seccomp filter blocks `socket(AF_UNIX, ...)`, so this is the only way; `true` also allows `AF_VSOCK`; on WSL2 reopens the interop socket for `cmd.exe`, `powershell.exe`. Missing filter (see `/sandbox` Dependencies tab) means no blocking |
| `allowLocalBinding` | Any file | Boolean | `false` | macOS: listen on ports and connect to any localhost port; no effect on Linux/WSL2 (own loopback per command) |
| `allowMachLookup` | Any file | array of service names | unset | macOS XPC/Mach names (iOS Simulator, Playwright); trailing `*` prefix, `"*"` all; sandbox does not confine what those services do |
| `tlsTerminate` | User or managed | object `{caCertPath, caKeyPath}` | unset | Proxy terminates TLS to read HTTPS requests; `{}` generates an ephemeral CA, or give your own paths. Required for `mask` credential substitution. Highest source wins: managed, then `--settings`, then user |

```json
{ "sandbox": { "network": { "allowedDomains": ["github.com", "*.npmjs.org", "api.example.com:443"], "deniedDomains": ["uploads.github.com"] } } }
```

# Limits and defaults

- Scope for most keys is Any file with limits on project/local settings under an admin-required sandbox; a repository cannot turn on `strictAllowlist` or `tlsTerminate` or supply a CA.
- A custom proxy takes over filtering entirely.
