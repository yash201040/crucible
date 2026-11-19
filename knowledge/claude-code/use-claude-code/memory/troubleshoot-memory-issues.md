---
type: "Guide"
title: "Troubleshoot instructions not followed"
description: "Debug steps when CLAUDE.md or AGENTS.md is ignored, and what survives /compact."
resource: "https://code.claude.com/docs/en/memory"
tags: [troubleshooting, claude-md, compact, hooks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "includeGitInstructions"
  - "attribution"
  - "--append-system-prompt"
  - "InstructionsLoaded"
  - "Instruction file not loaded"
  - "/compact"
  - "claude --debug"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "memory"
    resource: "https://code.claude.com/docs/en/memory"
    title: "How Claude remembers your project"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

CLAUDE.md is delivered as a user message after the system prompt, not as part of it, so compliance is not guaranteed, especially for vague or conflicting instructions.

# How to use it

- Run `/context all` and check **Memory files**. An `Instruction file not loaded` notice has an errors-page explanation. A subdirectory CLAUDE.md is not listed (on-demand); when it loads a `Loaded` line with its path appears. Create test files from your shell rather than via Claude, then ask Claude to read a file in that subdirectory.
- Make instructions specific; remove conflicts across files.
- If your CLAUDE.md sets commit or PR rules, turn off built-in ones with `includeGitInstructions` and set text with `attribution`.
- Instructions that must run at a fixed point (before every commit, after each edit) should be hooks, which run regardless of what Claude decides.
- For system-prompt-level instructions use `--append-system-prompt` at launch (better for scripts and automation); resume behavior is under system prompt flags in the CLI reference.
- Use the `InstructionsLoaded` hook to log which CLAUDE.md and rules files load, when and why.
- AGENTS.md not loading: check for a CLAUDE.md or CLAUDE.local.md on the path (other than `~/.claude/CLAUDE.md`); `claude --version` is v2.1.277+ (v2.1.281+ for Bedrock or telemetry-off sessions); `/config` Project instructions is not `claude-md` or `managed-only`; confirm with `/memory`.
- Unknown auto memory contents: `/memory`, then the auto memory folder.

# Limits and defaults

After `/compact`, project-root CLAUDE.md is re-read from disk and re-injected; nested CLAUDE.md files and `paths:` rules load again on demand. Lost instructions were given only in conversation, sit in a not-yet-reloaded nested file, or are unmatched path-scoped rules. Put conversation-only instructions in CLAUDE.md.
