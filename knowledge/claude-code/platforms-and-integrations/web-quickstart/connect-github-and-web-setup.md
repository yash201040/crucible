---
type: "Guide"
title: "Connect GitHub and /web-setup"
description: "Connect GitHub for cloud sessions via the browser or /web-setup (gh token), the Default environment, and common failures."
resource: "https://code.claude.com/docs/en/web-quickstart"
tags: [github, web-setup, cloud-environment, onboarding]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [web, cli]
requires: "claude.ai login (not API key); Team/Enterprise Owner must enable GitHub connector and, for /web-setup, Quick setup"
identifiers:
  - "/web-setup"
  - "gh auth login"
  - "gh auth token"
  - "gh auth refresh -s workflow"
  - "claude --cloud"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "web-quickstart"
    resource: "https://code.claude.com/docs/en/web-quickstart"
    title: "Get started with Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Connecting GitHub is one-time. Browser path: claude.ai/code > Sign in with GitHub. A browser connection lets sessions clone any public repo; private repos need the Claude GitHub App installed on the account/org (this also enables Auto-fix). Terminal path: `/web-setup` reads the token printed by `gh auth token`, asks for confirmation, and sends it to Anthropic (stored encrypted with the claude.ai account); sessions you start can then reach any repo that token can, with no App install. Threads in a project still need the GitHub App. It replaces an existing browser connection (warns first). On success it prints `Connected as <your-github-username>` and opens claude.ai/code. If no cloud environment exists it creates one with Limited network access and no setup script.

# How to use it

1. `gh auth login` in the shell. 2. `/login` in the CLI (check `/status` shows a claude.ai Login method). 3. `/web-setup`.

Environment: Pro/Max/Ultra get an environment named **Default** automatically; Team/Enterprise see a "Create your first cloud environment" form (Create & finish), or Quick setup creates it. Default uses Limited network access (package registries and allowlisted domains).

Remove: disconnect GitHub at claude.ai/customize/connectors (deletes credentials, cloud sessions lose GitHub access); revoke the token on GitHub (GitHub CLI entry under Authorized OAuth Apps) to invalidate it.

# Limits and defaults

- Zero Data Retention, HIPAA configuration and customer-managed encryption keys (CMEK) organizations cannot use cloud sessions or `/web-setup`.
- `/web-setup` is hidden (`No commands match`, `Unknown command`) with API key or third-party provider auth, on Team/Enterprise until Quick setup is on, when cloud sessions are disabled by policy (message `Cloud sessions are disabled by your organization's policy` from v2.1.268), or with ZDR/HIPAA.
- Errors: `Not signed in to Claude. Run /login first.`; missing `workflow` scope warning (pushes touching workflow files may be rejected; fix `gh auth refresh -s workflow`); `Could not create a cloud environment` / `No cloud environment available` with `--cloud` (run `/web-setup` or add an environment); "Claude Code isn't available on your account" (seat lacks Claude Code).
