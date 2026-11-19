---
type: "Limit"
title: "Network path reads always prompt"
description: "From v2.1.292, reads of UNC or /net paths prompt regardless of allow rules, hooks or auto mode; dontAsk denies them."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, network-paths, windows, prompts]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli]
requires: ""
identifiers:
  - "--add-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A network path can reach another computer: a UNC path (`\\server\share\file`) on Windows, a `/net` automount path (`/net/fileserver/notes.txt`) on macOS and Linux. Read, Grep and Glob reads there get their own permission check because lookup can contact the host (on Windows, sending credentials).

# How to use it

In v2.1.292 and later the prompt stays despite: allow rules (even a whole-tool `Read`), a PreToolUse hook returning `"allow"`, and auto mode (the prompt goes to you, not the classifier). `dontAsk` denies the read. `bypassPermissions`, and interactive terminal plan-mode sessions with bypass permissions available, run it without the prompt.

To avoid the prompt give the share a local path: on Windows map it to a drive letter and run `claude --add-dir Z:\`; on macOS and Linux mount it under `/mnt` or `/Volumes`.

# Notes

Most network paths cannot be added as working directories. Shell commands have their own check (a read-only Bash/PowerShell command with a UNC path prompts on Windows).
