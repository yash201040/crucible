---
type: "Feature"
title: "HTTP hooks"
description: "type http hooks POST the event JSON to a URL and read the decision from the response body; headers interpolate allowed env vars."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, http, webhooks, audit]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "type: http"
  - "url"
  - "headers"
  - "allowedEnvVars"
  - "onFailure"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An `http` hook POSTs the same JSON a command hook gets on stdin to an endpoint, useful for a web server, cloud function or shared audit service. The endpoint answers with the same JSON output format.

# How to use it

```json
{"type":"http","url":"http://localhost:8080/hooks/tool-use","headers":{"Authorization":"Bearer $MY_TOKEN"},"allowedEnvVars":["MY_TOKEN"]}
```

- 2xx status: return `hookSpecificOutput` fields in the body to block a call.
- Any other status or a failed request: a non-blocking error and the action continues, unless the hook is one whose failure blocks; set `onFailure: "block"` to make a failed endpoint block.
- Header values interpolate `$VAR_NAME` or `${VAR_NAME}`; only variables listed in `allowedEnvVars` resolve, others stay empty.
