---
type: "Feature"
title: "Include files and skills in REVIEW.md"
description: "A line of just @filename in the root REVIEW.md pulls in files beside it or a .claude/skills SKILL.md, subject to limits of eight files and 150,000 bytes."
resource: "https://code.claude.com/docs/en/code-review-customize"
tags: [code-review, review-md, includes, skills]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Root REVIEW.md read from a protected branch"
identifiers:
  - "@review-security.md"
  - "@.claude/skills/<folder>/SKILL.md"
  - "SKILL.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-customize"
    resource: "https://code.claude.com/docs/en/code-review-customize"
    title: "Customize Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An include line is `@` plus a file name alone on a line in the root `REVIEW.md`; Code Review substitutes the file's contents. Included files sit at the repository root beside `REVIEW.md`. On an unprotected default branch the `@` line stays as plain text (and is dropped if the PR changes that file).

# How to use it

Skill file: `@.claude/skills/<folder>/SKILL.md` on its own line. Code Review does not run skills; it gets only the `SKILL.md` body. Rules: folder name without spaces; path exactly that form with the folder directly under `skills/`; a regular text file (symlinks are not followed); at most 30,000 bytes including frontmatter; at most eight skill lines (repeats count); not inside code fences or unclosed HTML comment, `<pre>`, `<script>`, `<style>`, `<textarea>` blocks. Content from other `.claude/` files or bundled, personal or plugin skills cannot be included; copy it to a file beside `REVIEW.md`.

What a skill loses: frontmatter (repeat needed conditions in the body), `!` injected commands (the whole line or block becomes a placeholder), `$ARGUMENTS` and substitutions (left as written), supporting files, linked or `@file` references. Exclusions and Nit caps must live in `REVIEW.md` or a file beside it, not in a skill. Some characters in skill text are rewritten (backticks, `[`/`]`, `<`, `|`, `@`).

# Limits and defaults

- At most eight different included files; `REVIEW.md` plus included files under 150,000 bytes combined; a file that would exceed it is skipped whole. The skill file counts toward both and has its own 30,000-byte limit.
- Includes are one level only: an `@` line in an included file or a subdirectory `REVIEW.md` stays plain text (skill files differ).
- A path into a subdirectory such as `@docs/review-rules.md` is not included (except a skill file). A name that matches no file stays as plain text without being reported.
- Markdown links: at most 64 across `REVIEW.md` and included files (`http`, `https`, `mailto` and `#` anchor links and links in skill files do not count). Past that the whole root `REVIEW.md` is skipped. The check run reports skipped include lines by count.
