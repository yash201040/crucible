---
type: "Feature"
title: "Git configuration and Anthropic git proxy"
description: "How runners get git identity, credentials and signing: --configure-git, shipped config, Anthropic-managed git (github.com only), URL rewrites."
resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
tags: [self-hosted, git, credentials, git-proxy, signing]
kind: "mixed"
maturity: "beta"
since: "2.1.267"
surfaces: [cloud]
requires: "Git 2.24+; git proxy needs Claude Code v2.1.267+ and git 2.32+"
identifiers:
  - "--configure-git"
  - "SELF_HOSTED_RUNNER_CONFIGURE_GIT"
  - "--use-anthropic-git-proxy"
  - "CLAUDE_RUNNER_USE_GIT_PROXY"
  - "--git-host-rewrite"
  - "--git-ssh-rewrite"
  - "--push-outcome-on-release"
  - "GIT_SSL_CAINFO"
  - "GIT_SSL_NO_VERIFY"
  - "GIT_TERMINAL_PROMPT"
  - "GCM_INTERACTIVE"
  - "GIT_SSH_COMMAND"
  - "GIT_ASKPASS"
  - "attribution.sessionUrl"
  - "--environment"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-deploy"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-deploy"
    title: "Deploy self-hosted environments to production"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The runner manages checkouts but sets no git identity or credentials by default. Options: let the runner configure git, ship config in the image, or ask Anthropic to serve git for github.com repositories (Anthropic-managed git, the git proxy).

# How to use it

- `--configure-git` (or `SELF_HOSTED_RUNNER_CONFIGURE_GIT=1`) writes global config: `user.name = Claude`, `user.email = noreply@anthropic.com`, SSH commit/tag signing through Anthropic's signing service (git 2.34+, else startup error), `push.negotiate = true` (v2.1.257+), and `core.hooksPath` hooks adding a `Co-authored-by:` trailer from `CCR_SESSION_ACCOUNT_EMAIL`. From v2.1.280, commits in `checkout`/`post-session` hooks are signed as the session. Push credentials remain yours.
- Image approach: `git config --system user.name/user.email` and `safe.directory '*'`. Mint push tokens per session in a wrapper. Image-level credentials should be scoped tightly (single-repo deploy key with `url.<base>.insteadOf`, a `credential.helper`, or `GIT_SSH_COMMAND`). They must work without a prompt: the runner sets `GIT_TERMINAL_PROMPT=0`, SSH `BatchMode=yes`, `GCM_INTERACTIVE=never`, and clears `core.askPass` (use `GIT_ASKPASS`).
- Git proxy: `--use-anthropic-git-proxy` or `CLAUDE_RUNNER_USE_GIT_PROXY=1`. Startup prints `Registering as opted in to Anthropic-managed git (--use-anthropic-git-proxy)`; each served session logs `[runner:session]` with `governed git ACTIVE`.
- URL rewrites: `--git-host-rewrite <from>=<to>` (split-horizon DNS) and `--git-ssh-rewrite <host>`; host rewrite runs first; no effect on repositories the proxy serves.
- Non-GitHub repo session: from a checkout, `claude -p "Fix the login bug" --environment ccpool_abc123 --output-format json`. `origin` host must be a domain and path `<owner>/<name>` (no nesting), else `requires a git source, but no GitHub remote was detected`.
- Built-in `gh` (v2.1.287+): only `gh api`, for runners with managed git and no GitHub CLI in the image; log shows `gh_path_shim=true`; absent if `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set.
- Private CA (v2.1.283+): `GIT_SSL_CAINFO` (PEM, max 1 MiB, needs a system CA bundle) is honored; `GIT_SSL_NO_VERIFY` does not help for the runner's own managed-git clone.

# Limits and defaults

- Git proxy: github.com only (no GitHub Enterprise Server); credentials only for the session's repositories; branch pushes only (no deletes or tags); creators need a connected GitHub account; requires `--capacity 1` (runner exits at startup otherwise; Kubernetes and Compose recipes use 4); deletes and replaces the global git config (`~/.gitconfig`, `GIT_CONFIG_GLOBAL`, `$XDG_CONFIG_HOME/git`) of the runner's user with no backup; per-session decision, and withheld sessions fail to start (`the server withheld Anthropic-managed git for this session`, `remote: access denied by the git proxy`, `GitHub authentication required`).
- Bot and agent sessions use the organization's GitHub App installation token; user sessions use the creator's stored GitHub OAuth token.
- Git floors: signing 2.34, proxy 2.32, resume from `--push-outcome-on-release` branches 2.29.
- Sessions always instruct Claude to end commits with a `Claude-Session: <url>` trailer; set `attribution.sessionUrl` to false in the host `~/.claude/settings.json` to omit.
- Claude Tag channel repositories need the Claude GitHub App installed, the org linked under Git providers, and a repository grant in Claude Tag admin settings.
