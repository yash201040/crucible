---
type: "Limit"
title: "Artifact page constraints"
description: "CSP and format rules for an artifact page: allowed CDNs, no backend, source types, 16 MiB size, no self-started downloads."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, csp, limits, cdn]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: ""
identifiers:
  - "cdnjs.cloudflare.com"
  - "cdn.jsdelivr.net"
  - "cdn.tailwindcss.com"
  - "code.jquery.com"
  - "unpkg.com"
  - "fonts.googleapis.com"
  - "fonts.gstatic.com"
  - "*.claudeusercontent.com"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code wraps the published file in an HTML shell and serves it under a strict Content Security Policy.

# Limits and defaults

| Constraint | Effect |
| --- | --- |
| External requests | Typefaces from Google Fonts; scripts from five CDN hosts: cdnjs, unpkg, Tailwind, jQuery and selected jsDelivr paths such as `/npm/`. Every external image and all other external scripts, stylesheets and fonts are blocked. `fetch`, XHR and WebSocket reach only the page's own origin and Google Fonts hosts. Embed images as data URIs; inline other CSS/JS |
| No backend | Static page; cannot authenticate viewers |
| Downloads | Page cannot start one; use the downloads capability |
| Source file types | `.html`, `.htm` or `.md`; must decode as UTF-8 (or little-endian UTF-16 by BOM). A file that fails to decode or contains `U+FFFD` is refused with line and column. Markdown renders as styled document pages |
| Source location | A path naming a network host is refused unread (mapped-drive exception on Windows) |
| Rendered size | 16 MiB or smaller; large embedded images are the usual failure |

# Notes

The viewer loads each artifact from a sandboxed `*.claudeusercontent.com` origin; allowlist it with `claude.ai` if outbound access is restricted. Google Fonts hosts are optional (fallback fonts if blocked). Blocked CDN library hosts have no fallback; block with fast rejection, not silent drop.
