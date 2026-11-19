---
type: "Guide"
title: "Self-hosted environments quickstart"
description: "Prerequisites, guided and manual setup of one runner, and routing a first session to a self-hosted environment."
resource: "https://code.claude.com/docs/en/self-hosted-environments-quickstart"
tags: [self-hosted, quickstart, runner, environment-secret, setup]
kind: "mixed"
maturity: "beta"
since: "2.1.224"
surfaces: [cloud, cli]
requires: "Team or Enterprise plan; Owner enables Allow self-hosted environments; Claude Code v2.1.224+; git 2.24+; Linux or macOS runner host"
identifiers:
  - "claude self-hosted-runner"
  - "claude self-hosted-runner setup"
  - "claude self-hosted-runner --help"
  - "--environment-secret-file"
  - "--base-dir"
  - "claude auth login"
  - "./runner-setup/CHEAT-SHEET.md"
  - "Registered: runner_id="
  - "Picked up session"
  - "poll auth failed"
  - "[runner:exit] account workload drained"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-quickstart"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-quickstart"
    title: "Self-hosted environments quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A self-hosted environment runs Claude Code cloud sessions on infrastructure you operate, via runner processes. The quickstart builds the smallest one: one runner on one host serving a test session. The feature is in public beta.

# How to use it

Prerequisites: an Owner turns on **Allow self-hosted environments** (Cloud environments admin page; the **New** button is hidden otherwise); GitHub connector enabled and each developer's GitHub connection; Linux/macOS host or container (Windows not supported as a runner host) with outbound HTTPS to `api.anthropic.com`, `claude.ai` (install), and the git host; repository clonable by HTTPS URL without prompts (an SSH key alone is not enough); NTP-synced clock. Claude Code v2.1.224+ (v2.1.229+ and `python3` for Claude Tag sessions); check with `claude self-hosted-runner --help` (older versions print general help).

Guided: `claude self-hosted-runner setup` on a machine signed in with `claude auth login` as an Owner (API key or third-party provider fails org checks). It creates the environment, starts a runner, writes `./runner-setup/CHEAT-SHEET.md`, does not start a test session, and stops its runner at the end.

Manual:
1. Create environment (Admin > Cloud environments > Self-hosted environments > New > Create > **Copy environment key**). Shown once; expires 365 days after creation; `ccpool_...` ID stays visible. Rotate by creating a second secret on the Configuration tab, rolling out, revoking the old one.
2. `mkdir -p /etc/claude` then `(umask 077 && cat > /etc/claude/environment-secret)`; run `claude self-hosted-runner --environment-secret-file '/etc/claude/environment-secret' --base-dir '<writable-dir>'`. Base dir defaults to `/workspace` (needs to exist or run as root); use a dedicated directory because the runner may reset or delete files in `<base>/<owner>/<repo>`.
3. Status shows **Healthy** within seconds (from **No runners deployed**).
4. Start a session at claude.ai/code and pick the environment.

# Limits and defaults

- A runner started this way exits by design after serving one session (`[runner:exit] account workload drained — exiting`); under an orchestrator restart it. Exits also on `[runner:fatal]` with `runner record gone server-side` or `poll auth failed`.
- Revoked secret: runners fail next poll, log `poll auth failed`, exit.
- Git error `could not read Username for` means no HTTPS credentials; fix then archive/delete failed session or restart the runner so it does not pick up the failed one.
