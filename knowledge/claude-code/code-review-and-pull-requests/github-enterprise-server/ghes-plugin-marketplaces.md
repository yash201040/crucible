---
type: "Feature"
title: "Plugin marketplaces on GHES"
description: "Host plugin marketplaces on GitHub Enterprise Server: full git URL, extraKnownMarketplaces pre-registration, strictKnownMarketplaces hostPattern allowlist."
resource: "https://code.claude.com/docs/en/github-enterprise-server"
tags: [ghes, plugins, marketplaces, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web, cloud]
requires: "Git access to the GHES host from each machine (CLI, desktop, managed settings)"
identifiers:
  - "/plugin marketplace add"
  - "extraKnownMarketplaces"
  - "strictKnownMarketplaces"
  - "hostPattern"
  - "managed-settings.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-enterprise-server"
    resource: "https://code.claude.com/docs/en/github-enterprise-server"
    title: "Claude Code with GitHub Enterprise Server"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Surface | How it works | Per-user need |
| :- | :- | :- |
| CLI and desktop | Clones with the machine's git credentials | Git access to GHES |
| Managed settings (`extraKnownMarketplaces`) | Registers and clones with machine credentials | Git access |
| claude.ai org plugin settings | Anthropic backend syncs via the GitHub App | None per user; the Owner needs their own GHES account connected at add time and the App installed on the marketplace repo |
| claude.ai user settings | Backend fetches via the user's own GHES connection | Own GitHub Enterprise account connected (not covered by the admin setup or by anyone else's connection) |
| Cloud sessions | Cloned in sandbox, reaching only the session repo's instance | Not reliable; use CLI, managed settings or claude.ai |

# How to use it

`owner/repo` shorthand always means github.com, so use a full git URL: `/plugin marketplace add https://github.example.com/platform/claude-plugins.git` (HTTPS recommended; SSH works only if the host is in `known_hosts`, because git runs non-interactively).

Pre-register for everyone: `"extraKnownMarketplaces": {"internal-tools": {"source": {"source": "git", "url": "https://github.example.com/platform/claude-plugins.git"}}}` (works from any settings file; managed settings deliver it org-wide; a missing credential fails the clone without prompting, shown in the `/plugin` Errors tab).

Allowlist: `"strictKnownMarketplaces": [{"source": "hostPattern", "hostPattern": "^github\\.example\\.com$"}]`.

# Notes

A policy error on `/plugin marketplace add` means the org restricted sources; ask the admin for a `hostPattern` entry. A generic "Marketplace couldn't be added" on claude.ai means your own GHES account is not connected (the Browse tab's "Connect to GitHub" signs in to github.com only); connect via the repository picker at claude.ai/code or the Git providers page.
