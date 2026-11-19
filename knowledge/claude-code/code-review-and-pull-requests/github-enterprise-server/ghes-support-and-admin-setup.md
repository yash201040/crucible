---
type: "Feature"
title: "GitHub Enterprise Server support and admin setup"
description: "What works on GHES for Team and Enterprise (cloud sessions, Code Review, teleport) and how an Owner connects an instance with a generated GitHub App."
resource: "https://code.claude.com/docs/en/github-enterprise-server"
tags: [ghes, github-enterprise, admin, github-app]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cloud, cli]
requires: "Team or Enterprise plan; Owner or Primary Owner role; permission to create GitHub Apps on the GHES instance"
identifiers:
  - "claude --cloud"
  - "claude --teleport"
  - "/install-github-app"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-enterprise-server"
    resource: "https://code.claude.com/docs/en/github-enterprise-server"
    title: "Claude Code with GitHub Enterprise Server"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An Owner connects a self-hosted GitHub instance once; developers then get cloud sessions and Code Review without per-repository configuration.

| Feature | GHES |
| :- | :- |
| Cloud sessions | Supported (`claude --cloud`, claude.ai/code) |
| Code Review | Supported |
| Claude Security | Supported; public beta for Enterprise plans |
| Teleport sessions | Supported (`--teleport`) |
| Plugin marketplaces | Supported; credentials differ per surface |
| GitHub Actions | Supported with manual workflow setup; `/install-github-app` is github.com only |
| Contribution metrics | Not supported (needs github.com repos; analytics still shows usage) |
| GitHub MCP server | Not supported; use `gh auth login --hostname <host>` and `gh` locally |

# How to use it

Organization settings > Git providers > GitHub Enterprise: **Connect** (or **Add instance**) > **Set up automatically**; enter a display name (up to 20 characters), the GHES hostname and optionally a CA certificate; **Continue to GitHub Enterprise** creates the app from a prefilled manifest; install it on repositories; enable Code Review at claude.ai/admin-settings/claude-code. If the redirect is blocked choose **Add manually**: create the app yourself and enter display name, hostname and optional port, app ID, client ID, client secret, webhook secret, private key, optional CA and read-replica hostnames; copy the generated webhook URL (**More options** > **Copy webhook URL**) into the app.

# Limits and defaults

Manifest permissions: Contents R/W, Pull requests R/W, Issues R/W, Checks R/W, Actions R, Commit statuses R, Repository hooks R/W (marketplace webhook when **Sync automatically** is on), Metadata R, Organization members R. Subscribed events: `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, `check_run`, `status`. Apps created from an older manifest keep their old permissions; add missing ones in app settings and an owner of each installation must approve.

# Notes

Developers just clone from GHES and run `claude --cloud "..."`; Claude detects the host from the git remote. `claude --teleport` verifies you are in a checkout of the same GHES repository.
