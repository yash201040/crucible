---
type: "Feature"
title: "Environment caching"
description: "Anthropic snapshots the filesystem after a setup script completes within about five minutes and reuses it for later sessions."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, caching, snapshot, startup]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: "Anthropic-hosted environment"
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The setup script runs the first time you start a session in an environment. If it completes within roughly five minutes, Anthropic snapshots the filesystem and reuses it as the starting point for later sessions, which then skip the setup script. You do not enable or manage caching.

# How to use it

Put slow provisioning in the setup script: packages, `docker compose pull` or `docker compose build` (pulled images stay on disk). The cache is a filesystem snapshot: installed packages, pulled images and written files carry over. Running processes (a started database, a `docker compose up` stack) do not; start them per session by asking Claude or with a SessionStart hook.

# Limits and defaults

- Setup over roughly five minutes: environment is not cached.
- The script reruns to rebuild the cache when you change the setup script or allowed network hosts, and when the cache expires after roughly seven days.
- The setup script does not run when a VM is restored after idle.
