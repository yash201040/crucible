---
type: "Reference"
title: "HTTP hook URL and env-var allowlists"
description: "Settings that restrict which URLs HTTP hooks may call and which environment variables they may interpolate into headers."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, hooks, http, security]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
  - "allowedEnvVars"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two array settings (any file; arrays merge across files; set in managed settings to cover org-deployed hooks) that constrain HTTP hooks.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `allowedHttpHookUrls` | array of URL patterns, `*` wildcard | unset (any URL) | A covered hook runs only if its URL matches a pattern in the merged list. Hostname match is case-insensitive and treats `hooks.example.com.` as `hooks.example.com` |
| `httpHookAllowedEnvVars` | array of env var names | unset | A hook can put an env var in a header (for example `Authorization: Bearer $HOOK_TOKEN`) only if both its own `allowedEnvVars` and this merged list name it |

Example: `{ "allowedHttpHookUrls": ["https://hooks.example.com/*", "http://localhost:*"] }`.

# Notes

In the Agent SDK's `managedSettings` option a list with entries is ignored; pass it in the SDK's `settings` option instead.
