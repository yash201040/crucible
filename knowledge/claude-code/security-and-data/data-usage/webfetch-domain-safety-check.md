---
type: "Feature"
title: "WebFetch domain safety check"
description: "WebFetch sends the requested hostname to api.anthropic.com for a blocklist check regardless of provider; opt out with skipWebFetchPreflight."
resource: "https://code.claude.com/docs/en/data-usage"
tags: [webfetch, network, privacy, blocklist]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "skipWebFetchPreflight"
  - "WebFetch"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "data-usage"
    resource: "https://code.claude.com/docs/en/data-usage"
    title: "Data usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Before fetching a URL, WebFetch sends only the hostname (not path or contents) to `api.anthropic.com` to check it against an Anthropic blocklist. A passing hostname is cached for five minutes; a blocked or failed one is re-checked on the next request.

# Limits and defaults

- Runs regardless of model provider and is not affected by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.
- If the network blocks `api.anthropic.com`, WebFetch fails until the domain is allowlisted or `skipWebFetchPreflight: true` is set in settings. Disabling it means any URL is attempted, so combine with `WebFetch` permission rules.
