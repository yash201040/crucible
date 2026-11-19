---
type: "Feature"
title: "Network secrets (agent proxy credentials)"
description: "Store an API key on a cloud environment so Anthropic's agent proxy attaches it to requests for listed hosts without the session seeing it."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, secrets, agent-proxy, credentials]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud, desktop, mobile]
requires: "Pro, Max, Ultra, Team or Enterprise; Anthropic-hosted environment"
identifiers:
  - "Network secrets"
  - "Allowed websites"
  - "Custom headers"
  - "Authorization"
  - "X-Api-Key"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A network secret is a key or token stored on an Anthropic-hosted cloud environment. Anthropic's agent proxy adds it to requests for the hosts you list after each request leaves the VM, so the key never enters the VM (not in env vars or files). It applies in every session in the environment, whoever started it, until deleted.

# How to use it

1. Open the environment for editing, select the **Network secrets** row (for a shared environment, an Owner uses the Cloud environments page in admin settings).
2. **Add secret**. Keep **Secret type** Bearer for header-carried keys. **Allowed websites**: hosts such as `api.example.com`; a leading `*.` matches subdomains. **Custom headers**: one row; default header name `Authorization`, prefix `Bearer`, paste the key as Value. For `X-Api-Key`-style headers change the name and clear the prefix.
3. **Add**. Saved without Save changes; the value cannot be viewed again.

Without an organization admin role on Team/Enterprise, **Add secret** is a shorter form: one **Host** (no `*.` wildcard), **Secret type** Token (with **Header** field for non-Authorization headers) or Username and password.

Verify by asking Claude to `curl` the API in a session. A secret marked **Not sent** shows why in a note. Two secrets with overlapping but non-identical hosts get no marker and the proxy sends only one. To change hosts or value, delete and re-add.

# Limits and defaults

- Requirements: Anthropic-hosted environment (not self-hosted); API reachable from the internet; no customer-managed encryption keys. On Team/Enterprise, Owners hold the organization admin role; Admins do not.
- Sessions can reach listed hosts even when the network access level would block them.
- The proxy never attaches a secret to: GitHub (handled by the GitHub proxy); `api.anthropic.com`, `registry.npmjs.org`, `jsr.io`, `npm.jsr.io`, `pypi.org`, `files.pythonhosted.org`, `index.crates.io`, `proxy.golang.org`; setup script requests (the proxy connects after the setup script ran); Claude Code's own telemetry export.
