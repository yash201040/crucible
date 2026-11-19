---
type: "Limit"
title: "Chrome file uploads and screenshots"
description: "Claude can attach local files to web upload fields in local and remote sessions, with size, permission, hard-link and credential-name limits."
resource: "https://code.claude.com/docs/en/chrome"
tags: [chrome, uploads, limits, files]
kind: "limit"
maturity: "unlabelled"
since: "2.1.293"
surfaces: [cli, ide]
requires: "Claude in Chrome"
identifiers:
  - ".env"
  - ".pem"
  - ".key"
  - ".ssh"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "chrome"
    resource: "https://code.claude.com/docs/en/chrome"
    title: "Use Claude Code with Chrome"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code reads a local file and sends its contents to the browser, so uploads work in both local and remote sessions. Screenshots can be saved to disk (Claude reports the path), and GIF recordings capture everything visible, including account details.

# How to use it

Ask in plain words, for example "attach logs/session.log to the issue".

# Limits and defaults

- Permissions: upload only if the session may read the file; `Read` deny rules also block uploading.
- Size: up to 10 MB of files in total per upload.
- Hard links: files with multiple hard links are refused (common in `node_modules` stores); upload a copy.
- Credential names: files or folders such as `.env`, `.pem`, `.key`, anything under `.ssh` are refused. Requires Claude Code v2.1.293 or later.
