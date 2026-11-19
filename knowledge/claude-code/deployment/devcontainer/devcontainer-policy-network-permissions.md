---
type: "Guide"
title: "Dev container policy, egress and unattended runs"
description: "Enforce managed settings, restrict network egress and run without permission prompts inside a dev container."
resource: "https://code.claude.com/docs/en/devcontainer"
tags: [devcontainer, managed-settings, egress, unattended]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/etc/claude-code/managed-settings.json"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "DISABLE_AUTOUPDATER"
  - "npm install -g @anthropic-ai/claude-code@X.Y.Z"
  - "--dangerously-skip-permissions"
  - "permissions.disableBypassPermissionsMode"
  - "init-firewall.sh"
  - "NET_ADMIN"
  - "NET_RAW"
  - "runArgs"
  - "remoteUser"
  - ".mcp.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "devcontainer"
    resource: "https://code.claude.com/docs/en/devcontainer"
    title: "Development containers"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Patterns for applying organization policy and isolation in a dev container, including unattended operation.

# How to use it

- Managed settings: Claude Code reads `/etc/claude-code/managed-settings.json` on Linux at highest precedence; copy it in from the Dockerfile (`RUN mkdir -p /etc/claude-code` / `COPY managed-settings.json ...`). Because anyone with repo write access can edit the Dockerfile, use server-managed settings or MDM for policy engineers cannot bypass.
- Env in `containerEnv`: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (telemetry and error reporting off; also disables feature-flag evaluation, so Remote Control and other flag-dependent features are unavailable) and `DISABLE_AUTOUPDATER=1`.
- Version pinning: the feature always installs latest; to pin, install `npm install -g @anthropic-ai/claude-code@X.Y.Z` in the Dockerfile and set `DISABLE_AUTOUPDATER=1`.
- MCP: define servers at project scope in `.mcp.json` at repo root; install stdio server binaries in the Dockerfile; allow remote server domains in network rules.
- Egress: restrict outbound traffic to needed domains (see the network config page). The reference container's `init-firewall.sh` needs the `NET_ADMIN` and `NET_RAW` capabilities via `runArgs`; neither is required by Claude Code itself.
- Unattended: `--dangerously-skip-permissions` is rejected by the CLI when run as root, so set `remoteUser` to a non-root account. It lets Claude modify any file in the bind-mounted workspace and reach anything the network policy allows; pair with egress limits. Alternative: auto mode (classifier-reviewed). Block the flag fleet-wide with `permissions.disableBypassPermissionsMode` = `"disable"` in managed settings.

# Notes

Reference container in the `anthropics/claude-code` repository (`devcontainer.json`, `Dockerfile`, `init-firewall.sh`) is a working example, not a maintained base image. It combines the CLI, egress firewall, persistent volumes and a Zsh shell.
