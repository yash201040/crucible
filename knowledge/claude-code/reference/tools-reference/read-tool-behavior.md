---
type: "Feature"
title: "Read tool behavior and large files"
description: "File types Read handles, size and token limits, and allow_large for whole-file reads."
resource: "https://code.claude.com/docs/en/tools-reference#read-tool-behavior"
tags: [read, files, limits, pdf, images]
kind: "tool"
maturity: "unlabelled"
since: "2.1.296"
surfaces: [cli, sdk]
requires: "pdftoppm (poppler-utils) for PDF page-range reads"
identifiers:
  - "Read"
  - "CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS"
  - "allow_large"
  - "offset"
  - "limit"
  - "pages"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Returns file contents with line numbers. An empty file gives a notice; an `offset` past the end gives a notice with the line count. It reads files only, not directories.

# How to use it

- Images: PNG, JPEG, GIF, WebP returned visually, resized and recompressed if large; refused over 128 MB.
- PDFs: short ones whole; over 10 pages use `pages` (such as `"1-5"`), up to 20 pages at a time, rendered with `pdftoppm` (without it: `pdftoppm is not installed`).
- Notebooks: `.ipynb` returns all cells with outputs; errors if cells exceed 256 KB or the token limit; refuses files over 100 MB.
- Extensions treated as binary (`.xlsx`, `.parquet`, `.heic`, `.zip`) are refused with a suggestion; an `@`-mentioned refused file gives Claude only its path.

# Limits and defaults

- One call returns at most 25,000 tokens (or `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`) and a whole file over 256 KB is refused; read in pages with `offset` and `limit`.
- Over the token limit for a whole file: first page plus a `PARTIAL view` notice. Whole file over 256 KB, or an `offset`/`limit` read over the token limit: an error suggesting a smaller portion or Grep.
- From v2.1.296, `allow_large: true` reads a whole file or long range sized against remaining context window; images, PDFs and notebooks keep their limits.
