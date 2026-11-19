---
type: "Feature"
title: "Code Review managed service"
description: "Managed multi-agent pull request review on GitHub for Team and Enterprise: find, verify, rank, post; never approves or blocks."
resource: "https://code.claude.com/docs/en/code-review"
tags: [code-review, github, pull-requests, multi-agent]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan; GitHub repositories (including GitHub Enterprise Server and GitHub Enterprise Cloud with data residency); an Owner turns it on"
identifiers:
  - "Claude Code Review"
  - "@claude review"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review"
    resource: "https://code.claude.com/docs/en/code-review"
    title: "Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Several agents read each pull request alongside surrounding code, a verification step filters false positives, and the review posts inline comments ranked by severity, a summary and a check run named **Claude Code Review**. A review never approves or blocks the PR, and the check run does not conclude as a failure. By default it focuses on correctness (bugs that break production), not formatting or missing tests.

# How to use it

Pipeline on Anthropic infrastructure: 1 Find (agents examine the diff in parallel), 2 Verify, 3 Rank (deduplicate), 4 Post. A **Code review found no issues** note is posted when nothing is found. Reviews start per each repository's setting (once on open, after every push, or manual) and anyone with write access can comment `@claude review`. Admin setup is on [Set up Code Review](./code-review-setup-admin.md) page concepts; see also the sibling pages for customization, costs and troubleshooting.

# Limits and defaults

- Not available with Zero Data Retention or the HIPAA configuration, not covered by Anthropic's BAA, and not yet available with customer-managed encryption keys (CMEK).
- A Claude organization on Team or Enterprise is needed even if developers use Bedrock, Google Cloud's Agent Platform or Foundry.
- Code Review chooses the models; admin settings offer no model choice. Thoroughness is set by the review level.
- Access: runs in a managed environment, not in self-hosted environments; read-only repository access, no pushed commits; it posts comments and the check run, resolves its own earlier threads, and can react to a command with an eyes emoji. It reads the diff and surrounding code without building or running code.
- Automatic reviews skip drafts and forks. `REVIEW.md` is read from the base or default branch, never from the PR's own changes.

# Notes

| Option | Starts when | Where it runs | Who |
| :- | :- | :- | :- |
| Code Review | PR activity per repo setting, or `@claude review` | Anthropic infrastructure | Team/Enterprise with GitHub |
| `/code-review` | You run it | Your session | Any plan |
| Ultrareview | You start it | Cloud sandbox | claude.ai sign-in required |
| GitHub Actions / GitLab CI/CD | Pipeline events | Your runners | Anyone with API key or cloud credentials |
| Your own reviewer subagent or skill | You or Claude invoke it | Wherever Claude Code runs | Anyone |

Review levels: **Quick** (lightest, fastest, cheapest), **Standard** (default), **Deep** (most thorough, slowest, costliest); one org default plus per-repository overrides.
