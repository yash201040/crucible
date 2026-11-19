---
type: "Guide"
title: "Amazon Bedrock setup, wizard and region"
description: "Enable Claude Code on Amazon Bedrock with the /setup-bedrock wizard or environment variables, and how the AWS region is resolved."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, aws, setup, region]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "AWS account with Amazon Bedrock access and Anthropic use case form submitted"
identifiers:
  - "CLAUDE_CODE_USE_BEDROCK"
  - "AWS_REGION"
  - "AWS_DEFAULT_REGION"
  - "AWS_PROFILE"
  - "AWS_SHARED_CREDENTIALS_FILE"
  - "AWS_CONFIG_FILE"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION"
  - "/setup-bedrock"
  - "/status"
  - "/logout"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to point Claude Code at Amazon Bedrock: an interactive login wizard, or plain environment variables (the route for CI and scripted rollouts).

# How to use it

- Once per AWS account, submit the Anthropic use case form in the Bedrock console Model catalog; access is granted immediately. With AWS Organizations, submit once from the management account with the `PutUseCaseForModelAccess` API (needs `bedrock:PutUseCaseForModelAccess`); approval extends to child accounts.
- Wizard: run `claude`, choose **3rd-party platform** then **Amazon Bedrock**; if already signed in, run `/setup-bedrock`. The command is hidden from the menu until `CLAUDE_CODE_USE_BEDROCK=1` is set, but can be typed in full. It offers AWS profile, Bedrock API key, access key and secret, or ambient credentials; asks region; checks which models the account can invoke; lets you pin them. It writes the `env` block of `~/.claude/settings.json` (or `$CLAUDE_CONFIG_DIR/settings.json`).
- Manual: `export CLAUDE_CODE_USE_BEDROCK=1`, optionally `AWS_REGION=us-east-1`, `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` (no effect on Bedrock without `ANTHROPIC_DEFAULT_HAIKU_MODEL` or the deprecated `ANTHROPIC_SMALL_FAST_MODEL`), and `ANTHROPIC_BEDROCK_BASE_URL` for custom endpoints or gateways.
- Region order: `AWS_REGION`, `AWS_DEFAULT_REGION`, the active profile's `region` (credentials file then config file), then `us-east-1`. A value containing a slash, dot or space counts as unset. Active profile is `AWS_PROFILE` or `default`; `AWS_SHARED_CREDENTIALS_FILE` / `AWS_CONFIG_FILE` move the files. `/status` shows the resolved region and its source.

# Limits and defaults

- `/logout` is unavailable on Bedrock.
- The WebSearch tool is not available on Bedrock.
- Put variables such as `AWS_PROFILE` in settings files to keep them from leaking to other processes.
