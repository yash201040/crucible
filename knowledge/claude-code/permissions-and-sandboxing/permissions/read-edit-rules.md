---
type: "Concept"
title: "Read and Edit rules: coverage and gaps"
description: "Edit rules cover all file-editing tools, Read deny is best-effort for readers and attachments; Write/Glob/Grep path rules never match."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, read, edit, deny-rules, secrets]
kind: "setting"
maturity: "unlabelled"
since: "2.1.228"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "Read(./.env)"
  - "Read(./secrets/**)"
  - "Edit(docs/**)"
  - "Read(docs/**)"
  - "Write(docs/**)"
  - "Grep(docs/**)"
  - ".claudeignore"
  - "NotebookEdit"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

To block file tools from a path add a `Read` deny rule (`Read(./.env)`, `Read(./secrets/**)`). A `.claudeignore` file has no effect; move its entries into `Read` deny rules.

# How to use it

- `Edit` rules apply to all built-in tools that edit files. `Read(path)` deny is a best-effort attempt for tools like Grep and Glob, `@file` mentions, and IDE selection/open-file context.
- A `Read` deny also applies to pasted or dragged image paths (the image is not attached) and to directory @-mentions (the listing omits matched names). Checked from v2.1.290.
- A `Read` deny also blocks Edit and Write on the path, including creating a file there. `NotebookEdit` is not covered, so add an `Edit` deny for paths no tool may change. The Write check needs v2.1.228+.
- Path rules on `Write`, `NotebookEdit`, legacy `MultiEdit`, `Glob` or `Grep` are accepted but never match. Use `Edit(docs/**)` instead of `Write(docs/**)`, and `Read(docs/**)` instead of `Grep(docs/**)`. As an ask rule `Read(docs/**)` prompts when Grep/Glob targets a matching path, not when a search of a higher directory returns matching files. A bare tool name still matches every use.

# Limits and defaults

Read/Edit deny rules also apply in Bash commands Claude Code can analyze (redirect targets, `cat`, `head`, `tail`, `sed`, `tee`). They do not apply to commands that read without naming files (`grep -r pattern .`) or to subprocesses (a Python or Node script opening files). For OS-level enforcement enable the sandbox and turn off the unsandboxed retry (strict sandbox mode).
