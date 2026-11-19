---
type: "Feature"
title: "Sandbox filesystem allow and deny rules"
description: "Configure extra write paths and deny or re-allow read paths for sandboxed commands, with path conventions and merge behavior."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, filesystem, allowwrite, denyread]
kind: "setting"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "sandbox.filesystem.allowWrite"
  - "sandbox.filesystem.denyWrite"
  - "sandbox.filesystem.denyRead"
  - "sandbox.filesystem.allowRead"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "--setting-sources"
  - "settingSources"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings that widen or narrow filesystem access for sandboxed commands, enforced at the OS level for all child processes. Prefer `allowWrite` for a tool needing a specific location over excluding the tool with `excludedCommands`.

# How to use it

```
{ "sandbox": { "enabled": true,
  "filesystem": { "allowWrite": ["~/.kube", "/tmp/build"] } } }
```

- Sandbox paths use standard conventions: `/tmp/build` absolute, `~/.kube` home-relative. This differs from Read/Edit permission rules (`//path` absolute, `/path` project-relative).
- `denyRead` blocks reads; `allowRead` re-opens paths inside a denied region. The narrower path wins on overlap: `denyRead ["~/"]` plus `allowRead ["~/projects"]` makes only `~/projects` readable; `allowRead ["~/"]` plus `denyRead ["~/.env"]` or `["~/**/.env"]` keeps the deny, so a broad allow cannot re-expose a secret.
- Block reading the home directory but keep the project: `denyRead ["~/"]`, `allowRead ["."]` in project `.claude/settings.json` (`.` resolves to the project root there; in `~/.claude/settings.json` it would resolve to `~/.claude`).
- `permissions.blockReadsOutsideWorkingDirectories` denies sandboxed reads of home directories and mounted volumes while keeping working directories readable, without path rules.

# Limits and defaults

- On Linux and WSL2 an entry for a path that does not exist yet has no effect; create it first.
- The same array in several settings scopes is merged (paths combined), except entries covered by a lock (see [admin-required sandbox](./admin-required-sandbox-and-locks.md)).
- Excluding a source with `--setting-sources` or the SDK `settingSources` makes Claude Code ignore that source's `sandbox.filesystem` entries, `Edit` permission rules and `Read` deny rules when building the sandbox. Requires v2.1.246 or later.
- Edits to these lists apply to the running session at the next sandboxed command.
