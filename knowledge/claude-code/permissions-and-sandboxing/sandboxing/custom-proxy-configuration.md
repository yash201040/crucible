---
type: "Feature"
title: "Custom sandbox proxy ports"
description: "Replace the built-in sandbox proxy with your own local proxy via httpProxyPort and socksProxyPort, and which settings files may set them."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, proxy, network, tls-inspection]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.network.httpProxyPort"
  - "sandbox.network.socksProxyPort"
  - "HTTPS_PROXY"
  - "HTTP_PROXY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

To inspect, filter or log sandbox traffic with your own tooling, run a proxy on the same machine and set its localhost ports. For a corporate proxy elsewhere on the network, set `HTTPS_PROXY` instead so Claude Code's allowlist still applies.

# How to use it

```
{ "sandbox": { "network": { "httpProxyPort": 8080, "socksProxyPort": 8081 } } }
```

If a port and `HTTPS_PROXY`/`HTTP_PROXY` are both set, Claude Code does not forward your proxy's traffic to the proxy those variables name; configure your proxy to forward to it. Which files may set a port (first match applies): `allowManagedDomainsOnly` on: managed settings only; admin-required sandbox or a narrower network lock: managed, `--settings` and user settings; otherwise any settings file. A port set elsewhere is ignored. Before v2.1.285 any settings file could set a port.

# Limits and defaults

Once a port applies, your proxy must filter everything: `allowedDomains`, `deniedDomains`, `strictAllowlist`, approval prompts and the local-address check stop applying to that traffic. If only one port is set, Claude Code's lists on the other proxy do not limit what the command reaches through yours.
