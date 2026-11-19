---
type: "Concept"
title: "Prompt injection safeguards and trust verification"
description: "Safeguards including network approval, WebFetch summaries, trust dialog behavior (none in -p mode), credential storage and the Windows WebDAV warning."
resource: "https://code.claude.com/docs/en/security"
tags: [prompt-injection, trust, credentials, webdav, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "-p"
  - ".mcp.json"
  - "/feedback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security"
    resource: "https://code.claude.com/docs/en/security"
    title: "Security"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Safeguards listed against prompt injection: permission system and network command approval in Manual mode; most network-making tools require approval by default; WebFetch runs a separate model call over the page and Claude receives that answer instead of the raw page; trust verification; command injection detection; secure credential storage.

# Limits and defaults

- Trust: interactive sessions show the workspace trust dialog for untrusted folders; `.mcp.json` servers have their own approval prompt. A `-p` session shows neither prompt. When started directly in the home directory, trust is held for the session only and never written to disk (no setting persists it); start from a project subdirectory for per-directory saved trust.
- Credentials: macOS Keychain when available; Linux file with mode `0600`; Windows file inheriting the user profile ACLs.
- Windows WebDAV warning: avoid enabling WebDAV or letting Claude Code access paths like `\\*`; it can trigger network requests that bypass the permission system.
- Best practices for untrusted content: review commands, avoid piping untrusted content, verify changes to critical files, use VMs for scripts and external web interaction, report with `/feedback`. No system is immune.
