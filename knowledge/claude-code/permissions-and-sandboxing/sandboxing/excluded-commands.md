---
type: "Feature"
title: "excludedCommands: run commands outside the sandbox"
description: "Pattern list of commands that run unsandboxed, with matching rules, permission handling and the warnings about full access."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, excludedcommands, escape-hatch, permissions]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.excludedCommands"
  - "Bash(...)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`sandbox.excludedCommands` lists command patterns that run with no filesystem restrictions and no network proxy. Use it for a tool that cannot work in the sandbox and that you trust with full access. A tool needing one more directory or host may work with `allowWrite` or `allowedDomains`, which keep it sandboxed.

# How to use it

```
{ "sandbox": { "enabled": true, "excludedCommands": ["docker compose *"] } }
```

Matching rules:
- Entries use `Bash(...)` permission rule syntax; no wildcard means exact match. `docker` matches only bare `docker`; `docker *` matches with or without arguments.
- Every command in a chained call must match: `npm ci && docker compose build` stays sandboxed unless `npm ci` is also covered.
- Matching is on the call text: a script or `make` target that calls `docker`, or `/usr/local/bin/docker`, does not match.
- A redirect to a file, a `cd`, or command substitution `$(...)` keeps the whole call sandboxed.
- `git clone` needs a relative path with no `..`; absolute, `~` or `..` paths are not covered.
- Under an admin-required sandbox, entries in `.claude/settings.json` and `.claude/settings.local.json` are ignored.

An excluded command goes through the regular permission flow: read-only commands and allow-rule matches run without a prompt; auto mode uses the classifier; `bypassPermissions` runs it unless an ask rule matches. To test, use Manual mode and run `docker compose up -d`; the prompt is titled "Bash command (unsandboxed)".

# Notes

Excluded commands run with full access. A pattern covering an interpreter, a script in the working directory, or a tool acting on a file there (like a compose file) lets Claude write the file then run it outside the sandbox. Narrower patterns leave less exposed. Adding a clipboard tool (`pbcopy`, `xclip`, `wl-copy`) here does not take that call out of the sandbox on its own.
