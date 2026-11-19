---
type: "Feature"
title: "Identify the machine a session ran on"
description: "OTEL_RESOURCE_INCLUDE_HOST adds host.name and host.id resource attributes; includes a troubleshooting checklist."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, host, resource-attributes, troubleshooting]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, desktop]
requires: "Claude Code v2.1.326 or later"
identifiers:
  - "OTEL_RESOURCE_INCLUDE_HOST"
  - "host.name"
  - "host.id"
  - "OTEL_RESOURCE_ATTRIBUTES"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Setting `OTEL_RESOURCE_INCLUDE_HOST=1` adds `host.name` (host name) and `host.id` (unhashed OS machine ID) to the resource block of metrics, events and traces, not to metric datapoints. The machine ID is `/etc/machine-id` on Linux, `IOPlatformUUID` on macOS, `MachineGuid` registry value on Windows; it is left out if unreadable (for example a container with no machine ID).

# How to use it

Set it under `env` in managed or user settings, or in the shell that starts `claude`, not in project or local settings. Both attributes name the machine Claude Code runs on (in a Desktop SSH session that is the remote machine). In a container `host.name` is the container's host name; declare the machine name yourself in `OTEL_RESOURCE_ATTRIBUTES` instead.

Troubleshooting when missing: Claude Code older than v2.1.326; set only in project or local settings (run `/status` to see ignored variables); value `0` in a managed or user file overrides a `1` set lower; set after session start (read once at startup); desktop-started local sessions do not get it from the shell profile; Anthropic-hosted cloud sessions do not add the attributes; any exporter listing `console` (remove it from the three exporter variables); a per-signal endpoint that is not a URL (write `http://10.0.0.1:4317`, not `10.0.0.1:4317`); a backend that hides resource attributes (with `prometheus` look at `host_name`/`host_id` labels of `target_info`).

# Notes

Host names often contain a person's name and `host.id` is a lasting identifier; Claude Code shows users no notice if set in managed settings.
