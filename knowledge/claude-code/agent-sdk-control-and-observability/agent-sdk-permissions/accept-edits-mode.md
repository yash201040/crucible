---
type: "Feature"
title: "Accept edits mode"
description: "acceptEdits auto-approves file edits and common filesystem commands inside working directories."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, acceptedits, file-edits]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "acceptEdits"
  - "add_dirs"
  - "additionalDirectories"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Auto-approves file operations so Claude can edit without prompting. Other tools (Bash commands that are not filesystem operations) still need normal permissions.

# How to use it

Auto-approved: edits with Edit, Write, NotebookEdit; and the commands `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`. Both apply to paths inside the working directory or a directory you add (`add_dirs` in Python, `additionalDirectories` in TypeScript).

# Limits and defaults

Not auto-approved: paths outside that scope; writes to a protected path; `rm`/`rmdir` of a recognized critical path; `touch` with an option, a glob, or a `timeout 5` or `LANG=C` prefix.

# Notes

Use for prototyping or isolated directories.
