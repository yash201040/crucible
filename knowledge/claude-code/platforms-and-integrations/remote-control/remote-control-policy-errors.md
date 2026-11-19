---
type: "Reference"
title: "Remote Control policy and eligibility errors"
description: "Error messages when Remote Control is blocked by organization policy, plan, feature flags or API endpoint, with the fix for each."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [remote-control, errors, policy, admin, troubleshooting]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Remote Control is disabled by your organization's policy"
  - "Remote Control was turned off by your organization's policy"
  - "Couldn't verify your organization's policy for remote control"
  - "Remote Control requires a claude.ai subscription"
  - "Remote Control requires a full-scope login token"
  - "Remote Control isn't enabled for this account"
  - "Couldn't verify Remote Control eligibility"
  - "Remote Control requires feature-flag evaluation"
  - "Remote Control is only available when using Claude via api.anthropic.com"
  - "Remote credentials fetch failed"
  - "DISABLE_GROWTHBOOK"
  - "CLAUDE_CODE_USE_BEDROCK"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Message | Cause and fix |
|---|---|
| `Remote Control is disabled by your organization's policy` | Check in order: `disableRemoteControl` in settings (remove, or ask admin if managed); stale Team/Enterprise login on a Pro/Max/Ultra plan (`/status`, re-login); HIPAA configuration (also earlier worded as compliance policy before v2.1.267); missing custom-role permissions; Zero Data Retention; or an Owner has not enabled the toggle (off by default on Team/Enterprise) |
| `Remote Control was turned off by your organization's policy` | Policy changed mid-session. `/remote-control`/`claude --remote-control`/auto-connect: session keeps running, archived at claude.ai. `claude remote-control`: server stops, archives sessions, exits. No automatic reconnect |
| `Couldn't verify your organization's policy for remote control` | Policy unreachable and no saved copy (offline, VPN, proxy); before v2.1.281 shown as the "disabled" message. Run `claude doctor` |
| `Remote Control requires a claude.ai subscription` / `Remote Control requires claude.ai subscription auth.` | Signed out, or API key / `apiKeyHelper` / `ANTHROPIC_AUTH_TOKEN` in use. `claude auth login` |
| `Remote Control isn't enabled for this account` | Stale entitlements after plan change (before v2.1.239: "not yet enabled for your account"). Logout/login, update |
| `Couldn't verify Remote Control eligibility` | Feature-flag service unreachable |
| `Remote Control requires feature-flag evaluation` | Named variable (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`, `DISABLE_GROWTHBOOK`) must be unset; telemetry vars acceptable on v2.1.283+ |
| `Remote Control is only available when using Claude via api.anthropic.com` | Bedrock, Agent Platform, Foundry, or custom `ANTHROPIC_BASE_URL` |
| `Remote credentials fetch failed` | Short-lived credential fetch failed; check proxy/firewall on port 443 |
| `Your organization requires Trusted Devices for Remote Control, but this device is not enrolled` | Run `/login` |
