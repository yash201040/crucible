---
type: "Guide"
title: "Desktop device policies, sign-in control and network access"
description: "Admin console toggles, MDM and policy file locations, forceLoginOrgUUID, firewall hosts and deployment methods for Desktop."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, enterprise, mdm, network, sso]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Team or Enterprise plan"
identifiers:
  - "forceLoginOrgUUID"
  - "forceLoginMethod"
  - "com.anthropic.claudefordesktop"
  - "SOFTWARE\\Policies\\Claude"
  - "/etc/claude-desktop/managed-settings.json"
  - "requireCoworkFullVmSandbox"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "bridge.claudeusercontent.com"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways IT controls the desktop app: admin console (Desktop, Cloud sessions, Remote Control), Claude Code managed settings, and Desktop's own device policies.

# How to use it

- **Device policies**: macOS preference domain `com.anthropic.claudefordesktop` (Jamf, Kandji); Windows registry `SOFTWARE\Policies\Claude`; Linux root-owned `/etc/claude-desktop/managed-settings.json` (refused if non-root can write it or its folder). Policies cover enabling Claude Code, auto-updates (macOS/Windows) and a custom deployment URL.
- **Restrict sign-in**: `forceLoginOrgUUID` in the Desktop policy (v1.2581.0+); wrong ID locks out users. Claude Code `forceLoginMethod`/`forceLoginOrgUUID` do not change the Desktop sign-in screen. Do not deploy it alone with a Console organization ID.
- **Telemetry**: Code tab sessions need `CLAUDE_CODE_ENABLE_TELEMETRY` and `OTEL_*` in the managed settings `env` block; the Cowork OpenTelemetry form applies to Cowork only.
- **Deployment**: macOS `.dmg` via MDM; Windows MSIX. Data: local and SSH sessions go to the configured model provider (Anthropic by default); cloud sessions to Anthropic's API.
- **Network**: HTTPS 443 to `anthropic.com`, `*.anthropic.com`, `claude.ai`, `*.claude.ai`, `claude.com`, `*.claude.com`, `claude.app`, `*.claude.app`, `*.claudeusercontent.com`, `*.claudemcpcontent.com`; a reduced explicit list includes `api.anthropic.com`, `downloads.claude.ai`, `platform.claude.com`, `sso.claude.com`, `*.livepreview.claude.ai`. With IP allowlisting route `bridge.claudeusercontent.com` through the same egress. Artifacts optionally use `fonts.googleapis.com`, `fonts.gstatic.com` and library CDNs (`cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `cdn.tailwindcss.com`, `code.jquery.com`, `unpkg.com`).

# Limits and defaults

Setting `requireCoworkFullVmSandbox` disables the iOS Simulator pane. HIPAA organizations have Desktop off by default.
