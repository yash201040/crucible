---
type: "Guide"
title: "GitHub Actions on Bedrock, Agent Platform and Foundry"
description: "Route claude-code-action inference through your cloud via use_bedrock, use_vertex or use_foundry with OIDC federation and no static cloud credentials."
resource: "https://code.claude.com/docs/en/github-actions-cloud-providers"
tags: [github-actions, bedrock, oidc, cloud-providers]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [headless, cloud]
requires: "Admin access to the repo; permission to create identity resources in the cloud account; Claude model access on the provider"
identifiers:
  - "use_bedrock"
  - "use_vertex"
  - "use_foundry"
  - "AWS_ROLE_TO_ASSUME"
  - "GCP_WORKLOAD_IDENTITY_PROVIDER"
  - "GCP_SERVICE_ACCOUNT"
  - "AZURE_CLIENT_ID"
  - "AZURE_TENANT_ID"
  - "AZURE_SUBSCRIPTION_ID"
  - "APP_ID"
  - "APP_PRIVATE_KEY"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "CLOUD_ML_REGION"
  - "ANTHROPIC_FOUNDRY_RESOURCE"
  - "id-token: write"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-actions-cloud-providers"
    resource: "https://code.claude.com/docs/en/github-actions-cloud-providers"
    title: "Use Claude Code GitHub Actions with cloud providers"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The action calls the Claude API by default. Set one provider input in the step's `with:` block (`use_bedrock: "true"`, `use_vertex: "true"` for Google Cloud's Agent Platform, `use_foundry: "true"`) and make the cloud trust the workflow's GitHub OIDC token, so no long-lived cloud credential is stored. The workflow must have `id-token: write`.

# How to use it

1. Pick a GitHub identity: official Claude GitHub App; a custom GitHub App (webhooks disabled; Contents, Issues, Pull requests read/write; generate a private key, note App ID, install on the repo); or the automatic `GITHUB_TOKEN` (no app, but GitHub does not trigger your CI on its commits).
2. Cloud trust. Bedrock: GitHub OIDC provider `https://token.actions.githubusercontent.com` with audience `sts.amazonaws.com`; IAM role granting `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:ListInferenceProfiles`, `bedrock:GetInferenceProfile` plus two `aws-marketplace` subscription actions; trust limited with a subject condition like `repo:your-org/your-repo:*`. Agent Platform: enable IAM Credentials, STS and `aiplatform.googleapis.com`; Workload Identity Pool with GitHub provider and a repo attribute condition; service account with `roles/aiplatform.user` only. Foundry: Entra application (or user-assigned managed identity) with a federated credential and the `Foundry User` role on the resource.
3. Secrets: `AWS_ROLE_TO_ASSUME`; `GCP_WORKLOAD_IDENTITY_PROVIDER` and `GCP_SERVICE_ACCOUNT`; `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`; custom app: `APP_ID` and `APP_PRIVATE_KEY`.
4. Workflow: checkout, `actions/create-github-app-token@v2`, then `aws-actions/configure-aws-credentials@v4` (exports `AWS_REGION`), `google-github-actions/auth@v2`, or `azure/login@v2`, then the action with `github_token: ${{ steps.app-token.outputs.token }}` and `claude_args: '--model ...'`. Env needed: Agent Platform `ANTHROPIC_VERTEX_PROJECT_ID` (from the auth step) and `CLOUD_ML_REGION` (e.g. `us-east5`); Foundry `ANTHROPIC_FOUNDRY_RESOURCE`. Bedrock model IDs carry a cross-region prefix such as `us.` (example `us.anthropic.claude-sonnet-4-6`).

# Limits and defaults

- Cross-region Bedrock inference profiles need model access granted in every region of the group.
- Bound run length and cost with `--max-turns` in `claude_args`.
- Warning: on public repos any user's comment with the trigger phrase starts the workflow; credential steps run before the action checks write access, leaving audit-log entries and using Actions minutes. Add a step verifying commenter write access before credentials.

# Notes

Auth errors are usually OIDC misconfiguration: missing `id-token: write`, repo condition not matching exactly, or secret names not matching.
