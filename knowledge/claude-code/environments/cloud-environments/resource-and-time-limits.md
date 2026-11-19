---
type: "Limit"
title: "Cloud VM resource and time limits"
description: "Approximate VM ceilings (4 vCPU, 16 GB, 30 GB) and the time limits for commands, hooks, setup scripts and idle sessions."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, limits, timeouts, resources]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: "Anthropic-hosted environment"
identifiers:
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
  - "async: true"
  - "timeout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limits for Anthropic-hosted cloud sessions. The resource ceilings are approximate and may change.

# Limits and defaults

| Limit | Value |
| - | - |
| vCPUs | 4 |
| RAM | 16 GB |
| Disk | 30 GB |
| Foreground command | waits 2 minutes by default; Claude can ask up to 10 minutes (the cloud environment sets no command timeout of its own) |
| Command past timeout | moved to background unless it starts with `sleep`; may run up to 30 more minutes |
| SessionStart `command` hook | cancelled after 600 seconds unless `timeout` (seconds) is set; not enforced for `async: true` hooks |
| Setup script | longer than roughly 5 minutes is not cached |
| Idle session | VM pauses after a few minutes of inactivity with files saved; a paused VM can later be reclaimed |

The VM may stop tasks needing significantly more memory (large builds, memory-intensive tests). For bigger workloads use Remote Control on your own hardware or a self-hosted environment.

# How to use it

Set `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` (milliseconds) in the environment variables, for example `BASH_DEFAULT_TIMEOUT_MS=600000` for a 10 minute default. Setting `BASH_DEFAULT_TIMEOUT_MS` above `1800000` also lengthens the background limit.
