---
type: "Reference"
title: "Path patterns in Read and Edit rules"
description: "How to write path patterns for Read and Edit rules: Edit covers all file writers; // is absolute, / is working-directory relative."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permissions, path-patterns, edit-rules]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Edit(path)"
  - "Read(path)"
  - "Write(path)"
  - "NotebookEdit(path)"
  - "Edit(//secrets/**)"
  - "Edit(/secrets/**)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Scoped `Read` and `Edit` rules take a path pattern. `Edit(path)` governs all built-in file-writing tools including `Write` and `NotebookEdit`. A rule written as `Write(path)` or `NotebookEdit(path)` matches no call and has no effect.

# How to use it

In `allowed_tools`/`disallowed_tools`:

| Prefix | Meaning | Example |
| :- | :- | :- |
| `//path` | Absolute path | deny `Edit(//secrets/**)` blocks writes under `/secrets` from file tools and Bash such as `tee` and `> file` |
| `/path` | Inside the session working directory | `Edit(/secrets/**)` matches `secrets` in the working directory |

# Limits and defaults

A script Claude runs that opens files itself can still write under a denied path. For OS-level enforcement use the sandboxed Bash tool.
