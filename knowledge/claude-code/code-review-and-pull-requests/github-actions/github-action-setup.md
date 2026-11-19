---
type: "Guide"
title: "GitHub Action setup, secrets and app permissions"
description: "Install claude-code-action via /install-github-app or manually, with ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN, org rollout, OIDC federation and App permissions."
resource: "https://code.claude.com/docs/en/github-actions"
tags: [github-actions, setup, oidc, secrets]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [headless, cloud]
requires: "Admin access to the repository; /install-github-app works only with github.com repositories"
identifiers:
  - "/install-github-app"
  - "ANTHROPIC_API_KEY"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "claude setup-token"
  - "anthropic_api_key"
  - "claude_code_oauth_token"
  - "anthropic_federation_rule_id"
  - "anthropic_organization_id"
  - "anthropic_service_account_id"
  - "anthropic_workspace_id"
  - "id-token: write"
  - "claude.yml"
  - "claude-code-review.yml"
  - "anthropics/claude-code-action"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-actions"
    resource: "https://code.claude.com/docs/en/github-actions"
    title: "Claude Code GitHub Actions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`anthropics/claude-code-action` runs Claude Code inside GitHub workflows: respond to `@claude` mentions, run a prompt on any GitHub event, turn issues into PRs. It is built on the Agent SDK. Distinct from the managed Code Review service, cloud sessions and GHES.

# How to use it

Quick setup: run `/install-github-app` in the repo (needs `gh` signed in); it installs the Claude GitHub App via browser, optionally sets up the `@claude` mentions workflow and a PR review workflow, saves the credential as a repo secret (`ANTHROPIC_API_KEY` for an API key, `CLAUDE_CODE_OAUTH_TOKEN` for a subscription token), and opens a PR with the workflow files. It prints a notice and exits for gitlab.com or bitbucket.org remotes. Before v2.1.229 the review workflow wrote its review only to the run log; to update an older file add `--comment` to the `prompt` and the example's `claude_args` line.

Manual: install the Claude GitHub App (Contents, Issues, Pull requests read and write used by the action), add a secret (`ANTHROPIC_API_KEY`, or `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token` for Pro, Max, Ultra, Team, Enterprise), copy `examples/claude.yml` to `.github/workflows/`; pass the secret as `anthropic_api_key` or `claude_code_oauth_token`.

Organization rollout: install the App once at org level, store the secret as an org Actions secret (prefer an API key, since an OAuth token is tied to the subscription of whoever ran `claude setup-token`), add the workflow to each repo or use a reusable workflow. Workload identity federation avoids long-lived secrets: set `anthropic_federation_rule_id` (`fdrl_...`), `anthropic_organization_id`, optional `anthropic_service_account_id` (`svac_...`), optional `anthropic_workspace_id` (`wrkspc_...`), and grant `id-token: write` (needed even with your own `github_token`).

# Limits and defaults

The official Claude GitHub App has a single permission set shared by the Action, Code Review and web auto-fix: Actions R/W, Administration R, Checks R/W, Contents R/W, Dependabot alerts R, Discussions R/W, Issues R/W, Members R, Merge queues R, Metadata R, Pull requests R/W, Repository creation R/W, Repository hooks R/W, Statuses R, Workflows R/W. GitHub does not allow accepting a subset; a custom GitHub App with only Contents, Issues and Pull requests covers the Action alone (Code Review and web auto-fix need the official app). Permission changes require owner approval.

# Notes

Uninstall: delete workflows using the action, the secrets (the credential itself stays valid; delete the key in the Console to retire it), and the App if no other Claude feature uses it; for cloud providers also delete `AWS_ROLE_TO_ASSUME`, `GCP_*`, `AZURE_*`, `APP_ID`, `APP_PRIVATE_KEY`.
