---
type: "Feature"
title: "Network access levels and allowed domains"
description: "Each environment has one of three network access levels (None, Limited, Full) plus an allowed-domains list; some paths bypass it."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, network, allowlist, isolation]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud, desktop, mobile]
requires: ""
identifiers:
  - "None"
  - "Limited"
  - "Full"
  - "Allow package managers"
  - "Allowed domains"
  - "*.frame.claudeusercontent.com"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The **Network access** field of an environment controls outbound connections of its sessions. A new environment starts at **Limited** with **Allow package managers** checked.

# How to use it

| Level | Outbound connections |
| - | - |
| **None** | No outbound access through the session's network |
| **Limited** | Default allowlist of package registries, GitHub and cloud SDKs while Allow package managers is checked, plus domains you list |
| **Full** | Any domain |

- Allow domains: choose Limited, list one domain per line in **Allowed domains**; leading `*.` matches subdomains. Clear Allow package managers to drop the default allowlist.
- Changing an Anthropic-hosted environment's level applies to existing sessions within about a minute (for requests going through the network allowlist); no new session needed.
- A shared environment is read-only in the dialog; an Owner changes it on the admin page.
- Environments saved as **Trusted** open as Limited with package managers checked; saved as **Custom** open as Limited with their list, or Full if the list had a bare `*`.
- Cloud scheduled task editor also has the network access control.

# Limits and defaults

Paths that bypass the allowlist at any level: GitHub (via its proxy); enabled MCP connectors (traffic goes through Anthropic's servers; turn off connectors you do not need); hosts of the environment's network secrets (except those that never get a secret); the Anthropic API for Claude Code's own requests, even at None.

`*.frame.claudeusercontent.com` is not needed for reading your organization's artifacts (Claude Code reads them via its Anthropic connection). Keep it in the list when sessions open another organization's public artifacts, or for the local CLI or self-hosted runner allowlists.

Each environment has its own list; domains cannot be pushed org-wide.
