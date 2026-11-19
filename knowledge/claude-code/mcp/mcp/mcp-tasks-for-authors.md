---
type: "Reference"
title: "MCP tasks for server authors"
description: "Wire format Claude Code expects when a tools/call is answered with a task, tasks/get polling and per-status handling."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, tasks, server-author, protocol]
kind: "api"
maturity: "beta"
since: "2.1.304"
surfaces: [cli, sdk]
requires: "protocol revision 2026-07-28"
identifiers:
  - "io.modelcontextprotocol/clientCapabilities"
  - "io.modelcontextprotocol/tasks"
  - "resultType"
  - "taskId"
  - "status"
  - "statusMessage"
  - "pollIntervalMs"
  - "ttlMs"
  - "createdAt"
  - "lastUpdatedAt"
  - "tasks/get"
  - "tasks/update"
  - "tasks/cancel"
  - "inputRequests"
  - "inputResponses"
  - "elicitation/create"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A server answers a long `tools/call` with a task object as the JSON-RPC `result`. Requests on a 2026-07-28 connection carry client capabilities at `params._meta["io.modelcontextprotocol/clientCapabilities"]` with `"io.modelcontextprotocol/tasks": {}` under `extensions`; a call that cannot become a task omits it. Answer with a task only when the extension is present, else the tool error `Unsupported result type 'task' for tools/call` (also when `taskId` or a valid `status` is missing).

# How to use it

| Field | Handling |
|---|---|
| `resultType` | `"task"` to mark the reply; otherwise read as plain result |
| `taskId` | required; at most 128 printable ASCII characters, no spaces, else error `MCP server "<name>" returned a malformed task handle for tool "<tool>"`; must stay answerable across connections |
| `status` | required: `working`, `input_required`, `completed`, `failed`, `cancelled` |
| `createdAt`, `lastUpdatedAt`, `ttlMs` | required by the extension (`ttlMs` may be `null`); a task is not dropped when `ttlMs` passes; omitting them is accepted (before v2.1.317 it failed) |
| `pollIntervalMs` | optional; clamped to 250-30000; 2000 when absent or `null`; re-read from each `tasks/get` |
| `statusMessage` | optional; `/tasks` shows the latest `tasks/get` value |

Claude Code sends `tasks/get` right after, then once per poll interval. Responses need `"resultType": "complete"`, `taskId`, `status`, timestamps, `ttlMs`.

| Status or method | Handling |
|---|---|
| `working` | keep polling |
| `completed` | top-level `result` is the normal tools/call result; `isError: true` reported as failure |
| `failed` | top-level `error.message`, else `statusMessage`, else `Task failed` |
| `cancelled` | `statusMessage`, else `Task was cancelled by the server` |
| `input_required` | reads `inputRequests` (key to `{ method, params }`), answers each once via `tasks/update` with `{ taskId, inputResponses }`; keys beyond 16 per task ignored |
| methods in `inputRequests` | `elicitation/create` only in interactive terminal sessions; `roots/list` everywhere; unservable requests cause a cancel request |
| other status | cancel asked, reported failed |
| JSON-RPC `-32602` | unknown task ID; background task keeps asking up to five minutes then outcome unknown |
| `tasks/cancel` | sent when Claude or the person stops the task while connected; not on exit |
| `tasks/result`, `tasks/list`, `notifications/tasks` | not used |

# Notes

On HTTP or claude.ai connector servers the task answer must start within the per-request timer, so accept the job and answer first.
