---
type: "Reference"
title: "permissions object and rule arrays"
description: "permissions.allow, ask, deny, additionalDirectories, defaultMode, disableBypassPermissionsMode and rule syntax, with evaluation order deny then ask then allow."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [permissions, rules, permission-modes, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, ide, cloud]
requires: ""
identifiers:
  - "permissions"
  - "permissions.allow"
  - "permissions.ask"
  - "permissions.deny"
  - "permissions.additionalDirectories"
  - "permissions.defaultMode"
  - "permissions.disableBypassPermissionsMode"
  - "--allowedTools"
  - "--disallowedTools"
  - "--add-dir"
  - "/add-dir"
  - "--permission-mode"
  - "--dangerously-skip-permissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `permissions` object controls which tools Claude may use without asking, which prompt and which are blocked, and sets the default permission mode. All keys scope `Any file`, default unset.

# How to use it

| Key | Type | What it does |
| :- | :- | :- |
| `permissions.allow` | array of rule strings | Approve without asking. In an MCP rule `*` may appear only in the tool name after `mcp__<server>__` (e.g. `mcp__github__get_*`). Project `allow` rules apply only after the workspace trust dialog. `--allowedTools` adds rules for a session |
| `permissions.ask` | array | Prompt even in `acceptEdits` or `bypassPermissions`; in `dontAsk` a match is denied. A `PermissionRequest` hook or a mod can still allow it; sandbox auto-allow can skip a bare `Bash` ask rule |
| `permissions.deny` | array | Block; also excluded from discovery/search and Edit/Write blocked. `--disallowedTools` adds rules |
| `permissions.additionalDirectories` | array of paths | Extra working directories (file access, not `.claude/` configuration). `--add-dir`, `/add-dir` add for a session. Project entries need workspace trust |
| `permissions.defaultMode` | string | Default permission mode for new sessions |
| `permissions.disableBypassPermissionsMode` | `"disable"` | Rejects `--dangerously-skip-permissions` and ignores an agent definition's `permissionMode: bypassPermissions` (subagent uses parent's mode; before v2.1.223 the frontmatter mode applied anyway) |

`defaultMode` values: `"default"` (reads only), `"acceptEdits"` (also edits and mkdir/mv), `"plan"` (no edits until a plan is approved), `"auto"` (background classifier checks actions), `"dontAsk"` (auto-deny every would-be prompt; a mod can still approve some; reads in working dirs and pre-approved tools run), `"bypassPermissions"` (no asking), `"manual"` (alias of `"default"`). `--permission-mode` and `--dangerously-skip-permissions` override for one session.

Rule syntax `Tool` or `Tool(specifier)`: `Bash`, `Bash(npm run *)`, `Read(./.env)`, `WebFetch(domain:example.com)`.

# Limits and defaults

- Evaluation order: deny, then ask, then allow; the first match decides regardless of specificity. Deny rules apply in every mode including `bypassPermissions`.
- Tool names accept globs: `"*"` denies every tool, `"mcp__*"` every MCP tool. A deny for `EndConversation` is ignored while another tool is available. `Bash(curl *)` does not stop `/usr/bin/curl` or `sh -c 'curl ...'`.
- Read/Edit denies cover built-in file tools, recognized Bash file commands (`cat`, `head`, `tail`, `sed`, `tee`) and redirection targets, but not `grep -r pattern .` or arbitrary subprocesses; use the sandbox for OS enforcement. `permissions.deny` replaces deprecated `ignorePatterns`.
- `auto` and `bypassPermissions` from `defaultMode` do not take effect from project or local settings (before v2.1.257 `bypassPermissions` did). The VS Code extension reads only user, managed and `--settings` values. In cloud sessions only `acceptEdits`, `plan`, `default`, `auto` are honored.
