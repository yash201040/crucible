---
type: "Guide"
title: "GHES network requirements and troubleshooting"
description: "Anthropic-hosted sessions and reviews must reach the GHES instance (allowlist outbound IPs); fixes for clone failures, connection tests and org UUID errors."
resource: "https://code.claude.com/docs/en/github-enterprise-server"
tags: [ghes, networking, troubleshooting, self-hosted]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "Connection test passed, but a second test failed."
  - "Connection test passed, but a second test could not run."
  - "Unable to get organization UUID"
  - "Authentication failed while accessing the repository"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-enterprise-server"
    resource: "https://code.claude.com/docs/en/github-enterprise-server"
    title: "Claude Code with GitHub Enterprise Server"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For Anthropic-hosted sessions the GHES instance must be reachable from Anthropic infrastructure; behind a firewall allowlist Anthropic's outbound IP addresses. Sessions in a self-hosted environment clone from inside your network, unless the runner uses the Anthropic git proxy, which needs the same reachability. Hosted pre-session flows such as the repository picker run on Anthropic's side even for self-hosted sessions, and the SCM connector is not available, so internally-only-routable GHES hosts do not work for those flows.

# How to use it

- Clone failure on `claude --cloud`: confirm an Owner finished setup, the App is installed on the repo, and the registered hostname matches the git remote hostname. "Authentication failed while accessing the repository" means you have not connected your own GitHub Enterprise account (connect from the repository picker at claude.ai/code, then start a new session).
- `Connection test passed, but a second test failed.`: the second test mirrors how cloud sessions connect; allow all Anthropic outbound IPs or retry. `Connection test passed, but a second test could not run.`: retry in a few minutes. Retest via the connection's **More options** > **Test connection**.
- `Unable to get organization UUID`: sign in with `/login` using an account in a Team or Enterprise organization.

# Notes

Related: self-hosted environment configuration, network configuration page, analytics (usage metrics still work for GHES repos).
