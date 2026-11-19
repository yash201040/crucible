---
type: "Feature"
title: "Glob and Grep tool behavior"
description: "Glob and Grep are absent by default on macOS, Linux and WSL; when they return, and their search semantics and limits."
resource: "https://code.claude.com/docs/en/tools-reference#glob-tool-behavior"
tags: [glob, grep, search, tools, ripgrep]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Glob"
  - "Grep"
  - "CLAUDE_CODE_GLOB_NO_IGNORE"
  - "--tools"
  - "--allowedTools"
  - "--restricted"
  - "files_with_matches"
  - "content"
  - "count"
  - "head_limit"
  - "offset"
  - "multiline"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Windows both tools are in the default set. On macOS, Linux and WSL they are left out, and Claude searches with `find` and `grep` through Bash, which run embedded `bfs` and `ugrep`; those searches reach hooks and permission rules as `Bash` calls.

# How to use it

They come back when: you name `Glob` or `Grep` in `--tools` (you get those listed) or `--allowedTools` (naming either restores both; a settings-file allow rule does not) or in the equivalent SDK options; a deny rule, `--disallowedTools` or `--restricted` removes `Bash`; or a subagent lists them in `tools` without `Bash` (for that subagent, or the whole session when it is the main agent via `--agent` or the `agent` setting).

Glob: standard glob syntax (`**/*.js`, `src/**/*.ts`, `*.{json,yaml}`); results sorted by modification time, capped at 100 files with a truncation flag; does not respect `.gitignore` unless `CLAUDE_CODE_GLOB_NO_IGNORE=false` is set before launch.

Grep: built on ripgrep (ripgrep regex, escape metacharacters such as `interface\{\}`); output modes `files_with_matches` (default), `content`, `count` (total covers all matches even if `head_limit` or `offset` truncate the list); `glob` and `type` parameters scope results; `multiline: true` matches across lines; respects `.gitignore` (pass a path directly to search ignored files). Rejected patterns return ripgrep's diagnostic (before v2.1.208 they reported `No files found`). Offset past the last match returns `No entries at this offset`.

# Limits and defaults

Permission is decided before checking the search directory exists; a missing path outside working directories still gets the read check. A null byte in `pattern` or `path` returns an error.
