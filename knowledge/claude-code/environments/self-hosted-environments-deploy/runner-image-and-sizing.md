---
type: "Guide"
title: "Build the runner image and size resources"
description: "Dockerfile starting point, version pinning, CPU and memory starting values, per-session memory limits, and pid limits for runner containers."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, docker, kubernetes, sizing, version-pinning]
kind: "mixed"
maturity: "beta"
since: "2.1.224"
surfaces: [cloud]
requires: "Claude Code v2.1.224+ (v2.1.229+ and python3 for Claude Tag sessions)"
identifiers:
  - "FORCE_AUTOUPDATE_PLUGINS"
  - "--exec-path"
  - "--min-idle"
  - "podPidsLimit"
  - "--pids-limit"
  - "TasksMax"
  - "MemoryMax"
  - "pids.max"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Anthropic publishes no pre-built runner image. You build one around the `claude` binary (downloaded from `https://downloads.claude.ai/claude-code-releases/<version>/<platform>/claude`, platforms `linux-x64`, `linux-arm64`, and `-musl` variants) plus git, curl, ca-certificates, openssh-client, jq and python3 (python3 needed for Claude Tag hook scripts).

# How to use it

- Pin version: build with a fixed `CLAUDE_CODE_VERSION`; the `stable` file gives the current stable release. Sessions run the runner's own binary and auto-update is off inside sessions; a host update takes effect at next runner start. Check model-required minimum versions first, otherwise the API returns "Claude Code does not support this model". For on-demand runners change the image the `spawn-runner` hook starts; already-up runners (including `--min-idle` standbys) keep their version. `--exec-path` or a `command` hook can start a different binary. `FORCE_AUTOUPDATE_PLUGINS=1` lets plugins update.
- Per-session starting values: memory request and limit 4 GiB each; CPU request 2, limit 4. At `--capacity N` multiply by N; for several runner containers per host multiply by the sum of capacities. The runner does not divide resources between sessions.
- For isolated memory limits, run `--capacity 1` per container (`limits.memory`, Docker `--memory`, Compose `mem_limit`) or one runner per host under systemd with `MemoryMax`. `ulimit -v` and kubelet `singleProcessOOMKill` do not separate sessions.
- Process/thread limits (`EAGAIN`, `Resource temporarily unavailable`): `podPidsLimit` (kubelet; per Pod), Docker `--pids-limit`/`pids_limit`, systemd `TasksMax` (default from `DefaultTasksMax`, 15% of lowest kernel limit), `ulimit -u` (not enforced for root). Measure peak with `pids.peak` or `pids.current` in the runner cgroup, multiply by sessions sharing the limit; kernel log line `cgroup: fork rejected by pids controller in` shows hits.

# Notes

Kubernetes and Compose recipes on the page use `--capacity 4`, which does not give per-session isolation; use `--capacity 1` per container or on-demand runners for production.
