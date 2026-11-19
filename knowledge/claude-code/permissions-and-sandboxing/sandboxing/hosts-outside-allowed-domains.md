---
type: "Reference"
title: "Hosts outside allowed domains, local addresses, IPv6"
description: "What happens per permission mode when a sandboxed command reaches an unlisted host, the loopback and metadata refusal, and IPv6 entry spelling."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, network, permission-modes, ipv6]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.284"
surfaces: [cli]
requires: ""
identifiers:
  - "bypassPermissions"
  - "acceptEdits"
  - "dontAsk"
  - "sandbox.network.deniedDomains"
  - "sandbox.network.strictAllowlist"
  - "sandbox.network.allowManagedDomainsOnly"
  - "claude doctor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A sandboxed command that connects to a host not in the allowed domains stays in the sandbox and waits for a decision. In an interactive terminal session:

| Permission mode | What happens |
| - | - |
| `bypassPermissions`, and plan mode with bypass available | Allowed without a prompt |
| Manual, `acceptEdits`, and plan mode otherwise | Prompt |
| Auto mode | Refused unless the command listed the host and the classifier approved |
| `dontAsk` | Refused |

With `strictAllowlist` or `allowManagedDomainsOnly` on, the proxy refuses in every mode. A host in `deniedDomains` is refused in every mode.

# How to use it

Local addresses: after a hostname passes the allowlist, the proxy resolves it and refuses the connection if it resolves only to local addresses (loopback such as `127.0.0.1`, link-local such as the `169.254.169.254` metadata endpoint, addresses of your own machine). `localhost` and `*.localhost` may resolve to loopback. Intranet names resolving to private ranges like `10.0.0.0/8` connect. To permit a refused address, add the IP to `allowedDomains` (e.g. `"127.0.0.1:8080"`). The check applies to hostnames only and is skipped for connections sent through an upstream corporate proxy. The 403 body reads like `Connection to myapp.test blocked: resolved to a loopback address`. Before v2.1.284 the proxy connected to whatever address an allowed hostname resolved to.

IPv6 in `allowedDomains`, `deniedDomains` or `WebFetch(domain:...)`: use brackets, `"[::1]"` (all ports) or `"[::1]:443"` (v2.1.229+). Unbracketed `::1:443` is ambiguous: deny lists block every reading; allow lists rewrite to host-and-port if it parses, or may drop the entry. `claude doctor` warns `Sandbox network domain entries have unreliable spellings`.
