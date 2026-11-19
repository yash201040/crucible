---
type: "Feature"
title: "Self-hosted environments overview"
description: "Run Claude Code cloud sessions on your own infrastructure through environments and runners, in public beta on Team and Enterprise."
resource: "https://code.claude.com/docs/en/self-hosted-environments"
tags: [self-hosted, cloud-sessions, runners, beta, environments]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [web, desktop, mobile, cli, cloud]
requires: "Team or Enterprise plan; an Owner turns on Allow self-hosted environments; cloud sessions enabled"
identifiers:
  - "claude --cloud"
  - "--environment"
  - "Allow self-hosted environments"
  - "api.anthropic.com"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments"
    resource: "https://code.claude.com/docs/en/self-hosted-environments"
    title: "Self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A self-hosted environment executes Claude Code cloud sessions (sessions run somewhere other than the developer's machine) on infrastructure your organization operates, instead of Anthropic's. Cloud sessions start from claude.ai, the mobile and desktop apps, `claude --cloud`, and cloud scheduled tasks. Terminal and IDE sessions always run on the developer's machine, so nothing here applies to them. For an always-on own machine driven from other devices, the page points to Remote Control (also on Pro, Max, Ultra).

Three parts: **environment** (named destination created in claude.ai admin settings, groups runners), **runner** (program on your hosts that executes sessions, like a CI runner), **session** (one task). The session-start UI shows an environment picker listing Anthropic-hosted and your environments. The control plane queues the session; a runner claims it, clones the chosen repository, and starts a Claude Code child process. Anthropic never connects into your network.

# How to use it

An Owner enables **Allow self-hosted environments** on the Cloud environments admin page (`https://claude.ai/admin-settings/cloud-environments`). Run runners yourself, or use the autoscaling orchestrator that starts runners as sessions queue. Sibling pages: quickstart, deploy, configuration, testing, reference, identity.

# Limits and defaults

- Public beta; Team and Enterprise only; off by default.
- Unavailable with Zero Data Retention or the HIPAA configuration.
- Inference uses the Anthropic API unless the runner is configured for Amazon Bedrock or Google Cloud's Agent Platform; on such a runner server-managed settings and claude.ai organization policies do not reach sessions. Session content goes to Anthropic either way.
- Repositories: GitHub or GitHub Enterprise Server; an `--environment` dispatch can also use another git host.
- Claude Tag sessions can run in them but cannot use Access bundles yet; Claude Security and Code Review sessions do not route to them yet.
- Billing: counts toward organization Claude Code usage like Anthropic-hosted environments.
- Runners run on Linux or macOS hosts per the configuration page.

# Notes

You own the runner image, fleet and network. Repository checkouts, build artifacts, secrets and created files stay on your machines; the conversation (prompts, responses, tool results) goes to `api.anthropic.com` and Anthropic stores the transcript so sessions resume from other surfaces. Orchestration, queueing and claude.ai remain Anthropic-hosted.
