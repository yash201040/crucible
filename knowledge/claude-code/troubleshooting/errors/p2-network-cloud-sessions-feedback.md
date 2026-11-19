---
type: "Reference"
title: "Cloud session, teleport and feedback errors"
description: "Cloud environment allowlist blocks, teleport and Remote Control resume failures, and transcript or feedback upload errors."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, cloud-sessions, teleport, remote-control, feedback]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud, web]
requires: ""
identifiers:
  - "x-deny-reason: host_not_allowed"
  - "claude --teleport"
  - "/teleport"
  - "/remote-env"
  - "/feedback"
  - "/bug"
  - "/share"
  - "claude --resume"
  - "claude --continue"
  - "/tasks"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Failures for cloud sessions and cloud scheduled tasks, session pulls, and reports sent to Anthropic.

# How to use it

- **Host not allowed in a cloud session:** a 403 (often with `x-deny-reason: host_not_allowed`), a DNS error like `ENOTFOUND`, or a mismatched TLS certificate means the cloud environment's network allowlist blocked the host. Local CLI sessions are unaffected. Edit your environment: Network access **Limited**, add domains one per line to **Allowed domains**, optionally check **Allow package managers**, or choose **Full**. Org-shared environments are read-only; an Owner changes them under Cloud environments in admin settings. The Default environment is Limited with Allow package managers checked. GitHub operations and MCP connector traffic use separate channels.
- **Cloud environments service returned an empty or unexpected response:** HTTP 200 with empty, non-JSON or list-less body; retry, check status.claude.com. Before v2.1.236 a raw TypeError was shown.
- **Failed to fetch session from Sessions API:** `claude --teleport <session-id>`, `/teleport` or `/tasks` could not read history; the command exits with code 1. Before v2.1.296 failed reads were not retried and could open an empty conversation.
- **Couldn't load the history of cloud session `<id>`:** history request returned not found; open the printed claude.ai link.
- **Couldn't reconnect to your Remote Control session:** resume with `claude --resume` or `--continue` failed temporarily; run `/remote-control` or start `claude --remote-control`.
- **N sessions ended while this machine was offline:** printed by `claude remote-control` when the server cleaned up the environment; sessions cannot be resumed, recover uncommitted work from listed kept worktrees, start a fresh environment.
- **Couldn't share the transcript:** the upload limit is 8 MiB; long sessions are progressively reduced. Local archive saved instead on third-party providers, Claude apps gateway sessions, or with no Anthropic credentials.
- **Couldn't send feedback / Feedback payload too large:** treat as not received. Org refusals (feedback not enabled, custom data retention) make `/feedback` report disabled for seven days. Draft details hold at most 10 KB; set Send transcript to `no`.

# Notes

Before v2.1.281 every send failed once a Remote Control Stop or urgent cross-session message arrived with the dialog open.
