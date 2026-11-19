---
type: "Feature"
title: "Edit tool behavior, Perforce mode and non-UTF-8 files"
description: "Exact-string edit rules, read-before-edit requirements, and how non-UTF-8 files are handled."
resource: "https://code.claude.com/docs/en/tools-reference#edit-tool-behavior"
tags: [edit, files, encoding, perforce]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Edit"
  - "old_string"
  - "new_string"
  - "replace_all"
  - "CLAUDE_CODE_PERFORCE_MODE"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Edit replaces `old_string` with `new_string`; no regex or fuzzy matching. A path matched by a `Read` deny rule is refused, including creating a new file.

# How to use it

Checks that must pass:
- Read-before-edit: Opus 4.6, Haiku 4.5 and older models always require a prior read (a read cut short with a `PARTIAL view` notice does not count). Newer models can edit an unread file when reading it would not need a permission prompt and Read is available.
- `old_string` must match exactly, including whitespace, and appear exactly once; otherwise a longer string or `replace_all: true`.
- A file changed on disk after the last read can still be edited if `old_string` matches current content unambiguously and can be read without prompting; the result notes other changes.
- Viewing a file with a Bash command on one file with no pipes or redirects (`cat`, `nl`, `bat`, `batcat`, `head`, `tail`, `sed -n 'X,Yp'`, `grep`, `egrep`, `fgrep`, `rg`) also satisfies read-before-edit, unless nothing of the file was printed. That view also loads subdirectory `CLAUDE.md` and path-scoped rules.
- `CLAUDE_CODE_PERFORCE_MODE=1`: Edit, Write and NotebookEdit refuse read-only files and tell Claude to run `p4 edit` first.

# Limits and defaults

Non-UTF-8 files: NotebookEdit refuses any non-valid-UTF-8 file; Edit does too unless the file starts with a little-endian UTF-16 byte-order mark (legacy encodings like Windows-1252 or Shift-JIS, binary files, invalid UTF-8). Nothing is written; Claude is told to use a shell command or ask about conversion. Write can still replace such a file (saved as UTF-8) unless the new content contains `U+FFFD`.
