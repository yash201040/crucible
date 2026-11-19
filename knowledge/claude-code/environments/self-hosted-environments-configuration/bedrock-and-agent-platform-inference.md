---
type: "Guide"
title: "Send model requests to Bedrock or Agent Platform"
description: "Configure a runner so sessions call models in your AWS or Google Cloud account, and what changes in those sessions."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, bedrock, vertex, inference, model]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Self-hosted environments; Amazon Bedrock or Google Cloud Agent Platform account"
identifiers:
  - "CLAUDE_CODE_USE_BEDROCK"
  - "AWS_REGION"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLOUD_ML_REGION"
  - "ANTHROPIC_VERTEX_PROJECT_ID"
  - "--confine-repo-settings"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "bedrock:InvokeModel"
  - "bedrock:InvokeModelWithResponseStream"
  - "aiplatform.endpoints.predict"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runners can route model requests to your own Amazon Bedrock or Google Cloud Agent Platform (formerly Vertex AI) account. The runner still polls Anthropic and the event stream (prompts, responses, tool results) still goes to `api.anthropic.com`. Plan and Zero Data Retention exclusions still apply.

# How to use it

1. Prepare the account: Bedrock use-case details and an IAM policy limiting `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` to the inference profiles used; Agent Platform API enabled and a custom role with only `aiplatform.endpoints.predict`; allow provider endpoints through egress.
2. Give narrowly scoped, self-renewing credentials (file-based web identity such as IRSA or Workload Identity Federation). Anyone who can run code in a session, including through prompt injection, can use these credentials; the shell, Claude Code hooks and stdio MCP servers can read them. Denying the metadata endpoint also blocks instance-profile credentials. Wrapper-exported credentials are not renewed.
3. Set exactly one provider's variables in the runner environment (or on the workload an on-demand hook starts), then restart: Bedrock `CLAUDE_CODE_USE_BEDROCK=1` and `AWS_REGION=us-east-1`; Agent Platform `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION=global`, `ANTHROPIC_VERTEX_PROJECT_ID=<id>`. If both appear, Bedrock is used.
4. Start these runners with `--confine-repo-settings enforce` (try default `warn` first).
5. Verify from inside a session with `env | grep -E 'CLAUDE_CODE_USE_(BEDROCK|VERTEX)'`.

Configure every runner in the environment identically, since requeued sessions can move runners.

# Limits and defaults

- Server-managed settings and claude.ai organization policies do not reach these sessions; put rules in the runner image's managed settings file.
- Account skills are not downloaded; claude.ai/app file attachments do not arrive and the `SendUserFile` tool cannot send files back.
- Model selection: the control plane sends the model; the runner removes `ANTHROPIC_MODEL` and `ANTHROPIC_DEFAULT_MODEL` from the session environment. Per-family pinning variables do reach sessions and affect alias resolution only. Enable the background model and the auto mode classifier model too.
- Web search is unavailable on Amazon Bedrock; fast mode is unavailable on both.
- If provider endpoints are unreachable Claude Code can retry for hours before an error shows.
