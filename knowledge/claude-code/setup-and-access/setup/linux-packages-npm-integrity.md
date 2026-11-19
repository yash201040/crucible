---
type: "Guide"
title: "Specific versions, package managers, npm and binary integrity"
description: "Installing a pinned version, apt/dnf/apk repositories, npm install, network storage hazards and manifest signature verification."
resource: "https://code.claude.com/docs/en/setup#advanced-installation-options"
tags: [install, npm, signing, package-managers]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.89"
surfaces: [cli]
requires: "npm install needs Node.js 22 or later (runtime does not use it)"
identifiers:
  - "npm install -g @anthropic-ai/claude-code@latest"
  - "bash -s stable"
  - "bash -s 2.1.89"
  - "DISABLE_UPDATES"
  - "manifest.json"
  - "manifest.json.sig"
  - "security@anthropic.com"
  - "https://downloads.claude.ai/keys/claude-code.asc"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "setup"
    resource: "https://code.claude.com/docs/en/setup"
    title: "Advanced setup"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The native installer accepts a version number or channel: `curl -fsSL https://claude.ai/install.sh | bash -s stable` or `bash -s 2.1.89` (PowerShell: `& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 2.1.89`). The chosen channel becomes the auto-update default.

# How to use it

- Signed apt, dnf, apk repositories each offer `stable` and `latest`; repo URLs under `https://downloads.claude.ai/claude-code/{apt,rpm,apk}/{stable,latest}`. Signing key fingerprint `31DDDE24DDFAB679F42D7BD2BAA929FF1A7ECACE`. Upgrades: `sudo apt update && sudo apt upgrade claude-code`, `sudo dnf upgrade claude-code`, `apk update && apk upgrade claude-code`.
- npm: `npm install -g @anthropic-ai/claude-code@latest`, never with `sudo`; avoid `npm update -g`. Installs the same native binary via a per-platform optional dependency (`darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `linux-x64-musl`, `linux-arm64-musl`, `win32-x64`, `win32-arm64`). npm 12 needs the dedicated troubleshooting steps.
- Integrity: each release publishes `manifest.json` with SHA256 checksums per platform, GPG-signed (`manifest.json.sig`, from release 2.1.89 onward). macOS binaries signed and notarized, Windows signed, Linux binaries not individually signed.

# Limits and defaults

- Network storage: a running session reads its executable from disk; if truncated or deleted it crashes (Bus error on Linux). Install on local disk, keep each version in its own directory, delete old versions only when no machine can run them, and set `DISABLE_UPDATES` (not just `DISABLE_AUTOUPDATER`). The native installer keeps the launcher's version, versions running locally and the two newest, deleting the rest.
- Uninstall paths: remove `~/.local/bin/claude` and `~/.local/share/claude` (native); `brew uninstall --cask`, `winget uninstall Anthropic.ClaudeCode`, package manager removal, `npm uninstall -g`. Config removal (`~/.claude`, `~/.claude.json`, project `.claude`, `.mcp.json`) deletes settings, allowed tools, MCP config and session history.
