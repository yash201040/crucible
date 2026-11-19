---
type: "Guide"
title: "Harden a self-hosted runner deployment"
description: "Checklist of isolation, credential, egress, IAM and repo-settings controls to apply before connecting self-hosted runners to production systems."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, security, isolation, runner, egress]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan; an Owner enables Allow self-hosted environments"
identifiers:
  - "--capacity"
  - "--drain-grace-sec"
  - "--lock-to-account"
  - "--confine-repo-settings"
  - "--trust-workspace"
  - "--hooks-dir"
  - "169.254.169.254"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Self-hosted environments are labelled public beta. A runner executes model-directed code for everyone who can dispatch a session to its environment: any member of the Anthropic organization, plus anyone who can start a Claude Tag channel session in a scope an Owner routed to the environment. The page lists controls to apply first.

# How to use it

| Control | What to do |
| :- | :- |
| Ephemeral containers | One fresh container or VM per runner process, with `--capacity 1` and default `--drain-grace-sec 0`, so each serves one session. Never reuse a filesystem across owners. |
| Credentials | No long-lived SSH keys, cloud keys or broad PATs in the image; mint per-session credentials from a wrapper script. Initial clone happens before the wrapper, so use a `checkout` lifecycle hook or `--use-anthropic-git-proxy`. |
| Environment secret | It registers runners and picks up any queued session. Prefer on-demand runners so it stays on the orchestrator host. After suspected compromise: select **Revoke token** on the session (Activity tab) first, then an Owner creates a new secret and revokes the old one (Configuration tab). |
| Egress | Default-deny at your own network boundary on every environment. |
| Host IAM | Least privilege; sessions get their own credentials via the wrapper. |
| Metadata endpoint | Block in the container itself: IMDSv2 hop limit 1, GKE Workload Identity with metadata concealment, or deny `169.254.169.254`. Applies to wrapper and lifecycle hooks too. |
| Filesystem | Per-runner working directory; `--hooks-dir`, the wrapper and host `~/.claude/` read-only to sessions. |
| Repo-settings guard | `--confine-repo-settings` is `warn` (default, logs and still spawns), `enforce` (refuses session) or `off`. Scans for grants resolving outside the workspace (`additionalDirectories`, Edit/Write/NotebookEdit allow rules, `sandbox.filesystem.allowWrite/allowRead`), non-empty `env`, and overrides like `sandbox.enabled: false`. Runs regardless of `--trust-workspace`; does not cover repo hooks, `.mcp.json` or Bash rules. |

# Limits and defaults

- Dispatch has no per-environment access control; `--lock-to-account` bounds which account's sessions a host runs but not who can dispatch.
- An Owner can hide Anthropic-hosted environments for the whole organization on the Cloud environments page.
- When a session stops, a process still running after its shell command exited (a daemonized service) gets no signal; destroying the container ends it.
- If IP allowlisting is on, add runner, session container and (for on-demand) orchestrator public addresses. It is not a substitute for egress control.
