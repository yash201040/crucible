---
type: "Feature"
title: "Read an artifact shared with you"
description: "Claude reads another person's artifact like a WebFetch summary and Claude Code asks approval in several cases."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, reading, permissions, webfetch]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "WebFetch"
  - "WebFetch(domain:claude.ai)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Give Claude the artifact URL or attach it from `/artifacts`. Claude reads someone else's page the way it reads a web page with WebFetch: it gets a summary of what it asked about, not the raw page, and the summary reports instructions written into the page instead of relaying them. Claude Code also saves the full source to a local file, which Claude can open for exact content, for example to republish as an editor.

# How to use it

Claude Code asks approval before reading, in addition to any mode or rule prompt, in these cases:

- Cloud session without network access (the **None** level). Auto mode: the classifier can approve; Cowork session: approval is yours alone.
- Another organization's public artifact: asked even in auto mode. Where it cannot ask (such as `bypassPermissions`), Claude cannot read it. Needs feature-flag fetching on.
- Unconfirmed owner or network setting: it asks; in auto mode the classifier approves or blocks.
- Plan mode: asks before the Artifact tool reads an artifact someone else in your organization made.

# Notes

WebFetch's own prompting rules still apply when WebFetch is used. A `WebFetch` deny or ask rule with no `domain:` part does not block artifact reads; a `WebFetch(domain:claude.ai)` rule in `deny` or `ask` does.
