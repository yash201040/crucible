---
type: "Limit"
title: "Limits: hook time, process, model, fs, http, store"
description: "Time and size limits on mod hooks and mods API calls; a hook exceeding a time limit is skipped."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, limits, timeouts, quotas]
kind: "limit"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.process.run"
  - "$.model.complete"
  - "maxTokens"
  - "$.fs.read"
  - "$.fs.write"
  - "$.http.fetch"
  - "$.store"
  - "$.session.messages()"
  - "timeoutMs"
  - "claude plugin test"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code skips a hook that exceeds a time limit.

| Limit | Value |
| :- | :- |
| A hook's own execution time for one event (excludes time inside `next` or mods API calls other than `$.clock.sleep`) | 10 seconds; 50 ms for a `prompt.edit` hook |
| A `.catch` handler's execution time | 1 second |
| All `session.end` hooks together | the SessionEnd hook budget, 1.5 seconds unless changed, counted from when settings `SessionEnd` hooks finish |
| `$.process.run` timeout | 30 seconds default, 10 minutes max |
| `$.process.run` `stdout` and `stderr` | 4 MiB each; `isStdoutTruncated`/`isStderrTruncated` true when cut |
| `$.model.complete` `maxTokens` | 1024 default, up to 64,000 or the model's output limit |
| `$.fs.read` and `$.fs.write` | 4 MiB per file |
| `$.http.fetch` request body | 4 MiB counted in characters; larger rejects |
| `$.http.fetch` response body | 4 MiB; `text` holds the first 4 MiB; a larger declared `Content-Length` rejects with a reason ending `is over the 4194304-byte limit`, except when the last request after redirects uses `HEAD` (exemption needs v2.1.296+) |
| One `$.http.fetch` call incl. redirects and body | 30 seconds |
| Redirects one `$.http.fetch` follows | 5 |
| `$.store` | 4 MiB of JSON total |
| `$.session.messages()` | newest 4,096 entries |
| One `claude plugin test` test | 5 seconds unless the test sets `timeoutMs` |

# Limits and defaults

- A hook's `drop` reason or `config.set` `deny` reason is limited to 4,096 characters; the end is cut and the drop/deny still applies (cut needs v2.1.292+; earlier, the hook fails).
- Scopes (functions, blocks, loops) nested in one file of a hooks module: 2,000.
- Command, tool, subagent type and pane names, the `id` of a placed row and a backdrop `scene`: letters, digits, `_`, `-`, up to 64 characters.
- Nesting depth limits (28,000 levels, need v2.1.299+): a mods API call's arguments reject with a message ending `nesting deeper than 28000 levels is not supported`; a changed event passed to `next` (outside async generator hooks such as `turn.step`) rejects likewise; a hook's return value (outside `ui.render`, `ui.resolve`, async generators) is refused and the notice includes that text.
