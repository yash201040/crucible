---
type: "Feature"
title: "Cloud sessions, environments and GitHub access"
description: "Cloud sessions run Claude Code on Anthropic or self-hosted infrastructure, started from web, mobile, desktop, terminal or schedules, with GitHub connection options."
resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
tags: [cloud, sessions, github, environments]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, web, desktop, mobile, cloud]
requires: "Pro, Max, Ultra or Team plan, or Enterprise premium / Chat + Claude Code seats; custom roles need cloud sessions permission; not ZDR, HIPAA or CMEK orgs"
identifiers:
  - "claude --cloud"
  - "/web-setup"
  - "allow_remote_sessions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-code-on-the-web"
    resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
    title: "Use Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A cloud session runs Claude Code on Anthropic-managed infrastructure (or the organization's self-hosted environment when routed there). It keeps running after the laptop closes and can be steered from any device. It counts toward plan usage limits; no separate VM charge. Start surfaces: browser (claude.ai/code), Claude app Code tab, Desktop app (Cloud environment selector), terminal `claude --cloud`, and cloud scheduled tasks (each run is a cloud session). Many sessions for one body of work is covered by Projects; steering a local session remotely is Remote Control.

# How to use it

Each session runs in a cloud environment (saved config for network access, environment variables, setup scripts). Onboarding creates a Default environment with Limited network access.

| GitHub method | Connect | Reach | Best for |
| - | - | - | - |
| GitHub App | authorize Claude GitHub App in web onboarding | public repos and private repos where the app is installed | browser onboarding, Auto-fix |
| `/web-setup` | run in terminal to send local `gh` token to Claude account | any repo the `gh` token can access | developers already using `gh` |

Auto-fix and Projects need the Claude GitHub App installed on the repository. In Anthropic-hosted environments GitHub credentials stay on Anthropic servers, outside the VM; the GitHub proxy attaches them.

Quick setup (Team and Enterprise, off by default): an Owner turns on the Quick setup toggle at Organization settings > Claude Code. Then `/web-setup` is available (hidden when off), onboarding skips the GitHub App prompt, and creates the Default environment for members.

# Limits and defaults

- Zero Data Retention or HIPAA orgs cannot use `/web-setup` or cloud sessions; CMEK orgs cannot start them.
- Rate limits are shared with all other Claude usage; parallel tasks consume proportionally more.
- Repository cloning in Anthropic-hosted environments and PR creation require GitHub; GitHub Enterprise Server supported for Team and Enterprise. Non-GitHub repos can be sent as a local bundle with `CCR_FORCE_BUNDLE=1` but cannot push back.
- Isolation: isolated VMs, limited-by-default network access (can be disabled; with network disabled the Anthropic API is still reachable), git credentials and signing keys outside the sandbox, network secrets attached after requests leave the session (not in self-hosted environments).
- Time limits: commands and SessionStart hooks have default timeouts; a setup script is cached only if it finishes in roughly five minutes.
