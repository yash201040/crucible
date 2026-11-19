---
type: "Concept"
title: "Default environment and how sessions pick one"
description: "Cloud sessions run in an environment; Default has Limited network and no config, and each surface picks an environment differently."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, environments, selection, remote-env]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.224"
surfaces: [cli, desktop, web, mobile, cloud]
requires: "Pro, Max, Ultra or Team plan; Enterprise with premium seats or Chat + Claude Code seats"
identifiers:
  - "/remote-env"
  - "/web-setup"
  - "claude --cloud"
  - "--environment"
  - "remote.defaultEnvironmentId"
  - "ccpool_"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each cloud session runs in a cloud environment. An environment sets network access, environment variables, network secrets and a setup script. The same environments apply to the Desktop app, mobile app, claude.ai/code, `claude --cloud`, cloud scheduled tasks (routines) and Claude Tag. Each surface can also route to a self-hosted environment. Remote Control sessions use your own machine, not a cloud environment.

# How to use it

- The **Default** environment is created by onboarding: `/web-setup` creates it; Pro/Max/Ultra web onboarding gives it automatically; Team/Enterprise web onboarding shows a "Create your first cloud environment" form (unless an Owner enabled Quick setup) and "Create & finish" gives the same Default.
- Default has Limited network access and defines no variables or setup script, so sessions have only the pre-installed tools.
- With one environment, every session uses it. With several: desktop, mobile and claude.ai/code use the selector (an organization default set by an Owner fills it when unpicked; project threads use the project's environment setting).
- From the CLI: the `/remote-env` pick, else the Anthropic-hosted environment if your list has one, else the first environment that is not a Remote Control bridge environment.
- For a self-hosted environment, `--environment <environment-id>` with its `ccpool_` ID overrides the `/remote-env` pick and fallback for that invocation (dispatching a session). Anthropic-hosted `env_` IDs are rejected by the flag; use `/remote-env` for those.

# Limits and defaults

The `--environment` flag requires Claude Code v2.1.224 or later.
