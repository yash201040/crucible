---
type: "Reference"
title: "Orchestrator CLI flags and SCM connector"
description: "Flags of self-hosted-runner orchestrator for on-demand runners: hook concurrency and timeouts, pre-warming, shutdown drain, SCM connector."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, orchestrator, on-demand-runners, cli-flags, spawn-runner]
kind: "cli_flag"
maturity: "beta"
since: "2.1.299"
surfaces: [cloud, cli]
requires: ""
identifiers:
  - "self-hosted-runner orchestrator"
  - "--hook-concurrency"
  - "--hook-timeout"
  - "--expected-spawn-seconds"
  - "--min-idle"
  - "--shutdown-drain-sec"
  - "--debug-dir"
  - "--scm-connector-host"
  - "--scm-connector-id"
  - "--scm-connector-provider"
  - "--scm-connector-ca-file"
  - "--scm-connector-host-rewrite"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The orchestrator subcommand spawns on-demand runners. It accepts `--api-url`, `--environment-secret-file`, `--hooks-dir`, `--health-port`, `--log-level` like the runner, except `--hooks-dir` is required and must hold a `spawn-runner` hook. It also takes the flags below.

# How to use it

| Flag | Default | What it does |
| :- | :- | :- |
| `--hook-concurrency <n>` | `4` | Max parallel `spawn-runner` hooks; also caps requests claimed per poll; next poll waits for all started hooks to finish |
| `--hook-timeout <sec>` | `60` | Terminates the hook's process tree; timeout plus 5 s kill grace must stay below `--expected-spawn-seconds` (checked at startup) |
| `--expected-spawn-seconds <sec>` | `120` | Expected p99 from spawn request to runner registration; server range 10 to 3600; sent as lease, after which the session is re-offered with a new order ID; same on all replicas |
| `--min-idle <n>` | `0` | Keep n idle slots free with standby runners; pair with runner `--exit-if-unused-min` |
| `--shutdown-drain-sec <n>` | `0` | On SIGTERM let running hooks and unanswered poll finish up to n s (max 3600); v2.1.299+ |
| `--debug-dir <path>` | unset | Writes each work order and hook stderr to disk; debug only |
| `--scm-connector-host <host[:port]>` | unset | GitHub Enterprise Server host (port 443) |
| `--scm-connector-id <n>` | required with host | Numeric ID of the organization's GHES connection |
| `--scm-connector-provider <slug>` | `ghe` | Matches `^[a-z0-9-]{1,32}$` |
| `--scm-connector-ca-file <path>` | unset | Extra PEM CA bundle |
| `--scm-connector-host-rewrite <from>=<to_host:to_port>` | unset | End-to-end testing only |

# Limits and defaults

The SCM connector is stated as not available: leave its flags unset (setting the host keeps a connection retrying; runners still start). It is a standing WebSocket from the orchestrator to the control plane, retrying with exponential backoff capped at 30 s plus jitter. The orchestrator does not accept the proxy-authorization flags; pass them to the runners it starts.
