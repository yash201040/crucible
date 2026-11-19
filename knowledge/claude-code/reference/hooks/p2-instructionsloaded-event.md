---
type: "Feature"
title: "InstructionsLoaded hook event"
description: "Observability-only event fired when a CLAUDE.md or .claude/rules file is loaded, eagerly or lazily."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, instructions, claude-md, audit]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "InstructionsLoaded"
  - "file_path"
  - "memory_type"
  - "load_reason"
  - "session_start"
  - "nested_traversal"
  - "path_glob_match"
  - "include"
  - "globs"
  - "trigger_file_path"
  - "parent_file_path"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fires when a `CLAUDE.md` or `.claude/rules/*.md` file is loaded into context: at session start for eager files, and later for lazy loads (nested CLAUDE.md when Claude accesses a subdirectory, conditional rules with `paths:` frontmatter). Runs asynchronously, no blocking or decision control; JSON fields like `systemMessage` and `continue` are discarded. Use for audit logging, compliance, observability.

# How to use it

The matcher runs against `load_reason`, e.g. `"session_start"` or `"path_glob_match|nested_traversal"` for lazy loads only.

| Field | Description |
| :- | :- |
| `file_path` | Absolute path of the loaded file |
| `memory_type` | `"User"`, `"Project"`, `"Local"` or `"Managed"` |
| `load_reason` | `"session_start"`, `"nested_traversal"`, `"path_glob_match"`, `"include"`, or `"compact"` (re-load after compaction) |
| `globs` | Patterns from the file's `paths:` frontmatter; only for `path_glob_match` |
| `trigger_file_path` | File whose access triggered a lazy load |
| `parent_file_path` | Parent instruction file for `include` loads |

# Limits and defaults

- Does not fire when Claude reads `AGENTS.md` directly through the Project instructions setting. It does fire when a CLAUDE.md imports AGENTS.md (`load_reason` `include`) or CLAUDE.md is a symlink to it.
