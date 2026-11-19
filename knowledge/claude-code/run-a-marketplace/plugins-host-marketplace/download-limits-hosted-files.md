---
type: "Limit"
title: "Download and extraction limits for hosted files"
description: "Size, time and redirect limits for url-hosted marketplace.json and archive plugin zips, plus zip extraction limits."
resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
tags: [limits, archive, marketplace, download, redirects]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "archive"
  - "url"
  - "marketplace.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-host-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
    title: "Host and maintain a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Downloads fail beyond these limits when users add a `marketplace.json` URL or install an `archive` entry.

# Limits and defaults

| File | Largest download | Server response time | Redirects |
|---|---|---|---|
| `marketplace.json` from a `url` source | 5 MiB | 10 seconds | cross-origin redirect must be `https://` and not loopback, link-local or cloud-metadata host; `https` to `http` fails |
| Zip from `archive` source | 256 MiB | 120 seconds | at most five; every target `https://` and not loopback, link-local or cloud-metadata |

Redirects to a different origin carry none of the configured headers.

Extraction limits (install fails if exceeded): 100,000 entries (files and directories); 512 MiB per file uncompressed; 1 GiB total uncompressed; compression ratio 50 times.
