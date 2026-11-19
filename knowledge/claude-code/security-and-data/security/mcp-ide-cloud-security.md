---
type: "Concept"
title: "MCP, IDE and cloud execution security"
description: "MCP server trust model, plus controls for Anthropic-hosted cloud sessions (isolated VMs, proxy-held GitHub credentials, push restrictions) and Remote Control."
resource: "https://code.claude.com/docs/en/security"
tags: [mcp, cloud-sessions, remote-control, github-proxy, isolation]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud, cli, ide]
requires: ""
identifiers:
  - ".mcp.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security"
    resource: "https://code.claude.com/docs/en/security"
    title: "Security"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

MCP: project-scoped servers live in `.mcp.json`, but other scopes, claude.ai connectors and plugins can add servers, so reviewing `.mcp.json` does not show every server. Anthropic reviews connectors for the Anthropic Directory but does not security-audit or manage any MCP server. Restrict via managed MCP configuration.

Cloud sessions (Anthropic-hosted): each in an isolated managed VM; network limited by default (can be disabled or allow specific domains); GitHub credentials stored encrypted server-side and never enter the VM (the VM holds a short-lived session-scoped credential; an Anthropic proxy attaches the real one); the GitHub proxy rejects branch deletions and pushes of anything other than a branch (e.g. tags), and GitHub branch protection rules apply, but a rule the connected access can bypass does not block a push; all operations audit-logged; VMs reclaimed after inactivity; sessions deletable. Self-hosted environments leave isolation, egress and git credentials to your deployment.

# Limits and defaults

Remote Control: execution and file access stay local, no cloud VMs or sandboxing; traffic uses TLS through the Anthropic API; transcript is stored on Anthropic servers while connected; uses multiple short-lived, narrowly scoped credentials.
