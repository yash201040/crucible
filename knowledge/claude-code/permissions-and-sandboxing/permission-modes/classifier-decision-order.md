---
type: "Concept"
title: "How the classifier evaluates actions"
description: "Fixed decision order for each action in auto mode, rule exceptions, dropped allow rules, and what the classifier sees."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, decision-order, allow-rules, hooks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.222"
surfaces: [cli]
requires: ""
identifiers:
  - "classifierContext"
  - "SendMessage"
  - "Monitor"
  - "Bash(*)"
  - "PowerShell(*)"
  - "Agent"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

First matching step wins:
1. Actions matching allow, ask or deny rules resolve immediately, except: protected-path writes route to the classifier even with an allow rule (a symlinked settings file target may prompt); no allow rule approves recognized `rm`/`rmdir` critical-path removals; MCP tools marked `requiresUserInteraction` and organization-`ask` connector tools prompt directly; a shell command carrying per-command allowed domains goes to the classifier even with an allow rule; ask rules matching command content (such as `Bash(git push *)`) fall back to a prompt; a write the symlink check resolves to a protected path prompts when the requested path is not itself protected; network-path reads prompt.
2. Read-only actions and working-directory file edits are auto-approved (except protected paths and the first-read prompt). Under server-side review these (and sandboxed shell commands) wait for that review. A working-directory write that resolves outside prompts. Network-path reads prompt. Reading another's artifact has its own approval cases.
3. Everything else goes to the classifier (not critical-path removals under default handling; the prompting MCP/connector tools never reach it). With Code Mode on, the code Claude writes goes to the classifier once and the calls inside do not (deny/ask rules still apply, but Bash can run in forms rules don't match). Outside Code Mode, the classifier reviews `SendMessage` messages to other agents before delivery; an allow rule on `SendMessage` or a `PreToolUse` `"allow"` can skip this (needs v2.1.222+); it also runs in plan mode while the classifier reviews commands.
4. If it blocks, Claude receives the reason, usually the policy name such as `[Destructive or Unwanted Actions]`.

# How to use it

On entering auto mode these broad allow rules are dropped: `Bash(*)`, `PowerShell(*)`, wildcarded interpreters (`Bash(python*)`), wrapper-plus-wildcard (`Bash(timeout *)`), shell rules starting with a wildcard (`Bash(* --version)`), some wildcarded paths (`Bash($HOME/bin/*)`), package-manager run commands, `Agent` allow rules, and `Monitor` allow rules (before v2.1.236 Monitor rules stayed). Narrow rules like `Bash(npm test)` stay. Dropped rules return when leaving auto.

A PostToolUse hook's `classifierContext` field annotates a result for the classifier (v2.1.236+). An installed mod can also approve an action.

# Limits and defaults

- Claude Code may run `git status` before `git reset --hard` or `rm -rf` so the classifier sees uncommitted work (untracked files reported even with `status.showUntrackedFiles=no`). Under server review it can skip `git status` unless auto recently blocked an action, so `git reset --hard` on a clean tree can be blocked, then allowed on retry.
- In classifier requests sent by Claude Code, the classifier sees user messages, non-read-only tool calls and CLAUDE.md; tool results are stripped so hostile content cannot manipulate it directly. A separate server-side probe scans incoming tool results.
