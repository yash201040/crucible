---
type: "Reference"
title: "Artifact publishing errors"
description: "Refusals from the Artifact tool: one-step updates blocked by hooks, invalid UTF-8 sources, network share files, repeated stale publishes, Cowork reads."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, artifacts, hooks, publishing]
kind: "tool"
maturity: "unlabelled"
since: "2.1.267"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "PreToolUse"
  - "--add-dir"
  - "U+FFFD"
  - "&#xFFFD;"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages in the Artifact tool result when publishing a page fails. Nothing is published in each case.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Refusing to apply edits to <path>: a hook is configured for file edits in this session` | One-step updates (small edits included in a publish) are not allowed while a `PreToolUse` hook or mod exists on `Edit` or `Write` | Edit the file, then publish without edits; relaunch; or turn off one-step updates |
| `file_path: the source file is not valid UTF-8 text (first invalid byte at line N, column M)` / `... has the replacement character U+FFFD` | File decoded as UTF-8 (or UTF-16 with a little-endian BOM); adds `(+2 more)` counts. Before v2.1.267 the upload went unchecked and the server refused | Re-save as UTF-8; write an intended U+FFFD as `&#xFFFD;` in HTML |
| `Not published: that file is on a network share` | Windows `\\server\share` not under a mapped drive passed with `--add-dir` at launch, or macOS/Linux `/net/<host>/...` automount; looking up the path can leak credentials on Windows | Copy to a local disk; Windows `net use Z: \\server\share` then `claude --add-dir Z:\`; mount under `/mnt` or `/Volumes` |
| `Not published: Claude sent the same content again after a newer version of the artifact turned it away` | Repeat publish after a conflict with a newer version (editor or another session). Four variants | Ask Claude to fetch current version, merge, publish; or publish again where the line says `should go through` |
| `Reading a local file from outside this session's connected folders ... needs the approval card` | Cowork session on the Desktop app cannot show an approval card (e.g. skip-all-approvals) | Use a plain file inside connected folders |

# Notes

Cowork sessions run on the user's machine in the Claude Desktop app.
