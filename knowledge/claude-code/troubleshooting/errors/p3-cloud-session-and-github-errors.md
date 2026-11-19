---
type: "Reference"
title: "Cloud session and GitHub connection errors"
description: "Errors when creating cloud sessions: org policy, claude.ai login vs API key, GitHub connection, org SSO/IP policy, repo upload refusals, teleport stash."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, cloud-sessions, github, teleport, policy]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.268"
surfaces: [cli, cloud]
requires: "claude.ai login for cloud sessions"
identifiers:
  - "allow_remote_sessions"
  - "--cloud"
  - "--teleport"
  - "/teleport"
  - "/remote-env"
  - "/web-setup"
  - "/autofix-pr"
  - "/schedule"
  - "/install-github-app"
  - "ANTHROPIC_API_KEY"
  - "gh auth refresh -h github.com -s repo,workflow"
  - "core.ignoreCase"
  - "core.attributesFile"
  - "attr.tree"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Refusals from Claude Code when starting, resuming or messaging a cloud session (`--cloud`, `--teleport`, `/teleport`, `/web-setup`, `/autofix-pr`, `/schedule`), or when an ultrareview needs a GitHub clone.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Cloud sessions are disabled by your organization's policy` | Org policy `allow_remote_sessions` is off; also returned by `/teleport`, `/remote-env`, `/web-setup` (before v2.1.268 those gave `Unknown command`) | An Owner enables cloud sessions at claude.ai/admin-settings/claude-code |
| Same plus `This session is using ANTHROPIC_API_KEY ... Cloud sessions use your claude.ai login.` | Policy checked for the org that issued the API key (form since v2.1.296) | Cloud sessions run on the claude.ai login, not the key |
| `Couldn't verify your organization's policy for cloud sessions` | Policy request unfinished; inside a session also asks to restart Claude Code | Check network and retry |
| `Cloud sessions aren't available: ...` | Policy request failed (no route to api.anthropic.com, proxy 403, server error, rejected credentials; may say to unset `ANTHROPIC_API_KEY`) since v2.1.296 | Fix the named cause |
| `Nothing was stashed because a folder replaced a tracked file` | Stash option while teleporting a cloud session into the terminal; checkout unchanged | Commit or move the folder |
| `GitHub isn't connected to your Claude account` | No GitHub account connected or expired; for `/schedule` it is a setup note that does not block the task | `/web-setup` or claude.ai/connect-github, retry a minute later (before v2.1.268 reported as a Claude GitHub App check failure) |
| `The GitHub App preflight failed transiently` | Repo bundle upload failed AND the clone-check hit a retryable error | Retry; before v2.1.251 the message ended with `Please set up GitHub on https://claude.ai/code` |
| `Not uploading this working tree: core.ignoreCase ...` | Upload of a local repo (or ultrareview branch) cannot follow `core.ignoreCase`, `core.attributesFile` or `attr.tree`; nothing uploaded | Move the setting into the repo `.git/config` or `~/.gitconfig` |
| `A GitHub organization policy is blocking Claude` | IP allow list, SAML SSO, or Microsoft Entra ID Conditional Access blocked the repo check | Allow Anthropic IP ranges; reconnect GitHub and click Authorize; or ask the Entra admin |
| `Single sign-on authorization needed` | `/install-github-app` on an SSO org with an unauthorized `gh` token (since v2.1.273; before, `Admin permissions required`) | `gh auth refresh -h github.com -s repo,workflow`, or Configure SSO on a `GH_TOKEN` PAT |

# Notes

The ultrareview-specific preflight errors (no GitHub account, repo not visible, diff too large, no merge-base, no branches) are in [workspace trust and ultrareview errors](./p3-trust-and-ultrareview-errors.md).
