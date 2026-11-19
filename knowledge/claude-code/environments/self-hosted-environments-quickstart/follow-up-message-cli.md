---
type: "Feature"
title: "Send follow-ups to a cloud session from the CLI"
description: "claude -p with --cloud posts one message to an existing cloud or self-hosted session from any logged-in machine."
resource: "https://code.claude.com/docs/en/self-hosted-environments-quickstart"
tags: [cloud-sessions, headless, follow-up, cli]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: "claude auth login with a claude.ai account"
identifiers:
  - "claude -p"
  - "--cloud"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-quickstart"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-quickstart"
    title: "Self-hosted environments quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A one-shot message to a running session without the web UI.

# How to use it

```
claude -p "your message" --cloud <session-id>
```

`<session-id>` may be a bare `session_...` or `cse_...` ID or the session's claude.ai/code URL. The machine need not be the one that started the session. Success prints `Sent to cloud session.` with the ID and a view link. A finished turn does not end the session, so no runner restart is needed. Accepted ID forms, JSON output and policy requirements are documented on the claude-code-on-the-web page (works the same for Anthropic-hosted sessions).
