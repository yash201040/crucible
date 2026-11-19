---
type: "Guide"
title: "Filesystem configuration for agent containers"
description: "Mount code read-only, sanitize credential files, and use tmpfs, overlay or dedicated volumes for writes."
resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
tags: [filesystem, docker, secrets, read-only, tmpfs]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk, cli]
requires: ""
identifiers:
  - "-v /path/to/code:/workspace:ro"
  - "--tmpfs /workspace:rw,noexec,size=500m"
  - ".dockerignore"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-secure-deployment"
    resource: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
    title: "Securely deploying AI agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Read-only mounting (`docker run -v /path/to/code:/workspace:ro agent-image`) lets the agent analyze but not modify code. Even read-only access can expose credentials.

# How to use it

Files to exclude or sanitize before mounting: `.env`, `.env.local`; `~/.git-credentials`; `~/.aws/credentials`; `~/.config/gcloud/application_default_credentials.json`; `~/.azure/`; `~/.docker/config.json`; `~/.kube/config`; `.npmrc`, `.pypirc`; `*-service-account.json`; `*.pem`, `*.key`. Copy only needed source files or use `.dockerignore`-style filtering.

Writable options: `--read-only` with `--tmpfs` mounts for ephemeral in-memory workspaces cleared at stop; an overlay filesystem so writes go to a separate layer to inspect, apply or discard; a dedicated volume for persistent output, kept apart from sensitive directories.
