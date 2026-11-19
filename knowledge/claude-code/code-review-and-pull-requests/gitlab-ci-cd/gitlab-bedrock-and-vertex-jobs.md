---
type: "Guide"
title: "GitLab jobs on Bedrock and Agent Platform with OIDC"
description: "GitLab CI job templates that exchange GITLAB_OIDC_TOKEN for AWS or Google Cloud credentials and run Claude Code with CLAUDE_CODE_USE_BEDROCK or CLAUDE_CODE_USE_VERTEX."
resource: "https://code.claude.com/docs/en/gitlab-ci-cd"
tags: [gitlab, bedrock, oidc, workload-identity]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [headless]
requires: "Amazon Bedrock or Google Cloud's Agent Platform access; GitLab OIDC configured as an identity provider"
identifiers:
  - "AWS_ROLE_TO_ASSUME"
  - "AWS_REGION"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_VERTEX"
  - "GCP_WORKLOAD_IDENTITY_PROVIDER"
  - "GCP_SERVICE_ACCOUNT"
  - "GCP_PROJECT_ID"
  - "CLOUD_ML_REGION"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "GOOGLE_APPLICATION_CREDENTIALS"
  - "GITLAB_OIDC_TOKEN"
  - "id_tokens"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "gitlab-ci-cd"
    resource: "https://code.claude.com/docs/en/gitlab-ci-cd"
    title: "Claude Code GitLab CI/CD"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both provider jobs mint the OIDC token from an `id_tokens:` block (exposed as `GITLAB_OIDC_TOKEN`, `aud` set to the audience configured on the identity provider, e.g. the GitLab instance URL) so no static keys are stored.

# How to use it

Amazon Bedrock: IAM OIDC provider for GitLab, IAM role with least-privilege Bedrock invoke permissions and trust limited to the project and protected refs. CI variables `AWS_ROLE_TO_ASSUME` and `AWS_REGION` (e.g. `us-west-2`). The job writes the token to a file as `AWS_WEB_IDENTITY_TOKEN_FILE`, runs `aws sts assume-role-with-web-identity` (`--duration-seconds 3600`) and exports the access key, secret and session token, then runs `claude` with `CLAUDE_CODE_USE_BEDROCK: "1"`. Bedrock model IDs carry region prefixes such as `us.anthropic.claude-sonnet-4-6`.

Agent Platform: enable IAM Credentials, STS and Agent Platform APIs; Workload Identity Pool and provider for GitLab OIDC; dedicated service account with Agent Platform roles; allow the WIF principal to impersonate it. Variables `GCP_WORKLOAD_IDENTITY_PROVIDER` (resource name without the `//iam.googleapis.com/` prefix), `GCP_SERVICE_ACCOUNT`, `GCP_PROJECT_ID`, `CLOUD_ML_REGION` (e.g. `us-east5`). The job writes the token to `/tmp/oidc_token`, writes an `external_account` credential config with `credential_source.file`, sets `GOOGLE_APPLICATION_CREDENTIALS`, authenticates `gcloud` with `--cred-file`, and sets `CLAUDE_CODE_USE_VERTEX: "1"` and `ANTHROPIC_VERTEX_PROJECT_ID`. Image: `gcr.io/google.com/cloudsdktool/google-cloud-cli:slim`.

# Notes

`ANTHROPIC_API_KEY` is not used with Bedrock or Agent Platform. With Workload Identity Federation no service account keys are stored; use repository-specific trust conditions and least-privilege service accounts.
