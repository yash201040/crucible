---
type: "Guide"
title: "Chrome connection troubleshooting and errors"
description: "Fixes for undetected extension, native messaging host paths, dropped connections, org mismatch and common Chrome error messages."
resource: "https://code.claude.com/docs/en/chrome"
tags: [chrome, troubleshooting, errors, native-messaging]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, ide]
requires: "Claude in Chrome"
identifiers:
  - "claude --version"
  - "/status"
  - "chrome://extensions"
  - "com.anthropic.claude_code_browser_extension.json"
  - "bridge.claudeusercontent.com"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "chrome"
    resource: "https://code.claude.com/docs/en/chrome"
    title: "Use Claude Code with Chrome"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Troubleshooting steps for the Chrome integration.

# How to use it

- Extension not detected: check it is enabled in `chrome://extensions`, run `claude --version` to update, ensure Chrome is running, run `/chrome` then "Reconnect extension", then restart both. The first enable installs a native messaging host config that Chrome reads on startup, so restart Chrome once. The connect tab opens only on first install.
- Host file `com.anthropic.claude_code_browser_extension.json`: macOS Chrome `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/`; Linux Chrome `~/.config/google-chrome/NativeMessagingHosts/`; Edge macOS `~/Library/Application Support/Microsoft Edge/NativeMessagingHosts/`; Edge Linux `~/.config/microsoft-edge/NativeMessagingHosts/`; Windows uses registry keys under `HKCU\Software\<Browser>\NativeMessagingHosts\`. Other Chromium browsers use their own config directory.
- Browser not responding: a JS alert/confirm/prompt dialog blocks commands; dismiss it. Or open a new tab, or toggle the extension.
- Connection drops: the extension service worker can go idle; `/chrome` then "Reconnect extension". If `Status` reads "Not connected", the session's own connection failed. Before v2.1.290, Reconnect only opened the page and did not restart a failed connection.
- Multiple claude.ai orgs: extension and Claude Code must be signed in to the same organization (check `/status` Organization row). Logging out of the extension loses its shortcuts and scheduled tasks.
- Windows: named pipe conflict (EADDRINUSE) means close other sessions using Chrome; host crash means reinstall; before v2.1.211 the setup tab could fail to open.

# Limits and defaults

| Error | Fix |
| - | - |
| "Browser extension is not connected" | same account and org; restart; `/chrome`; check IP allowlist for `bridge.claudeusercontent.com` |
| "Not detected" in `/chrome` | install or enable the extension |
| "No tab available" | ask Claude to create a new tab |
| "Receiving end does not exist" | service worker idle; Reconnect extension |
| "No browsers are connected" | Chrome open, same account and org, network reaches `bridge.claudeusercontent.com` |
