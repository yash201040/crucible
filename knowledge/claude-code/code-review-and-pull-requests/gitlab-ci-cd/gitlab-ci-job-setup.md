---
type: "Guide"
title: "Claude Code in GitLab CI/CD jobs"
description: "Run claude -p in a .gitlab-ci.yml job with a masked ANTHROPIC_API_KEY, acceptEdits permission mode and allowedTools; beta, maintained by GitLab."
resource: "https://code.claude.com/docs/en/gitlab-ci-cd"
tags: [gitlab, ci-cd, headless, beta]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [headless]
requires: "GitLab runners; ANTHROPIC_API_KEY or cloud provider credentials"
identifiers:
  - "ANTHROPIC_API_KEY"
  - "GITLAB_ACCESS_TOKEN"
  - "CI_JOB_TOKEN"
  - "AI_FLOW_INPUT"
  - "AI_FLOW_CONTEXT"
  - "AI_FLOW_EVENT"
  - "claude -p"
  - "--permission-mode acceptEdits"
  - "--allowedTools"
  - "mcp__gitlab"
  - "--max-turns"
  - "timeout"
  - "GIT_STRATEGY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gitlab-ci-cd"
    resource: "https://code.claude.com/docs/en/gitlab-ci-cd"
    title: "Claude Code GitLab CI/CD"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Beta integration maintained by GitLab (support through a GitLab issue), built on the Claude Code CLI and Agent SDK. Event-driven: a trigger (such as a comment mentioning `@claude` in an issue, MR or review thread) starts a job that collects thread and repo context, builds a prompt and runs Claude Code in a container with strict network and filesystem rules and workspace-scoped write permissions; every change goes through an MR so approvals still apply. Claude can create/update MRs from issues, fix bugs, analyze regressions and respond to follow-up comments.

# How to use it

Quick setup: add masked CI/CD variable `ANTHROPIC_API_KEY`; add a job with stage `ai`, image `node:24-alpine3.21`, rules on `$CI_PIPELINE_SOURCE == "web"` and/or `"merge_request_event"`, `GIT_STRATEGY: fetch`, `before_script` installing git, curl, bash and `curl -fsSL https://claude.ai/install.sh | bash` then `export PATH="$HOME/.local/bin:$PATH"`, and script: `claude -p "${AI_FLOW_INPUT:-'Review this MR and implement the requested changes'}" --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab" --debug` (optionally `/bin/gitlab-mcp-server || true` first).

Production setup: configure provider access; for GitLab API operations use `CI_JOB_TOKEN` or a Project Access Token with `api` scope stored as masked `GITLAB_ACCESS_TOKEN`; optionally add a "Comments (notes)" project webhook to an event listener that calls the pipeline trigger API with `AI_FLOW_INPUT` and `AI_FLOW_CONTEXT` when a comment contains `@claude`.

# Limits and defaults

Cost controls: `--max-turns`, job-level `timeout` (e.g. `30m`), limited concurrency, specific `@claude` commands. Costs are runner minutes plus API tokens. Exact flags vary by `@anthropic-ai/claude-code` version; run `claude --help` in the job.

# Notes

Troubleshooting: pipeline not triggered (manual, MR event or note listener), variables missing, comment must contain `@claude` not `/claude`; write failures: check `CI_JOB_TOKEN` permissions or use a PAT with `api` scope, `mcp__gitlab` must be in `--allowedTools`, and the job needs MR context or `AI_FLOW_*`. Guidance: keep `CLAUDE.md` concise, cache npm installs, use masked variables, limit job permissions and network egress, review Claude's MRs like any contributor.
