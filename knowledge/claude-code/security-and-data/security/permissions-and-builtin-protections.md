---
type: "Concept"
title: "Permission modes and built-in protections"
description: "Auto and manual permission modes, accept edits, working directory boundary, sandboxed Bash and fail-closed matching."
resource: "https://code.claude.com/docs/en/security"
tags: [permissions, auto-mode, sandbox, manual-mode, protections]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "/sandbox"
  - "/permissions"
  - "permissions.deny"
  - "Bash(curl *)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "security"
    resource: "https://code.claude.com/docs/en/security"
    title: "Security"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission mode sets what Claude can do without asking. Auto mode is the built-in starting mode for interactive terminal and VS Code sessions: a separate classifier model reviews actions and blocks unsafe ones; explicit ask and deny rules still apply; the organization can turn it off. Manual mode starts read-only and asks before edits, tests or commands (a built-in set of read-only commands like `ls`, `cat`, `git status` runs without asking).

# How to use it

- Sandboxed Bash: filesystem and network isolation, configure with `/sandbox`.
- Working directory boundary (Manual mode): file tools ask before reading or writing outside the start folder; it is a permission prompt, so an approved Bash command can still write anywhere the user account can. Use additional directories to read without a prompt; use sandboxing for OS-level restriction.
- Accept Edits mode: auto-approves file edits and a fixed set of filesystem Bash commands (`mkdir`, `touch`, `rm`, `mv`, `cp`, `sed`) in the working directory.
- Network commands such as `curl` and `wget` prompt by default; add `Bash(curl *)` as an allow rule, or put commands in `permissions.deny` (matches the command as written; sandbox network isolation does not depend on text).
- Audit with `/permissions`.

# Limits and defaults

Fail-closed matching: in Manual mode unmatched commands need approval. Commands Claude cannot fully analyze prompt even with a partial allow rule like `Bash(git *)`, except sandboxed commands in auto-allow mode.
