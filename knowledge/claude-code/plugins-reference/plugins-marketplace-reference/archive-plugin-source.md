---
type: "Feature"
title: "archive plugin source"
description: "Zip-over-HTTPS plugin source with optional sha256 integrity pin and its URL restrictions."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, archive, sha256, integrity]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "archive"
  - "url"
  - "sha256"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `archive` plugin source downloads a zip file over HTTPS.

# How to use it

```json
{ "name": "formatter", "source": { "source": "archive", "url": "https://artifacts.example.com/formatter-2.0.0.zip", "sha256": "<64 hex chars>" } }
```

- `url` must use `https://` and cannot point at a loopback, link-local or cloud-metadata host.
- The plugin root may be at the top of the zip or one directory down.
- `sha256`: 64 hex characters, upper or lower case; when set, a mismatching download is refused.
- Size, timeout, redirect and extraction limits are on the host-marketplace page.

# Notes

Entry `headers` and `headersHelper` apply only to archive sources. Validation warns when a `headersHelper` is used without a `sha256` pin, and errors when an archive entry sets `headersHelper` without `"strict": false`.
