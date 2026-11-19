---
type: "Feature"
title: "allowManagedPermissionRulesOnly"
description: "Managed Boolean that makes managed settings the only source of permission rules and, from v2.1.282, ignores skill allowed-tools from user and repository sources."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [managed-settings, permissions, skills, enterprise]
kind: "setting"
maturity: "unlabelled"
since: "2.1.282"
surfaces: [cli, desktop]
requires: "allowed-tools handling v2.1.282; @inline plugin handling v2.1.305"
identifiers:
  - "allowManagedPermissionRulesOnly"
  - "allowed-tools"
  - "disallowed-tools"
  - "@inline"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Scope `Managed`, Boolean, default unset. When `true`, `allow`, `ask` and `deny` rules in user, project, local and `--settings` files are ignored, `--allowedTools` is ignored, always-allow choices in prompts are hidden and new rules are not saved.

# How to use it

```json
{ "allowManagedPermissionRulesOnly": true }
```

It does not lock the MCP allowlist; use `allowManagedMcpServersOnly` for that.

# Limits and defaults

- Parent settings from an embedding host count as managed tier but lose their `allow` rules and `additionalDirectories`; their `deny` and `ask` rules stay except `Read`/`Edit` rules whose pattern starts with `!`.
- `--disallowedTools` rules and the current session's `deny` and `ask` rules still apply, including after a mid-session settings reload (before v2.1.257 they were dropped at the first reload).
- From v2.1.282 the skill/command `allowed-tools` frontmatter is also ignored when it comes from: a repository `.claude/`, `~/.claude/skills/` and `~/.claude/commands/` (including skills synced from claude.ai), an `--add-dir` directory, plugins declared with a `.claude-plugin` manifest inside `~/.claude/skills/` or the project's `.claude/skills/`, and one-session `@inline` plugins in Desktop-started Code or Cowork sessions (not cloud) when managed settings themselves set the key and the session runs v2.1.305 or later.
- Skills from managed settings and bundled skills keep `allowed-tools`; `@inline` plugins outside those Desktop sessions keep theirs, except one named `anthropic-skills`. A skill's `disallowed-tools` still applies.
