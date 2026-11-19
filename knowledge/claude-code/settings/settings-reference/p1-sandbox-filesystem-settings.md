---
type: "Reference"
title: "Sandbox filesystem settings"
description: "sandbox.filesystem lists (allowWrite, denyWrite, denyRead, allowRead), managed lock allowManagedReadPathsOnly, disabled, plus path prefixes and wildcard rules."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [sandbox, filesystem, paths, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.224"
surfaces: [cli, headless]
requires: "macOS, Linux or WSL2"
identifiers:
  - "sandbox.filesystem"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.filesystem.denyWrite"
  - "sandbox.filesystem.denyRead"
  - "sandbox.filesystem.allowRead"
  - "sandbox.filesystem.allowManagedReadPathsOnly"
  - "sandbox.filesystem.disabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls which paths sandboxed commands can read and write. By default they write to the working directory, the per-user temp directory and directories from `--add-dir`, `/add-dir` or `permissions.additionalDirectories`, and read the rest of the filesystem including credential files. Enforced at the OS boundary, so it applies to every subprocess. Your `Edit` allow/deny rules feed `allowWrite`/`denyWrite`, `Read` deny rules feed `denyRead`, and `WebFetch(domain:...)` rules feed the network lists.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `allowWrite` | Any file (project/local limited) | array of paths | unset | Extra writable paths. On Linux/WSL2 a path that does not exist yet has no effect. Cannot lift a protected path |
| `denyWrite` | Any file | array | unset | Block writes, even inside writable dirs (e.g. `/etc`, `/usr/local/bin`) |
| `denyRead` | Any file | array | unset (credential files readable) | Block reads. Not enforced when `filesystem.disabled` is `true` |
| `allowRead` | Any file (project/local limited) | array | unset | Re-open reading inside a `denyRead` region; `.` resolves to project root in project settings and `~/.claude` in user settings. Exact or wildcard `denyRead` entries stay blocked inside a broader `allowRead`; before v2.1.236 on macOS wildcard-matched paths were re-opened |
| `allowManagedReadPathsOnly` | Managed | Boolean | `false` | Honor only managed `allowRead`; `denyRead` still merges from all scopes |
| `disabled` | User or managed (only managed if managed settings configure `sandbox.filesystem` or a `credentials.files` entry with `"mode": "deny"`) | Boolean | `false` | Skip filesystem isolation but keep network isolation (egress confined to `network.allowedDomains`). `denyRead` and `credentials.files` deny entries are then not enforced; `credentials.envVars` and applied `mask` entries still work |

```json
{ "sandbox": { "filesystem": { "denyRead": ["~/"], "allowRead": ["."] } } }
```

Path prefixes (`allowWrite`, `denyWrite`, `denyRead`, `allowRead`, `credentials.files`):

| Prefix | Meaning |
| :- | :- |
| `/` | absolute path (`//path` also works) |
| `~/` | relative to home |
| `./` or none | project root for project settings; `~/.claude` for user settings |

# Limits and defaults

- Lists merge across settings files unless a lock applies; entries from repository settings are left out while `permissions.blockReadsOutsideWorkingDirectories` is on or an admin-required repository lock applies. Edits during a session apply to the running session.
- Trailing slashes are stripped (before v2.1.224 they were passed through and paths under such `denyRead`/`denyWrite` entries could still be accessed).
- Wildcards `*`, `?`, `**` work in all four lists on macOS. On Linux/WSL2: `denyRead`/`allowRead` allow a trailing `/**` and other wildcards only after the first directory name of the full path (`/**/*.pem` covers nothing; write `/srv/**/*.pem`); `allowWrite`/`denyWrite` allow only a trailing `/**` (`./src/*` matches only an entry literally named `*`; write `./src`). `/sandbox` Config tab warns about `Edit` rules with other wildcards.
- Directory names with brackets: write the real name (`./app/[slug]`) and omit a trailing `/**`; the directory must exist at start. Brackets are also a pattern on macOS (all lists) and in `denyRead`/`allowRead` on Linux/WSL2, so `[slug]` also matches `app/s`, `app/g`. Names like `[user-id]` (hyphen's left char sorts after right) match exactly; before v2.1.304 Linux/WSL2 sandboxed commands failed to start with such an entry. Braces and parentheses are ordinary characters.
