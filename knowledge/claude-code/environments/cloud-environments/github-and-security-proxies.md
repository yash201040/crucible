---
type: "Feature"
title: "GitHub proxy and security proxy"
description: "In Anthropic-hosted environments GitHub traffic goes through a credential-swapping proxy with push and GraphQL restrictions, and all traffic through a security proxy."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, github, proxy, security]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: "Anthropic-hosted environment"
identifiers:
  - "GH_TOKEN"
  - "GITHUB_TOKEN"
  - "proxy-injected"
  - "gh api"
  - "attribution.sessionUrl"
  - "Claude-Session"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In Anthropic-hosted environments, all GitHub operations go through a dedicated proxy that keeps real GitHub credentials outside the VM, whatever the access level. All outbound internet traffic from the session also passes through an HTTP/HTTPS security proxy (malicious request protection, rate limiting, abuse prevention). Self-hosted environments use your own credentials and network boundary (the proxy is an opt-in there).

# How to use it

The GitHub proxy provides:
- **Git credentials**: the VM's git client holds a scoped credential that the proxy swaps for your token.
- **API requests**: built-in GitHub tools and `gh` calls get real credentials substituted. If neither `GH_TOKEN` nor `GITHUB_TOKEN` is set and the proxy handles auth, both read as the placeholder `proxy-injected`; a script reading `GITHUB_TOKEN` directly gets the placeholder. A token you set passes through unchanged (and is readable by anyone using the environment). Check with `echo $GH_TOKEN`.
- **Push restrictions**: rejects branch deletions and pushes of non-branches such as tags; does not limit which branches can be updated (use GitHub branch protection or rulesets).
- **Repository scope**: only repositories attached to the session. Others get a 403 starting `GitHub access to` ... `is not enabled for this session`, including source archives via `github.com/{owner}/{repo}/archive/` or `codeload.github.com`, even for public repos.
- **GraphQL**: rejected with a 403 beginning `GitHub GraphQL is not available from Claude Code sessions`, regardless of credentials (a set `GH_TOKEN` gets the same). `gh pr` and `gh issue` (GraphQL-based) fail; use `gh api repos/{owner}/{repo}/...` and REST subcommands like `gh workflow list`. GraphQL-only APIs such as Projects v2 are unreachable.

Files from public repos arrive via `raw.githubusercontent.com` (default allowlist) through the security proxy.

# Notes

Commits Claude makes in a cloud session carry a `Claude-Session: <url>` trailer and PR bodies include the session URL; set `attribution.sessionUrl` to `false` to omit both. For other output, run `echo "https://claude.ai/code/${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}"` (converts the `cse_` prefix to `session_`).
