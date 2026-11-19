---
type: "Concept"
title: "Network isolation and the sandbox proxy"
description: "How sandboxed commands reach the network only through a local filtering proxy, which tools work, and the allowlist, approval and lockdown options."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, network, proxy, allowlist]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.219"
surfaces: [cli]
requires: ""
identifiers:
  - "HTTP_PROXY"
  - "HTTPS_PROXY"
  - "ALL_PROXY"
  - "NO_PROXY"
  - "sandbox.network.allowedDomains"
  - "sandbox.network.deniedDomains"
  - "sandbox.network.strictAllowlist"
  - "sandbox.network.allowManagedDomainsOnly"
  - "WebFetch(domain:...)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A sandboxed command has no direct network route. On Linux/WSL2 it runs in a separate network namespace; on macOS Seatbelt blocks everything except the proxy. Claude Code runs a proxy on your machine outside the sandbox, and points commands at it with `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` and related variables. The proxy checks each connection's hostname against allowed and denied domains. By default it does not terminate or inspect TLS.

# How to use it

- Tools that read proxy variables (`curl`, `npm`, `git` over HTTPS) connect once their host is allowed; an `allowedDomains` entry with no port allows every port.
- Tools that ignore them (plain `ssh`, most database drivers) cannot connect even to allowed hosts. UDP, HTTP/3 over QUIC and ICMP (`ping`) cannot leave the sandbox.
- Allowed domains start empty. Choosing Yes on a prompt allows the host for the session; "Yes, and don't ask again" saves a `WebFetch(domain:...)` allow rule to local settings (to user settings under an admin-required sandbox).
- Pre-allow with `network.allowedDomains`; `WebFetch(domain:...)` allow rules are also pre-allowed. `WebFetch(domain:...)` in the sandbox honors a leading `*.` and a bare `*` (bare `*` needs v2.1.186+); other wildcard positions have no effect on sandboxed commands.
- `strictAllowlist: true` (user, managed or `--settings`; ineffective in repository files; v2.1.219+) denies hosts outside the allowlist instead of prompting, for sandboxed commands only; WebFetch still follows permission rules.
- `allowManagedDomainsOnly` in managed settings blocks non-allowed domains and honors only managed `allowedDomains` and `WebFetch(domain:...)` allow rules.
- Corporate proxy: set `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY` in the settings `env` block (so background agents get them) or in the launch environment; Claude Code applies the allowlist then tunnels through the upstream proxy. `http://` and `https://` proxy URLs with basic auth work.

# Limits and defaults

The allowlist uses the requested hostname. The experimental `network.tlsTerminate` makes the proxy terminate TLS (needed for [mask credentials](./mask-credentials.md)).

See also [hosts outside allowed domains](./hosts-outside-allowed-domains.md).
