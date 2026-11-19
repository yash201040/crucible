---
type: "Feature"
title: "HTTP hooks and response handling"
description: "HTTP hook fields, header env-var interpolation, and how status codes and bodies are interpreted."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, http, headers, response]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: ""
identifiers:
  - "url"
  - "headers"
  - "allowedEnvVars"
  - "onFailure"
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An HTTP hook (`type: "http"`) POSTs the event's JSON input as the request body with `Content-Type: application/json`. The response body uses the same JSON output format as command hooks.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `url` | yes | POST target |
| `headers` | no | Extra headers; values support `$VAR_NAME` or `${VAR_NAME}`; only variables listed in `allowedEnvVars` are resolved |
| `allowedEnvVars` | no | Env var names allowed in header interpolation; unlisted references become empty strings; required for any interpolation |
| `onFailure` | no | `"continue"` or `"block"`, v2.1.295+ |

Example: `{"type":"http","url":"http://localhost:8080/hooks/pre-tool-use","timeout":30,"headers":{"Authorization":"Bearer $MY_TOKEN"},"allowedEnvVars":["MY_TOKEN"]}`.

Response handling (except events with their own failure contract, such as `WorktreeCreate`):
- 2xx with empty body: success, same as exit 0 with no output
- 2xx with JSON object: parsed with the command-hook schema; failing validation is a non-blocking error
- 2xx with other body (plain text): non-blocking error; text not added to context
- non-2xx status or connection failure: non-blocking error
- timeout: hook canceled

To block a tool call or deny a permission, return 2xx with JSON decision fields. To block on request failure or non-2xx, set `onFailure: "block"`.

# Notes

Allowlists `allowedHttpHookUrls` and `httpHookAllowedEnvVars` are described in [locations and scope](./p1-hook-locations-and-scope.md). An HTTP `WorktreeCreate` hook returns JSON (`hookSpecificOutput.worktreePath`) and can include `terminalSequence`.
