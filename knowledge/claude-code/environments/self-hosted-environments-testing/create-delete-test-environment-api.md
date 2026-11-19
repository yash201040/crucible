---
type: "Feature"
title: "Create and delete test environments via API"
description: "Programmatic create and delete of self-hosted environments with the ccr-byoc beta header, so each CI run gets a clean environment."
resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
tags: [self-hosted, api, ci, environment, secrets]
kind: "api"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Owner-role claude.ai OAuth token; Allow self-hosted environments enabled; curl 7.55+ for -H @-"
identifiers:
  - "https://api.anthropic.com/v1/code/runners/self-hosted/pools"
  - "anthropic-beta: ccr-byoc-2025-07-29"
  - "anthropic-version: 2023-06-01"
  - "SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET"
  - "pool_secret"
  - "pool.pool_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-testing"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-testing"
    title: "Test self-hosted environments end to end"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The same endpoints the Cloud environments admin page uses, requiring header `anthropic-beta: ccr-byoc-2025-07-29`.

# How to use it

- Create: `POST https://api.anthropic.com/v1/code/runners/self-hosted/pools` with JSON `{"name":"ci-test-environment"}` and headers `anthropic-version: 2023-06-01`, content-type JSON. Response gives `.pool.pool_id` (the `ccpool_...` ID) and `.pool_secret`, a long-lived credential that can register runners; store as a masked CI secret, print only the ID. Start a runner with `SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET=$ENVIRONMENT_SECRET`.
- Delete: `DELETE https://api.anthropic.com/v1/code/runners/self-hosted/pools/$ENVIRONMENT_ID`.
- Admin token: an OAuth access token from `claude auth login` as an Owner; read it fresh each run (rotates; 30-day refresh cap) and pass the header via stdin (`-H @-`, curl 7.55+; older curl sends no authorization) so it stays out of the process list and logs.

# Limits and defaults

Until an Owner enables Allow self-hosted environments the call fails with `403` `permission_error` reading `self-hosted runners are disabled by your organization's policy`.
