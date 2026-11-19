---
type: "Feature"
title: "Amazon Bedrock Mantle endpoint"
description: "Mantle serves Claude through the native Anthropic API shape on Bedrock; how to enable it, pick models, combine with Invoke and route via a gateway."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, mantle, gateway, models]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Amazon Bedrock; models allowlisted by AWS account team"
identifiers:
  - "CLAUDE_CODE_USE_MANTLE"
  - "ANTHROPIC_BEDROCK_MANTLE_BASE_URL"
  - "CLAUDE_CODE_SKIP_MANTLE_AUTH"
  - "bedrock-mantle:CreateInference"
  - "bedrock-mantle:CountTokens"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Mantle is a Bedrock endpoint that serves Claude via the native Anthropic API shape instead of the Invoke API. It reuses AWS credentials and `awsAuthRefresh`, but has its own IAM actions under `bedrock-mantle:`.

# How to use it

- Enable: `CLAUDE_CODE_USE_MANTLE=1` (or `true`) plus `AWS_REGION`. Grant `bedrock-mantle:CreateInference` and `bedrock-mantle:CountTokens`. Override URL with `ANTHROPIC_BEDROCK_MANTLE_BASE_URL`. `/status` shows `Amazon Bedrock (Mantle)`.
- Model IDs start with `anthropic.` and have no version suffix, e.g. `anthropic.claude-sonnet-5`, `anthropic.claude-haiku-4-5`; set via `--model` or `/model`. Access is per organization grant.
- Together with Invoke: set both `CLAUDE_CODE_USE_BEDROCK=1` and `CLAUDE_CODE_USE_MANTLE=1`; Mantle-format IDs go to Mantle, others to Invoke. List Mantle IDs in `availableModels` to show them in `/model` (this also restricts the picker; listing a Mantle ID drops the bare alias, so list prefixes or full IDs too). `/status` then shows `Amazon Bedrock + Amazon Bedrock (Mantle)`.
- Via a central LLM gateway that injects AWS credentials: `CLAUDE_CODE_USE_MANTLE=1`, `CLAUDE_CODE_SKIP_MANTLE_AUTH=1` (no SigV4 or `x-api-key`), `ANTHROPIC_BEDROCK_MANTLE_BASE_URL=<gateway>`.

# Limits and defaults

- Service tier variable has no effect on Mantle.
- 403 naming a `bedrock-mantle:` action: grant it. 403 with no action: account lacks model access. 400 naming the model: not served on Mantle (inference profile IDs like `us.anthropic.claude-sonnet-4-6` do not work).
