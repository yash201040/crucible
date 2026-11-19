---
type: "Guide"
title: "Attribute telemetry to Desktop SSH sessions"
description: "Name the remote machine of a Desktop SSH session with OTEL_RESOURCE_INCLUDE_HOST or a custom attribute set on that machine."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, desktop, ssh, attribution]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [desktop]
requires: "Claude Code v2.1.326 or later on the remote machine for OTEL_RESOURCE_INCLUDE_HOST"
identifiers:
  - "OTEL_RESOURCE_INCLUDE_HOST"
  - "OTEL_RESOURCE_ATTRIBUTES"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to see which remote machine a Desktop SSH session ran on: `OTEL_RESOURCE_INCLUDE_HOST=1` (host.name only in the resource block) or a custom `host.name` in `OTEL_RESOURCE_ATTRIBUTES` (also on datapoints and events by default).

# How to use it

Set the variable on the remote machine, in the `env` block that turns telemetry on, in the managed settings file the session reads. Write each machine's name literally (e.g. `"OTEL_RESOURCE_ATTRIBUTES": "host.name=build-7"`); `$(hostname)` is not expanded.

# Notes

If the name does not arrive: it was set on the computer running Desktop (not passed to SSH sessions); it was exported in `/etc/profile` or another login-shell-only file (Desktop does not start Claude Code via a login shell); a value contains a space (run `/status` on the remote machine); or something already sets the variable in the launch environment, which takes precedence over settings files (see the debug log).
