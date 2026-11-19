---
type: "Concept"
title: "Why the classifier billing notice appears"
description: "Plans that never see the notice and the usual causes: a gateway or proxy in the path, or server-side checks not yet reaching a platform, region or credential."
resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing#why-the-notice-appears"
tags: [auto-mode, gateway, troubleshooting, classifier]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/status"
  - "/feedback"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-classifier-billing"
    resource: "https://code.claude.com/docs/en/auto-mode-classifier-billing"
    title: "Auto mode classifier request charges"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On a Pro, Max, Ultra or Team plan you never see the notice. Otherwise it has two usual causes.

# How to use it

- An LLM gateway or proxy in the path that strips or rewrites request headers, drops unrecognized request fields, or edits responses, so the server never receives the check request or Claude Code never receives results. When configuration or responses identify the gateway, the notice names it.
- Server-side checks have not yet reached your platform, region or credential (depends on that platform's rollout). If you see the notice with no gateway or proxy and it keeps appearing, this is likely; confirm with support or your admin, or report with `/feedback`.

Check a session in auto mode with `/status`: the **Auto mode server** row is `Enabled` or `Disabled` (fallen back). Which sessions request server checks, and the Claude Code version each needs, is documented under "Server-side classifier review" in the permission modes page.
