---
type: "Guide"
title: "Multi-tenant isolation in a shared SDK container"
description: "Use settingSources empty, CLAUDE_CODE_DISABLE_AUTO_MEMORY, per-tenant CLAUDE_CONFIG_DIR and cwd, and per-tenant egress rules to keep tenants apart."
resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
tags: [agent-sdk, multi-tenant, isolation, memory, config]
kind: "setting"
maturity: "unlabelled"
since: "0.3.234"
surfaces: [sdk]
requires: "CLAUDE_CODE_PROJECT_DIR_NAME needs TypeScript Agent SDK v0.3.234 or later, or Python v0.2.140 or later"
identifiers:
  - "settingSources"
  - "setting_sources"
  - "CLAUDE_CODE_DISABLE_AUTO_MEMORY"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "cwd"
  - "env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hosting"
    resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
    title: "Hosting the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default the SDK reads settings and `CLAUDE.md` memory from the filesystem, which can leak one tenant's context into another's session in a shared container.

# How to use it

| Step | Detail |
| - | - |
| Skip settings | `settingSources: []` (TypeScript) or `setting_sources=[]` (Python) skips user, project and local settings |
| Turn off auto memory | `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`; auto memory at `~/.claude/projects/<project>/memory/` loads into the system prompt regardless of `settingSources` (other unconditional inputs are listed under "What settingSources does not control") |
| Per-tenant config | Point `CLAUDE_CONFIG_DIR` at a per-tenant directory so tenants do not share `~/.claude.json`. With one working directory per config directory and no `SessionStore`, `CLAUDE_CODE_PROJECT_DIR_NAME` in `env` keeps transcript paths short |
| Per-tenant cwd | Pass `cwd` explicitly on every `query()` call |
| Egress | Per-tenant rules at the proxy (distinct outbound IPs, credentials or domain allowlists) |

In TypeScript `env` replaces the subprocess environment, so spread `...process.env` to keep `PATH` and `ANTHROPIC_API_KEY`; in Python `env` merges on top of the inherited environment.
