---
type: "Feature"
title: "Trusted Devices for Remote Control"
description: "Optional org or personal setting that requires an enrolled device and a sign-in under 18 hours old to view or steer Remote Control sessions."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [trusted-devices, security, remote-control, admin]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [web, mobile, desktop, cli]
requires: "Pro, Max, Ultra, Team or Enterprise; off by default"
identifiers:
  - "Require trusted devices"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When on, interacting with a Remote Control session from claude.ai, the mobile apps or Claude Desktop needs an enrolled device credential and a sign-in no more than 18 hours old. Older sign-ins are refreshed by a Face ID, Touch ID, Windows Hello or passkey step-up (hardware key or re-sign-in if no platform authenticator). Biometrics stay on-device; only the public key and basic metadata are stored. Also applies to Computer access in Cowork. Regular chat, terminal Claude Code and API usage are unaffected.

# How to use it

- Team/Enterprise: an Owner turns on **Require trusted devices** at Organization settings > Capabilities > Remote sessions. Applies to all members, only to sessions started after enabling; no per-team scoping.
- Pro/Max/Ultra: turn it on yourself in settings (Cowork or Account page).
- Enrollment is offered shortly after a full sign-in, once per device. The terminal machine gets its credential automatically at CLI sign-in (no separate step); `/login` fixes "this device is not enrolled".
- Members review and revoke devices at claude.ai/settings/account (Trusted devices). Credentials expire if unused. Admins can use "Sign out everywhere".
- Errors: `session expired for trusted-device check` means sign-in over 18 hours old.

# Notes

With Trusted Devices required, `DISABLE_TELEMETRY` or `DO_NOT_TRACK` make Remote Control unavailable.
