---
type: "Feature"
title: "Repository identity attributes"
description: "OTEL_METRICS_INCLUDE_REPOSITORY tags metrics and events with vcs.* attributes derived from the origin remote."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, repository, vcs, attribution]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.269"
surfaces: [cli, cloud]
requires: "Claude Code v2.1.269 or later"
identifiers:
  - "OTEL_METRICS_INCLUDE_REPOSITORY"
  - "vcs.repository.url.full"
  - "vcs.owner.name"
  - "vcs.repository.name"
  - "vcs.provider.name"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With `OTEL_METRICS_INCLUDE_REPOSITORY=true`, a shared collector can attribute usage per repository. Values derive once per session from the `origin` remote; HTTPS and SSH remotes with the same host and path give identical values on GitHub, GitLab and Bitbucket Cloud.

# How to use it

| Attribute | Value |
| - | - |
| `vcs.repository.url.full` | browser URL without `.git` |
| `vcs.owner.name` | owner or group path; omitted for a single-segment path |
| `vcs.repository.name` | bare repository name |
| `vcs.provider.name` | `github`, `gitlab`, `bitbucket` or `gitea` when recognized; else omitted |

Values are lowercased; credentials, query strings and fragments never appear. Omitted when there is no `origin` remote, the remote is not URL-shaped, or the only enclosing repository is the home directory. A `vcs.*` key declared in `OTEL_RESOURCE_ATTRIBUTES` replaces the derived value; declaring `vcs.repository.url.full` stops Claude Code reading the remote at all. Declare all wanted `vcs.*` keys when HTTPS and SSH clones report different values (for example a self-hosted install with a path prefix).

# Notes

For cloud sessions set the variables on the cloud environment and allow the collector domain in network access. The attributes go only to your exporters; Anthropic's telemetry drops every `vcs.*` key.
