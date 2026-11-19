---
type: "Concept"
title: "How permissions interact with sandboxing"
description: "Permissions gate tools and paths, sandboxing enforces OS limits on shell commands; autoAllowBashIfSandboxed skips the Bash prompt."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, sandboxing, bash, defense-in-depth]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.autoAllowBashIfSandboxed"
  - "Bash"
  - "Bash(*)"
  - "Bash(git push *)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permissions control which tools Claude Code can use and which files or domains they reach (Bash, Read, Edit, WebFetch, MCP, all tools except that a deny or ask cannot block `EndConversation` while others remain). Sandboxing is OS-level enforcement on shell commands' filesystem and network access, covering Bash, PowerShell and Monitor tool commands and their children. Use both: sandbox limits still hold if a prompt injection bypasses Claude's decisions. Paths and domains from sandbox settings and permission rules are merged into the final sandbox configuration.

# How to use it

With sandboxing on and `sandbox.autoAllowBashIfSandboxed` set to `true`, sandboxed Bash commands run without prompting, even with a bare `Bash` ask rule or `Bash(*)`: the sandbox boundary replaces that whole-tool prompt.

Still applies:
- content-scoped ask rules such as `Bash(git push *)` force a prompt;
- other sandboxed commands can go through the regular permission flow (Auto-allow mode);
- commands that do not run sandboxed, such as excluded commands, respect the bare `Bash` ask rule.

# Notes

In plan mode the substitution is skipped. Without an ask rule built-in read-only commands run without prompts and other shell commands use the regular flow; with a bare `Bash` ask rule every Bash command prompts, including sandboxed read-only ones.
