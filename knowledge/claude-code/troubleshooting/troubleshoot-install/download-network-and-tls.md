---
type: "Guide"
title: "Download, network, proxy and TLS errors"
description: "Fixes for installer download failures, proxies, corporate CA certificates, revocation checks, update retries and release verification."
resource: "https://code.claude.com/docs/en/troubleshoot-install"
tags: [install, proxy, tls, update, network]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.202"
surfaces: [cli]
requires: ""
identifiers:
  - "downloads.claude.ai"
  - "https://claude.ai/install.sh"
  - "https://claude.ai/install.ps1"
  - "https://claude.ai/install.cmd"
  - "HTTPS_PROXY"
  - "HTTP_PROXY"
  - "CURL_CA_BUNDLE"
  - "NODE_EXTRA_CA_CERTS"
  - "--ssl-revoke-best-effort"
  - "claude update"
  - "claude install"
  - "claude doctor"
  - "brew install --cask claude-code"
  - "brew install --cask claude-code@latest"
  - "winget install Anthropic.ClaudeCode"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshoot-install"
    resource: "https://code.claude.com/docs/en/troubleshoot-install"
    title: "Troubleshoot installation and login"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Troubleshooting for the installer and updater reaching `downloads.claude.ai`: HTML or 403 instead of the install script, `curl: (56)`, TLS handshake errors, blocked revocation checks, dropped update downloads, release verification failures, and an auto-update failure line in the footer.

# How to use it

- Connectivity check: `curl -sI https://downloads.claude.ai/claude-code-releases/latest` (use `curl.exe` on Windows PowerShell). A `200` first line means reachable; `403` is usually a proxy/filter or an unsupported region; `5xx` is temporary.
- Behind a proxy set `HTTPS_PROXY` and `HTTP_PROXY` before running the installer or `claude update`.
- Corporate TLS inspection: on macOS/Linux set `CURL_CA_BUNDLE` (for the install script's curl) and `NODE_EXTRA_CA_CERTS` (for `claude install` and later runtime) to a PEM with the proxy CA. On Windows the PowerShell installer uses the Windows certificate store. In PowerShell 5.1 enable TLS 1.2 first.
- `CRYPT_E_NO_REVOCATION_CHECK` / `CRYPT_E_REVOCATION_OFFLINE`: rerun the CMD install curl with `--ssl-revoke-best-effort`, or use the PowerShell installer or WinGet.
- Homebrew has two casks: `claude-code` (stable channel, typically about one week behind) and `claude-code@latest`. `Cask 'claude-code' is unavailable` means run `brew update`; `Cask 'claude-code@latest' is not installed` means upgrade the cask you actually have.
- Alternative install methods (Homebrew, WinGet) do not auto-update by default.

# Limits and defaults

- Downloads are retried when the connection drops, stalls, or fails its checksum, up to 3 attempts total; HTTP errors such as 404 are not retried. Before v2.1.202 a drop failed immediately with bare `aborted`.
- A download not finished within 10 minutes fails with `Download timed out: exceeded the total deadline` and is not retried.
- `Release verification failed for Claude Code <version> (<reason>)`: nothing is installed, existing version keeps working. Reasons starting `sidecar_fetch_`: rerun the same command; other reasons: retry later.
- Red footer `Auto-update failed · Run claude doctor`: run `claude update` from the shell; `claude doctor` shows `Last update attempt: failed (install_failed)` with no cause.

# Notes

An install-script response that is HTML, XML (`System.Xml.XmlDocument`) or a 403 means the URL did not return the script; `App unavailable in region` means Claude Code is not offered in that country.
