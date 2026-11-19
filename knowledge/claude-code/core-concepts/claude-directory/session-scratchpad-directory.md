---
type: "Feature"
title: "Session scratchpad directory"
description: "A per-session temp directory Claude uses instead of /tmp, its path per OS, retention, hook access via scratchpad_dir, and when a session has one."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [scratchpad, temp, sessions, hooks]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: "claude.ai account sign-in (not API key), Anthropic API (not Bedrock, Google Cloud Agent Platform or Microsoft Foundry), enableArtifact not false"
identifiers:
  - "scratchpad_dir"
  - "CLAUDE_CODE_TMPDIR"
  - "enableArtifact"
  - "claude purge"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The scratchpad is a per-session directory for temporary files: intermediate results, helper scripts, drafts. Claude uses it instead of `/tmp` and can create, edit and read files there without a permission prompt. It sits under Claude Code's temp directory, not `~/.claude`.

# How to use it

Paths:
- macOS: `/private/tmp/claude-<uid>/<project>/<session-id>/scratchpad/`
- Linux: `/tmp/claude-<uid>/<project>/<session-id>/scratchpad/` (same shape under `$TMPDIR` if set)
- Windows: `%TEMP%\claude\<project>\<session-id>\scratchpad\`

`<project>` is the working directory path with every non-letter, non-digit replaced by `-` (e.g. `-Users-you-my-project`); on Windows a 16-character hash; in a Desktop app session it can be the string itself. `CLAUDE_CODE_TMPDIR` moves the tree. Hooks receive the path as `scratchpad_dir` in common input fields.

# Limits and defaults

- Files last as long as the session transcript: the retention sweep deletes the directory with the transcript; `claude purge` does not touch the temp directory; the OS may clear it (e.g. at restart). Ask Claude to move anything to keep into the project.
- A session has a scratchpad only when signed in with a claude.ai account (not an API key), using the Anthropic API (not Bedrock, Google Cloud's Agent Platform or Microsoft Foundry), and `enableArtifact` is not `false`.
