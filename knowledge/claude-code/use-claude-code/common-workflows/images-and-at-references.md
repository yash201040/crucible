---
type: "Feature"
title: "Images and @ file references"
description: "Adding images and using @ to include files, directories and MCP resources, with size limits and the file-mentions disable variable."
resource: "https://code.claude.com/docs/en/common-workflows"
tags: [images, at-mentions, files, hooks, env-vars]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli]
requires: "CLAUDE_CODE_DISABLE_FILE_MENTIONS needs v2.1.299 or later"
identifiers:
  - "@"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "Ctrl+V"
  - "Alt+V"
  - "PreToolUse"
  - "Read"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "common-workflows"
    resource: "https://code.claude.com/docs/en/common-workflows"
    title: "Common workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Images can be added by drag and drop, by pasting with `Ctrl+V` (`Alt+V` on Windows and WSL), or by giving a path. Multiple images work in one conversation; references like `[Image #1]` can be opened with `Cmd+Click` (Mac) or `Ctrl+Click` (Windows/Linux).

`@` includes file contents or directory listings without waiting for Claude to read: `@src/utils/auth.js`, `@src/components`, or an MCP resource such as `@github:repos/owner/repo/issues`.

# Limits and defaults

- A file is included when it fits the Read tool's token limit, 25,000 tokens by default; a text file larger than 256KB is not included.
- Directory references list files, not contents. `@` file references also add `CLAUDE.md` in the file's directory and parent directories.
- `PreToolUse` hooks do not run for files included with `@` because no tool call is made. To control this: add a `Read` deny rule (Claude Code does not include a matching file), or set `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (shell, or the `env` block of user or managed settings; ignored in project and local settings), so Claude gets the path with a note to read it with its file tools and your matching hooks run first.
