---
type: "Feature"
title: "Write tool behavior"
description: "Whole-file create or overwrite and when a prior read is required."
resource: "https://code.claude.com/docs/en/tools-reference#write-tool-behavior"
tags: [write, files, read-before-write]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Write"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Creates a file or overwrites one with the full content given; no append or merge. It also overwrites an existing file whose bytes do not decode, saving as UTF-8. Partial changes use Edit.

# Limits and defaults

- Opus 4.6, Haiku 4.5 and older models must read an existing file in the conversation first, else the Write fails.
- Newer models can overwrite an unread file under the same conditions as read-before-edit (reading would not need a permission prompt, Read available).
- Jupyter notebooks, and files read only partially (`PARTIAL view`), require the read on every model. New files are exempt. Viewing the file with Bash also satisfies the requirement.
