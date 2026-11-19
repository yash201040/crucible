---
type: "Guide"
title: "Bedrock troubleshooting"
description: "Fixes for SSO auth loops, TLS-inspecting proxy certificate errors, region and throughput errors, gateway streaming content-type errors and zero /context counts."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, troubleshooting, proxy, streaming]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Amazon Bedrock"
identifiers:
  - "CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD"
  - "CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT"
  - "NODE_EXTRA_CA_CERTS"
  - "/context"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Known failure modes on Bedrock and the documented fixes.

# How to use it

- Repeated SSO browser tabs: remove `awsAuthRefresh`, run `aws sso login` manually.
- Certificate errors: CA store config applies to model discovery, token counting, STS/SSO role calls and the wizard checks; before v2.1.260 only requests via a configured proxy used it; before v2.1.261 the wizard's "Use credentials already in my environment" lookup failed (`unable to get local issuer certificate`, models shown `unreachable`).
- Region: `aws bedrock list-inference-profiles --region <r>`; "on-demand throughput isn't supported" means specify an inference profile ID.
- Streaming behind a gateway: Bedrock streams binary `application/vnd.amazon.eventstream`. A gateway that rewrites `Content-Type` (commonly to `text/event-stream`) triggers an error beginning `Bedrock streaming response has content-type`; the variable `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD` is named in that error. A gateway that drops the header and re-emits SSE forces a slower non-streaming path each turn; set `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT=1`. A gateway that converts to SSE is better connected as an LLM gateway via `ANTHROPIC_BASE_URL`.
- `/context` showed 0 tokens per tool group before v2.1.196 (count-tokens rejected schemas).
- Mantle: if `/status` lacks the Mantle provider line, the variable is not reaching the process.
