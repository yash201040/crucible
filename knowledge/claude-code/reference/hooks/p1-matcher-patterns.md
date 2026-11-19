---
type: "Reference"
title: "Matcher evaluation rules"
description: "How a hook matcher string is evaluated: match-all, exact list, or JavaScript regex, with narrower rules for FileChanged and StopFailure."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, matcher, regex, reference]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.267"
surfaces: [cli]
requires: ""
identifiers:
  - "matcher"
  - "if"
  - "cloud_credential_error"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `matcher` field filters when hooks in a group fire. Evaluation depends on the characters it contains.

# How to use it

| Matcher value | Evaluated as | Example |
| :- | :- | :- |
| `"*"`, `""`, or omitted | Match all | every occurrence |
| Only letters, digits, `_`, `-`, spaces, `,`, `\|` | Exact string, or list of exact strings separated by `\|` or `,` (optional whitespace) | `Bash`; `Edit\|Write`; `Edit, Write`; `code-reviewer` |
| Any other character | JavaScript regular expression, unanchored (`RegExp.prototype.test`) | `^Notebook`; `mcp__memory__.*` |

`Edit.*` matches both `Edit` and `NotebookEdit`; use `^Edit$` for whole-string matches.

`FileChanged` and `StopFailure` use a narrower exact set: letters, digits, `_` and `|` only. A hyphen, space or comma puts the matcher on the regex path, and only `|` separates alternatives. `FileChanged` builds its watch list by its own rules.

A `matcher` on an event with no matcher support is silently ignored.

For tool events you can narrow further per handler with `if`, which uses [permission rule syntax](./p1-handler-types-and-common-fields.md) against tool name and arguments: `"Bash(git *)"` or `"Edit(*.ts)"`.

# Limits and defaults

Matching `StopFailure` on `cloud_credential_error` requires v2.1.267 or later (earlier versions reported these as `server_error` or `unknown`).
