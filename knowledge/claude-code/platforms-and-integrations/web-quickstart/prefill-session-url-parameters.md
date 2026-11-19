---
type: "Reference"
title: "Pre-fill cloud session URL parameters"
description: "Query parameters on claude.ai/code that prefill the prompt, repositories and environment of a new cloud session."
resource: "https://code.claude.com/docs/en/web-quickstart"
tags: [url-parameters, integrations, prefill, cloud-sessions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [web]
requires: ""
identifiers:
  - "prompt"
  - "q"
  - "prompt_url"
  - "repositories"
  - "repo"
  - "environment"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "web-quickstart"
    resource: "https://code.claude.com/docs/en/web-quickstart"
    title: "Get started with Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Add URL-encoded query parameters to claude.ai/code, for example a button in an issue tracker that opens Claude Code with the issue as prompt:

```text
https://claude.ai/code?prompt=Fix%20the%20login%20bug&repositories=acme/webapp
```

| Parameter | What it does |
|---|---|
| `prompt` (alias `q`) | Prompt text prefilled in the input box |
| `prompt_url` | URL to fetch prompt text from, for long prompts; must allow cross-origin requests; ignored when `prompt` is set |
| `repositories` (alias `repo`) | Comma-separated `owner/repo` slugs to preselect |
| `environment` | Name or ID of the environment to preselect |

# Notes

The URL prefills only; the page does not say it submits automatically.
