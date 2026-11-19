---
type: "Concept"
title: "Sandbox temp directories and TMPDIR"
description: "The per-user temp directory writable in the sandbox, how TMPDIR differs between sandboxed and unsandboxed commands, and passing files between them."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, tmpdir, filesystem]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$TMPDIR"
  - "CLAUDE_CODE_TMPDIR"
  - "mktemp -d"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A per-user temp directory is writable in the sandbox alongside the working directory. Unless filesystem isolation is disabled, Claude Code sets `$TMPDIR` to it for sandboxed commands.

# How to use it

Unsandboxed commands inherit your shell's `$TMPDIR` if set, so sandboxed and unsandboxed commands resolve `$TMPDIR` to different directories. If your shell leaves it unset or empty, an unsandboxed command gets your `CLAUDE_CODE_TMPDIR` override, or the OS temp directory when there is no override or it is a long path. To pass temporary files between the two, write them under the working directory.

# Notes

With filesystem isolation off, sandboxed commands inherit your shell's `$TMPDIR`; on Linux it is often unset, and Bash tool guidance tells Claude to create scratch directories with `mktemp -d`.
